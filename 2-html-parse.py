from bs4 import BeautifulSoup
import sys
#import csv

reload(sys)
sys.setdefaultencoding("utf8")

soup = BeautifulSoup(open('output.html'))

table = soup.find('table', {'class':'tab2Precos'})
rows = table.findAll('tr', )
header = table.findAll('td', {'class':'th1Precos'})

field_estado = [] 
field_data = []
reg = []
prod_seq = 0
#writer = csv.writer(open("output.csv", 'w'), delimiter=';')

for heads in header:
    field_estado.append(unicode(heads)[37:39])
    field_data.append(unicode(heads)[44:50] + unicode(heads)[55:59])

for tr in rows:
    cols = tr.findAll('td', {'class':['td0Precos','td1Precos']})
    for td in cols:
        reg.append(unicode(td.find(text=True)))
print reg
print sys.getdefaultencoding()
'''
while prod_seq < len(reg):
    for est_seq in range (1, 18):
        print str(reg[prod_seq]) +';'+ str(field_estado[est_seq]) +';'+ str(field_data[est_seq]) +';'+ str(reg[prod_seq+est_seq].strip())
        print str(prod_seq) +'----'+str(est_seq)
    prod_seq += 18
'''
