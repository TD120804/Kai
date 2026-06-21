import random
import threading
import time

import pygetwindow as gw

from automation.kyoya_ai import (
    generate_kyoya_message
)


lock_in_mode = False

session_start = None

last_window = None
last_window_change = None


def get_active_window():

    try:

        window = (
            gw.getActiveWindow()
        )

        if window:

            return (
                window.title
            )

    except:
        pass

    return "Unknown"


def lock_in_loop():

    global last_window
    global last_window_change

    while lock_in_mode:

        wait_time = random.randint(
            10,
            15
        )

        time.sleep(
            wait_time
        )

        if not lock_in_mode:
            break

        current_window = (
            get_active_window()
        )

        now = time.time()

        if current_window != last_window:

            last_window = (
                current_window
            )

            last_window_change = (
                now
            )

        focus_time = int(

            (
                now
                -
                session_start
            ) / 60

        )

        same_window_time = int(

            (
                now
                -
                last_window_change
            ) / 60

        )

        message = (
            generate_kyoya_message(

                focus_time=
                focus_time,

                current_window=
                current_window,

                same_window_time=
                same_window_time
            )
        )

        print(
            f"\n🖤 KAI: {message}\n"
        )


def start_lock_in():

    global lock_in_mode
    global session_start
    global last_window
    global last_window_change

    if lock_in_mode:

        return (
            True,
            "Lock-in mode is already active."
        )

    lock_in_mode = True

    session_start = (
        time.time()
    )

    last_window = (
        get_active_window()
    )

    last_window_change = (
        time.time()
    )

    thread = threading.Thread(

        target=
        lock_in_loop,

        daemon=True
    )

    thread.start()

    return (
        True,
        "Very well. Your concentration is now under supervision."
    )


def stop_lock_in():

    global lock_in_mode

    if not lock_in_mode:

        return (
            True,
            "Lock-in mode is not active."
        )

    elapsed = int(

        (
            time.time()
            -
            session_start
        ) / 60

    )

    if elapsed < 25:

        remaining = (
            25 - elapsed
        )

        return (
            True,
            f"No. {remaining} minutes remain."
        )

    lock_in_mode = False

    return (
        True,
        f"Session complete. Focus time: {elapsed} minutes."
    )