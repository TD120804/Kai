import os
import webbrowser


# ==================================================
# APP PATHS
# ==================================================

APP_PATHS = {

    "chrome":
    "C:/Program Files/Google/Chrome/Application/chrome.exe",

    "vscode":
    "C:/Users/HP/AppData/Local/Programs/Microsoft VS Code/Code.exe",

    "spotify":
    "spotify:",

    "youtube":
    "https://youtube.com"
}


# ==================================================
# OPEN APP
# ==================================================

def open_app(app_name):

    app_name = (
        app_name
        .lower()
        .strip()
    )

    if app_name not in APP_PATHS:
        return False

    try:

        path = APP_PATHS[
            app_name
        ]

        if path.startswith(
            "http"
        ):

            webbrowser.open(
                path
            )

        else:

            os.startfile(
                path
            )

        return True

    except Exception as e:

        print(
            f"\nApp open error: {e}"
        )

        return False