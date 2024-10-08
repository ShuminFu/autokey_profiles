import subprocess
window_title = window.get_active_title()
window_class = window.get_active_class()
app = "org.gnome.Nautilus.org.gnome.Nautilus"

def get_window_id_by_class(window_class):
    # 使用wmctrl获取所有窗口的列表
    result = subprocess.check_output(["wmctrl", "-lx"]).decode("utf-8")
    for line in result.splitlines():
        # 检查窗口类是否匹配
        if window_class in line:
            # 返回窗口ID
            return line.split()[0]
    return None

def activate_window(window_id):
    # 使用xdotool将窗口展示在最前面
    subprocess.call(["xdotool", "windowactivate", window_id])

def hide_window(window_id):
    # 使用xdotool隐藏窗口
    subprocess.call(["xdotool", "windowminimize", window_id])

def start_finder():
    # 启动Finder窗口
    subprocess.call(["xdg-open", "/"])

window_id = get_window_id_by_class(app)

if window_id:    
    if app in window_class:
        hide_window(window_id)
    else:
        activate_window(window_id)
else:
    start_finder()

