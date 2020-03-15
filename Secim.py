# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:04:25 2019

@author: Admin
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import re
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Secim():
    
    def __init__(self, yakit, vites,browser, arac_markasi,araclink):
        self.yakit = yakit
        self.vites = vites
        self.browser = browser
        self.model_list = []
        self.value_list = []
        self.price_list = []
        self.date_list = []
        self.province_list = []
        self.id_list = []
        self.yakit_list = []
        self.vites_list = []
        self.arac_markasi = arac_markasi
        self.araclink = araclink
        self.marka_list = []
        
    def yakit_vites(self):
        
        #timeout = 12
        #browser.get("https://www.sahibinden.com/kategori/otomobil/alfa-romeo")
        self.browser.get(self.araclink)
        #WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn btn-block search-submit')))
        #self.browser.implicitly_wait(3) 
        self.browser.maximize_window()
        time.sleep(2.5)
        self.browser.execute_script("window.scrollTo(0, 730)")
        self.browser.execute_script("window.scrollTo(0, 730)")
        self.browser.find_element_by_link_text(self.yakit).click()
        self.browser.find_element_by_link_text(self.vites).click()
        self.browser.find_element_by_css_selector("button[class = 'btn btn-block search-submit']").click()
        #WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="search_cats"]/ul/li[1]/div/a')))
        #self.browser.implicitly_wait(2)
        #WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn btn-block search-submit')))
        time.sleep(3.5)
        model =  self.browser.find_elements_by_css_selector("td[class  ='searchResultsTagAttributeValue']")
        value = self.browser.find_elements_by_css_selector("td[class = 'searchResultsAttributeValue']")
        price = self.browser.find_elements_by_css_selector("td[class = 'searchResultsPriceValue']")
        date =  self.browser.find_elements_by_css_selector("td[class = 'searchResultsDateValue']")
        province = self.browser.find_elements_by_css_selector("td[class = 'searchResultsLocationValue']")
        id_ = self.browser.find_elements_by_class_name("searchResultsItem")
        
        
# =============================================================================
#         model_list = []
#         value_list =[]
#         price_list = []
#         date_list = []
#         province_list = []
#         id_list = []
#         yakit_list = []
#         vites_list = []
# =============================================================================
        
        
            
        
                
        for i in id_:
            data_id = i.get_attribute("data-id")    
            if data_id == None:
                pass
            else:
                self.id_list.append(data_id)
        
        for i  in model:
            self.model_list.append(i.text)
        for i in value:
            self.value_list.append(i.text)
        for i in price:
            self.price_list.append(i.text)
        for i in date:
            self.date_list.append(i.text)
        for i in province:
            self.province_list.append(i.text)
        for i in range(len(price)):
            self.yakit_list.append(self.yakit)
            self.vites_list.append(self.vites)
            self.marka_list.append(self.arac_markasi)
        
        while True :
            try:
                self.browser.execute_script("window.scrollTo(0, 2000)")
                self.browser.execute_script("window.scrollTo(0, 2000)")
                time.sleep(1)
                self.browser.find_element_by_link_text("Sonraki").click()
                #self.browser.implicitly_wait(1)
                #WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn btn-block search-submit')))
                time.sleep(5.5)
                a =  self.browser.find_elements_by_css_selector("td[class  ='searchResultsTagAttributeValue']")
                for i in a:
                    self.model_list.append(i.text)
                b = self.browser.find_elements_by_css_selector("td[class = 'searchResultsAttributeValue']")
                for i in b:
                    self.value_list.append(i.text)
                c = self.browser.find_elements_by_css_selector("td[class = 'searchResultsPriceValue']")
                for i in c:
                    self.price_list.append(i.text)
                d = self.browser.find_elements_by_css_selector("td[class = 'searchResultsDateValue']")
                for i in d:
                    self.date_list.append(i.text)
                e = self.browser.find_elements_by_css_selector("td[class = 'searchResultsLocationValue']")
                for i in e:
                    self.province_list.append(i.text)
                f = self.browser.find_elements_by_class_name("searchResultsItem")
                for i in f:
                    data_id = i.get_attribute("data-id")    
                    if data_id == None:
                        pass
                    else:
                        self.id_list.append(data_id)
                        
                for i in range(len(c)):
                    self.yakit_list.append(self.yakit)
                    self.vites_list.append(self.vites)
                    self.marka_list.append(self.arac_markasi)
                    
                    
        
                #time.sleep(1)
                
            except (NoSuchElementException,StaleElementReferenceException):
                     break
                
        #return self.model_list, self.value_list, self.price_list, self.date_list, self.province_list, self.id_list, self.yakit_list, self.vites_list, self.marka_list
    
    def process(self):
        
        list2 = []
        list3 = []
        for i in range(len(self.value_list)):
            if len(list3) < 3:
                list3.append(self.value_list[i])
            elif len(list3) == 3:
                list2.append(list3)
                list3 = []
                list3.append(self.value_list[i])
        if len(list3) == 0:
            pass
        else:
            list2.append(list3)
        
        #Model List
        list4 = []
        list3 = []
        for i in range(len(self.model_list)):
            if len(list3) < 2:
                list3.append(self.model_list[i])
            elif len(list3) == 2:
                list4.append(list3)
                list3 = []
                list3.append(self.model_list[i])
        if len(list3) == 0:
            pass
        else:
            list4.append(list3)
        #Model list, id_list ve value list birleştirme
        
        for i in range(len(list4)):
            if len(list4[i]) == 1:
                
                list2[i].insert(0,list4[i][0])
                list2[i].insert(0,list4[i][0])
                list2[i].insert(0,self.marka_list[i])
                list2[i].insert(0, self.id_list[i])
            else:
                
                list2[i].insert(0, list4[i][1])
                list2[i].insert(0,list4[i][0])
                list2[i].insert(0,self.marka_list[i])
                list2[i].insert(0, self.id_list[i])
            
        
            
        
        #Vites List, yakit list 
        for i in range(len(self.vites_list)):
            list2[i].append(self.vites_list[i])
            list2[i].append(self.yakit_list[i])
          
        
        
        #Province 
        for i in range(len(self.province_list)):
            a = re.findall(r"(\w+)",self.province_list[i])
            list2[i].append(a[0])
        
        #Date List
            
        
        for i in range(len(self.date_list)):
            if "\n" in self.date_list[i]:
                a = self.date_list[i].replace("\n"," ")
                list2[i].append(a)
            else:
                list2[i].append(self.date_list[i])
        #Price list
                
        for i in range(len(self.price_list)):
            list2[i].append(self.price_list[i])
        
        return list2
time.sleep(1)


