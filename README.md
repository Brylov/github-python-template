
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

## 🧠 Architecture Overview

```
.
├── .github/workflows/    # GitHub Actions (CI/CD)
├── configs/              # Configs (dev/prod/env)
├── core/                 # Interfaces, business logic, models
├── infrastructure/       # AWS, web framework integrations
├── services/             # Plug-and-play service files
│   ├── web/              # Drop-in web API logic here
│   └── lambda/           # Lambda entrypoint
├── main.py               # Web app entrypoint (auto-loads services)
├── tests/                # Unit tests
├── .env.example          # Sample environment file
├── .pre-commit-config.yaml  # Auto-format/lint hooks
├── Dockerfile            # Optional container support
└── Makefile              # Dev command shortcuts
```

- **SOLID Principles:** Core logic is modular and decoupled from frameworks
- **Plug-and-Play:** Just drop a service into `services/web/` and it’ll be auto-registered
- **Platform-Ready:** Works as both a local app and an AWS Lambda

---

## 🔌 How Services Are Loaded

### Web Services (`services/web/`)

Each file should have a `register_routes(app)` function:

```python
# services/web/my_api_service.py
def register_routes(app):
    @app.get("/hello")
    def hello():
        return {"message": "Hello from my service!"}
```

When you run `main.py`, all `.py` files in `services/web/` are discovered and registered automatically.

---

## 🛠️ Run Locally (Web Server)

Make sure you’ve added at least one service in `services/web/`, then run:

```bash
python main.py
```

The app will launch using FastAPI with routes auto-registered from your services.

---

## 🧪 Testing

Tests go in the `tests/` folder. To run:

```bash
pytest
```

---

## 🧼 Pre-Commit Hooks

This template uses [`pre-commit`](https://pre-commit.com/) to keep code clean.

### Setup:

```bash
pip install pre-commit
pre-commit install
```

Hooks include:

- `black` (auto formatter)
- `flake8` (linter)
- `end-of-file-fixer`
- `trailing-whitespace`
- `pyupgrade`

Run manually on all files:

```bash
pre-commit run --all-files
```

---

## 🔄 GitHub Actions (CI)

Included in `.github/workflows/test.yml`.

Automatically:

- Installs dependencies
- Lints code with `flake8`
- Runs all tests on push or pull request

You’ll see results in the **Actions** tab on GitHub after pushing your changes.

---

## 🐳 Docker (Optional)

To build and run in a container:

```bash
docker build -t my-python-app .
docker run -p 8000:8000 my-python-app
```

---

## 📦 Deployment: AWS Lambda

1. Put your handler in `services/lambda/handler.py`
2. Package with your dependencies (e.g. via `zip`, SAM, or Serverless Framework)
3. Deploy to AWS Lambda as usual

You can separate core logic into `core/` for reuse.

---

## 📁 Config Management

Environment-specific configs live in the `configs/` folder:

- `base_config.py` — shared defaults
- `dev_config.py` — development overrides
- `prod_config.py` — production config

Config loading example:

```python
from configs.dev_config import Config
print(Config.DEBUG)
```

`.env` selects which config file to use.

---

## 📂 Keeping Folders Tracked in Git

Git doesn't track empty folders by default.

We use `.gitkeep` files inside each empty folder so they exist in the repo. You can delete them once you start adding real files.

---

## 💻 Makefile (Optional Dev Commands)

You can use `make` commands like:

```bash
make install   # Install dependencies
make run       # Run the app
make test      # Run tests
```

(Or use `tasks.py` if you prefer Python-based automation.)

---

## 🙌 Contributing

Feel free to fork, improve, and PR — contributions are welcome!

---

## 📄 License

MIT – do what you want, but give credit. 😉

---

## 🧙 Final Tips

- Keep business logic inside `core/` for full framework independence
- Use `infrastructure/` for integrations like AWS, databases, etc.
- Use `services/` to plug in new flows easily without touching core
- Always test your app locally before deploying to Lambda
