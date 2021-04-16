# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:10:29 2020

@author: ntesh
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

# setting up your BeautifulSoup Object
webpage = urlopen("https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=WWHDFEEZZR0DXMFEDZ06&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1")
soup = BeautifulSoup( webpage.read(), features="lxml")

names = soup.h3.get_text()
print(names)

final_text = []    
inf= soup.find('div', class_="lister-list")
info = inf.find_all('h3')
for i in info:
    final_text.append(i.get_text())
    
print(final_text)
    
