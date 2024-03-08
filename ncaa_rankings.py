# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 04:25:12 2023

@author: Nelson.Chung
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 03:59:37 2022

@author: Owner
"""

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
from pandas.io.html import read_html

import numpy as np
import re
import pandas as pd
import os 
import itertools as it
import xlrd as xl
os.chdir('c:/Sabr/')



games=pd.DataFrame()

       
day=pd.DataFrame()
driver=wd.Chrome()
driver.get('https://www.ncaa.com/scoreboard/soccer-women/d1/2023/09/03/all-conf')
pg=driver.find_element_by_xpath('//*[(@id = "scoreboardGames")]')
page_txt=pg.get_attribute('innerHTML')
num_games=len(re.findall('game-'+'\d',page_txt))



for i in range(num_games):
    box=driver.find_element_by_id('game-'+str(i))
    game=box.get_attribute('innerHTML')
    name='<span class="gamePod-game-team-name">(.*?)</span>'
    score='<span class="gamePod-game-team-score">(.*?)</span>'
    status='<div class="gamePod-status">(.*?)</div>'
    vis=re.findall(name,game)[0]
    hom=re.findall(name,game)[1]
    vis_score=int(re.findall(score,game)[0])
    hom_score=int(re.findall(score,game)[1])
    status=re.findall(status,game)[0]
    cols=['vis','vis_score','hom','hom_score','status']
    obs=pd.DataFrame([[vis,vis_score,hom,hom_score,status]],columns=cols)
    day=pd.concat([day,obs],axis=0)
driver.close()






vis=driver.find_element_by_
    #Obtain the home & visiting team names, and scores, and runs allowed
    #name=driver.find_element_by_xpath('//div[@class="Page Title"]/ul/li/a')
    #create_series('home team',name.text)
    page=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "tabs_group", " " ))]')
    # //*[contains(concat( " ", @class, " " ), concat( " ", "tabs_group", " " ))]
    # //*[contains(concat( " ", @class, " " ), concat( " ", "tabs_group", " " ))]
    #//*[contains(concat( " ", @class, " " ), concat( " ", "tabs_group", " " ))]
    table_html=page.get_attribute('innerHTML')
    

    vis=read_html(table_html)[0]
    vis_pitch=read_html(table_html)[1]
    hom=read_html(table_html)[2]
    hom_pitch=read_html(table_html)[3]
    