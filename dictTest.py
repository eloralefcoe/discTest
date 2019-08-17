urlList = {'isf': 'https://www.ishares.com/uk/individual/en/products/251795/',
            'csru':'https://www.ishares.com/uk/individual/en/products/253736/',
            'itky':'https://www.ishares.com/uk/individual/en/products/251879/',
            'sedy':'https://www.ishares.com/uk/individual/en/products/251766/',
            'fxc':'https://www.ishares.com/uk/individual/en/products/251798/',
            'idvy':'https://www.ishares.com/uk/individual/en/products/251787/',
            'eimu':'https://www.ishares.com/uk/individual/en/products/295689/?referrer=tickerSearch',
            'ltam':'https://www.ishares.com/uk/individual/en/products/251856/',
            'ibzl':'https://www.ishares.com/uk/individual/en/products/251853/',
            'csx5':'https://www.ishares.com/uk/individual/en/products/253712/',
            'eue':'https://www.ishares.com/uk/individual/en/products/251781/',
            'cuks':'https://www.ishares.com/uk/individual/en/products/253474/',
            'midd':'https://www.ishares.com/uk/individual/en/products/251796/',
            'djsc':'https://www.ishares.com/uk/individual/en/products/251789/',
            'iwrd':'https://www.ishares.com/uk/individual/en/products/251881/',
            'ndia':'https://www.ishares.com/uk/individual/en/products/297617/',
            'cspx':'https://www.ishares.com/uk/individual/en/products/253743/',
            'iusa':'https://www.ishares.com/uk/individual/en/products/251900/',
            'cndx':'https://www.ishares.com/uk/individual/en/products/253741/'
}

urlListAddOn = '?switchLocale=y&siteEntryPassthrough=true'

# add extra bit to urlLis
for v in urlList:
    urlList[v] = urlList[v] + urlListAddOn
    print(urlList[v])