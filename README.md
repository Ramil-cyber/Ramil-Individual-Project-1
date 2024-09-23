
# Ramil Individual Project 1

### CI/CD Badges:
- **Test Status**: [![Run Tests](https://github.com/nogibjj/Ramil-Individual-Project-1/actions/workflows/test.yaml/badge.svg)](https://github.com/nogibjj/Ramil-Individual-Project-1/actions/workflows/test.yaml)
- **Code Formatting**: [![Format Code](https://github.com/nogibjj/Ramil-Individual-Project-1/actions/workflows/format_code.yaml/badge.svg)](https://github.com/nogibjj/Ramil-Individual-Project-1/actions/workflows/format_code.yaml)
- **Linting**: [![Run Lint](https://github.com/nogibjj/Ramil-Individual-Project-1/actions/workflows/lint.yaml/badge.svg)](https://github.com/nogibjj/Ramil-Individual-Project-1/actions/workflows/lint.yaml)

## Project Overview
This project demonstrates the setup of continuous integration for a Python data science project using Github CI/CD pipelines. It includes a Jupyter Notebook performing descriptive statistics with Pandas, test scripts and jupyter notebook, a shared library, and a Makefile to automate tasks such as formatting, linting, and testing. Github Actions run these tasks, with badges reflecting their status.

## YouTube video
[Link to the YouTube video](https://youtu.be/_rtJzRXfcG0)
---

### 1. **Jupyter Notebook**
- The notebook performs **descriptive statistics** using **Pandas**.
- It is tested using the `nbval` plugin for `pytest` to validate the correctness of the results.

### 2. **Python Scripts**
- `test_script.py`: Contains tests for a standalone script.
- `test_lib.py`: Tests the shared code in `lib.py`.
- `lib.py`: Shared utility code used in both the notebook and scripts.
- `main.py`: More advanced code built on the top of `lib.py`

### 3. **Makefile**
The `Makefile` includes the following commands:

- **Run all tests**: Executes tests on the notebook, script, and library.
- **Code formatting**: Formats the Python code using **black**.
- **Linting**: Lints the code using **Ruff**.
- **Install dependencies**: Installs all required packages listed in `requirements.txt`.

### 4. **requirements.txt**
A pinned list of dependencies for the project to ensure consistent environments across systems.

---

## Github Actions
Tasks from the Makefile are automated using Github CI/CD pipelines. The github worflows have following jobs that:
- Run tests on the Jupyter Notebook, scripts, and library.
- Format the code using **black**.
- Lint the code using **Ruff**.
- Install the dependencies via `pip`.

---

## Setup and Usage Instructions

### 1. Clone the repository:
```bash
git https://github.com/nogibjj/Ramil-Individual-Project-1.git
cd Ramil-Individual-Project-1
```

### 2. Install the dependencies:
```bash
make install
```

### 3. Run the Makefile commands:
- **Run all tests**:
  ```bash
  make test_code
  ```
- **Format code with black**:
  ```bash
  make format
  ```
- **Lint code with Ruff**:
  ```bash
  make lint
  ```
