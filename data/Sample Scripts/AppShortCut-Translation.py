# Enter script code
import subprocess
try:
    selection = clipboard.get_selection()
    clipboard.fill_clipboard(selection)
except Exception as e:
    pass

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
    return None,None
# keyboard.send_keys("<super>+w")
subprocess.call("translatium")
time.sleep(0.05)
keyboard.send_keys("<ctrl>+a")
time.sleep(0.01)
keyboard.send_keys("<backspace>")
time.sleep(0.01)
keyboard.send_keys("<ctrl>+v")

if app not in window_class:
    window.activate(app, matchClass=True)
else:
    window_id,_ = get_window_id_by_class(window_class)
    subprocess.call(["xdotool", "windowminimize", window_id])


