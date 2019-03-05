import requests
import feedparser


class Paper():

    def __init__(self, data):
        self.title = data['title'].replace('\n', '').replace('  ', ' ')
        self.authors = ', '.join([i['name'] for i in data['authors']])
        self.summary = ''.join(data['summary'])
        self.pdf_link = data['link'].replace('/abs/', '/pdf/')

    def print(self):
        print(self.title, '\n')
        print(self.authors, '\n')
        print(self.summary, '\n')


query = input('Input Query: ')
base = 'http://export.arxiv.org/api/query?search_query=all:'
url = base + query + '&start=0&max_results=5'
response = requests.get(url)
data = feedparser.parse(response.text)['entries']
papers = [Paper(i) for i in data]
for i in range(len(papers)):
    print('\n', i, '-\n')
    papers[i].print()
q = input('Download Index (-1 for dont download): ')
q = int(q)
if q == -1:
    exit()
assert q < len(papers)
assert q >= 0
paper = papers[q]

response = requests.get(paper.pdf_link, stream=True)

with open(paper.title + '.pdf', "wb") as handle:
    handle.write(response.content)

print('\nDownload Finished')
