# Enter script code
import subprocess

selection = clipboard.get_selection()
clipboard.fill_clipboard(selection)
keyboard.send_keys("<meta>+w")

window_title = window.get_active_title()
window_class = window.get_active_class()
app = "translatium.Translatium"

def get_window_id_by_class(window_class):
    # 使用wmctrl获取所有窗口的Noneaa列表
    result = subprocess.check_output(["wmctrl", "-lx"]).decode("utf-8")
    for line in result.splitlines():
        # 检查窗口类是否匹配
        if window_class in line:
            # 返回窗口ID
            return line.split()[0], line.split()[1]
    return None
keyboard.send_keys("<meta>+w")
time.sleep(0.05)
if app not in window_class:
    window.activate(app, matchClass=True)


