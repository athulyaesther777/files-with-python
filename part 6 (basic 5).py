import pyautogui


pyautogui.scroll(200)  # Scroll up 500 units
pyautogui.scroll(-500) # Scroll down 500 units
pyautogui.scroll(200)

# Type the string " Who is here ? " at the current cursor position
pyautogui.typewrite(" Who is here ? ")

# Press the Enter key
pyautogui.press("enter")

# Press and hold the Shift key (no action in this snippet as it's followed immediately by keyUp)
pyautogui.keyDown("shift")

# Release the Shift key
pyautogui.keyUp("shift")

#anywhere you place the mouse  there you can s
#watch 'who is there ' or what ever you placed in the
#typewrite
