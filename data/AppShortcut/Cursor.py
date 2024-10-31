app = "cursor.Cursor"
window_title = window.get_active_title()
window_class = window.get_active_class()
import subprocess

def get_active_window_id(window_id):
    # 使用wmctrl获取当前活动窗口的ID
    results = subprocess.check_output(["wmctrl", "-lx"]).decode("utf-8")
    target_window_id = None
    target_window_title = None
    for line in results.splitlines():
        if window_id in line:
            target_window_id = line.split()[0]
            target_window_title = line.split()[-1]
            break
    return target_window_id,target_window_title

def hide_window(window_id):
    if window_id:
        subprocess.call(["xdotool", "windowminimize", window_id])
        
window_id,_ = get_active_window_id(window_title)
app_window_id, app_window_title = get_active_window_id(app)

if app in window_class:
    hide_window(window_id)
    
else:
    if app_window_id:
        subprocess.call(["xdotool", "windowactivate", app_window_id])