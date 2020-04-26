
# extract FAQ to excel sheet from website using web scraping

import xlsxwriter
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = "https://www.who.int/news-room/q-a-detail/q-a-coronaviruses"

# opening up connect & grabbing the page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

filename = "corona.xlsx"
workbook = xlsxwriter.Workbook(filename=filename)
faq_sheet = workbook.add_worksheet('FAQ Sheet')
headers = ['Answer','Question','Question Type', 'Key Phrases']
faq_sheet.write_row('A1', headers)

# html parsing
page_soup = soup(page_html, "html.parser")
faqs = page_soup.findAll("div", {"class": "sf-accordion__panel"})

qna_list = []

count = 1
for qna in faqs:
	question = qna.div.findAll("a", {"class": "sf-accordion__link"})[0].text.strip()
	answer = qna.findAll("div", {"class": "sf-accordion__content"})[0].text.strip()
	qna_list.append({"question": question, "answer": answer})
	faq_sheet.write_row(count, 0, [answer, question,'', ''])
	count += 1
workbook.close()
print("QNA ==>")
print(qna_list)