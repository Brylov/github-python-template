import os
import glob
import importlib.util
from fastapi import FastAPI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Load environment config
ENV = os.getenv("ENV", "dev")
if ENV == "prod":
    from src.configs.prod_config import Config
else:
    from src.configs.dev_config import Config

# Create FastAPI app
app = FastAPI(title="Python Clean Template")

# Auto-load services from services/web/
def auto_register_services(app):
    service_files = glob.glob("services/web/*.py")
    for path in service_files:
        module_name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "register_routes"):
            module.register_routes(app)
            print(f"✅ Loaded: {module_name}")

auto_register_services(app)

# Optional: Run with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)
