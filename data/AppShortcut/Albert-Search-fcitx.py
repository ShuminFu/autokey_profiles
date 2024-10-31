import subprocess
result = subprocess.run(['fcitx-remote'], capture_output=True, text=True, check=True)
status = result.stdout.strip()
subprocess.call(["albert","toggle"])
time.sleep(0.05)
if status == '1':
    keyboard.send_keys("gg  ")
else:
    subprocess.call(['fcitx-remote','-t'])
    time.sleep(0.05)
    keyboard.send_keys("gg  ")