window_title = window.get_active_title()
window_class = window.get_active_class()

if "Chrome" in window_title:
    keyboard.send_keys("<alt>+<shift>+o")
elif "Cursor" in window_title:
    keyboard.send_keys("<ctrl>+<page_up>")
