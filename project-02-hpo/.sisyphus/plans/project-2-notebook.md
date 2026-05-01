# Project 2 Consolidated Notebook

## TL;DR
> **Summary**: Replace `notebooks/hpo_analysis.ipynb` with a MAT499 submission notebook that contains the full Project 2 workflow inline: deterministic setup, Sonar data loading, model/training helpers, 5-fold cross-validation experiments, result tables, and written answers.
> **Deliverables**:
> - Updated `notebooks/hpo_analysis.ipynb`
> - Inline model/training/evaluation code with no `src/` imports
> - Fold-level and aggregate result tables for Q1-Q3
> - Written markdown answers for Q1-Q4
> - Clean-kernel execution evidence and deterministic rerun checks
> **Effort**: Medium
> **Parallel**: YES - 2 waves
> **Critical Path**: Task 1 -> Task 2 -> Task 3 -> Task 4 -> Task 5 -> Task 6 -> Task 7

## Context
### Original Request
Convert Project 2 into a single `.ipynb` submission, and include the class files inline so everything is visible in one place for the instructor.

### Interview Summary
- Use MAT499 seed behavior (`499` for `random`, `numpy`, and `torch`).
- Replace `notebooks/hpo_analysis.ipynb` instead of creating a new notebook.
- Keep scope notebook-only; do not rely on helper modules outside the notebook.
- Preserve the assignment's requested experiment structure: Q1 baseline, Q2 dropout and weight decay comparisons, Q3 learning-rate sweep, Q4 cross-validation explanation.

### Metis Review (gaps addressed)
- Quote the assignment prompts directly from `project_2.pdf` instead of paraphrasing.
- Keep experiments controlled: identical folds, preprocessing, epochs, batch size, optimizer family, and metric definitions across Q1-Q3 unless the prompt explicitly changes them.
- Make the data loader robust: local-override variable allowed in the notebook, but default to the course GitHub Sonar CSV URL and fail with `Failed to load Sonar dataset` on bad input.
- Enforce determinism beyond the seed value by fixing fold indices, `DataLoader` generator state, and deterministic torch flags.
- Require clean-kernel notebook execution and deterministic rerun comparison as non-negotiable QA gates.

## Work Objectives
### Core Objective
Produce one readable, fully executable notebook that answers every Project 2 requirement in order and shows all model/training code inline so the grader never has to open separate class files.

### Deliverables
- `notebooks/hpo_analysis.ipynb` rewritten as the Project 2 submission notebook
- Inline code cells for setup, data loading, preprocessing, model definition, training loop, evaluation, and experiment runners
- Markdown cells that reproduce the assignment prompts and provide written conclusions for Q1-Q4
- Result tables with per-fold values plus `mean` and `std`
- Reproducibility/verification evidence from clean execution

### Definition of Done (verifiable conditions with commands)
- `jupyter nbconvert --to notebook --execute "notebooks/hpo_analysis.ipynb" --output /tmp/hpo_submission_run.ipynb --ExecutePreprocessor.timeout=1200` exits `0`
- `python - <<'PY'` JSON checks over `/tmp/hpo_submission_run.ipynb` confirm headings for `Setup`, `Question 1`, `Question 2`, `Question 3`, and `Question 4`
- `python - <<'PY'` JSON checks confirm a code cell contains `SEED = 499` and the Sonar CSV URL
- `python - <<'PY'` JSON checks confirm rendered outputs include 5-fold tables with `mean` and `std`
- `python - <<'PY'` rerun comparison over two executed notebook copies confirms deterministic summaries within `1e-6`

### Must Have
- Exact Project 2 questions reproduced in markdown cells
- `SEED = 499` visible near the top of the notebook
- Sonar dataset load, validation, and preprocessing performed inside the notebook
- Inline MLP implementation with baseline, dropout, and weight-decay configurations
- Q1-Q3 experiment results expressed as tables and referenced in the written conclusions
- Q4 explanation tied to observed fold variability rather than generic theory only

### Must NOT Have (guardrails, AI slop patterns, scope boundaries)
- No imports from `src/model_factory.py`, `src/train.py`, `src/search.py`, or `src/metrics.py`
- No scope creep into CI, packaging, README edits, or environment-file work
- No extra model families, extra datasets, or broad hyperparameter searches beyond the assignment
- No notebook sections that assume the grader will inspect separate files for hidden logic
- No unverifiable claims like "the results looked good" without table-backed evidence

