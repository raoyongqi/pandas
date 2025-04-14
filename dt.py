from bs4 import BeautifulSoup

with open('panda_ref/10min.html', 'r', encoding='utf-8') as file:
    
    html = file.read()

# Parse the original HTML
soup = BeautifulSoup(html, "html.parser")

# Modify the <dt> tag by adding translation attributes
dt_tag = soup.dt
dt_tag['data-immersive-translate-walked'] = '30b7bb95-054c-4717-81c4-2ecb20f40450'
dt_tag['data-immersive-translate-paragraph'] = '1'

# Modify the <a> tag's href attribute and add translation attributes
a_tag = dt_tag.find('a')
a_tag['href'] = "../reference/api/pandas.Series.html#pandas.Series"
a_tag['data-immersive-translate-walked'] = '30b7bb95-054c-4717-81c4-2ecb20f40450'

# Create <font> tags for translation content
font_outer = soup.new_tag('font', **{
                                'class': 'notranslate immersive-translate-target-wrapper',
                                'data-immersive-translate-translation-element-mark': '1',
                                'lang': 'zh-CN'
                            })

font_inner =  soup.new_tag('font', **{
                                'class': 'notranslate',
                                'data-immersive-translate-translation-element-mark': '1'
                            })

font_inner_inner =  soup.new_tag('font', **{
                                'class': 'notranslate immersive-translate-target-translation-theme-none '
                                        'immersive-translate-target-translation-inline-wrapper-theme-none '
                                        'immersive-translate-target-translation-inline-wrapper',
                                'data-immersive-translate-translation-element-mark': '1'
                            })
                            

# Create the translation content
translated_a_tag = soup.new_tag("a",**{ 
                                'data-immersive-translate-walked':"30b7bb95-054c-4717-81c4-2ecb20f40450", 
                                'title':"pandas.Series", 
                                'href':"../reference/api/pandas.Series.html#pandas.Series", 
                                'class':"reference internal"})
translated_code_tag = soup.new_tag("code",  **{
                                   'data-immersive-translate-walked':"30b7bb95-054c-4717-81c4-2ecb20f40450", 
                                   'class':"xref py py-class docutils literal notranslate"})


translated_span_tag = soup.new_tag("span", class_="pre")
translated_span_tag.string = "Series"
translated_code_tag.append(translated_span_tag)
translated_a_tag.append(translated_code_tag)

# Add the translated text
font_inner_inner.append(translated_a_tag)
font_inner_inner.append(" ：保存任意类型数据的一维标记数组")
font_inner.append(font_inner_inner)
font_outer.append(font_inner)

# Append the translation part after the original text in <dt>
dt_tag.append(" ")
dt_tag.append(font_outer)

# Output the final HTML
modified_html = soup.prettify()

with open("dt_html.html", "w", encoding="utf-8") as file:
    file.write(modified_html)

print("Modified HTML has been written to dt_html.html")
