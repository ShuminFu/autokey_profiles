import subprocess
import json
import shlex

interpreter = '/home/shumin/.cache/pypoetry/virtualenvs/ironforge-PnHFmv3W-py3.12/bin/python'
py_script = '/home/shumin/PycharmProjects/IronForge/translators/translate_API.py'
selection = None

# 获取ibus状态
result = subprocess.run(['ibus', 'engine'], capture_output=True, text=True, check=True)
current_engine = result.stdout.strip()
# 如果当前不是英文输入法,切换到英文
if current_engine != 'xkb:us::eng':
    subprocess.call(['ibus', 'engine', 'xkb:us::eng'])

try:
    selection = clipboard.get_selection()
except Exception as e:
    pass
    
target = "zh"    

if selection is not None: 
    result = subprocess.run([interpreter, py_script, selection, target], capture_output=True, text=True, check=True)
    #translation_result = json.loads(result.stdout)
    parsed_result = json.loads(result.stdout)
    json_result = json.dumps(parsed_result, ensure_ascii=False)
    clipboard.fill_clipboard(json_result)
    subprocess.call(["albert", "toggle"])
    
    time.sleep(0.05)
    keyboard.send_keys("tr ")
    keyboard.send_keys("<ctrl>+v")
else:
    query = "tr "
    subprocess.call(["albert", "toggle"])
    keyboard.send_keys(query)
    
