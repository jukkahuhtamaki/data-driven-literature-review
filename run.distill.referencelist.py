import simplejson as json

from pymongo import Connection

import csv
from csvunicode import CSVUnicodeWriter

from pprint import pprint

# authors = {}

samples = ['literature']

connection = Connection()
# db = connection.iend.literature20130519
db = connection.reino.literature20140226

def most_referenced_authors(sample,amount):
  authors = {}
  with open('data/02-refined/%s-rows.json' % sample, 'rU') as f:
    rows = json.load(f)
    for row in rows:
      # pprint(row.keys())
      for author in row['article']['authors']:
        if not authors.has_key(author):
          authors[author] = {'articles': 0, 'referenced': 0}
        authors[author]['articles'] += 1

      for reference in row['article']['referencelist']:
        for author in reference['authors']:
          if not authors.has_key(author):
            authors[author] = {'articles': 0, 'referenced': 0}
        authors[author]['referenced'] += 1

      # pprint(author)

  top_authors = sorted(authors.items(), key=lambda x: x[1]['referenced'],reverse=True)[:amount]
  return top_authors

def most_referenced(sample,amount):
  with open('data/02-refined/%s-rows.json' % sample, 'rU') as f:
    rows = json.load(f)
    for row in rows:
      # pprint(row.keys())
      for author in row['article']['authors']:
        if not authors.has_key(author):
          authors[author] = {'articles': 0, 'referenced': 0}
        authors[author]['articles'] += 1

      for reference in row['article']['referencelist']:
        for author in reference['authors']:
          if not authors.has_key(author):
            authors[author] = {'articles': 0, 'referenced': 0}
        authors[author]['referenced'] += 1

      pprint(author)

  with open('data/03-stats/%s-top-references.csv' % sample, 'wb') as f:
    writer = CSVUnicodeWriter(f)
    for row in rows:
      for reference in row['article']['referencelist']:
        for author in reference['authors']:
          for top_author,stats in sorted(authors.items(), key=lambda x: x[1]['referenced'],reverse=True)[:amount]:
            if author == top_author:
              writer.writerow([','.join(reference['authors']),reference['year'],reference['original']])

def references_by_authors_db(sample,authors):
  f = open('data/03-stats/%s-top-references.csv' % sample, 'wb')
  writer = CSVUnicodeWriter(f)

  for author,stats in authors:
    print author
    for reference in db.references.find({
        'articleset' : sample,
        'authors' : author
      }):
      # pprint(reference)
      writer.writerow([','.join(reference['authors']),reference['year'],reference['original']])

  f.close()

# for sample in samples:
#   glass = [('Glass R.', {}), ('Glass T.', {})]
#   pprint(references_by_authors_db(sample,glass))


for sample in samples:
  # most_referenced(sample,20)
  print sample
  top_authors = most_referenced_authors(sample,25)
  pprint(top_authors)
  references = references_by_authors_db(sample,top_authors)



  # pprint(references)
  # most_referenced_db(sample,25)
  # with open('view/%s-parsedebug.csv' % sample, 'wb') as f:
  #   writer = CSVUnicodeWriter(f)
  #   writer.writerow(['Author', 'Row'])
  #   for author,stats in :
  #     # print author,stats
  #     row = [author,author,unicode(stats['articles']),unicode(stats['referenced'])]
  #     writer.writerow(row)