## Verification Strategy
> ZERO HUMAN INTERVENTION - all verification is agent-executed.
- Test decision: none outside the notebook; verification is notebook execution plus machine checks over executed notebook JSON
- QA policy: every implementation task includes a happy path and a failure/edge scenario using Bash-driven notebook or JSON validation
- Evidence: `.sisyphus/evidence/task-{N}-{slug}.{ext}`

## Execution Strategy
### Parallel Execution Waves
> Target: 5-8 tasks per wave. Extract shared notebook foundations first, then parallelize experiment sections once shared helpers exist.

Wave 1: Tasks 1-3 (notebook skeleton, deterministic data pipeline, inline helper stack)
Wave 2: Tasks 4-7 (Q1 baseline, Q2 regularization, Q3 learning-rate sweep, Q4 narrative/final packaging)

### Dependency Matrix (full, all tasks)
- Task 1 blocks Tasks 2-7
- Task 2 blocks Tasks 3-7
- Task 3 blocks Tasks 4-7
- Task 4 blocks Tasks 5-7
- Task 5 blocks Tasks 6-7
- Task 6 informs Task 7
- Task 7 must complete before Final Verification Wave

### Agent Dispatch Summary (wave -> task count -> categories)
- Wave 1 -> 3 tasks -> `writing`, `python-development`
- Wave 2 -> 4 tasks -> `python-development`, `writing`, `unspecified-high`
- Final Verification -> 4 tasks -> `oracle`, `unspecified-high`, `deep`

## TODOs
> Implementation + Test = ONE task. Never separate.
> EVERY task MUST have: Agent Profile + Parallelization + QA Scenarios.

- [x] 1. Rebuild the notebook structure around the exact assignment flow

  **What to do**: Replace the current `notebooks/hpo_analysis.ipynb` content with a clean Project 2 narrative that starts with title/context, reproduces the assignment prompts from `project_2.pdf`, and establishes ordered sections for setup, data pipeline, inline helpers, Question 1, Question 2, Question 3, Question 4, final summary, and reproducibility appendix.
  **Must NOT do**: Do not leave HPO-only framing from the old notebook, do not paraphrase the question text when the PDF provides the exact wording, and do not place implementation details in hidden or collapsed external files.

  **Recommended Agent Profile**:
  - Category: `writing` - Reason: the primary work is notebook narrative structure and prompt framing.
  - Skills: `jupyter-notebook` - needed for notebook organization and safe scaffold editing.
  - Omitted: `frontend-design` - notebook presentation matters, but this is not a UI design problem.

  **Parallelization**: Can Parallel: NO | Wave 1 | Blocks: Tasks 2-7 | Blocked By: none

  **References** (executor has NO interview context - be exhaustive):
  - Pattern: `notebooks/hpo_analysis.ipynb` - existing notebook file to replace in place.
  - Reference: `project_2.pdf` - source of exact Q1-Q4 wording and experiment requirements.
  - Reference: `.sisyphus/plans/project-2-notebook.md` - authoritative scope, guardrails, and packaging decisions for execution.
  - Reference: `README.md` - repository framing showing notebook is the intended analysis surface.

  **Acceptance Criteria** (agent-executable only):
  - [ ] `python - <<'PY'` over `notebooks/hpo_analysis.ipynb` confirms markdown cells contain `Question 1`, `Question 2`, `Question 3`, and `Question 4`.
  - [ ] `python - <<'PY'` confirms there is a markdown heading for `Setup` and one for `Reproducibility Appendix`.
  - [ ] `python - <<'PY'` confirms notebook metadata remains valid JSON and cell order matches the planned section sequence.

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```text
  Scenario: Happy path structure check
    Tool: Bash
    Steps: Run a Python JSON inspection script that extracts markdown headings from `notebooks/hpo_analysis.ipynb` and compares them to the expected ordered list: Setup, Data Loading and Validation, Preprocessing, Inline Helpers, Question 1, Question 2, Question 3, Question 4, Final Summary, Reproducibility Appendix.
    Expected: Script exits 0 and prints the ordered heading list with no missing sections.
    Evidence: .sisyphus/evidence/task-1-structure.json

  Scenario: Failure path missing prompt text
    Tool: Bash
    Steps: Run a Python JSON inspection script that fails if any of `Question 1`, `Question 2`, `Question 3`, or `Question 4` headings are absent or duplicated.
    Expected: Script exits non-zero with a clear missing/duplicate-heading message when the structure is wrong.
    Evidence: .sisyphus/evidence/task-1-structure-error.log
  ```

  **Commit**: NO | Message: `chore(notebook): scaffold project 2 submission structure` | Files: `notebooks/hpo_analysis.ipynb`

