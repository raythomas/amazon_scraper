#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/JBL-Portable-Waterproof-Wireless-Bluetooth/dp/B07HKQ6YGX/ref=sr_1_1_sspa?dchild=1&keywords=jbl+speakers&qid=1606032130&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMEdPWk9ORjI4MUZDJmVuY3J5cHRlZElkPUEwODI1NDY2MkpYTTNSV1IyNFoySCZlbmNyeXB0ZWRBZElkPUEwODI0MDg3TTRaM0NTMDBEOEFUJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="priceblock_saleprice")

print(title)