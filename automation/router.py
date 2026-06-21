from automation.lock_in import (
    start_lock_in,
    stop_lock_in
)

from automation.spotify_control import (
    play_song,
    pause_music,
    next_song,
    previous_song
)

from automation.app_control import (
    open_app
)

from automation.web_actions import (
    open_website
)

from automation.file_control import (
    open_file_or_folder
)

from automation.screen_awareness import (
    analyze_screen
)


OPEN_WORDS = [
    "open",
    "launch",
    "start"
]


PROJECT_WORDS = [
    "project"
]


def clean_command(
    text
):

    return (
        text
        .replace(
            "for me",
            ""
        )
        .replace(
            "the",
            ""
        )
        .replace(
            "my",
            ""
        )
        .replace(
            "folder",
            ""
        )
        .strip()
    )


def handle_automation(
    user_input
):

    text = (
        user_input
        .lower()
        .strip()
    )

    # ==========================================
    # SCREEN INTERACTION
    # ==========================================

    if (
        "look at my screen" in text
        or
        "what am i looking at" in text
        or
        "what do you see" in text
    ):

        result = (
            analyze_screen(
                task="general"
            )
        )

        return (
            True,
            result
        )

    if (
        "help debug this" in text
        or
        "what error is this" in text
    ):

        result = (
            analyze_screen(
                task="debug"
            )
        )

        return (
            True,
            result
        )

    if (
        "explain this" in text
    ):

        result = (
            analyze_screen(
                task="explain"
            )
        )

        return (
            True,
            result
        )

    if (
        "summarize this page" in text
        or
        "summarize this" in text
    ):

        result = (
            analyze_screen(
                task="summary"
            )
        )

        return (
            True,
            result
        )

    if (
        "what should i do next" in text
    ):

        result = (
            analyze_screen(
                task="next_step"
            )
        )

        return (
            True,
            result
        )

    # ==========================================
    # LOCK IN MODE
    # ==========================================

    if text == "lock in":

        return (
            start_lock_in()
        )

    if (
        text == "stop lock in"
        or
        text == "im done studying"
    ):

        return (
            stop_lock_in()
        )

    # ==========================================
    # SPOTIFY CONTROL
    # ==========================================

    if text.startswith(
        "play "
    ):

        song = (
            text
            .replace(
                "play",
                "",
                1
            )
            .strip()
        )

        play_song(
            song
        )

        return (
            True,
            f"Playing {song}."
        )

    if (
        "pause music" in text
        or
        "pause spotify" in text
    ):

        pause_music()

        return (
            True,
            "Paused music."
        )

    if (
        "next song" in text
        or
        "skip song" in text
    ):

        next_song()

        return (
            True,
            "Skipping."
        )

    if (
        "previous song" in text
        or
        "last song" in text
    ):

        previous_song()

        return (
            True,
            "Going back."
        )

    # ==========================================
    # PROJECT SEARCH
    # ==========================================

    for trigger in PROJECT_WORDS:

        if text.startswith(
            trigger
        ):

            cleaned = (
                text
                .replace(
                    trigger,
                    "",
                    1
                )
                .strip()
            )

            success = (
                open_file_or_folder(
                    cleaned,
                    search_drive=True
                )
            )

            if success:

                return (
                    True,
                    f"Opening project {cleaned}."
                )

            return (
                True,
                f"I couldn't find {cleaned}."
            )

    # ==========================================
    # OPEN / LAUNCH
    # ==========================================

    for trigger in OPEN_WORDS:

        if text.startswith(
            trigger
        ):

            cleaned = clean_command(

                text.replace(
                    trigger,
                    "",
                    1
                )
            )

            success = (
                open_app(
                    cleaned
                )
            )

            if success:

                return (
                    True,
                    f"Opening {cleaned}."
                )

            success = (
                open_file_or_folder(
                    cleaned
                )
            )

            if success:

                return (
                    True,
                    f"Opening {cleaned}."
                )

            success = (
                open_website(
                    cleaned
                )
            )

            if success:

                return (
                    True,
                    f"Opening {cleaned}."
                )

            return (
                True,
                f"I couldn't find {cleaned}."
            )

    return (
        False,
        None
    )