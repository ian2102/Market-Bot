import pyautogui

def capture_positions():
    positions = []
    print("Move the mouse to the desired position and press Enter. Press Q when done.")

    while True:
        input_key = input()
        if input_key.lower() == 'q':
            break
        else:
            x, y = pyautogui.position()
            positions.append((x, y))
            print("Position captured:", (x, y))

    return positions

def main():
    positions = capture_positions()
    print("Positions captured:")
    for i, pos in enumerate(positions):
        print(f"Position {i+1}: {pos}")

if __name__ == "__main__":
    main()
