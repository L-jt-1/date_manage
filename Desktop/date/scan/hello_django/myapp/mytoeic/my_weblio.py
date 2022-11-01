# import logging
# import sys
#Weblio英和辞典へのリクエストのレスポンスから発音、意味を取得
from bs4 import BeautifulSoup 
import requests


url='https://ejje.weblio.jp/content/'

def search_weblio(word):#データの取得
    response = requests.get(url+word)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def parse_item(word):#データの抽出：日本語訳
    soup = search_weblio(word)
    pronunciation = soup.find(class_='phoneticEjjeDesc').get_text() if soup.find(class_='phoneticEjjeDesc') else ''
    japanese = soup.find(class_='content-explanation ej').get_text().strip()

    return japanese

def create_item(word):
    properties=parse_item(word)
    
    print(properties)
    return properties
    
    
import sys
if __name__ == '__main__':
    create_item(sys.argv[1])
    


    
