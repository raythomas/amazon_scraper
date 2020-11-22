from requests_html import HTMLSession

URLS = ['https://www.amazon.com/JBL-Waterproof-Portable-Bluetooth-Speaker/dp/B07QDPRYYD/ref=sr_1_1?dchild=1&keywords=JBL+go&qid=1606021303&s=amazon-devices&sr=1-1',
          'https://www.amazon.com/JBL-Bluetooth-Built-Waterproof-Dustproof/dp/B08KW1KR5H/ref=sr_1_2?dchild=1&keywords=JBL+go&qid=1606021303&s=amazon-devices&sr=1-2',
          'https://www.amazon.com/JBL-Flip-Waterproof-Portable-Bluetooth/dp/B07JW68JHT/ref=sr_1_14?dchild=1&keywords=waterproof+speakers&qid=1606064883&sr=8-14']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    }
    print(product)
    return product

speaker_prices = []
for url in URLS:
    speaker_prices.append(getPrice(url))

print(len(speaker_prices))
