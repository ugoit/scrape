# coding: utf-8
import lxml.html
import requests
import sys,codecs

sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='ignore')

target_url = 'https://ja.wikipedia.org/wiki/%E7%99%BD%E3%81%84%E3%83%90%E3%83%A9'
target_html = requests.get(target_url).text
root = lxml.html.fromstring(target_html)
a=root.cssselect('#mw-content-text > p')[0].text_content()
print(a)