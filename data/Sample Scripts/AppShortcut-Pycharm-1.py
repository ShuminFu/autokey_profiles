app = "jetbrains-pycharm"
window_title = window.get_active_title()
window_class = window.get_active_class()
import subprocess

def get_window_id_by_title(substring):
    # 使用wmctrl获取所有窗口的列表
    result = subprocess.check_output(["wmctrl", "-l"]).decode("utf-8")
    for line in result.splitlines():
        # 检查窗口标题是否包含指定的子字符串（不区分大小写）
        if substring.lower() in line.lower():
            # 返回窗口ID
            return line.split()[0]
    return None
    
def bring_pycharm_to_front():
    # 指定要匹配的子字符串
    substring = ".py"
    # 获取包含指定子字符串的窗口ID
    window_id = get_window_id_by_title(substring)
    if window_id:
        # 使用xdotool将窗口展示在最前面
        subprocess.call(["xdotool", "windowactivate", window_id])
        
def get_active_window_id():
    # 使用wmctrl获取当前活动窗口的ID
    window_id = subprocess.check_output(["wmctrl", "-lpG"]).decode("utf-8")
    active_window = None
    for line in window_id.splitlines():
        if f"{app}" in line:
            active_window = line.split()[0]
            break
    return active_window
window_id = get_active_window_id()

def hide_window():
    subprocess.call(["xdotool", "windowminimize", window_id])
    
keyboard.send_keys(f"{window_id}")
if window_id:
    if ".py" in window_title:
        hide_window()
    else:
        bring_pycharm_to_front()
else:
    subprocess.call(["/snap/pycharm-professional/412/bin/pycharm"])