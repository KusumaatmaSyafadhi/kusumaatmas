# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:54:38 2021

@author: Kusumaatma Syafadhi (kusatma25)
"""
#My Campus Website
import requests
import bs4
res = requests.get('https://unimma.ac.id/category/berita/')
type(res)

#Get News
soup = bs4.BeautifulSoup(res.text, 'lxml')
news = soup.select('.entry-title')

for i in soup.select('.entry-title'):
    print(i.text)

#Sorry if the results is in Indonesian. The website actually has an english version
#but when I copy the link, somehow the informations appears in Indonesian...


