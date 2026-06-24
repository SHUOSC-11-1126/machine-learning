# Session 4 Exam Scope Update Design

## Goal

Record the user's confirmed latest teacher update that Session 4 is not tested, and prevent repository review materials from directing exam preparation toward Session 4.

## Scope

- Do not modify `files-from-teacher/` or its Git submodule state.
- Update the highest-priority scope document to state that the main exam line is Sessions 0--3 and 5--7, with Session 4 explicitly excluded by the latest confirmed update.
- Remove Session 4 study tasks from `agents/plan.md` and list Session 4 among out-of-scope sessions.
- Correct older audit and disclosure documents so they no longer describe Session 4 as part of the tested main line.
- Preserve historical wording only when it is clearly labeled as superseded.

## Approach

The change is documentation-only. `review/highest-priority-exam-scope-2026-06-17.md` becomes the canonical repository record for the newer confirmation. All dependent summaries point to that record rather than independently asserting the older `session-0` through `session-7` rule.

## Files

- `review/highest-priority-exam-scope-2026-06-17.md`: canonical range rule and Session 4 exclusion.
- `agents/plan.md`: exam review plan, Session 4 tasks, and scope assumptions.
- `review/essential-cleaned-audit.md`: current-scope and conflict-resolution statements.
- `review/exam-disclosures-from-audio-video.md`: time-stamped disclosure summary; retain the 2026-06-17 statement as historical and add the newer override.
- `review/classmate-ml-revision-all-audit.md`: replace conditional handling of the Session 4 claim with confirmed handling.

## Verification

Run targeted `rg` checks to confirm that no current-scope claim includes Session 4, that `agents/plan.md` has no Session 4 study tasks, and that the canonical scope document explicitly excludes it. Inspect the resulting diff to ensure the teacher submodule and unrelated working-tree changes are untouched.
