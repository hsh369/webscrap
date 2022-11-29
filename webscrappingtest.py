import requests as r
from bs4 import BeautifulSoup 
import csv
# with open('index.html') as html_page:
#   soup = BeautifulSoup(html_page, 'lxml')


# for i in soup.find_all('div'):
#   print(f'Name: {i.h2.text} \n')

source = r.get('https://qalampir.uz/uz/news/category/intervyu').text
soup =BeautifulSoup(source,'lxml')

csv_file = open('qalampiruz.csv','w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['title','date','view'])

box_list = soup.find_all('div',class_='content')
count = 0 
for i in box_list:
  count +=1
  title = i.find('div')
  date = i.find('span', class_='date_view flex_row')
  view = i.find('span', class_='flex_row')
  csv_writer.writerow([title.text,date.span.text,view.text.split('\t')[11]])
  

csv_file.close()
