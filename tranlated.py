import os
from bs4 import BeautifulSoup

# 设置文件夹路径
folder_path = 'translate'
os.makedirs("C:\\Users\\r\\Desktop\\panda_ref\\translated",exist_ok=True)

# 遍历文件夹中的所有 HTML 文件
for filename in os.listdir(folder_path):
    # 只处理 HTML 文件
    if filename.endswith('.html'):
        file_path = os.path.join(folder_path, filename)
        
        # 读取原始的 HTML 文件
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        # 找到 id 为 'bd-docs-nav' 的元素
        nav = soup.find(id='bd-docs-nav')

        # 如果找到了该元素，进行链接替换
        if nav:
            # 查找所有包含 href 属性的 <a> 标签
            for link in nav.find_all('a', href=True):
                # 获取原始的 href
                original_href = link['href']
                
                # 如果 href 是以 'https://pandas.pydata.org/docs/user_guide/' 开头，进行替换
                if original_href.startswith('https://pandas.pydata.org/docs/user_guide/'):
                    # 提取文件名部分（去掉 URL 的基础部分）
                    file_name = original_href.replace('https://pandas.pydata.org/docs/user_guide/', '')
                    
                    # 修改 href 为本地路径
                    new_href = f'file:///C:/Users/r/Desktop/panda_ref/translate/{file_name}'
                    link['href'] = new_href

        modified_file_path = os.path.join(folder_path, f"translate/{filename}")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        print(f"替换完成，保存为 {modified_file_path}")
