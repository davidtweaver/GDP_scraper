import urllib.request as urllib
import requests
import re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#gdp from gov
url = 'https://www.ons.gov.uk/economy/grossdomesticproductgdp/timeseries/abmi/qna'
page = requests.get(url, verify=False)
soup = BeautifulSoup(page.text, 'html.parser')
table_contents = soup.find_all('td', text=True)

content = []
for td in soup.select('td'):
    content.append(td.string)

def graph_results(years,values):
    plt.plot(years, values)
    plt.show()

years = content[0::2]
values = content[1::2]

whole_years = years[:69]
whole_values = values[:69]
quarter_years = years[69:]
quarter_values = values[69:]

print("whole years", whole_years)
print("whole values", whole_values)
print("quarter years: ", quarter_years)
print("quarter values: ", quarter_values)

graph_results(whole_years, whole_values)
