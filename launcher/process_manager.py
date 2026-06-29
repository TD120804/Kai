import subprocess

from launcher.config import Config


# ==================================================
# START OLLAMA
# ==================================================

def start_ollama():

    print(
        "🧠 Starting Ollama..."
    )

    return subprocess.Popen(

        Config.OLLAMA_COMMAND,

        stdout=subprocess.DEVNULL,

        stderr=subprocess.DEVNULL
    )


# ==================================================
# START FASTAPI
# ==================================================

def start_api():

    print(
        "⚡ Starting FastAPI..."
    )

    return subprocess.Popen(

        Config.FASTAPI_COMMAND,

        cwd=Config.ROOT_DIR,

        stdout=subprocess.DEVNULL,

        stderr=subprocess.DEVNULL
    )


# ==================================================
# START KAI
# ==================================================

def start_kai():

    print(
        "🖤 Launching Kai..."
    )

    return subprocess.Popen(
        [str(Config.KAI_EXE)]
    )