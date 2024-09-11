window_title = window.get_active_title()
window_class = window.get_active_class()
if "zsh" in window_title:
    keyboard.send_keys("<ctrl>+<shift>+c")
elif "Terminal" in window_title:
    keyboard.send_keys("<ctrl>+<shift>+c")
else:
    keyboard.send_keys("<ctrl>+c")