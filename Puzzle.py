import csv 

data = open('find_the_link.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data) 


#66 characters in the link
#print (len(data_lines))

#For list in data_lines there is one part of the link



link_found = []
index = 0

for line in data_lines:
    link_found.append(line[index])
    index += 1
        
link = ' '
for character in link_found:
    link += character
    
print (link)

data.close()

import PyPDF2
import re

f = open ('Find_the_Phone_Number.pdf','rb')
reader = PyPDF2.PdfReader(f)

pattern = r'\d{3}.\d{3}.\d{4}'

all_text = ''
for pages in range(1,len(reader.pages)):
    page = reader.pages[pages]
    page_text = page.extract_text()
    all_text += ' ' + page_text

match = re.search (pattern, all_text)
print(match.group())

