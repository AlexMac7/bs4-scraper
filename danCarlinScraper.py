import bs4 as bs
import urllib.request

source = urllib.request.urlopen("https://en.wikipedia.org/wiki/Dan_Carlin").read()

soup = bs.BeautifulSoup(source, "lxml")

print(soup.get_text())

# for paragraph in soup.find_all("p"):
#     print(paragraph.text)
#
# for span_tag in soup.find_all("span"):
#     print(span_tag.text)
#
# for table_row in soup.find_all("tr"):
#     print(table_row.text)
#
# for table_header in soup.find_all("th"):
#     print(table_header.text)
#
# body = soup.body
# for paragraph in body.find_all("p"):
#     print(paragraph.text)
