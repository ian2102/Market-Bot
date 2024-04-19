import pyautogui
import pytesseract
import time
import re
import os
import datetime

data_dir = 'data/'

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

existing_files = os.listdir(data_dir)

counter = 0

for file in existing_files:
    match = re.search(r'(\d+)', file)
    if match:
        number = int(match.group(1))
        counter = max(counter, number)

counter += 1

filename = f'{data_dir}averages{counter}.csv'

print("Filename:", filename)


while True:
    screenshot = pyautogui.screenshot()

    #(left, upper, right, lower)
    region = (1490, 347, 1524, 952) #tb

    cropped_image = screenshot.crop(region)

    cropped_image = cropped_image.convert('L')

    text = pytesseract.image_to_string(cropped_image)
    new_text = ""
    lines = text.split("\n")
    for line in lines:
        new_line = line.split("x")
        new_text += new_line[0] + "\n"

    values = re.findall(r'(\d+\.\d+|\d+)', new_text)
    print(new_text)
    print(values)

    if values:
        total = sum(float(value) for value in values)
        average = total / len(values)
        low = values[0]
        high = values[-1]
    else:
        average = 0
        low = 0
        high = 0

    current_datetime = datetime.datetime.now()

    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    data = f"{formatted_datetime},{average},{high},{low}\n"
    with open(filename, "a") as file:
        file.write(data)

    time.sleep(10)
