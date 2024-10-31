app = "jetbrains-pycharm"
window_title = window.get_active_title()
window_class = window.get_active_class()
import subprocess

def get_window_id_by_strings(substrings):
    # 使用wmctrl获取所有窗口的列表
    result = subprocess.check_output(["wmctrl", "-lx"]).decode("utf-8")
    for line in result.splitlines():
        # 检查窗口标题是否包含指定的子字符串（不区分大小写）
        if any(substring.lower() in line.lower() for substring in substrings):
            # 返回窗口ID
            return line.split()[0]
    return None
    
def bring_pycharm_to_front(window_id):
    subprocess.call(["xdotool", "windowactivate", window_id])
       
    
substrings = ["Pycharm","pycharm"]
window_id = get_window_id_by_strings(substrings)

def hide_window(window_id):
    subprocess.call(["xdotool", "windowminimize", window_id])
    

if window_id:
    if "pycharm" in window_class or "pycharm" in window_class:
        hide_window(window_id)
    else:
        bring_pycharm_to_front(window_id)
else:
    subprocess.call(["/snap/pycharm-professional/412/bin/pycharm"])