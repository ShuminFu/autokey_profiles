import subprocess
import time

selection = None
try:
    selection = clipboard.get_selection()

except Exception as e:
    pass
    
# 获取ibus状态
result = subprocess.run(['ibus', 'engine'], capture_output=True, text=True, check=True)
current_engine = result.stdout.strip()

# 切换Albert
subprocess.call(["albert", "toggle"])

# 如果当前不是英文输入法,切换到英文
if current_engine != 'xkb:us::eng':
    subprocess.call(['ibus', 'engine', 'xkb:us::eng'])
    
time.sleep(0.05)
    
if selection is not None:
    translate_text = f"tr en {selection}"
    
    #clipboard.fill_clipboard(translate_text)
    #keyboard.send_keys(translate_text, send_mode=autokey.model.phrase.SendMode.CB_CTRL_V)
else:
    translate_text = "tr en "
    #keyboard.send_keys(translate_text)
subprocess.run(['xsel', '-c'])
keyboard.send_keys(translate_text, send_mode=autokey.model.phrase.SendMode.CB_CTRL_V)


