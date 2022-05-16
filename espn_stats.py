# import webdriver
from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
import os

DRIVER_PATH =r'C:\\Users\\geeth\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.espn.in/nhl/team/stats/_/name/ana/anaheim-ducks')   
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
df=pd.DataFrame() 
last_list=[] 
element_names = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[2]/div[5]/div/div/section/div/div[1]/div/select[1]')
skat=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[2]/div[5]/div/div/section/div/div[2]/nav/ul/li[1]/a')
element_season = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[4]/div[2]/div[5]/div/div/section/div/div[3]/div[1]/div/select[1]")
Goal=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[2]/div[5]/div/div/section/div/div[2]/nav/ul/li[2]/a')   
# # create action chain object
# action = ActionChains(driver)
# action.click(on_element = element)
# action.perform()
# #action.click(on_element = element)
sel_names=Select(element_names)
sel_seasons = Select(element_season)

options_names=sel_names.options
options_seasons= sel_seasons.options
l=['skating','Goaltending']

for index1 in range(1,len(options_names)):
#for index1 in range(0,4):
     path='C:/Users/geeth/Desktop/new/'
     name=options_names[index1].text
     path = os.path.join(path,name)
     os.mkdir(path)
     
     
     
     path1 = os.path.join(path,'skating')
     os.mkdir(path1)
      
#for index in range(0, len(options_names)):
  #for index2 in range(0,5):
     for index2 in range(0, len(options_seasons)):
     #for index2 in range(0,4):
    
       season=options_seasons[index2].text
    #sel.select_by_index(index)
       #table=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[2]/div[5]/div/div/section/div/div[6]/div[2]')
    #df.append(table.text)
       #last_list.append(table.text)
       all_tables=pd.read_html(driver.page_source)
       df = all_tables[1]
       n=all_tables[0].columns
    
    
    # df2=all_tables[0]
       df1= all_tables[0].shift(1)
       df1.loc[0][0]=n[0]
    # df=df1+df2
    #df['names']=df1
       df['names']=df1
    #names = pd.concat([pd.Series(df.columns[1]),df.iloc[:, 1]]).reset_index(drop=True)

    #df = pd.DataFrame({'Names': names})

       df.to_csv('C:/Users/geeth/Desktop/new/'+name+'/skating/'+season+'.csv')

    # --- show it ---
     action = ActionChains(driver)
     action.click(on_element =Goal)
     Goal.click()
     print(df)  

     path2 = os.path.join(path,'Goaltending')
     os.mkdir(path2)
      
#for index in range(0, len(options_names)):
  #for index2 in range(0,5):
     for index2 in range(0, len(options_seasons)):
     #for index2 in range(0,4):
    
       season=options_seasons[index2].text
    #sel.select_by_index(index)
       #table=driver.find_element_by_xpath('')
    #df.append(table.text)
       #last_list.append(table.text)
       all_tables=pd.read_html(driver.page_source)
       df = all_tables[1]
       n=all_tables[0].columns
    
    
    # df2=all_tables[0]
       df1= all_tables[0].shift(1)
       df1.loc[0][0]=n[0]
    # df=df1+df2
    #df['names']=df1
       df['names']=df1
    #names = pd.concat([pd.Series(df.columns[1]),df.iloc[:, 1]]).reset_index(drop=True)

    #df = pd.DataFrame({'Names': names})

       df.to_csv('C:/Users/geeth/Desktop/new/'+name+'/Goaltending/'+season+'.csv')
