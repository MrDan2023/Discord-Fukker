import requests
import concurrent.futures
import ctypes

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

custom_title = "Webhook Tool - Mr Dan"
set_console_title(custom_title)

def send_message(webhook_url, message, proxy=None):
    data = {
        'content': message
    }
    try:
        if proxy:
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            response = requests.post(webhook_url, json=data, proxies=proxies)
        else:
            response = requests.post(webhook_url, json=data)
        
        if response.status_code == 204:
            print('Message sent successfully!')
        else:
            print(f'Failed to send message. Status code: {response.status_code}')
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

webhook_url = input("Enter your Discord webhook URL: ")

message = input("Enter the custom message you want to send: ")

try:
    num_times = int(input("Enter the number of times to send the message: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit(1)

use_proxies = input("Do you want to use proxies? (y/n): ").strip().lower()

proxy_list = []

if use_proxies == 'y':
    try:
        with open("proxies.txt", 'r') as file:
            proxy_list = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("File 'proxies.txt' not found. No proxies will be used.")
else:
    proxy_list = [None] * num_times

messages_to_send = [message] * num_times

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(send_message, [webhook_url] * num_times, messages_to_send, proxy_list)

input("Press Enter to exit...")
