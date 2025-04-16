from bs4 import BeautifulSoup

# 假设你的HTML内容是这样的
with open('panda_ref/index.html', 'r', encoding='utf-8') as file:
    
    html = file.read()

soup = BeautifulSoup(html, 'lxml')


navbar = soup.find_all('nav', class_='bd-header navbar navbar-expand-lg bd-navbar')

# 使用decompose删除它们
for element in navbar:
    element.decompose()

modified_html = soup.prettify()

with open("bd_html.html", "w", encoding="utf-8") as file:
    
    file.write(modified_html)

print("Modified HTML has been written to p_html.html")