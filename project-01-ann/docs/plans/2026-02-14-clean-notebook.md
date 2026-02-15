# Clean Notebook Discussion Cells Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace code cells that use `display(Markdown(...))` in `notebooks/Project_1.ipynb` with pure markdown cells containing the pre-computed text.

**Architecture:** A Python script `scripts/clean_notebook.py` will use `nbformat` to transform the notebook.

**Tech Stack:** Python 3.12, nbformat.

---

### Task 1: Create Transformation Script

**Files:**
- Create: `scripts/clean_notebook.py`

**Step 1: Write the script**

```python
import nbformat
from pathlib import Path

def clean_notebook(notebook_path):
    path = Path(notebook_path)
    nb = nbformat.read(path, as_version=4)
    
    modified = False
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == 'code' and 'display(Markdown(' in cell.source:
            # Extract markdown from output
            markdown_content = None
            if 'outputs' in cell:
                for output in cell.outputs:
                    if 'data' in output and 'text/markdown' in output.data:
                        markdown_content = output.data['text/markdown']
                        break
            
            if markdown_content:
                # Convert to markdown cell
                new_cell = nbformat.v4.new_markdown_cell(source=markdown_content)
                nb.cells[i] = new_cell
                modified = True
                print(f"Converted cell {i} to markdown.")
            else:
                print(f"Skipping cell {i}: No markdown output found.")

    if modified:
        nbformat.write(nb, path)
        print(f"Successfully updated {notebook_path}")
    else:
        print("No changes made.")

if __name__ == "__main__":
    clean_notebook('notebooks/Project_1.ipynb')
```

**Step 2: Run the script**

Run: `python scripts/clean_notebook.py`
Expected: "Converted cell 7 to markdown.", "Converted cell 11 to markdown.", "Converted cell 15 to markdown.", "Successfully updated notebooks/Project_1.ipynb"

**Step 3: Verify the notebook**

I will manually inspect the JSON or read it back to verify the change.

**Step 4: Commit**

```bash
git add notebooks/Project_1.ipynb scripts/clean_notebook.py
git commit -m "chore: convert discussion code cells to markdown cells"
```
