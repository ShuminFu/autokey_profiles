window_title = window.get_active_title()
window_class = window.get_active_class()
if "zsh" in window_title:
    keyboard.send_keys("<ctrl>+<shift>+v")
elif "Terminal" in window_title:
    #keyboard.send_keys(f"{window_title}")
    keyboard.send_keys("<ctrl>+<shift>+v")
else:
    keyboard.send_keys("<ctrl>+v")
