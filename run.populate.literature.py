import simplejson as json

from pymongo import Connection

# samples = ['relational-capital', 'social-capital']
samples = []

with open('data/index.json','r') as f:
  samples = json.load(f)

connection = Connection()
db = connection.reino.literature20140226

for sample in samples:
  with open('data/02-refined/%s-articledata.json' % sample, 'rU') as f:
    articleset = json.load(f)
    for article in articleset:
      article['articleset'] = sample
      db.articles.insert(article)
      for reference in article['referencelist']:
        reference['articleset'] = sample
        db.references.insert(reference)
