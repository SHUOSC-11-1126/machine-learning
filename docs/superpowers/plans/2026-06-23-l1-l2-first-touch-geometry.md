# L1/L2 First-Touch Geometry Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a rendered, source-grounded HTML lesson that accurately explains L1/L2 first-touch geometry.

**Architecture:** One standalone lesson file owns its CSS, explanatory content, and two inline SVG diagrams. The diagrams use a shared visual grammar: parameter axes, feasible region, nested data-loss contours, an unconstrained optimum, and a marked first-touch solution.

**Tech Stack:** Semantic HTML5, embedded CSS, inline SVG, local browser/render inspection.

---

### Task 1: Build and verify the L1/L2 geometry lesson

**Files:**
- Create: `lessons/0003-l1-l2-first-touch-geometry.html`
- Test: local render or browser inspection of `lessons/0003-l1-l2-first-touch-geometry.html`

- [ ] **Step 1: Create the standalone lesson**

Include the following required content and SVG semantics:

```html
<section class="panels">
  <figure>
    <svg viewBox="0 0 560 420" role="img" aria-label="L1 diamond with loss contours and a first-touch point"></svg>
    <figcaption>L1: diamond constraint; first touch at a corner can set a weight to zero.</figcaption>
  </figure>
  <figure>
    <svg viewBox="0 0 560 420" role="img" aria-label="L2 circle with loss contours and a first-touch point"></svg>
    <figcaption>L2: circular constraint; first touch usually gives smooth shrinkage.</figcaption>
  </figure>
</section>
```

Each SVG must include visible `w₁`/`w₂` axes, nested ellipses centered outside the feasible region, the correct L1/L2 boundary, an arrow or label for the unconstrained optimum, and a distinct highlighted first-touch point. The explanatory prose must define contours, feasibility, the expand-until-first-touch reasoning, and L1 sparsity. Include an English-first exam answer and the exact Bag source path.

- [ ] **Step 2: Check source and structural requirements**

Run:

```bash
rg -n "BagOfQuestions-session-6-ah\.md|\\|w_1\\|\\+\\|w_2\\||w_1\^2\\+w_2\^2|first-touch|First-touch|L1|L2" lessons/0003-l1-l2-first-touch-geometry.html
```

Expected: the source, both penalty formulas, both regularization names, and first-touch explanation are present.

- [ ] **Step 3: Render and visually inspect**

Run the repository's available local HTML-rendering route, or open the local lesson in the in-app browser. Verify at desktop and narrow widths that SVG axes, labels, arrows, contours, feasible regions, and highlighted touch points are visible and do not overlap.

- [ ] **Step 4: Record verification result**

Report the rendered lesson path and whether the diagrams passed the structural and visual checks. Do not modify `files-from-teacher/`.
