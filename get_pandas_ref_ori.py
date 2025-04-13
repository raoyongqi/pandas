import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import sys
import re

url = "https://pandas.pydata.org/docs/user_guide/index.html"

chrome_options = uc.ChromeOptions()
chrome_options.headless = False  # 设为 True 可无头运行
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--user-data-dir=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default')

chrome_path = r'C:\ungoogled-chromium-windows\build\ungoogled-chromium_131.0.6778.85-1.1_windows_x64\ungoogled-chromium_131.0.6778.85-1.1_windows_x64\chrome.exe'

chrome_options.binary_location = chrome_path

driver = uc.Chrome(driver_executable_path="chromedriver.exe",options=chrome_options, browser_executable_path=chrome_path)


driver.get(url)

nav = driver.find_element(By.ID, 'bd-docs-nav')

hrefs = [a.get_attribute('href') for a in nav.find_elements(By.TAG_NAME, 'a')]

driver.quit()

os.makedirs("C:\\Users\\r\\Desktop\\panda_ref\\panda_ref",exist_ok=True)


single_file_path = "C:\\Users\\r\\Desktop\\zhuabao2\\single-file.exe"  # 指定 full path to single-file.exe


# match = re.search(r'/([^/]+)\.html$', url)

# if match:
#     last_part = match.group(1)
#     print(f"最后一个斜杠后的部分: {last_part}")
# else:
#     print("未找到匹配的部分")

# save_path = f"C:\\Users\\r\\Desktop\\panda_ref\\panda_ref\\{last_part}.html"


# exit_code = os.system(f' {single_file_path} --browser-arg --user-data-dir="C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default" {url} {save_path}')

# if exit_code != 0:
#     print(f'{single_file_path} --browser-arg --user-data-dir="C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default" {url} {save_path}')
#     print(f"❌ 错误: 命令执行失败 (退出码 {exit_code})，脚本终止。")
#     sys.exit(1)
# else:
#     print(f"✅ 成功处理 {url}")

total_hrefs = len(hrefs)

for index, href in enumerate(hrefs):
    match = re.search(r'/([^/]+)\.html$', href)
    if match:
        last_part = match.group(1)
        print(f"最后一个斜杠后的部分: {last_part}")
    else:
        print("未找到匹配的部分")
    save_path = f"C:\\Users\\r\\Desktop\\panda_ref\\panda_ref\\{last_part}.html"
    

    
    exit_code = os.system(f' {single_file_path} --browser-arg --user-data-dir="C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default" {href} {save_path}')
    
    if exit_code != 0:
        print(f'{single_file_path} --browser-arg --user-data-dir="C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default" {href} {save_path}')
        print(f"❌ 错误: 命令执行失败 (退出码 {exit_code})，脚本终止。")
        sys.exit(1)
    else:
        # Calculate remaining items
        remaining = total_hrefs - (index + 1)
        print(f"✅ 成功处理 {href}. 还剩 {remaining} 个链接。")
