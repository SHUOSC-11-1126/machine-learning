"""Generate mathematically aligned first-touch SVG diagrams without third-party packages."""

from math import cos, pi, sin, sqrt
from pathlib import Path


OUT = Path(__file__).parents[1] / "lessons" / "assets"
WIDTH, HEIGHT = 740, 570
LEFT, RIGHT, TOP, BOTTOM = 92, 690, 48, 500
XMIN, XMAX, YMIN, YMAX = -2.1, 3.4, -1.8, 3.8
SCALE_X = (RIGHT - LEFT) / (XMAX - XMIN)
SCALE_Y = (BOTTOM - TOP) / (YMAX - YMIN)
SCALE = min(SCALE_X, SCALE_Y)


def px(x):
    return LEFT + (x - XMIN) * SCALE_X


def py(y):
    return BOTTOM - (y - YMIN) * SCALE_Y


def point(x, y):
    return f"{px(x):.1f},{py(y):.1f}"


def ellipse(cx, cy, sx, sy, level, color, width):
    return (
        f'<ellipse cx="{px(cx):.1f}" cy="{py(cy):.1f}" '
        f'rx="{sqrt(level) * sx * SCALE_X:.1f}" ry="{sqrt(level) * sy * SCALE_Y:.1f}" '
        f'fill="none" stroke="{color}" stroke-width="{width}"/>'
    )


def header(title, desc):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title><desc id="desc">{desc}</desc>
  <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L9,5 L0,10 Z" fill="#d4571e"/></marker></defs>
  <rect width="{WIDTH}" height="{HEIGHT}" rx="18" fill="#fbfcfe"/>
  <style>text{{font-family:Arial,sans-serif;fill:#263846}} .small{{font-size:18px}} .label{{font-size:21px;font-weight:700}} .note{{font-size:18px;fill:#52616e}} .orange{{fill:#b94b1a}} .purple{{fill:#7654a8}} .blue{{fill:#176fb3}} .green{{fill:#178061}}</style>
  <line x1="{px(XMIN):.1f}" y1="{py(0):.1f}" x2="{px(XMAX):.1f}" y2="{py(0):.1f}" stroke="#52616e" stroke-width="2.4"/>
  <line x1="{px(0):.1f}" y1="{py(YMIN):.1f}" x2="{px(0):.1f}" y2="{py(YMAX):.1f}" stroke="#52616e" stroke-width="2.4"/>
  <text x="{px(XMAX)-6:.1f}" y="{py(0)+31:.1f}" class="label" text-anchor="end">w₁</text>
  <text x="{px(0)-10:.1f}" y="{py(YMAX)+20:.1f}" class="label" text-anchor="end">w₂</text>
  <text x="{px(0)-12:.1f}" y="{py(0)+29:.1f}" class="small" text-anchor="end">0</text>
'''


def footer():
    return "</svg>\n"


def write_l1():
    c, ox, oy, sx, sy = 1.3, 0.0, 3.1, 1.2, 1.0
    touch = (0.0, c)
    touch_loss = ((touch[0] - ox) / sx) ** 2 + ((touch[1] - oy) / sy) ** 2
    diamond = " ".join(point(*p) for p in [(0, c), (c, 0), (0, -c), (-c, 0)])
    svg = header(
        "L1 first-touch geometry",
        "The L1 diamond is centered at the origin. Elliptical data-loss contours centered at the unconstrained minimum first touch the upper diamond corner, where w1 equals zero.",
    )
    svg += f'''  <polygon points="{diamond}" fill="#dceef9" stroke="#176fb3" stroke-width="3"/>
  {ellipse(ox, oy, sx, sy, 0.35, '#9bc7e5', 2)}
  {ellipse(ox, oy, sx, sy, 1.3, '#6caad4', 2.4)}
  {ellipse(ox, oy, sx, sy, touch_loss, '#176fb3', 3.5)}
  <circle cx="{px(ox):.1f}" cy="{py(oy):.1f}" r="8" fill="#7654a8"/>
  <circle cx="{px(touch[0]):.1f}" cy="{py(touch[1]):.1f}" r="12" fill="#d4571e" stroke="white" stroke-width="3"/>
  <line x1="{px(0.72):.1f}" y1="{py(2.20):.1f}" x2="{px(touch[0]):.1f}" y2="{py(touch[1]):.1f}" stroke="#d4571e" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="{px(0.76):.1f}" y="{py(2.36):.1f}" class="label orange">first touch</text>
  <text x="{px(0.76):.1f}" y="{py(2.08):.1f}" class="small orange">corner: w₁ = 0</text>
  <text x="{px(0.24):.1f}" y="{py(3.26):.1f}" class="small purple">unregularized minimum</text>
  <text x="{px(-1.80):.1f}" y="{py(-0.36):.1f}" class="label blue">L1 feasible set</text>
  <text x="{px(-1.80):.1f}" y="{py(-0.68):.1f}" class="small blue">|w₁| + |w₂| ≤ c</text>
'''
    (OUT / "l1-first-touch.svg").write_text(svg + footer(), encoding="utf-8")


def l2_touch(c, ox, oy, sx, sy):
    best = (float("inf"), 0.0, 0.0)
    for i in range(100_001):
        theta = 2 * pi * i / 100_000
        x, y = c * cos(theta), c * sin(theta)
        value = ((x - ox) / sx) ** 2 + ((y - oy) / sy) ** 2
        if value < best[0]:
            best = (value, x, y)
    return best


def write_l2():
    c, ox, oy, sx, sy = 1.35, 2.05, 2.15, 1.45, 0.82
    touch_loss, tx, ty = l2_touch(c, ox, oy, sx, sy)
    svg = header(
        "L2 first-touch geometry",
        "The L2 circle is centered at the origin. Elliptical data-loss contours centered at the unconstrained minimum first touch the circle at a smooth non-axis point.",
    )
    svg += f'''  <circle cx="{px(0):.1f}" cy="{py(0):.1f}" r="{c * SCALE:.1f}" fill="#ddf3e9" stroke="#178061" stroke-width="3"/>
  {ellipse(ox, oy, sx, sy, 0.35, '#9bc7e5', 2)}
  {ellipse(ox, oy, sx, sy, 1.3, '#6caad4', 2.4)}
  {ellipse(ox, oy, sx, sy, touch_loss, '#176fb3', 3.5)}
  <circle cx="{px(ox):.1f}" cy="{py(oy):.1f}" r="8" fill="#7654a8"/>
  <circle cx="{px(tx):.1f}" cy="{py(ty):.1f}" r="12" fill="#d4571e" stroke="white" stroke-width="3"/>
  <line x1="{px(1.22):.1f}" y1="{py(1.02):.1f}" x2="{px(tx):.1f}" y2="{py(ty):.1f}" stroke="#d4571e" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="{px(1.25):.1f}" y="{py(1.22):.1f}" class="label orange">first touch</text>
  <text x="{px(1.25):.1f}" y="{py(0.94):.1f}" class="small orange">smooth boundary</text>
  <text x="{px(1.10):.1f}" y="{py(2.88):.1f}" class="small purple">unregularized minimum</text>
  <text x="{px(-1.84):.1f}" y="{py(-0.36):.1f}" class="label green">L2 feasible set</text>
  <text x="{px(-1.84):.1f}" y="{py(-0.68):.1f}" class="small green">w₁² + w₂² ≤ c²</text>
'''
    (OUT / "l2-first-touch.svg").write_text(svg + footer(), encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    write_l1()
    write_l2()
