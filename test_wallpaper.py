from modules.wallpaper_manager import show_friendly, show_alert, show_idle
import time

print("Testing friendly wallpaper")
show_friendly()
time.sleep(5)

print("Testing alert wallpaper")
show_alert()
time.sleep(5)

print("Testing idle wallpaper")
show_idle()

