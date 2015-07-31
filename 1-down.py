import urllib2

url = "http://www.ceasa.gov.br/precos.php?TIP=1&P01=1&P02=1&P03=0&P04=0"

headers = {'Host':'www.ceasa.gov.br',
            'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0",
            'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            'Accept-Language':"pt-BR,pt,q=0.5",
            'Content-Type':'iso-8859-1',
            'DNT':'1',
            'Referer':"http://www.ceasa.gov.br/precos.php?TIP=1&P01=1&P02=1&P03=0&P04=0",
}

request = urllib2.Request(url, None, headers)

raw_file = urllib2.urlopen(request)

output = open('output.html', 'w')

output.write(raw_file.read())
output.close()
