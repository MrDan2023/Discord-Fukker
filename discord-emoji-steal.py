import os
import requests
from PIL import Image
from io import BytesIO
import ctypes

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

custom_title = "Discord Emoji Stealer - Mr Dan"

set_console_title(custom_title)

def save_discord_emoji(emoji_url, custom_name):
    if not os.path.exists("Emojis"):
        os.makedirs("Emojis")

    emoji_name = custom_name if custom_name else emoji_url.split("/")[-1].split(".")[0]

    response = requests.get(emoji_url)

    if response.status_code == 200:
        emoji_image = Image.open(BytesIO(response.content))

        emoji_image.save(f"Emojis/{emoji_name}.png", "PNG")
        print(f"Saved emoji as Emojis/{emoji_name}.png")
    else:
        print("Failed to fetch the emoji from the provided URL")

if __name__ == "__main__":
    emoji_url = input("Enter the Discord emoji URL: ")
    custom_name = input("Enter a custom name (or press Enter to use the default name): ")
    save_discord_emoji(emoji_url, custom_name)