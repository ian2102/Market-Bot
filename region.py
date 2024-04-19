import pyautogui

print("Click on the top-left corner of the region")
input()
top_left_x, top_left_y = pyautogui.position()

print("Click on the bottom-right corner of the region")
input()
bottom_right_x, bottom_right_y = pyautogui.position()

region = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)

print(region)