import asyncio
from translator import google_translate_long_text_async
import os
import asyncio
from bs4 import BeautifulSoup, Tag
import json

async def process_html_translation(html,filename):

    soup = BeautifulSoup(html, 'lxml')

    # 找到所有需要处理的标签
    
    article_tag = soup.find('article')

    if article_tag is not None:

        section_tag = article_tag.find('section')
        
        if section_tag is not None:
            section_section_tags = section_tag.find('section')

            header_tags = section_tag.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            p_tags = section_tag.find_all('p')

            header_tags_outside_section = []
            p_tags_outside_section = []
            for header in header_tags:

                if not any(header in section_tag.find_all('h1, h2, h3, h4, h5, h6') for section in section_section_tags):
                    header_tags_outside_section.append(header)

            for p in p_tags:

                if not any(p in section_tag.find_all('p') for section in section_section_tags):
                    p_tags_outside_section.append(p)


            to_translate = []


            for header_tag in header_tags:
                to_translate.append(header_tag.get_text())

            for p_tag in p_tags :
                to_translate.append(p_tag.get_text())
            
            to_translate = [text if text.strip() else " " for text in  to_translate]

            for idx, text in enumerate(to_translate):

                if not text.strip():
                    print(f"Skipping text at index {idx} because it's empty or only whitespace.")
                else:
                        
                    to_translate[idx] = text.replace('\n', ' ').rstrip('#')

            batch_text = "\n".join(to_translate)


            translated_batch = await google_translate_long_text_async(batch_text, "zh-CN")
            
            translated_texts = translated_batch.split("\n")

            translated_texts = [text.replace("大熊猫", "pandas") for text in translated_texts]

            translated_texts = [text.replace("熊猫", "pandas") for text in translated_texts]
            
            assert len(to_translate) == len(translated_texts), \
                f"Mismatch in the number of texts before and after translation: {len(section_translate)} != {len(translated_texts)}"
            
            text_index = 0

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

                font_tag_4.string = translated_texts[text_index]
                text_index += 1

                font_tag_3.append(font_tag_4)
                font_tag_2.append(font_tag_3)
                font_tag_1.append(font_tag_2)

                header_tag.append(font_tag_1)

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

                # 使用翻译后的文本
                font_tag_4.string = translated_texts[text_index]
                text_index += 1

                br_tag = soup.new_tag('br')

                font_tag_3.append(font_tag_4)
                font_tag_2.append(font_tag_3)
                br_tag.append(font_tag_2)
                font_tag_1.append(br_tag)

                p_tag.append(font_tag_1)

            for section_section_tag in section_section_tags:

                section_header_tags = []
                
                section_p_tags = []

                if isinstance(section_section_tag, Tag):
                    # 如果是有效的 Tag 对象，那么就可以调用 find_all
                    section_header_tags = section_section_tag.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

                    section_p_tags = section_section_tag.find_all('p')


                section_translate = []

                if section_header_tags or section_p_tags:
                    
                    
                    for section_header_tag in section_header_tags:
                        section_translate.append(section_header_tag.get_text())

                    for section_p_tag in section_p_tags :
                        section_translate.append(section_p_tag.get_text())
                    
                    section_translate = [text if text.strip() else " " for text in section_translate]

                    for idx, text in enumerate(section_translate):

                        if not text.strip(): 
                            print(f"Skipping text at index {idx} because it's empty or only whitespace.")
                        else:
                                
                            section_translate[idx] = text.replace('\n', ' ').rstrip('#')
                    
                    if section_translate:
                        batch_text = "\n".join(section_translate)

                        
                        translated_batch = await google_translate_long_text_async(batch_text, "zh-CN")
                        
                        translated_texts = translated_batch.split("\n")

                        translated_texts = [text.replace("大熊猫", "pandas") for text in translated_texts]

                        translated_texts = [text.replace("熊猫", "pandas") for text in translated_texts]

                        assert len(section_translate) == len(translated_texts), \
                            f"Mismatch in the number of texts before and after translation: {len(section_translate)} != {len(translated_texts)}"
                        
                        print(len(section_translate))
                        text_index = 0

                        for section_header_tag in section_header_tags:

                            section_header_tag['data-immersive-translate-walked'] = '44326b63-304c-480b-97de-5d61dbb09b21'
                            section_header_tag['data-immersive-translate-paragraph'] = '1'

                            a_tag = section_header_tag.find('a')
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
                            font_tag_4.string = translated_texts[text_index]
                            text_index += 1

                            font_tag_3.append(font_tag_4)
                            font_tag_2.append(font_tag_3)
                            font_tag_1.append(font_tag_2)

                            section_header_tag.append(font_tag_1)

                        for section_p_tag in section_p_tags:
                            section_p_tag['data-immersive-translate-walked'] = '44326b63-304c-480b-97de-5d61dbb09b21'
                            section_p_tag['data-immersive-translate-paragraph'] = '1'

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

                            font_tag_4.string = translated_texts[text_index]
                            text_index += 1

                            br_tag = soup.new_tag('br')

                            font_tag_3.append(font_tag_4)
                            font_tag_2.append(font_tag_3)
                            br_tag.append(font_tag_2)
                            font_tag_1.append(br_tag)

                            section_p_tag.append(font_tag_1)

        links = article_tag.find_all('a', href=True)

        if links:
            for link in links:
                original_href = link['href']
                
                # 如果 href 是以 'https://pandas.pydata.org/docs/user_guide/' 开头，进行替换
                if original_href.startswith('https://pandas.pydata.org/docs/user_guide/'):
                    # 提取文件名部分（去掉 URL 的基础部分）
                    file_name = original_href.replace('https://pandas.pydata.org/docs/user_guide/', '')
                    
                    # 修改 href 为本地路径
                    new_href = f'file:///C:/Users/r/Desktop/panda_ref/translate/{file_name}'
                    link['href'] = new_href
        nav = soup.find(id='bd-docs-nav')

        if nav:

            links = nav.find_all('a', href=True)
                
            if links:
                for link in links:
                    # 获取原始的 href
                    original_href = link['href']
                    
                    if original_href.startswith('https://pandas.pydata.org/docs/user_guide/'):

                        file_name = original_href.replace('https://pandas.pydata.org/docs/user_guide/', '')
                        
                        new_href = f'file:///C:/Users/r/Desktop/panda_ref/translate/{file_name}'
                        link['href'] = new_href

        modified_html = soup.prettify()

        with open(f"translate/{filename}", "w", encoding="utf-8") as file:
            file.write(modified_html)

        print("Modified HTML has been written to all_html.html")


folder_path ="C:\\Users\\r\\Desktop\\panda_ref\\panda_ref"

async def process_html_files_in_folder(folder_path, output_folder="translate"):

    for filename in os.listdir(folder_path):
        
        if filename.endswith(".html"):

            file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(output_folder, filename) 
            
            if os.path.exists(output_file_path):  
                print(f"文件 {filename} 已存在，跳过处理.")
                continue
            

            with open(file_path, 'r', encoding='utf-8') as file:
                html = file.read()
            
            print(f"正在处理文件: {filename}")
            
            await process_html_translation(html, filename)
        
asyncio.run(process_html_files_in_folder(folder_path))