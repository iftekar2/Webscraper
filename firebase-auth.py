import requests
from bs4 import BeautifulSoup

def scrape_nbc_news_titles():
    url = "https://www.nbcnews.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles_set = set()  # Create a set to store unique titles
        
        # Find all the <h2> elements with the class 'storyline__headline'
        articles = soup.find_all('h2', class_='storyline__headline')
        
        if not articles:
            print("No articles found.")
            return
        
        for article in articles:
            # Find the <a> element within each <h2> element
            title_element = article.find('a')
            if title_element:
                title = title_element.text.strip()
                # Check if the title has already been stored
                if title not in titles_set:
                    print(title)
                    titles_set.add(title)  # Add the title to the set
            else:
                print("No title found for this article.")
    else:
        print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    scrape_nbc_news_titles()