- [ ] 2. Add deterministic setup, Sonar loading, and preprocessing cells

  **What to do**: Insert top-of-notebook code cells that define `SEED = 499`, seed `random`, `numpy`, and `torch`, enable deterministic torch behavior, define a local-override path variable plus the default course GitHub Sonar CSV URL, load the dataset, validate the expected `208 x 61` shape and binary labels, encode the target for binary classification, and standardize features in a fold-safe way.
  **Must NOT do**: Do not silently continue on bad data, do not hardcode a local absolute path, and do not fit preprocessing on full data before cross-validation splits.

  **Recommended Agent Profile**:
  - Category: `python-development` - Reason: data loading, deterministic behavior, and preprocessing logic are Python-heavy.
  - Skills: `python-development`, `jupyter-notebook` - needed for reproducible notebook code and safe data workflow.
  - Omitted: `database-design` - dataset loading here is file-based, not schema design.

  **Parallelization**: Can Parallel: NO | Wave 1 | Blocks: Tasks 3-7 | Blocked By: Task 1

  **References** (executor has NO interview context - be exhaustive):
  - Pattern: `notebooks/hpo_analysis.ipynb` - destination notebook for all data logic.
  - Requirement: `project_2.pdf` - seed and dataset expectations.
  - External: `https://raw.githubusercontent.com/benjaminmlucas/MAT499/refs/heads/main/module_2/sonar.csv` - default Sonar CSV source.
  - Reference: `.sisyphus/plans/project-2-notebook.md` - confirms MAT499 seed, notebook-only boundary, and data-loader guardrails.

  **Acceptance Criteria** (agent-executable only):
  - [ ] `python - <<'PY'` over notebook JSON confirms a code cell contains `SEED = 499` and seeds `random`, `numpy`, and `torch`.
  - [ ] Clean notebook execution reaches the dataset-validation cell and emits evidence of `208` rows, `61` columns, and two target classes.
  - [ ] Temporary bad-URL execution fails with `Failed to load Sonar dataset`.

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```text
  Scenario: Happy path data load
    Tool: Bash
    Steps: Execute `jupyter nbconvert --to notebook --execute "notebooks/hpo_analysis.ipynb" --output /tmp/task2-run.ipynb --ExecutePreprocessor.timeout=1200`, then run a Python script against `/tmp/task2-run.ipynb` to assert rendered output contains the dataset shape `208 x 61` (or equivalent row/column evidence) and two classes.
    Expected: Both commands exit 0; the validation output confirms the dataset loaded correctly.
    Evidence: .sisyphus/evidence/task-2-data-load.json

  Scenario: Failure path bad dataset URL
    Tool: Bash
    Steps: Create a temporary notebook copy in `/tmp`, replace the Sonar URL string with an invalid URL in that copy, execute it with `jupyter nbconvert`, and capture stderr/stdout.
    Expected: Notebook execution exits non-zero and logs `Failed to load Sonar dataset`.
    Evidence: .sisyphus/evidence/task-2-data-load-error.log
  ```

  **Commit**: NO | Message: `feat(notebook): add deterministic sonar data pipeline` | Files: `notebooks/hpo_analysis.ipynb`

