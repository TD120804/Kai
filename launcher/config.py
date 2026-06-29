from pathlib import Path


class Config:

    # ==========================================
    # PROJECT
    # ==========================================

    ROOT_DIR = Path(__file__).resolve().parent.parent

    UI_DIR = ROOT_DIR / "ui" / "kai_home"

    VENV_PYTHON = (
        ROOT_DIR
        / "venv"
        / "Scripts"
        / "python.exe"
    )

    KAI_EXE = (
        UI_DIR
        / "build"
        / "windows"
        / "x64"
        / "runner"
        / "Release"
        / "kai_home.exe"
    )

    # ==========================================
    # API
    # ==========================================

    API_HOST = "127.0.0.1"

    API_PORT = 8000

    API_URL = (
        f"http://{API_HOST}:{API_PORT}"
    )

    # ==========================================
    # COMMANDS
    # ==========================================

    OLLAMA_COMMAND = [
        "ollama",
        "serve"
    ]

    FASTAPI_COMMAND = [

        str(VENV_PYTHON),

        "-m",

        "uvicorn",

        "middleware.api_bridge:app"
    ]

    # ==========================================
    # TIMEOUTS
    # ==========================================

    CHECK_INTERVAL = 1

    API_TIMEOUT = 30

    OLLAMA_TIMEOUT = 30