window_title = window.get_active_title()

if "zsh" in window_title:
    keyboard.send_keys("<alt>+<backspace>")
elif "Terminal" in window_title:
    keyboard.send_keys("<alt>+<backspace>")
else:
    keyboard.send_keys("<ctrl>+<backspace>")
