# 🐍 Python Clean Architecture Template

This is a plug-and-play Python project template that follows **SOLID principles** and supports deployment as either a **web service** (e.g., with FastAPI) or an **AWS Lambda function**. Just drop your service files into the right folder, and you're good to go.

---

## 🚀 Quick Start

### 1. Clone this template

Click **"Use this template"** on GitHub or clone manually:

```bash
git clone https://github.com/your-username/python-clean-template.git
cd python-clean-template
```

### 2. Create your virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Load environment variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Inside `.env`, set the environment:

```env
ENV=dev
```

---

## 🧠 Project Structure

```
.
├── .github/workflows/        # GitHub Actions (CI/CD)
├── .env.example              # Environment variable example
├── Dockerfile                # Optional Docker support
├── main.py                   # App entry point (calls src/)
├── requirements.txt
├── tests/                    # Unit tests
├── .pre-commit-config.yaml   # Code formatting/lint hooks
└── src/                      # 📦 Application code lives here
    ├── configs/              # Environment-specific config files
    ├── core/                 # Interfaces, models, and use cases (pure logic)
    ├── infrastructure/       # External integrations (e.g., AWS, web frameworks)
    ├── services/             # 🔌 Web/Lambda services (plug-and-play)
    ├── utils/                # ✅ Reusable helpers (logger, date formatter, etc.)
    └── __init__.py
```

- **SOLID Principles:** Code is modular, reusable, and framework-independent
- **Plug-and-Play:** Just drop a file into `services/web/` and it auto-registers
- **Platform-Ready:** Can run locally or be deployed to AWS Lambda

---

## 🔌 How Services Are Loaded

### Web Services (`src/services/web/`)

Each service module should define a `register_routes(app)` function.

```python
# src/services/web/my_api_service.py
def register_routes(app):
    @app.get("/hello")
    def hello():
        return {"message": "Hello from my service!"}
```

These files are automatically discovered and registered when `main.py` runs.

---

## 🛠️ Run Locally

```bash
python main.py
```

Your FastAPI server will launch and include all registered services.

---

## 🧪 Testing

```bash
pytest
```

Tests live in the `tests/` folder.

---

## 🧼 Pre-Commit Hooks

```bash
pip install pre-commit
pre-commit install
```

Hooks included:

- `black` – format your code
- `flake8` – find potential issues
- `trailing-whitespace`, `end-of-file-fixer`, etc.

Run manually:

```bash
pre-commit run --all-files --hook-stage manual
```

---

## 🔄 GitHub Actions (CI)

Located in `.github/workflows/test.yml`. Automatically lints and tests your code on every push or pull request.

---

## 🐳 Docker (Optional)

```bash
docker build -t my-python-app .
docker run -p 8000:8000 my-python-app
```

---

## 📦 Deployment: AWS Lambda

- Put handler logic in `src/services/lambda/handler.py`
- Package with your dependencies
- Deploy using AWS tools (SAM, Serverless Framework, etc.)

---

## 📁 Config Management

Use files in `src/configs/`:

- `base_config.py` — shared defaults
- `dev_config.py` — dev settings
- `prod_config.py` — production settings

Environment is set via `.env`.

```python
from src.configs.dev_config import Config
```

---

## 🧰 Utilities (`src/utils/`)

The `utils/` folder contains small reusable tools to help your development flow:

- `logger.py` — central logging setup
- `dates.py` — handy datetime formatters and parsers

You can import and reuse them anywhere in the project:

```python
from src.utils.dates import format_date
```

---

## 🙌 Contributing

Feel free to fork, suggest improvements, or open PRs.

---

## 📄 License

MIT – do what you want, but give credit. 😉

---

## 🧙 Final Tips

- Keep logic in `core/`, isolated from frameworks
- Add new features by dropping service files in `services/`
- Use `utils/` for common helpers shared across services
- Use `configs/` to adapt behavior for different environments
