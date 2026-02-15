# Design Doc: Clean Discussion Cells in Notebook

## Goal
Replace code cells that use `display(Markdown(...))` with pure markdown cells containing the pre-computed text from the outputs.

## Approach
Scripted transformation using `nbformat`.

## Steps
1. Create `scripts/clean_notebook.py`.
2. Script will:
   - Load `notebooks/Project_1.ipynb`.
   - Find cells containing `display(Markdown(`.
   - Extract the markdown output.
   - Convert cell to markdown type with that output as source.
   - Strip code metadata (outputs, execution_count).
3. Run script.
4. Verify results.

## Reasoning
Scripted approach is safer than manual JSON editing and ensures the exact numbers from the last execution are preserved by reading them from the `outputs` field.