- [ ] 3. Inline the model, fold runner, and metric helpers inside the notebook

  **What to do**: Add notebook code cells defining the two-hidden-layer MLP builder, optional dropout handling, optimizer configuration that supports baseline and weight decay, mini-batch training loop, evaluation helpers for loss and classification error, k-fold split runner with fixed folds, and small smoke-test cells that verify output tensor shapes and fold bookkeeping before the full experiments run.
  **Must NOT do**: Do not import helper logic from `src/`, do not vary architecture/optimizer defaults across questions unless explicitly required, and do not hide fold generation logic in implicit notebook state.

  **Recommended Agent Profile**:
  - Category: `python-development` - Reason: this is the core PyTorch implementation block.
  - Skills: `python-development`, `jupyter-notebook` - needed for clean inline model/training code.
  - Omitted: `backend-development` - there is no service or API component.

  **Parallelization**: Can Parallel: NO | Wave 1 | Blocks: Tasks 4-7 | Blocked By: Task 2

  **References** (executor has NO interview context - be exhaustive):
  - Pattern: `project_2.pdf` - baseline architecture is 60-input -> 128 -> 64 -> binary output, 200 epochs, batch size 16, Adam default LR.
  - Destination: `notebooks/hpo_analysis.ipynb` - inline helper definitions must live here.
  - Non-reference: `src/model_factory.py`, `src/train.py`, `src/metrics.py`, `src/search.py` - placeholders only; do not depend on them.
  - Reference: `.sisyphus/plans/project-2-notebook.md` - confirms notebook-only implementation and controlled comparison rules.

  **Acceptance Criteria** (agent-executable only):
  - [ ] `python - <<'PY'` notebook JSON inspection confirms there are inline code cells for model definition, training loop, evaluation helper, and fold runner.
  - [ ] Executed notebook output includes a smoke test showing the model accepts a feature batch of width `60` and emits binary-classification-compatible output.
  - [ ] Executed notebook output shows exactly 5 fold identifiers were created before the experiment sections run.

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```text
  Scenario: Happy path helper smoke tests
    Tool: Bash
    Steps: Execute the notebook to `/tmp/task3-run.ipynb`, then run a Python script that asserts rendered outputs contain model forward-pass evidence, fold-count evidence equal to 5, and helper section headings.
    Expected: Notebook executes successfully and helper smoke-test outputs are present.
    Evidence: .sisyphus/evidence/task-3-helpers.json

  Scenario: Failure path fold mismatch guard
    Tool: Bash
    Steps: Run a Python JSON inspection script that fails if Q1/Q2/Q3 sections do not reference the same stored fold IDs or if fold count differs from 5.
    Expected: Script exits non-zero with a fold-mismatch message when the notebook loses shared fold state.
    Evidence: .sisyphus/evidence/task-3-helpers-error.log
  ```

  **Commit**: NO | Message: `feat(notebook): add inline pytorch helpers` | Files: `notebooks/hpo_analysis.ipynb`

- [ ] 4. Implement Question 1 baseline 5-fold cross-validation

  **What to do**: Add the Q1 notebook section that runs the baseline model with hidden sizes `128` and `64`, no dropout, no weight decay, 200 epochs, batch size 16, and Adam default learning rate on the fixed 5 folds. Capture training loss, training error, validation loss, and validation error for each fold, then present one results table with all five folds plus `mean` and `std`, followed by a markdown conclusion that comments on average train/validation behavior.
  **Must NOT do**: Do not change the fold definitions after Task 3, do not report only aggregate values, and do not omit either loss or error metrics from the table.

  **Recommended Agent Profile**:
  - Category: `python-development` - Reason: controlled CV execution and metric aggregation are the key work.
  - Skills: `python-development`, `jupyter-notebook` - needed for experiment logic and notebook presentation.
  - Omitted: `code-documentation` - markdown commentary is required, but the main challenge is experiment execution.

  **Parallelization**: Can Parallel: NO | Wave 2 | Blocks: Tasks 5-7 | Blocked By: Task 3

  **References** (executor has NO interview context - be exhaustive):
  - Requirement: `project_2.pdf` - Q1 baseline architecture and reporting requirements.
  - Destination: `notebooks/hpo_analysis.ipynb` - Q1 section lives here.
  - Reference: `.sisyphus/plans/project-2-notebook.md` - required metrics and narrative expectations.

  **Acceptance Criteria** (agent-executable only):
  - [ ] Executed notebook output contains a Q1 table with 5 fold rows and summary rows/columns for `mean` and `std`.
  - [ ] The Q1 table includes `training_loss`, `training_error`, `validation_loss`, and `validation_error` fields or equivalent labels.
  - [ ] A markdown cell immediately after the table comments on average training vs validation performance using those metrics.

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```text
  Scenario: Happy path baseline table
    Tool: Bash
    Steps: Execute the notebook to `/tmp/task4-run.ipynb`, then run a Python script that extracts rendered table text from the Q1 section and asserts the presence of fold identifiers 1-5, metric labels for train/validation loss/error, and `mean` and `std`.
    Expected: Script exits 0 and reports all required baseline metrics present.
    Evidence: .sisyphus/evidence/task-4-q1.json

  Scenario: Failure path missing metrics guard
    Tool: Bash
    Steps: Run a Python verification script that fails if any one of the four required Q1 metrics is absent from the executed notebook output.
    Expected: Script exits non-zero with the missing metric name.
    Evidence: .sisyphus/evidence/task-4-q1-error.log
  ```

  **Commit**: NO | Message: `feat(notebook): add q1 baseline cross-validation` | Files: `notebooks/hpo_analysis.ipynb`

