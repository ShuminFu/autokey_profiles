import subprocess
import time

# 获取ibus状态
result = subprocess.run(['ibus', 'engine'], capture_output=True, text=True, check=True)
current_engine = result.stdout.strip()

# 切换Albert
subprocess.call(["albert", "toggle"])
time.sleep(0.05)

# 如果当前不是英文输入法,切换到英文
if current_engine != 'xkb:us::eng':
    subprocess.call(['ibus', 'engine', 'xkb:us::eng'])
    time.sleep(0.05)

# 发送按键
keyboard.send_keys("gg  ")