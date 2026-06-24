# Session 4 Exam Scope Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update review documentation to exclude Session 4 from the current final-exam scope after the user's confirmed latest teacher update.

**Architecture:** Treat `review/highest-priority-exam-scope-2026-06-17.md` as the canonical current-scope record. Update downstream review summaries and remove Session 4 tasks from the review plan; retain older 2026-06-17 scope statements only as superseded historical records.

**Tech Stack:** Markdown, Git, ripgrep.

---

### Task 1: Update the canonical exam-scope record

**Files:**

- Modify: `review/highest-priority-exam-scope-2026-06-17.md:22-30`
- Modify: `review/highest-priority-exam-scope-2026-06-17.md:238-248`

- [ ] **Step 1: Replace the current main-line rule**

State that main exam preparation includes Sessions 0--3 and 5--7, and that Session 4 is excluded by the latest user-confirmed teacher update. Keep extra scope as Sessions 201, 202, and 203.

- [ ] **Step 2: Add the explicit Session 4 exclusion to the scope nuance**

State that Session 4 backpropagation, computation-graph, layer-interface, and implementation material are not current exam-preparation topics.

- [ ] **Step 3: Verify canonical wording**

Run: `rg -n -C 2 'Session 4|session-4|Sessions 0' review/highest-priority-exam-scope-2026-06-17.md`

Expected: the document states that Session 4 is excluded and does not describe `session-0` through `session-7` as the current main line.

### Task 2: Remove Session 4 from the active study plan

**Files:**

- Modify: `agents/plan.md:7`
- Modify: `agents/plan.md:21`
- Modify: `agents/plan.md:114-122`
- Modify: `agents/plan.md:184`
- Modify: `agents/plan.md:211`

- [ ] **Step 1: Update scope summaries**

Change every active scope summary from `session-0` through `session-7` to Sessions 0--3 and 5--7, with Session 4 excluded by the latest confirmed update.

- [ ] **Step 2: Delete Session 4 study entries**

Remove the backpropagation and layer-interface tasks that cite `files-from-teacher/session-4/` and `BagOfQuestions-session-4-*`.

- [ ] **Step 3: Add Session 4 to out-of-scope sessions**

Add `session-4` to the existing out-of-scope list and state that it remains excluded unless a newer teacher update reinstates it.

- [ ] **Step 4: Verify no active Session 4 tasks remain**

Run: `rg -n -C 1 'session-4|Session 4|backpropagation|Layer Interface' agents/plan.md`

Expected: no Session 4 review task remains; only the explicit out-of-scope statement may mention it.

### Task 3: Synchronize dependent review documents

**Files:**

- Modify: `review/essential-cleaned-audit.md:7-10,150,158`
- Modify: `review/exam-disclosures-from-audio-video.md:17-28,117-126,309`
- Modify: `review/classmate-ml-revision-all-audit.md:219-227`

- [ ] **Step 1: Update audit conclusions**

Replace assertions that Session 4 is part of `session-0` through `session-7` with the current exclusion, and replace the old conditional Session 4 treatment with the confirmed teacher update.

- [ ] **Step 2: Preserve dated historical disclosure accurately**

In `review/exam-disclosures-from-audio-video.md`, identify the 2026-06-17 Session 0--7 statement as superseded by the later confirmed Session 4 exclusion. Update operational review recommendations to omit Session 4.

- [ ] **Step 3: Verify dependent documents**

Run: `rg -n -C 1 'session-0.*session-7|0-7|0–7|Session 4|session-4' review/essential-cleaned-audit.md review/exam-disclosures-from-audio-video.md review/classmate-ml-revision-all-audit.md`

Expected: every remaining older Session 0--7 reference is explicitly historical or superseded; current scope excludes Session 4.

### Task 4: Perform scope-consistency verification

**Files:**

- Verify: `review/highest-priority-exam-scope-2026-06-17.md`
- Verify: `agents/plan.md`
- Verify: `review/essential-cleaned-audit.md`
- Verify: `review/exam-disclosures-from-audio-video.md`
- Verify: `review/classmate-ml-revision-all-audit.md`

- [ ] **Step 1: Run cross-document consistency checks**

Run: `rg -n -i -C 1 'current (main )?scope.*session-4|session-4.*(not tested|out of scope|excluded)|main.*session-0.*session-7' review agents --glob '*.md'`

Expected: Session 4 is excluded in current-scope statements; any legacy 0--7 statement is visibly superseded.

- [ ] **Step 2: Inspect the working-tree diff**

Run: `git diff -- review agents docs/superpowers`

Expected: only the five scope documents and the new design/plan files changed; `files-from-teacher` and unrelated user changes are absent from the diff.
