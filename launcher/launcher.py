from launcher.process_manager import (
    start_ollama,
    start_api,
    start_kai
)

from launcher.healthcheck import (
    wait_for_ollama,
    wait_for_api
)


# ==================================================
# BANNER
# ==================================================

def banner():

    print()

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("                KAI")
    print("           Boot Sequence")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    print()


# ==================================================
# MAIN
# ==================================================

def main():

    banner()

    # ----------------------------------------------

    start_ollama()

    if not wait_for_ollama():

        print(
            "Failed to start Ollama."
        )

        return

    # ----------------------------------------------

    start_api()

    if not wait_for_api():

        print(
            "Failed to start FastAPI."
        )

        return

    # ----------------------------------------------

    start_kai()

    print()

    print(
        "🖤 Welcome back, Commander."
    )

    print()


# ==================================================
# ENTRY
# ==================================================

if __name__ == "__main__":

    main()