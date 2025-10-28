from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find_all('table')[0]
world_titles = table.find_all('th')
world_table_titles = [ title.text.strip() for title in world_titles ]
for title in world_table_titles:
    print(title)

df = pd.DataFrame(columns=world_table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    single_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = single_row_data

print(df)

df.to_csv(r'/home/red.c/outputs/csv/wiki.csv', index = False )