window_title = window.get_active_title()
window_class = window.get_active_class()
if "zsh" in window_title:
    mouse.click_relative_self(0, 0, 3)
elif "Terminal" in window_title:
    mouse.click_relative_self(0, 0, 3)
else:
    keyboard.send_keys("<ctrl>+v")
