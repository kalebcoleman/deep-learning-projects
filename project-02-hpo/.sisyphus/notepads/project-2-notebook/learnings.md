## 2026-03-20 Task 1: Notebook Scaffold

### What was built
- notebooks/hpo_analysis.ipynb created with 12 cells (8 markdown, 4 code)
- EXACT PDF question text reproduced verbatim in Q1-Q4 heading cells
- Planned sequence: Title → Setup → Q1/Q2/Q3/Q4 placeholders → Final Summary → Reproducibility Appendix

### Key decisions
- "Assignment Context" merged into "Setup" section to satisfy the "Setup" heading QA requirement
- Placeholder code cells (TODO comments) inserted for Q1-Q4 so Tasks 2-7 can fill them in
- Reproducibility Appendix includes seed 499, execution command, dataset URL

### Issues/gotchas
- The plan QA references "Setup" heading - the original design had "Assignment Context" instead; fixed by renaming
- nbformat 4.5 used (safe, Jupyter-compatible)
- No execution_count on code cells (clean kernel start)

### Files modified
- notebooks/hpo_analysis.ipynb (created)

## 2026-03-20 Implementation + Verification

- Root cause 1: `nbconvert` defaulted to Homebrew Jupyter Python instead of the Conda env with `torch`; fixed by binding notebook kernelspec to `school`.
- Root cause 2: `BCELoss` input/target shape mismatch caused by `.squeeze()` on model outputs; fixed by keeping outputs as shape `[batch, 1]`.
- Verification: notebook executed cleanly twice via `jupyter nbconvert --execute`, and key result sections matched exactly across reruns.
- Best observed configuration: weight decay `0.001` with learning rate `1e-3`.
