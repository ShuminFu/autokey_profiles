app = "Cursor"
window_title = window.get_active_title()
window_class = window.get_active_class()
import subprocess

def get_active_window_id():
    # 使用wmctrl获取当前活动窗口的ID
    window_id = subprocess.check_output(["wmctrl", "-lpG"]).decode("utf-8")
    active_window = None
    for line in window_id.splitlines():
        if f"{window_title}" in line:
            active_window = line.split()[0]
            break
    return active_window

def hide_window():
    # 获取当前活动窗口的ID
    window_id = get_active_window_id()
    if window_id:
        # 使用xdotool隐藏窗口
        subprocess.call(["xdotool", "windowminimize", window_id])

if app in window_title:
    hide_window()
    #keyboard.press_key("<super>")
    #keyboard.press_key("h")
    #keyboard.release_key("<super>")
    #keyboard.release_key("h")
    
else:
    window.activate(app)