import webbrowser
import requests
import urllib.parse


# ==================================================
# KNOWN WEBSITES
# ==================================================

KNOWN_WEBSITES = {

    "claude":
    "https://claude.ai",

    "perplexity":
    "https://www.perplexity.ai",

    "notion":
    "https://www.notion.so",

    "figma":
    "https://www.figma.com",

    "cursor":
    "https://cursor.com",

    "chatgpt":
    "https://chat.openai.com",

    "openai":
    "https://openai.com",

    "canva":
    "https://www.canva.com",

    "github":
    "https://github.com",

    "youtube":
    "https://youtube.com"
}


# ==================================================
# GOOGLE SEARCH
# ==================================================

def search_google(query):

    query = (
        query
        .strip()
    )

    if not query:
        return False

    url = (
        "https://www.google.com/search?q="
        +
        urllib.parse.quote(
            query
        )
    )

    webbrowser.open(
        url
    )

    return True


# ==================================================
# CHECK WEBSITE EXISTS
# ==================================================

def website_exists(url):

    try:

        response = requests.get(
            url,
            timeout=5,
            allow_redirects=True
        )

        return (
            response.status_code
            < 400
        )

    except:

        return False


# ==================================================
# OPEN WEBSITE
# ==================================================

def open_website(
    site_name
):

    site_name = (
        site_name
        .strip()
        .lower()
    )

    if not site_name:
        return False

    # =====================================
    # KNOWN WEBSITE OVERRIDE
    # =====================================

    if site_name in KNOWN_WEBSITES:

        url = (
            KNOWN_WEBSITES[
                site_name
            ]
        )

        print(
            f"\n🌐 Opening known site: "
            f"{url}"
        )

        webbrowser.open(
            url
        )

        return True

    # =====================================
    # SMART DOMAIN GUESSING
    # =====================================

    possible_urls = [

        f"https://{site_name}.com",

        f"https://{site_name}.ai",

        f"https://{site_name}.io",

        f"https://{site_name}.so",

        f"https://{site_name}.org",

        f"https://{site_name}.app",

        f"https://www.{site_name}.com"
    ]

    for url in possible_urls:

        print(
            f"\nTrying: {url}"
        )

        if website_exists(url):

            print(
                f"\n🌐 OPENING: {url}"
            )

            webbrowser.open(
                url
            )

            return True

    # =====================================
    # FALLBACK SEARCH
    # =====================================

    print(
        "\nCould not resolve website."
    )

    search_google(
        f"{site_name}"
    )

    return True