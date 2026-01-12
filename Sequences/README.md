# BioSequence FASTA Parser

This repository contains a small Python codebase for parsing FASTA files and working with biological sequences using object-oriented design. It includes:

- A `FastaFile` parser class
- A `BioSequence` superclass
- `DNASequence` and `ProteinSequence` subclasses
- Full Python type annotations compatible with **mypy**

The codebase has been refactored to include explicit type hints for variables, function arguments, return types, and special methods (such as `__iter__`), following standard Python typing conventions.

---

## Requirements

- Python **3.9+** (recommended)
- `mypy` for static type checking

You can check your Python version with:

```bash
python --version
```

---

## Installing mypy

It is recommended to install `mypy` in a virtual environment.

### 1. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\\Scripts\\activate  # Windows
```

### 2. Install mypy using pip

```bash
pip install mypy
```

Verify installation:

```bash
mypy --version
```

---

## Using mypy for Type Checking

To run mypy on the codebase, execute the following command from the root of the repository:

```bash
mypy .
```

This will:

- Analyse all Python files in the project
- Report any type mismatches or missing annotations

### Running mypy in strict mode

For more thorough checking, you can enable strict mode:

```bash
mypy --strict .
```

Strict mode enables additional checks such as:

- Ensuring all functions have return type annotations
- Catching implicit `Any` types
- Highlighting potentially unsafe operations

---

## Notes on Type Annotations

- Generator methods (such as FASTA parsers) are annotated using `Iterator[T]`
- The `__iter__` method in `BioSequence` returns `Iterator[str]`, since iterating over a sequence yields individual characters
- Polymorphic factory methods use `TypeVar` with upper bounds to preserve type safety
- Assertions are used where necessary to satisfy static analysis (e.g. preventing division by zero)

Type hints follow guidance from the official mypy documentation and the provided Moodle type hints cheat sheet.

---

## Example mypy Output

When the code is correctly annotated, mypy should report no errors:

```text
Success: no issues found in 4 source files
```

---

## Author

Osaronosakhare