- [ ] 5. Implement Question 2 controlled dropout and weight-decay comparisons

  **What to do**: Add the Q2 section that reruns the same fixed 5 folds twice: first with dropout `0.3` and no weight decay, then with weight decay `0.001` and no dropout. Produce one results table for the dropout model and one for the weight-decay model, each with per-fold metrics plus `mean` and `std`, then add markdown conclusions answering whether dropout helped, whether weight decay helped, and which regularizer worked better overall.
  **Must NOT do**: Do not change seed, folds, preprocessing, architecture widths, epoch count, batch size, or optimizer family between baseline/dropout/weight-decay runs; do not combine dropout and weight decay in the same comparison unless explicitly called out as out of scope.

  **Recommended Agent Profile**:
  - Category: `python-development` - Reason: this is experiment-control work with repeated evaluation.
  - Skills: `python-development`, `jupyter-notebook` - needed for reproducible comparisons and notebook output.
  - Omitted: `code-refactoring` - the work is additive notebook experimentation, not refactor cleanup.

  **Parallelization**: Can Parallel: NO | Wave 2 | Blocks: Tasks 6-7 | Blocked By: Task 4

  **References** (executor has NO interview context - be exhaustive):
  - Requirement: `project_2.pdf` - Q2 regularization requirements.
  - Destination: `notebooks/hpo_analysis.ipynb` - Q2 section lives here.
  - Dependency: Task 4 results - use the same baseline fold setup for direct comparison.
  - Reference: `.sisyphus/plans/project-2-notebook.md` - confirms dropout `0.3` and weight decay `0.001` values.

  **Acceptance Criteria** (agent-executable only):
  - [ ] Executed notebook output contains separate labeled tables for baseline, dropout, and weight-decay results, each with 5 folds plus `mean` and `std`.
  - [ ] JSON/text verification over the executed notebook confirms dropout and weight-decay sections reuse the same fold IDs as Q1.
  - [ ] Markdown answers explicitly state whether dropout improved the model, whether weight decay improved the model, and which regularizer worked better.

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```text
  Scenario: Happy path regularization comparison
    Tool: Bash
    Steps: Execute the notebook to `/tmp/task5-run.ipynb`, then run a Python script that extracts the Q2 section and asserts the presence of labeled baseline, dropout, and weight-decay outputs, shared fold IDs, and conclusion text covering all three required questions.
    Expected: Script exits 0 and confirms controlled regularization comparisons.
    Evidence: .sisyphus/evidence/task-5-q2.json

  Scenario: Failure path uncontrolled comparison guard
    Tool: Bash
    Steps: Run a Python verification script that fails if the Q2 outputs indicate different fold IDs, missing labels, or both dropout and weight decay enabled simultaneously in a comparison row.
    Expected: Script exits non-zero with a controlled-comparison failure message.
    Evidence: .sisyphus/evidence/task-5-q2-error.log
  ```

  **Commit**: NO | Message: `feat(notebook): add q2 regularization comparison` | Files: `notebooks/hpo_analysis.ipynb`

