window_title = window.get_active_title()
window_class = window.get_active_class()
keyboard.send_keys(f"{window_title}")
if "Chrome" in window_title:
    keyboard.send_keys("<ctrl>+<shift>+t")
else:
    keyboard.send_keys("<alt>+<shift>+t")