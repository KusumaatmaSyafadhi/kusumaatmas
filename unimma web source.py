# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:48:39 2021

@author: User
"""


from urllib import request
with request.urlopen('https://unimma.ac.id/category/berita/') as response:
    html = response.read().decode('utf-8')
    print(html)