import time
import requests

from launcher.config import Config


# ==================================================
# WAIT FOR API
# ==================================================

def wait_for_api():

    print(
        "⏳ Waiting for FastAPI..."
    )

    start = time.time()

    while True:

        try:

            response = requests.get(
                Config.API_URL,
                timeout=1
            )

            if response.status_code == 200:

                print(
                    "✅ FastAPI Online"
                )

                return True

        except Exception:

            pass

        if (
            time.time() - start
            >
            Config.API_TIMEOUT
        ):

            print(
                "❌ FastAPI failed to start."
            )

            return False

        time.sleep(
            Config.CHECK_INTERVAL
        )


# ==================================================
# WAIT FOR OLLAMA
# ==================================================

def wait_for_ollama():

    print(
        "⏳ Waiting for Ollama..."
    )

    start = time.time()

    while True:

        try:

            response = requests.get(
                "http://127.0.0.1:11434",
                timeout=1
            )

            if response.status_code in [200, 404]:

                print(
                    "✅ Ollama Online"
                )

                return True

        except Exception:

            pass

        if (
            time.time() - start
            >
            Config.OLLAMA_TIMEOUT
        ):

            print(
                "❌ Ollama failed to start."
            )

            return False

        time.sleep(
            Config.CHECK_INTERVAL
        )