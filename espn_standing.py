# import webdriver
from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
import numpy as np
import os
from selenium.webdriver.common.action_chains import ActionChains

DRIVER_PATH =r'C:\\Users\\geeth\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.espn.in/nhl/table')

   
tab=['Standing','Wild card','Expanded','Division']
standing_element=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/section/div/section/div[2]/nav/ul/li[1]/a')
Wild_card_element=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div[1]/section/div/section/div[2]/nav/ul/li[2]/a')
Expanded_element=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/section/div/section/div[2]/nav/ul/li[3]/a')
Division_element=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/section/div/section/div[2]/nav/ul/li[3]/a')
df=pd.DataFrame() 
path='C:/Users/geeth/Desktop/new/'
tab_element=[standing_element,Wild_card_element,Expanded_element,Division_element]

for index1 in range(0,len(tab)):
  action = ActionChains(driver)
  action.click(on_element=tab_element[index1])
  tab_element[index1].click()
  
  path2 = os.path.join(path,tab[index1])
  os.mkdir(path2)

  league=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/section/div/section/div[2]/div/section/section/div/div/a[1]')
  action = ActionChains(driver)
  action.click(on_element =league)
  league.click()

  year=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div[1]/section/div/section/div[2]/div/section/section/section/div[1]/select[1]') 
  year=Select(year)
  year_options=year.options
  for index2 in range(0,len(year_options)):
     all_tables=pd.read_html(driver.page_source)
     df = all_tables[1]
     n=all_tables[0].columns
     df1= all_tables[0].shift(1)
     df1.loc[0][0]=n[0]
     #df=all_tables[-1]
     df['names']=df1
     #df[df.at[31,'names']]='Montreal Canadiens'
     df.loc[31,'names']='Montreal Canadiens'
     
     df.replace(np.nan,'Montreal Canadiens')
     y=year_options[index2].text
     df.to_csv('C:/Users/geeth/Desktop/new/'+tab[index1]+'/'+y+'.csv')