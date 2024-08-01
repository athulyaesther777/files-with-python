# We use pyautogui using pip install pyautogui in terminal
# pip install --upgrade pyscreeze Pillow opencv-python-headless

import pyautogui
import time

# Add a delay to ensure the screen is ready
time.sleep(2)

# Get screen width and height
screenWidth, screenHeight = pyautogui.size()  # #GetScreenSize

# Move the mouse to the center of the screen
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)  # #MoveToCenter

# Locate the button on the screen and click it
try:
    button_location = pyautogui.locateCenterOnScreen("create_button.jpg", confidence=0.6)  # #LocateButton
    if button_location:
        button_x, button_y = button_location
        pyautogui.click(button_x, button_y)  # #ClickButton
        print("Button found and clicked!")
    else:
        print("Could not locate the image 'create_button.jpg'.")
except pyautogui.ImageNotFoundException:
    print("ImageNotFoundException: Could not locate the image 'create_button.png'. Please check the file path and ensure the image is on the screen.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Move the mouse with duration
pyautogui.moveTo(100, 100, duration=2)  # #MoveToCoordinates
pyautogui.moveTo(200, 0, duration=2)  # #MoveToAnotherCoordinates

# Perform click actions
pyautogui.click(100, 100)  # #SingleClick
pyautogui.doubleClick(100, 100)  # #DoubleClick
pyautogui.rightClick(100, 100)  # #RightClick

# Drag the mouse to a location with duration
pyautogui.dragTo(100, 100, duration=2)  # #DragToCoordinates
pyautogui.dragRel(200, 0, duration=2)  # #DragRelatively

# Scroll the mouse
pyautogui.scroll(200)  # #Scroll

# Type a message
pyautogui.typewrite("Hello Guys")  # #TypeMessage
pyautogui.press("enter")  # #PressEnter

# Press and release a key
pyautogui.keyDown("shift")  # #KeyDown
pyautogui.keyUp("shift")  # #KeyUp

# Take a screenshot
iml = pyautogui.screenshot()  # #TakeScreenshot
iml.save("iml.png")  # #SaveScreenshot

# Locate button on screen
try:
    pyautogui.locateOnScreen("create_button.png", confidence=0.6)  # #LocateButtonOnScreen
    pyautogui.locateCenterOnScreen("create_button.png", confidence=0.6)  # #LocateCenterOnScreen
except pyautogui.ImageNotFoundException:
    print("ImageNotFoundException: Could not locate the image 'create_button.png' during this step.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Use a hotkey combination
pyautogui.hotkey("ctrl", "o")  # #Hotkey

# Type with a delay between each character
pyautogui.typewrite("Hello Guys", interval=0.25)  # #TypeWithInterval

# Press the 'home' key
pyautogui.press("home")  # #PressHome
