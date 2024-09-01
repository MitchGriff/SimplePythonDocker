import random
import requests
from bs4 import BeautifulSoup

# Prints out IMDB top movie list

URL = 'http://www.imdb.com/chart/top'

def main():
    headers = headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    response = requests.get(URL, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    get_html = soup.find_all('div', class_='sc-b189961a-0 iqHBGn cli-children')
    
    for html in get_html:
        movie_name = html.find('h3', class_='ipc-title__text').text.strip()
        print(movie_name)
    

if __name__ == '__main__':
    main()