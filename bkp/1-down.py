import urllib2

url = "http://www.ceasa.gov.br/precos.php?TIP=1&P01=1&P02=1&P03=0&P04=0"
'''
headers = {'Host':'www.ceasa.gov.br',
            'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0",
            'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            'Accept-Language':"pt-BR,pt,q=0.5",
            'Accept-Encoding':'gzip, deflat',
            'DNT':'1',
            'Referer':"http://www.ceasa.gov.br/precos.php?TIP=1&P01=1&P02=1&P03=0&P04=0",
            'Cookie':"PHPSESSID=tal40cjdfpa9on0rbmd7vva3j5; __utma=42102583.595977994.1404338129.1404338129.1404353217.2; __utmc=42102583; __utmz=42102583.1404338129.1.1.utmcsr=(    direct)|utmccn=(direct)|utmcmd=(none)"
}

request = urllib2.Request(url, None, headers)
'''
raw_file = urllib2.urlopen(url)

output = open('output.html', 'w')

output.write(raw_file.read())
output.close()

