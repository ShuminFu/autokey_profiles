window_title = window.get_active_title()
window_class = window.get_active_class()
if "zsh" in window_title:
    #keyboard.send_keys("1")
    keyboard.send_keys("<ctrl>+<shift>+c")
elif "Terminal" in window_title:
    #keyboard.send_keys("2")
    keyboard.send_keys("<ctrl>+<shift>+c")
elif "dingtalk" in window_class:
    selection = clipboard.get_selection()
    if selection:
        clipboard.fill_clipboard(selection)
elif "chrome" in window_class:
    keyboard.send_keys("<ctrl>+c")
    keyboard.send_keys("<ctrl>+c")
else:
    keyboard.send_keys("<ctrl>+c")
    #selection = clipboard.get_selection()
    #if selection:
        #clipboard.fill_clipboard(selection)
