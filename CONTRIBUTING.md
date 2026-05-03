# Contributing to Vellon

First off, thank you for considering contributing to Vellon! It's people like you who make the open-source community such an amazing place to learn, inspire, and create.

## 🚀 Getting Started

1.  **Fork the repository** on GitHub.
2.  **Clone your fork** locally:
    ```bash
    git clone https://github.com/Devrancis/Vellon.git
    ```
3.  **Add the upstream remote**:
    ```bash
    git remote add upstream https://github.com/Devrancis/Vellon.git
    ```
4.  **Create a new branch** for your feature or bugfix:
    ```bash
    git checkout -b feature/your-feature-name
    ```

## 🛠️ Development Standards

### Coding Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Use meaningful variable and function names.
- Document complex logic with comments and docstrings.

### Commit Messages
- Use the imperative mood ("Add feature" not "Added feature").
- Keep the first line short (under 50 characters).
- Reference issues and pull requests after the first line.

### Branch Naming
- Features: `feature/short-description`
- Bugfixes: `fix/short-description`
- Documentation: `docs/short-description`
- Refactoring: `refactor/short-description`

## 🧪 Testing

Before submitting a pull request, ensure that:
1.  All existing tests pass:
    ```bash
    python manage.py test
    ```
2.  You have added tests for any new functionality.
3.  Code coverage has not decreased significantly.

## 📬 Pull Request Process

1.  **Sync your branch** with the latest upstream changes:
    ```bash
    git fetch upstream
    git rebase upstream/main
    ```
2.  **Push your changes** to your fork:
    ```bash
    git push origin feature/your-feature-name
    ```
3.  **Open a Pull Request** against the `main` branch of the original repository.
4.  **Describe your changes** clearly in the PR description. Link any related issues.
5.  **Respond to feedback**: Be prepared to make changes if requested by the maintainers.

## ⚖️ Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. We expect all contributors to be respectful, inclusive, and professional.

## 💎 Premium Standards

Vellon is a premium product. We strive for excellence in:
- **UI/UX**: Ensure any frontend changes are responsive, modern, and high-quality.
- **Performance**: Optimize database queries and avoid N+1 issues.
- **Security**: Never expose sensitive data and follow Django security best practices.

Thank you for your contribution!
