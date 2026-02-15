import nbformat
from pathlib import Path


def clean_notebook(notebook_path):
    path = Path(notebook_path)
    if not path.exists():
        print(f"File not found: {notebook_path}")
        return

    nb = nbformat.read(path, as_version=4)

    modified = False
    for i, cell in enumerate(nb.cells):
        is_discussion_cell = False
        markdown_content = None

        # Case 1: Code cell with display(Markdown(...))
        if cell.cell_type == "code" and "display(Markdown(" in cell.source:
            is_discussion_cell = True
            if "outputs" in cell:
                for output in cell.outputs:
                    if "data" in output and "text/markdown" in output.data:
                        markdown_content = output.data["text/markdown"]
                        break

        # Case 2: Mismatched cell (markdown with outputs) - likely a bad conversion
        elif cell.cell_type == "markdown" and (
            "outputs" in cell or "execution_count" in cell
        ):
            is_discussion_cell = True
            markdown_content = cell.source

        if is_discussion_cell and markdown_content:
            # Normalize markdown content
            if isinstance(markdown_content, list):
                markdown_content = "".join(markdown_content)

            # Create a clean markdown cell
            new_cell = nbformat.v4.new_markdown_cell(source=markdown_content)
            nb.cells[i] = new_cell
            modified = True
            print(f"Cleaned up cell {i} (converted/fixed to markdown).")

    if modified:
        nbformat.write(nb, path)
        print(f"Successfully updated {notebook_path}")
    else:
        print("No changes needed or no discussion cells matched.")


if __name__ == "__main__":
    clean_notebook("notebooks/Project_1.ipynb")
