import time
import pyautogui
import subprocess
import pygetwindow as gw


def focus_spotify():

    try:

        windows = gw.getWindowsWithTitle(
            "Spotify"
        )

        if windows:

            window = windows[0]

            if window.isMinimized:
                window.restore()

            window.activate()

            time.sleep(1)

            return True

    except:
        pass

    return False


def open_spotify():

    try:

        subprocess.Popen(
            "spotify"
        )

        time.sleep(4)

    except:
        print(
            "Couldn't open Spotify."
        )


def play_song(
    song_name
):

    # Focus or open Spotify
    focused = (
        focus_spotify()
    )

    if not focused:

        open_spotify()

        focus_spotify()

    time.sleep(1)

    # Open search
    pyautogui.hotkey(
        "ctrl",
        "k"
    )

    time.sleep(0.5)

    # Clear previous text
    pyautogui.hotkey(
        "ctrl",
        "a"
    )

    pyautogui.press(
        "backspace"
    )

    # Type song
    pyautogui.write(

        song_name,

        interval=0.03
    )

    time.sleep(1)

    # Search
    pyautogui.press(
        "enter"
    )

    time.sleep(2)

    # Play top result
    pyautogui.press(
        "enter"
    )

    return True


def pause_music():

    pyautogui.press(
        "playpause"
    )


def next_song():

    pyautogui.press(
        "nexttrack"
    )


def previous_song():

    pyautogui.press(
        "prevtrack"
    )