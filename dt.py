from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

with open('panda_ref/10min.html', 'r', encoding='utf-8') as file:
    
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

new_dl = '''
<dl class="simple">
  <dt>
    <a class="reference internal" href="https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series" title="pandas.Series">
      <code class="xref py py-class docutils literal notranslate">
        <span class="pre">Series</span>
      </code>
    </a>
    : a one-dimensional labeled array holding data of any type
  </dt>
  <dd>
    <p>such as integers, strings, Python objects etc.</p>
  </dd>
</dl>
'''

new_soup = BeautifulSoup(new_dl, 'html.parser')

new_dl_tag = new_soup.find('dl')


soup.find('dl').replace_with(new_dl_tag)


ori_text = soup.find('dt').text


soup = BeautifulSoup(html, 'html.parser')

dt_tag = soup.find('dt')
dt_tag['data-immersive-translate-walked'] = '876be6db-3ad1-4b45-b8f2-d3786b46a801'
dt_tag['data-immersive-translate-paragraph'] = '1'

a_tag = dt_tag.find('a')
a_tag['href'] = '../reference/api/pandas.Series.html#pandas.Series'
a_tag['data-immersive-translate-walked'] = '876be6db-3ad1-4b45-b8f2-d3786b46a801'

code_tag = a_tag.find('code')
code_tag['data-immersive-translate-walked'] = '876be6db-3ad1-4b45-b8f2-d3786b46a801'

font_tag = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-wrapper',
    'data-immersive-translate-translation-element-mark': '1',
    'lang': 'zh-CN'
})

font_tag.append(ori_text)

dt_tag.contents[-1].insert_after(font_tag)

with open("dt.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

print("Modified HTML has been written to dt.html")
