import pyautogui
import win32api
import time
a = -1
print("Press F7 to get mouse position (x, y)")



print("Press F7 on the top-left corner of the region")
while True:
    x = 0
    y = 0
    top_left_x, top_left_y = pyautogui.position()
    a = win32api.GetKeyState(0x76)
    if a < 0:
        time.sleep(1)
        break
    time.sleep(0.1)


print("Press F7 on the bottom-right corner of the region")
while True:
    x = 0
    y = 0
    bottom_right_x, bottom_right_y = pyautogui.position()
    a = win32api.GetKeyState(0x76)
    if a < 0:
        break
    time.sleep(0.1)

region = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)

print(region)

# Save region coordinates to a file
with open("region.txt", "w") as file:
    file.write(str(region))
