import pyautogui
import cv2
import time
import math

color_gear_scores = {
    (15, 13, 12): 5,   # Black
    (15, 14, 14): 7,   # Grey
    (33, 32, 31): 10,  # White
    (18, 27, 6): 15,   # Green
    (9, 22, 34): 20,   # Blue
    (28, 14, 32): 30,  # Purple
    (33, 19, 5): 40    # Orange
}

def euclidean_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

def move_cursor_to_position(x, y):
    pyautogui.moveTo(x, y)

def capture_pixel_color(x, y):
    screenshot = pyautogui.screenshot()
    color = screenshot.getpixel((x + 76, y + 44))
    return color

def calculate_gear_score(color):
    closest_match = None
    min_distance = float('inf')

    for rarity, score in color_gear_scores.items():
        distance = euclidean_distance(rarity, color)
        if distance < min_distance:
            min_distance = distance
            closest_match = score
    
    return closest_match


def main():
    time.sleep(2)
    gear_positions = [
        (961, 515), (856, 491), (938, 444), (773, 441), (854, 345),
        (954, 371), (753, 372), (857, 226), (923, 237), (1033, 253),
        (680, 254), (1076, 555), (1065, 503), (1065, 451), (658, 578),
        (640, 508), (649, 452)
    ]
    gear_scores = []

    for position in gear_positions:
        move_cursor_to_position(position[0], position[1])
        time.sleep(0.1)
        after_color = capture_pixel_color(position[0], position[1])
        print(after_color)
        gear_score =  calculate_gear_score(after_color)
        gear_scores.append(gear_score)

    total_gear_score = sum(gear_scores)
    print("Total Gear Score:", total_gear_score)

if __name__ == "__main__":
    main()
