from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import os
import time
import random
import matplotlib.pyplot as plt
import datetime

FILES_DIR = 'Testing files'

APP_URL = 'http://localhost:5000'

CHROME_DRIVER_PATH = 'C:/webdrivers/chromedriver.exe'

def upload_random_file(_):
    file_name = random.choice(os.listdir(FILES_DIR))
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(APP_URL)

    absolute_file_path = os.path.abspath(os.path.join(FILES_DIR, file_name))

    start_time = time.time()

    file_input = driver.find_element(By.NAME, 'file')
    file_input.send_keys(absolute_file_path)

    submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    submit_button.click()

    time.sleep(2)  # Wait for upload to complete

    end_time = time.time()
    driver.quit()

    return end_time - start_time  # Return the time taken for upload

num_uploads = 40

times_taken = []
with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(upload_random_file, range(num_uploads))
    times_taken = list(results)

current_timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
filename = f'upload_performance_{current_timestamp}.png'

plt.figure(figsize=(10, 6))
plt.hist(times_taken, bins=20, color='skyblue', edgecolor='black')
plt.title('File Upload Performance')
plt.xlabel('Time Taken (s)')
plt.ylabel('Number of Uploads')
plt.grid(True)
plt.savefig(filename)
plt.show()