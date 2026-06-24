#!/usr/bin/env python3
"""Generate a reproducible optimizer-trajectory SVG for Session 5 revision.

All displayed paths are calculated from the stated loss, initial point,
hyperparameters, and deterministic mini-batch noise sequence.  This is not a
claim that Momentum or Adam has one universal path on every loss surface.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).parents[1] / "lessons/assets/optimizer-trajectories.svg"
H1, H2 = 1.0, 20.0
# Start inside the long, shallow valley so the figure isolates the effect of
# high-frequency mini-batch noise across the steep w2 direction.
INITIAL = (-4.0, 0.2)
STEPS = 48
EPSILON = 1e-8


def noise(t: int) -> tuple[float, float]:
    """Fixed pseudo mini-batch-gradient error: no random state is hidden."""
    return (
        0.8 * math.sin(1.7 * t) + 0.35 * math.cos(0.37 * t),
        # Alternating mini-batches create high-frequency ravine noise.  This
        # makes the smoothing effect of a moving average directly visible.
        8.0 * (-1.0) ** t + 0.5 * math.sin(0.29 * t),
    )


def gradient(w: list[float], noisy: bool, t: int) -> list[float]:
    g = [H1 * w[0], H2 * w[1]]
    if noisy:
        n1, n2 = noise(t)
        g[0] += n1
        g[1] += n2
    return g


def full_batch_gd() -> list[tuple[float, float]]:
    w = list(INITIAL)
    points = [tuple(w)]
    for t in range(STEPS):
        g = gradient(w, noisy=False, t=t)
        w[0] -= 0.04 * g[0]
        w[1] -= 0.04 * g[1]
        points.append(tuple(w))
    return points


def mini_batch_sgd() -> list[tuple[float, float]]:
    w = list(INITIAL)
    points = [tuple(w)]
    for t in range(STEPS):
        g = gradient(w, noisy=True, t=t)
        w[0] -= 0.04 * g[0]
        w[1] -= 0.04 * g[1]
        points.append(tuple(w))
    return points


def momentum() -> list[tuple[float, float]]:
    """Course convention: u <- beta*u + (1-beta)*g; w <- w - eta*u."""
    eta, beta = 0.20, 0.90
    w, u = list(INITIAL), [0.0, 0.0]
    points = [tuple(w)]
    for t in range(STEPS):
        g = gradient(w, noisy=True, t=t)
        for j in range(2):
            u[j] = beta * u[j] + (1.0 - beta) * g[j]
            w[j] -= eta * u[j]
        points.append(tuple(w))
    return points


def adam() -> list[tuple[float, float]]:
    eta, beta1, beta2 = 0.24, 0.90, 0.999
    w, m, v = list(INITIAL), [0.0, 0.0], [0.0, 0.0]
    points = [tuple(w)]
    for t in range(1, STEPS + 1):
        g = gradient(w, noisy=True, t=t - 1)
        for j in range(2):
            m[j] = beta1 * m[j] + (1.0 - beta1) * g[j]
            v[j] = beta2 * v[j] + (1.0 - beta2) * g[j] ** 2
            m_hat = m[j] / (1.0 - beta1**t)
            v_hat = v[j] / (1.0 - beta2**t)
            w[j] -= eta * m_hat / (math.sqrt(v_hat) + EPSILON)
        points.append(tuple(w))
    return points


# Symmetric ranges make the origin and all loss contours stay inside every
# panel; the coordinates use equal semantic units on both sides of zero.
X_MIN, X_MAX = -5.0, 5.0
Y_MIN, Y_MAX = -1.6, 1.6
PANEL_W, PANEL_H = 605, 290
# 510 px / 10 w1-units = 51 px per unit.  The vertical plot height is chosen
# to use the same scale, so contour geometry is not stretched by the SVG.
PLOT_LEFT, PLOT_RIGHT, PLOT_TOP, PLOT_BOTTOM = 58, 568, 89, 253


def xy(w: tuple[float, float]) -> tuple[float, float]:
    x = PLOT_LEFT + (w[0] - X_MIN) / (X_MAX - X_MIN) * (PLOT_RIGHT - PLOT_LEFT)
    y = PLOT_BOTTOM - (w[1] - Y_MIN) / (Y_MAX - Y_MIN) * (PLOT_BOTTOM - PLOT_TOP)
    return x, y


def polyline(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.2f},{y:.2f}" for x, y in map(xy, points))


def contour(level: float) -> str:
    center_x, center_y = xy((0.0, 0.0))
    scale_x = (PLOT_RIGHT - PLOT_LEFT) / (X_MAX - X_MIN)
    scale_y = (PLOT_BOTTOM - PLOT_TOP) / (Y_MAX - Y_MIN)
    return (
        f'<ellipse class="contour" cx="{center_x:.2f}" cy="{center_y:.2f}" '
        f'rx="{math.sqrt(level) * scale_x:.2f}" '
        f'ry="{math.sqrt(level / H2) * scale_y:.2f}"/>'
    )


def panel(title: str, subtitle: str, equation: str, color: str, points: list[tuple[float, float]]) -> str:
    axis_x, axis_y = xy((0.0, 0.0))
    start_x, start_y = xy(points[0])
    end_x, end_y = xy(points[-1])
    dots = "".join(
        f'<circle class="iterate" cx="{x:.2f}" cy="{y:.2f}" r="2.5" fill="{color}"/>'
        for x, y in map(xy, points[1:-1])
    )
    # Keep every displayed contour within its panel.  The starting point lies
    # outside these low-loss contours, which is intentional: it shows descent
    # from a high-loss initial point into the narrow valley.
    contours = "".join(contour(level) for level in (0.5, 2, 4.5, 8, 12))
    return f'''<g>
      <rect class="panel" width="{PANEL_W}" height="{PANEL_H}" rx="12"/>
      <text x="{PANEL_W / 2:.0f}" y="31" text-anchor="middle" class="title">{title}</text>
      <text x="{PANEL_W / 2:.0f}" y="52" text-anchor="middle" class="subtitle">{subtitle}</text>
      <text x="{PANEL_W / 2:.0f}" y="72" text-anchor="middle" class="formula">{equation}</text>
      <line class="axis" x1="{PLOT_LEFT}" y1="{axis_y:.2f}" x2="{PLOT_RIGHT}" y2="{axis_y:.2f}"/>
      <line class="axis" x1="{axis_x:.2f}" y1="{PLOT_TOP}" x2="{axis_x:.2f}" y2="{PLOT_BOTTOM}"/>
      {contours}
      <circle cx="{axis_x:.2f}" cy="{axis_y:.2f}" r="5" fill="#172b3a"/>
      <text x="{axis_x + 8:.2f}" y="{axis_y + 19:.2f}" class="small">minimum</text>
      <polyline class="path" points="{polyline(points)}" stroke="{color}" marker-end="url(#arrow-{color[1:]})"/>
      {dots}
      <circle cx="{start_x:.2f}" cy="{start_y:.2f}" r="5.5" fill="{color}"/>
      <text x="{start_x + 8:.2f}" y="{start_y - 8:.2f}" class="small">t=0</text>
      <circle cx="{end_x:.2f}" cy="{end_y:.2f}" r="5.5" fill="{color}"/>
      <text x="{PLOT_RIGHT - 12}" y="{PLOT_BOTTOM + 19}" class="label">w₁</text>
      <text x="{axis_x + 8:.2f}" y="{PLOT_TOP + 14}" class="label">w₂</text>
    </g>'''


def marker(color: str) -> str:
    return f'<marker id="arrow-{color[1:]}" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="{color}"/></marker>'


def main() -> None:
    trajectories = {
        "GD": full_batch_gd(),
        "SGD": mini_batch_sgd(),
        "Momentum": momentum(),
        "Adam": adam(),
    }
    assert all(points[0] == INITIAL and len(points) == STEPS + 1 for points in trajectories.values())

    panels = [
        panel("Full-batch GD", "exact full gradient", "w ← w − 0.04∇L(w)", "#1261a0", trajectories["GD"]),
        panel("Mini-batch SGD", "same deterministic noisy gradient sequence", "w ← w − 0.04ĝₜ", "#d95f02", trajectories["SGD"]),
        panel("Momentum", "β = 0.90, η = 0.20", "u ← 0.9u + 0.1ĝₜ;  w ← w − 0.2u", "#16803c", trajectories["Momentum"]),
        panel("Adam", "β₁ = 0.90, β₂ = 0.999, η = 0.24", "m,v → m̂,v̂;  w ← w − 0.24m̂/(√v̂ + ε)", "#7043a6", trajectories["Adam"]),
    ]
    final_points = "; ".join(f"{name}=({p[-1][0]:.3f}, {p[-1][1]:.3f})" for name, p in trajectories.items())
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1360" height="860" viewBox="0 0 1360 860" role="img" aria-labelledby="title desc">
  <title id="title">Reproducible trajectories of GD, SGD, Momentum, and Adam</title>
  <desc id="desc">All paths are calculated for the stated quadratic loss, initial point, hyperparameters, and deterministic mini-batch noise. Final points: {final_points}.</desc>
  <defs>
    {''.join(marker(c) for c in ("#1261a0", "#d95f02", "#16803c", "#7043a6"))}
    <style>
      .panel {{ fill:#fff; stroke:#ccd6e0; stroke-width:2; }}
      .axis {{ stroke:#5d6b78; stroke-width:1.7; }}
      .contour {{ fill:none; stroke:#91bad8; stroke-width:1.8; }}
      .title {{ font:700 21px Arial, sans-serif; fill:#172b3a; }}
      .subtitle {{ font:14px Arial, sans-serif; fill:#526678; }}
      .formula {{ font:13px Arial, sans-serif; fill:#334e68; }}
      .label {{ font:14px Arial, sans-serif; fill:#526678; }}
      .small {{ font:12px Arial, sans-serif; fill:#526678; }}
      .path {{ fill:none; stroke-width:3.6; stroke-linecap:round; stroke-linejoin:round; opacity:.96; }}
      .iterate {{ opacity:.72; }}
    </style>
  </defs>
  <rect width="1360" height="860" fill="#f6f9fc"/>
  <text x="680" y="37" text-anchor="middle" style="font:700 27px Arial,sans-serif;fill:#172b3a">Reproducible optimizer trajectories / 可复现优化器轨迹</text>
  <text x="680" y="62" text-anchor="middle" style="font:15px Arial,sans-serif;fill:#526678">L(w₁,w₂) = ½(w₁² + 20w₂²),  ∇L = (w₁, 20w₂),  w⁽⁰⁾ = ({INITIAL[0]:g}, {INITIAL[1]:g}),  {STEPS} updates</text>
  <text x="680" y="84" text-anchor="middle" style="font:14px Arial,sans-serif;fill:#526678">For SGD, Momentum, and Adam: ĝₜ = ∇L(wₜ) + ξₜ, where ξₜ is the fixed deterministic sequence defined in the generator.</text>
  <g transform="translate(55 115)">{panels[0]}</g>
  <g transform="translate(700 115)">{panels[1]}</g>
  <g transform="translate(55 440)">{panels[2]}</g>
  <g transform="translate(700 440)">{panels[3]}</g>
  <rect x="55" y="750" width="1250" height="78" rx="10" fill="#e9f1f8"/>
  <text x="80" y="777" style="font:700 15px Arial,sans-serif;fill:#172b3a">How to read this figure:</text>
  <text x="80" y="801" style="font:14px Arial,sans-serif;fill:#334e68">Each dot is one numerically calculated update. Momentum smooths noisy gradients through u; Adam smooths through m and rescales each coordinate through √v̂. Their exact curves change if L, noise, or hyperparameters change.</text>
  <text x="80" y="821" style="font:14px Arial,sans-serif;fill:#334e68">考试画图只需表达典型趋势；这张图额外给出一个完全指定、可重复验证的例子。</text>
</svg>'''
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT}")
    print(f"final points after {STEPS} updates: {final_points}")


if __name__ == "__main__":
    main()
