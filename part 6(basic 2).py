import pyautogui

# Move the mouse cursor to the absolute position (100, 100) on the screen
# This movement will take 10 seconds to complete
pyautogui.moveTo(100, 50, duration=5)


# Move the mouse cursor 200 pixels to the right and 90 pixels down from its current position
# This movement will also take 10 seconds to complete
pyautogui.moveRel(30, 90, duration=5)


"""
detailed  explanation:

X-coordinate: Specifies the horizontal position (left to right).
Y-coordinate: Specifies the vertical position (top to bottom).

This function moves the mouse cursor to the coordinates (100, 100) relative to the top-left corner of the screen.
The movement will take 10 seconds, meaning the cursor will move smoothly over 
the screen to the specified coordinates during this time.

This function moves the mouse cursor 200 pixels to the right (positive x direction) and
 90 pixels down (positive y direction) from its current position.
The movement will take 10 seconds, meaning the cursor will 
move smoothly over the screen to the new relative position 
during this time.

"""


"""
here you can move mouse on the screen 
it moves the cursor to specific coordinates (x, y)
relative to the top-left corner of the screen

pyautogui.moveTo(x, y, duration)

The pyautogui.moveRel() function moves the mouse 
cursor relative to its current position. 
This means it moves the cursor
by a certain number of pixels from its current location

pyautogui.moveRel(xOffset, yOffset, duration)

xOffset: The number of pixels to move the cursor
 horizontally (positive values move right, 
negative values move left).

yOffset: The number of pixels to move the cursor vertically
 (positive values move down, negative values move up).
 
"""