- [ ] 6. Implement Question 3 learning-rate sweep on the preferred Q2 model

  **What to do**: Add the Q3 section that selects the preferred configuration from Q2 and evaluates at least 5 explicit learning rates while keeping all other settings fixed. Present a results table with the chosen candidate learning rates, the evaluation metric used to judge them, and a markdown conclusion naming the best learning rate and justifying the choice from the observed results.
  **Must NOT do**: Do not re-open dropout vs weight decay as a new search space, do not test fewer than 5 rates, and do not declare a best rate without citing the table values.

  **Recommended Agent Profile**:
  - Category: `python-development` - Reason: this is a constrained hyperparameter sweep inside the notebook.
  - Skills: `python-development`, `jupyter-notebook` - needed for controlled experiment code and clear result presentation.
  - Omitted: `research-paper-assistant` - explanatory writing is required, but this is not a paper-format task.

  **Parallelization**: Can Parallel: NO | Wave 2 | Blocks: Task 7 | Blocked By: Task 5

  **References** (executor has NO interview context - be exhaustive):
  - Requirement: `project_2.pdf` - Q3 requires at least 5 learning-rate values on the preferred Q2 model.
  - Destination: `notebooks/hpo_analysis.ipynb` - Q3 section lives here.
  - Dependency: Task 5 output - use the selected best regularization configuration only.
  - Guardrail: `.sisyphus/plans/project-2-notebook.md` - keep the comparison notebook-only and table-backed.

  **Acceptance Criteria** (agent-executable only):
  - [ ] Executed notebook output contains a Q3 table listing at least 5 explicit learning-rate values.
  - [ ] The notebook states which Q2 model configuration was carried into Q3.
  - [ ] Markdown after the Q3 table names one preferred learning rate and justifies it from the reported metrics.

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```text
  Scenario: Happy path learning-rate sweep
    Tool: Bash
    Steps: Execute the notebook to `/tmp/task6-run.ipynb`, then run a Python script that parses the Q3 section for at least 5 learning-rate values, a chosen best value, and explanatory text tying the choice to the table.
    Expected: Script exits 0 and confirms Q3 includes a controlled 5-rate sweep and a justified choice.
    Evidence: .sisyphus/evidence/task-6-q3.json

  Scenario: Failure path under-specified sweep guard
    Tool: Bash
    Steps: Run a Python verification script that fails if fewer than 5 learning rates appear or if no preferred rate is stated.
    Expected: Script exits non-zero with an under-specified-sweep message.
    Evidence: .sisyphus/evidence/task-6-q3-error.log
  ```

  **Commit**: NO | Message: `feat(notebook): add q3 learning-rate sweep` | Files: `notebooks/hpo_analysis.ipynb`

- [ ] 7. Finish Question 4, final summary, and reproducibility appendix

  **What to do**: Add the Q4 markdown explanation comparing cross-validation against a single train/validation split, explicitly tie the answer to observed fold-to-fold variability from earlier sections, summarize the preferred final model choice, and append a reproducibility appendix that documents seed usage, shared folds, notebook execution command, optional local dataset override behavior, and any exported results such as `outputs/results.csv` if the notebook writes them.
  **Must NOT do**: Do not answer Q4 with generic textbook language only, do not omit references to observed validation variability, and do not introduce new experiments in the final summary.

  **Recommended Agent Profile**:
  - Category: `writing` - Reason: the task is mostly synthesis, explanation, and final packaging.
  - Skills: `jupyter-notebook` - needed for notebook-safe markdown/code appendix updates.
  - Omitted: `code-review` - this is packaging, not a review pass.

  **Parallelization**: Can Parallel: NO | Wave 2 | Blocks: none | Blocked By: Tasks 5, 6

  **References** (executor has NO interview context - be exhaustive):
  - Requirement: `project_2.pdf` - Q4 explanation prompt and overall submission expectations.
  - Destination: `notebooks/hpo_analysis.ipynb` - Q4, summary, and appendix sections live here.
  - Dependencies: Tasks 4-6 outputs - Q4 must cite actual observed fold variability and preferred-model findings.
  - Reference: `.sisyphus/plans/project-2-notebook.md` - presentation and instructor-request context.

  **Acceptance Criteria** (agent-executable only):
  - [ ] Executed notebook output contains markdown answering why cross-validation is better than a single split on this dataset and explicitly references fold variability or standard deviation.
  - [ ] The notebook includes a final summary stating the preferred regularization choice and preferred learning rate.
  - [ ] The appendix includes the clean execution command and notes the optional local dataset override and default remote URL behavior.

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```text
  Scenario: Happy path final narrative check
    Tool: Bash
    Steps: Execute the notebook to `/tmp/task7-run.ipynb`, then run a Python script that extracts markdown content from Q4, Final Summary, and Reproducibility Appendix and checks for references to cross-validation stability, fold variability/standard deviation, preferred regularizer, preferred learning rate, and execution command text.
    Expected: Script exits 0 and confirms all required narrative elements are present.
    Evidence: .sisyphus/evidence/task-7-summary.json

  Scenario: Failure path generic-analysis guard
    Tool: Bash
    Steps: Run a Python verification script that fails if Q4 lacks words such as `standard deviation`, `fold`, or equivalent evidence-driven stability language.
    Expected: Script exits non-zero with a missing-evidence narrative message.
    Evidence: .sisyphus/evidence/task-7-summary-error.log
  ```

  **Commit**: NO | Message: `feat(notebook): add q4 analysis and final packaging` | Files: `notebooks/hpo_analysis.ipynb`

