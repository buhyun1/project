import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import re
import time

def get_news_titles(section_url, reg_date):
    all_titles = []
    page = 1
    prev_items = None

    while True:
        url = f"{section_url}{page}&regDate={reg_date}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to retrieve {url} (Status Code: {response.status_code})")
            break

        print(f"Processing {url}")
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.select('.box_etc li > div.cont_thumb > strong.tit_thumb')

        if prev_items == news_items:
            print(f"No new articles found for {url}. Ending the process.")
            break

        if not news_items:
            print(f"No more articles found for {url}. Ending the process.")
            break

        for item in news_items:
            title = item.select_one('a.link_txt').text.strip()
            link = item.select_one('a.link_txt')['href']
            all_titles.append({"Title": title, "Link": link})

        prev_items = news_items
        page += 1

    return all_titles

def is_english(text):
    words = text.split()
    english_words = [word for word in words if re.match(r'^[a-zA-Z]+$', word)]
    return len(english_words) / len(words) > 0.5 if words else False

# Define section URLs
section_urls = {
    "economic": "https://news.daum.net/breakingnews/economic?page="
}

# Define the date range for scraping
start_date = datetime(2023, 10, 1)
end_date = datetime(2023, 10, 31)

# Record start time
start_time = time.time()

# Iterate through section URLs and crawl news
for section_name, section_url in section_urls.items():
    current_date = start_date
    while current_date <= end_date:
        reg_date = current_date.strftime('%Y%m%d')
        news_titles = get_news_titles(section_url, reg_date)
        news_df = pd.DataFrame(news_titles)
        news_df = news_df[~news_df['Title'].str.contains('\\[포토\\]|\\[인사\\]|\\[부고\\]|\\[사진\\]|\\[동영상\\]')]
        news_df = news_df[~news_df['Title'].apply(is_english)]

        # Ensure unique filename for each day
        excel_filename = f'{reg_date}_news.xlsx'
        news_df.to_excel(excel_filename, index=False, engine='openpyxl')
        print(f"Successfully saved {section_name} news for {reg_date} to {excel_filename}")

        current_date += timedelta(days=1)

# Print execution time
end_time = time.time()
print(f"Script execution time: {end_time - start_time} seconds")
