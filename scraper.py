import csv
import requests
from BeautifulSoup import BeautifulSoup

url = "insert URL here"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./FILENAME.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["NAME", "OF", "ATTRIBUTE"])
writer.writerows(list_of_rows)