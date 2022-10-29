# import logging
# import sys

from bs4 import BeautifulSoup 
import requests

# notion_token = {Internal Integration Token}
# database_id = {データベースの ID}

# notion = Client(auth=notion_token)
url='https://ejje.weblio.jp/content/'

def search_weblio(word):
    response = requests.get(url+word)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def parse_item(word):
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
    


    
