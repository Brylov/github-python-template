# Contributing Guidelines

Thank you for your interest in contributing to this project.

This document outlines the process for setting up the project, writing code, and submitting changes. Please follow these guidelines to ensure consistency and maintainability across the codebase.

---

## Getting Started

1. **Fork the repository**Create a personal fork of the project on GitHub.
2. **Clone your fork**

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
3. **Set up a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   ```
4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Branching Strategy

- Use feature branches for new functionality:
  ```
  feature/<short-description>
  ```
- Use fix branches for bug fixes:
  ```
  fix/<short-description>
  ```

Avoid pushing directly to the `main` branch. All changes should go through pull requests.

---

## Code Standards

- Follow [PEP 8](https://peps.python.org/pep-0008/) for code style
- Run `pre-commit` before committing:
  ```bash
  pre-commit run --all-files --hook-stage manual
  ```
- Use meaningful commit messages
- Keep code modular and maintainable

---

## Testing

All contributions should include tests when applicable.

- Place tests under the `tests/` directory
- Use `pytest` to run the test suite:
  ```bash
  pytest
  ```

Ensure that all tests pass before submitting a pull request.

---

## Making a Pull Request

Before opening a pull request:

- Ensure your branch is up to date with `main`
- Run all tests and pre-commit hooks
- Update documentation if necessary
- Fill out the pull request template completely

---

## File Structure Notes

This project follows a `src/` layout. Major folders include:

- `core/` — business logic, models, interfaces
- `services/` — plug-and-play components (web/Lambda)
- `configs/` — environment-specific settings
- `utils/` — shared utilities (e.g. logging, date formatting)

Services should be modular and placed in the appropriate `services/` subfolder. Services with a `register_routes(app)` function will be auto-loaded into the app.

---

## Communication

If your contribution is complex or unclear, open an issue or draft PR first to start the discussion.

---

## Licensing

By contributing to this project, you agree that your code will be released under the same license.

---

Thank you for contributing.
