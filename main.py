import pyautogui
import pytesseract
import time
import re
import os
import datetime
import requests

import graph


if not os.path.exists("region.txt"):
    print("Region file 'region.txt' not found. Please run 'region.py' first.")
    exit()

with open("region.txt", "r") as file:
    region_str = file.read().strip()

region_str = region_str.strip("()")
region = tuple(map(int, region_str.split(",")))


def send_file_to_discord(webhook_url, file_path, message):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        payload = {'content': message}
        response = requests.post(webhook_url, files=files, data=payload)
        if response.status_code == 200:
            print("File sent successfully to Discord webhook!")
        else:
            print(f"Failed to send file to Discord webhook: {response.status_code}")

webhook_url = 'https://discord.com/api/webhooks/1231039323512508526/n6z2xij7Iqt0tSIW4yo3kUIGfVZQ5fP_SfE-Kra_zNfjK6Fv-3BkaRk__UeX5HN3ofMv'


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


text = """
Market Master by Ian
Join our Discord server:
Dark Investments Chamber of Commerce | D.I.C.C
https://discord.gg/khQyWQHK

Open Dark and Darker, navigate to the item you want to monitor on the market, and position your mouse over the search button.
Press Ctrl-C to finish. Data will be automatically sent to the Discord graph channel.
"""

print(text)

try:
    while True:
        screenshot = pyautogui.screenshot()

        cropped_image = screenshot.crop(region)

        cropped_image = cropped_image.convert('L')

        text = pytesseract.image_to_string(cropped_image)
        new_text = ""
        lines = text.split("\n")
        for line in lines:
            new_line = line.split("x")
            new_text += new_line[0] + "\n"

        values = re.findall(r'(\d+\.\d+|\d+)', new_text)

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

        pyautogui.click()
        time.sleep(10)

except KeyboardInterrupt:
    print("KeyboardInterrupt: Escaping and plotting...")
    pass

file_path = f'{data_dir}plot{counter}.png'

graph.plot(file_path)

# Include the date in the message
message = f"{formatted_datetime}"
send_file_to_discord(webhook_url, file_path, message)
