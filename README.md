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

### 4. Add your service logic

#### 🔌 Web service (e.g., REST API with FastAPI or Flask):

Put your service file in the `services/web/` folder.

Example:

```python
# services/web/my_api_service.py
def register_routes(app):
    @app.get("/hello")
    def hello():
        return {"message": "Hello from my service!"}
```

#### ☁️ AWS Lambda:

Use the `services/lambda/handler.py` and inject your logic there, or dynamically load from `core/` modules.

---

## 🧠 Architecture Overview

```
.
├── configs/             # Configs (dev/prod/env)
├── core/                # Interfaces, business logic, models
├── infrastructure/      # AWS, web framework integrations
├── services/            # Plug-and-play service files
│   ├── web/             # Drop-in web API logic here
│   └── lambda/          # Lambda entrypoint
├── main.py              # Web app entrypoint
```

- **SOLID Principles:** Core logic is modular and decoupled from frameworks
- **Plug-and-Play:** Just drop a service into `services/web/` and it'll be auto-registered
- **Flexible Deployment:** Works locally or in the cloud (e.g., AWS Lambda)

---

## 🛠️ Run Locally (Web Server)

Make sure you’ve added a file like `my_api_service.py` under `services/web/`.

Then start the app:

```bash
python main.py
```

---

## 🧪 Testing

Tests go in the `tests/` folder. To run them:

```bash
pytest
```

---

## 📦 Deployment

### As an AWS Lambda:

- Use the `services/lambda/handler.py` as your Lambda entrypoint.
- Package your code with dependencies (e.g., using `zip` or AWS SAM).

---

## 📁 Config Management

Use the files in `configs/` to define different environments:

- `base_config.py` — Shared default settings
- `dev_config.py` — Development overrides
- `prod_config.py` — Production config

You can load configs in your app like this:

```python
from configs.dev_config import Config
```

---

## 🙌 Contributing

If you're improving this template, feel free to fork and PR with suggestions or changes.

---

## 📄 License

MIT – do what you want, but give credit. 😉

---

## 🧙 Final Tips

- Keep your core logic in `core/` — it's reusable, testable, and framework-agnostic
- Use `infrastructure/` for anything that talks to the outside world (web servers, AWS, DBs)
- Use `services/` for plugging in new endpoints or business flows
