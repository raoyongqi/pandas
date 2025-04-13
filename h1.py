from bs4 import BeautifulSoup

with open('panda_ref/index.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')

header_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

for header_tag in header_tags:
    header_tag['data-immersive-translate-walked'] = '44326b63-304c-480b-97de-5d61dbb09b21'
    header_tag['data-immersive-translate-paragraph'] = '1'

    a_tag = header_tag.find('a')
    if a_tag:
        a_tag['data-immersive-translate-walked'] = '44326b63-304c-480b-97de-5d61dbb09b21'

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
                  'immersive-translate-target-translation-inline-wrapper-theme-none '
                  'immersive-translate-target-translation-inline-wrapper',
        'data-immersive-translate-translation-element-mark': '1'
    })
    
    font_tag_4 = soup.new_tag('font', **{
        'class': 'notranslate immersive-translate-target-inner '
                  'immersive-translate-target-translation-theme-none-inner',
        'data-immersive-translate-translation-element-mark': '1'
    })

    font_tag_4.string = header_tag.get_text()

    font_tag_3.append(font_tag_4)
    font_tag_2.append(font_tag_3)
    font_tag_1.append(font_tag_2)

    header_tag.append(font_tag_1)

modified_html = soup.prettify()

with open("h1_h6_html.html", "w", encoding="utf-8") as file:
    file.write(modified_html)

print("Modified HTML has been written to h1_h6_html.html")
