import subprocess
window_title = window.get_active_title()
window_class = window.get_active_class()
app = "obsidian.obsidian"

def get_window_id_by_class(window_class):
    # 使用wmctrl获取所有窗口的Noneaa列表
    result = subprocess.check_output(["wmctrl", "-lx"]).decode("utf-8")
    for line in result.splitlines():
        # 检查窗口类是否匹配
        if window_class in line:
            # 返回窗口ID
            return line.split()[0], line.split()[1]
    return None

def activate_window(window_id):
    # 使用xdotool将窗口展示在最前面
    subprocess.call(["xdotool", "windowactivate", window_id])

def hide_window(window_id):
    # 使用xdotool隐藏窗口
    subprocess.call(["xdotool", "windowminimize", window_id])

def start_app():
    # 启动App窗口
    subprocess.call(["/home/shumin/AppImages/obsidian.appimage", "--no-sandbox"])

window_id,desktop_id = get_window_id_by_class(app)
_, current_desktop_id =get_window_id_by_class(window_class) 
if window_id:    
    if app in window_class:
        hide_window(window_id)
    else:
        if desktop_id != current_desktop_id:
            window.move_to_desktop(app, current_desktop_id, matchClass=True)
        activate_window(window_id)
else:
    start_app()

