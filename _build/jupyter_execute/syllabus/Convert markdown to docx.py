mds = !ls *.md

for md in mds:
    name = md.split('.')[0]
    
    !pandoc -s {name}.md -o {name}.docx

!pandoc -s staff.docx  -o staff.md

faq = '1X7qCbdZdQdFFy4vzOpkwce3VavF5n8P1nzyNhDJrr7A'
file_id = faq
url = 'https://docs.google.com/document/d/'+ file_id + '/export?format=doc'

import requests

r = requests.get(url)

with open('faq2.docx', 'wb') as outfile:
    outfile.write(r.content)
    
!pandoc -s faq2.docx  -o faq2.md

from IPython.display import Markdown

with open('faq2.md', 'r') as infile:
    md = infile.read()
    
Markdown(md)

!pwd

