import os


FILE_ALIASES = {

    "desktop":
    r"C:\Users\HP\OneDrive\Desktop",

    "downloads":
    r"C:\Users\HP\Downloads",

    "documents":
    r"C:\Users\HP\OneDrive\Documents",
}


def search_c_drive(
    target
):

    target = (
        target.lower()
        .strip()
    )

    print(
        f"🔍 Searching C drive for {target}..."
    )

    for root, dirs, files in os.walk(
        "C:\\"
    ):

        # ==========================
        # Search folders
        # ==========================

        for folder in dirs:

            if target in folder.lower():

                return os.path.join(
                    root,
                    folder
                )

        # ==========================
        # Search files
        # ==========================

        for file in files:

            if target in file.lower():

                return os.path.join(
                    root,
                    file
                )

    return None


def open_file_or_folder(
    target,
    search_drive=False
):

    target = (
        target.strip()
    )

    lowered = (
        target.lower()
    )

    # =====================================
    # Alias support
    # =====================================

    if lowered in FILE_ALIASES:

        path = (
            FILE_ALIASES[
                lowered
            ]
        )

        if os.path.exists(
            path
        ):

            os.startfile(
                path
            )

            return True

    # =====================================
    # Raw Windows path support
    # =====================================

    if os.path.exists(
        target
    ):

        os.startfile(
            target
        )

        return True

    # =====================================
    # Optional C drive search
    # =====================================

    if search_drive:

        found_path = (
            search_c_drive(
                target
            )
        )

        if found_path:

            os.startfile(
                found_path
            )

            return True

    return False