#-*- coding: utf-8 -*-
import csv

# 
f = open('../Pob__.csv', 'r', encoding='utf8')
rdr = csv.reader(f, delimiter='	')
tr_kr = []

for line in rdr:
  tr_kr.append(line)
f.close()

with open('../translate_kr_.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for line in tr_kr:
      spamwriter.writerow(line)

with open('../spread_upload.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='	')
    for line in tr_kr:
      spamwriter.writerow(line)

count = 0
for line in tr_kr:
  count += 1

print(count)