# L1/L2 First-Touch Geometry Lesson Design

## Goal

Create a self-contained HTML revision lesson that explains the first-touch geometry in `BagOfQuestions-session-6-ah.md` without Markdown/ASCII alignment failures.

## Scope

- Output: `lessons/0003-l1-l2-first-touch-geometry.html`.
- Two inline SVG panels placed side by side on wide screens and stacked on narrow screens.
- Left panel: L1 feasible set as a diamond; data-loss ellipses; an annotated first-touch point at a diamond corner; coordinate axes; a concise sparse/zero-weight annotation.
- Right panel: L2 feasible set as a circle; data-loss ellipses; an annotated first-touch point; coordinate axes; a concise smooth-shrinkage annotation.
- Below the diagrams: Chinese, step-by-step explanation of contours, feasibility, expansion, and first touch; English-first exam-ready answer with Chinese translation; source path.
- No non-teacher sources and no extra course topics.

## Diagram semantics

1. Each plane uses `(w_1, w_2)` parameter coordinates.
2. The nested ellipses are equal-data-loss contours. Inner contours have lower data loss.
3. The feasible set is centered at the origin. The unconstrained loss minimum is deliberately outside it.
4. The highlighted point is the first feasible point reached by expanding the contour from the unconstrained minimum. It is therefore the lowest data-loss feasible parameter setting.
5. The L1 panel makes the corner/axis relationship visually explicit; the L2 panel distinguishes its smooth circle.

## Quality checks

- Render locally and verify SVG text, arrows, axes, labels, and touch points do not overlap at desktop and narrow widths.
- Confirm the stated L1/L2 formulas and geometry match `BagOfQuestions-session-6-ah.md`.
- Confirm all source paths are present and no Markdown ASCII art is used for the geometry.
