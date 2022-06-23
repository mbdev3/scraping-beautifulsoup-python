from bs4 import BeautifulSoup 

with open('tailwind-landing-page-main/index.html','r',encoding="utf8") as html_file:
    content = html_file.read()
    print(content)