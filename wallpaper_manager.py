# import ctypes
# import os
# from utils.config import BASE_DIR   # assuming your config defines project root

# # Wallpaper image paths
# FRIENDLY = os.path.join(BASE_DIR, "data", "wallpapers", "friendly.jpg")
# ALERT = os.path.join(BASE_DIR, "data", "wallpapers", "alert.jpg")
# IDLE = os.path.join(BASE_DIR, "data", "wallpapers", "idle.jpg")


# def _set_wallpaper(path: str):
#     """Change Windows wallpaper"""
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)


# def show_friendly():
#     _set_wallpaper(FRIENDLY)


# def show_alert():
#     _set_wallpaper(ALERT)


# def show_idle():
#     _set_wallpaper(IDLE)

# ********************************************************************

import ctypes
import os

# Get project root automatically from this file location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Wallpaper image paths
# FRIENDLY = os.path.join(BASE_DIR, "data", "wallpapers", "friendly.jpg")
# ALERT = os.path.join(BASE_DIR, "data", "wallpapers", "alert.jpg")
# IDLE = os.path.join(BASE_DIR, "data", "wallpapers", "idle.jpg")

# wallpaper_manager.py mein in lines ko update karein:
FRIENDLY = os.path.join(BASE_DIR, "wallpapers", "friendly.jpg")
ALERT = os.path.join(BASE_DIR, "wallpapers", "alert.jpg")
IDLE = os.path.join(BASE_DIR, "wallpapers", "idle.jpg")

def _set_wallpaper(path: str):
    """Change Windows wallpaper"""
    if os.path.exists(path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
    else:
        print(f"[Wallpaper] Image not found: {path}")


def show_friendly():
    _set_wallpaper(FRIENDLY)


def show_alert():
    _set_wallpaper(ALERT)


def show_idle():
    _set_wallpaper(IDLE)

