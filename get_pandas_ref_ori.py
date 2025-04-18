import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import sys
import re
import time
from selenium.webdriver.common.action_chains import ActionChains

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

# selenium的对于保存页面的支持很差，放弃了


# # 关闭浏览器前先对特定的hrefs使用浏览器原生方法进行保存
# spec_hrefs =['https://pandas.pydata.org/docs/user_guide/10min.html']


# driver.get(spec_hrefs[0])
# match = re.search(r'/([^/]+)\.html$',spec_hrefs[0])
# if match:
#     last_part = match.group(1)
#     print(f"最后一个斜杠后的部分: {last_part}")
# else:
#     print("未找到匹配的部分")


# save_path = f"C:\\Users\\r\\Desktop\\panda_ref\\panda_ref\\{last_part}.html"
# actions = ActionChains(driver)
# actions.send_keys(Keys.CONTROL + 's')  # Windows 上 Ctrl+S，Mac 上可以使用 Keys.COMMAND + 's'
# actions.perform()


# time.sleep(500)
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

# hrefs = [x for x in hrefs if x not in spec_hrefs]

total_hrefs = len(hrefs)

for index, href in enumerate(hrefs):
    match = re.search(r'/([^/]+)\.html$', href)
    if match:
        last_part = match.group(1)
        print(f"最后一个斜杠后的部分: {last_part}")
    else:
        print("未找到匹配的部分")
    save_path = f"C:\\Users\\r\\Desktop\\panda_ref\\panda_ref\\{last_part}.html"
    
    if os.path.exists(save_path):
            print(f"文件 {save_path} 已存在，跳过保存。")
            continue  # 如果文件存在，跳过保存过程
        
    
    exit_code = os.system(f' {single_file_path} --browser-arg --user-data-dir="C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default" {href} {save_path}')
    
    if exit_code != 0:
        print(f'{single_file_path} --browser-arg --user-data-dir="C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default" {href} {save_path}')
        print(f"❌ 错误: 命令执行失败 (退出码 {exit_code})，脚本终止。")
        sys.exit(1)
    else:
        # Calculate remaining items
        remaining = total_hrefs - (index + 1)
        print(f"✅ 成功处理 {href}. 还剩 {remaining} 个链接。")
