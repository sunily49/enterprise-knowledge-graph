import requests
import lxml
from bs4 import BeautifulSoup
from serpapi import GoogleSearch

from bs4 import BeautifulSoup
import requests, lxml

headers = {
    'User-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://www.google.com/search?q=goldman sachs&hl=en', headers=headers)


def get_knowledge_graph():
    soup = BeautifulSoup(html.text, 'lxml')

    title = soup.select_one('#rhs .mfMhoc span').text
    subtitle = soup.select_one('.wwUB2c span').text
    try:
        snippet = soup.select_one('.zsYMMe+ span').text
    except:
        snippet = None

    print(f"{title}\n{subtitle}\n{snippet}\n")

    for result in soup.select(".rVusze"):
        key_element = result.select_one(".w8qArf").text
        if result.select_one(".kno-fv"):
            value_element = result.select_one(".kno-fv").text.replace(": ", "")
        else:
            value_element = None
        key_link = f'https://www.google.com{result.select_one(".w8qArf a")["href"]}'
        try:
            key_value_link = f'https://www.google.com{result.select_one(".kno-fv a")["href"]}'
        except:
            key_value_link = None

        print(f"{key_element}{value_element}\nkey_link: {key_link}\nkey_value_link: {key_value_link}")

def get_top_10_search():
    # The code to get the html contents here.

    soup = BeautifulSoup(html, 'html.parser')

    # Find all the search result divs
    divs = soup.select("#search div.g")
    for div in divs:
        # Search for a h3 tag
        results = div.select("h3")

        # Check if we have found a result
        if (len(results) >= 1):
            # Print the title
            h3 = results[0]
            print(h3.get_text())


search_list = ['Dell','Apple']
for search_key in search_list:
    html = requests.get('https://www.google.com/search?q='+search_key+'&hl=en', headers=headers)
    get_knowledge_graph()
    get_top_10_search()