## Final Verification Wave (MANDATORY - after ALL implementation tasks)
> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.
> **Do NOT auto-proceed after verification. Wait for user's explicit approval before marking work complete.**
> **Never mark F1-F4 as checked before getting user's okay.** Rejection or user feedback -> fix -> re-run -> present again -> wait for okay.

- [ ] F1. Plan Compliance Audit - oracle

  **What to do**: Compare the implemented notebook against this plan and verify every required section, experiment, guardrail, and acceptance criterion is represented.
  **Tool**: oracle
  **Steps**:
  - Read `.sisyphus/plans/project-2-notebook.md` and the final `notebooks/hpo_analysis.ipynb`.
  - Check that Tasks 1-7 are all satisfied, including prompt text, inline code, controlled comparisons, and reproducibility appendix.
  - Produce a pass/fail report listing any missing plan items.
  **Expected**: Oracle reports full compliance or returns a concrete defect list tied to task numbers.

- [ ] F2. Code Quality Review - unspecified-high

  **What to do**: Review the notebook code for correctness, determinism, duplication, and notebook-specific hidden-state risks.
  **Tool**: unspecified-high
  **Steps**:
  - Read executed notebook output and source cells.
  - Flag dead code, hidden state dependencies, nondeterministic behavior, or logic that depends on external modules.
  - Confirm helper cells run top-to-bottom without relying on out-of-order execution.
  **Expected**: Reviewer approves notebook code quality or returns a precise list of defects to fix.

- [ ] F3. Real Manual QA - unspecified-high (+ playwright if UI)

  **What to do**: Execute the notebook from a clean kernel and validate rendered outputs, failure handling, and deterministic reruns using the planned shell-based checks.
  **Tool**: unspecified-high
  **Steps**:
  - Run `jupyter nbconvert --to notebook --execute "notebooks/hpo_analysis.ipynb" --output /tmp/hpo_submission_run.ipynb --ExecutePreprocessor.timeout=1200`.
  - Run the planned Python JSON verification scripts against `/tmp/hpo_submission_run.ipynb`.
  - Re-execute to `/tmp/hpo_submission_run_2.ipynb` and compare extracted summary outputs for deterministic agreement.
  **Expected**: All execution and verification commands exit 0; the rerun comparison stays within the defined tolerance.

- [ ] F4. Scope Fidelity Check - deep

  **What to do**: Confirm the final notebook stays within the agreed notebook-only project scope and does not drift into unrelated repo cleanup or extra experimentation.
  **Tool**: deep
  **Steps**:
  - Inspect the diff and final notebook content.
  - Verify no substantive logic was moved into `src/`, no CI/env/package files were added, and no extra model families or dataset changes were introduced.
  - Report any scope creep relative to the plan's `Must NOT Have` section.
  **Expected**: Deep reviewer confirms scope fidelity or returns a specific list of out-of-scope changes.

## Commit Strategy
- Default execution mode: no commits unless the user explicitly requests commits during implementation.
- If commits are requested, follow Metis's milestone ordering: scaffold notebook -> add data/helpers -> add Q1 -> add Q2 -> add Q3/Q4 -> final execution lock.

## Success Criteria
- The notebook is the sole source of truth for the submission and can be graded without opening any other code file.
- All Q1-Q4 prompts, code, tables, and conclusions appear in order in `notebooks/hpo_analysis.ipynb`.
- The notebook executes from a clean kernel and produces deterministic summary results for the same seed.
- All written claims are traceable to notebook outputs rather than external artifacts or hidden modules.
