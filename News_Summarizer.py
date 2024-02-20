from bs4 import BeautifulSoup
import requests
from newspaper import Article

def fetch_news_headlines():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h3', class_='gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text')
    news_links = []
    for headline in headlines:
        link = headline.a['href']
        news_links.append('https://www.bbc.com' + link)
    return news_links

def summarize_article(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    print("Title:", article.title)
    print("Summary:", article.summary)

def main():
    print("Fetching news headlines from BBC...")
    news_links = fetch_news_headlines()
    print("Found", len(news_links), "headlines.")

    for i, link in enumerate(news_links, 1):
        print(f"{i}. {link}")

    while True:
        try:
            choice = int(input("Enter the number of the article you want to summarize (or 0 to exit): "))
            if choice == 0:
                print("Exiting...")
                break
            elif 0 < choice <= len(news_links):
                summarize_article(news_links[choice - 1])
            else:
                print("Invalid choice. Please enter a number between 1 and", len(news_links))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

