# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:53:16 2021

@author: priya
"""



def find_data(soup,part,clas):
    return soup.find('part', {'class':'clas'})

def get_text_strip(val):
    return val.get_text().strip()
    