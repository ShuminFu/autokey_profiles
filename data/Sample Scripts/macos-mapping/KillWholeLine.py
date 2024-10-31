window_title = window.get_active_title()

if "zsh" in window_title:
    keyboard.send_keys("<ctrl>+u")
elif "Terminal" in window_title:
    keyboard.send_keys("<ctrl>+u")
else:
    keyboard.send_keys("<home>")
    keyboard.send_keys("<shift>+<end>")
    time.sleep(0.01)
    keyboard.send_keys("<backspace>")