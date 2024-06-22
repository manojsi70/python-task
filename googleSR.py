import requests
from bs4 import BeautifulSoup

def get_google_search_results(query, num_results=5):
    # URL encode the query string
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}&num={num_results}"

    # Set up headers to make the request look like it's coming from a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Ensure we notice bad responses
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for g in soup.find_all('div', class_='tF2Cxc', limit=num_results):
        title = g.find('h3').text
        link = g.find('a')['href']
        snippet = g.find('div', class_='VwiC3b').text
        results.append({'title': title, 'link': link, 'snippet': snippet})

    return results

# Example usage
query = 'Vimal Daga'
top_results = get_google_search_results(query)

for i, result in enumerate(top_results, start=1):
    print(f"Result {i}:")
    print(f"Title: {result['title']}")
    print(f"Link: {result['link']}")
    print(f"Snippet: {result['snippet']}")
    print("\n")
