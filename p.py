from bs4 import BeautifulSoup


with open('panda_ref/index.html', 'r', encoding='utf-8') as file:
    
    html = file.read()

soup = BeautifulSoup(html, 'lxml')

article_tag = soup.find('article')
if article_tag is not None:
    p_tag = article_tag.find('p')
else:
    print("No <article> tag found")
    p_tag = None 

article_tag = soup.find('article')

if article_tag is not None:
    p_tags = article_tag.find_all('p')
else:
    print("No <article> tag found")
    p_tags = []

for p_tag in p_tags:
    p_tag['data-immersive-translate-walked'] = '44326b63-304c-480b-97de-5d61dbb09b21'


    p_tag['data-immersive-translate-paragraph'] = '1'

    font_tag_1 = soup.new_tag('font', **{
        'class': 'notranslate immersive-translate-target-wrapper',
        'data-immersive-translate-translation-element-mark': '1',
        'lang': 'zh-CN'
    })

    font_tag_2 = soup.new_tag('font', **{
        'class': 'notranslate',
        'data-immersive-translate-translation-element-mark': '1'
    })
    
    font_tag_3 = soup.new_tag('font', **{
        'class': 'notranslate immersive-translate-target-translation-theme-none '
                  'immersive-translate-target-translation-block-wrapper-theme-none '
                  'immersive-translate-target-translation-block-wrapper',
        'data-immersive-translate-translation-element-mark': '1'
    })
    
    font_tag_4 = soup.new_tag('font', **{
        'class': 'notranslate immersive-translate-target-inner '
                  'immersive-translate-target-translation-theme-none-inner',
        'data-immersive-translate-translation-element-mark': '1'
    })

    font_tag_4.string = p_tag.get_text()
    br_tag = soup.new_tag('br')

    font_tag_3.append(font_tag_4)
    font_tag_2.append(font_tag_3)
    br_tag.append(font_tag_2)
    font_tag_1.append(br_tag)

    p_tag.append(font_tag_1)

modified_html = soup.prettify()

with open("p_html.html", "w", encoding="utf-8") as file:
    
    file.write(modified_html)

print("Modified HTML has been written to p_html.html")