import pyautogui

# Move the cursor to position (200, 100)
pyautogui.moveTo(200, 100)

# Move the cursor relative to its current position by (10, 10)
pyautogui.moveRel(10, 10)

# Get the current mouse position
currentMouseX, currentMouseY = pyautogui.position()

# Perform a single click
pyautogui.click()

# Perform a double click
pyautogui.doubleClick()

# Drag the cursor to position (500, 500) over 0.55 seconds
pyautogui.dragTo(500, 500, duration=0.55)

# Type a message with a 0.25-second interval between each character
pyautogui.typewrite("Hey What's up guys, Everyone is fine?", interval=0.25)

# Simulate pressing the 'ctrl' and 'o' keys together
# Ctrl+O is a keyboard shortcut used in computing
# to open a file or a document.

pyautogui.hotkey("ctrl", "o")
