# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:40:18 2019

@author: Admin
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import Secim
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException,ElementClickInterceptedException

def main_secim():
    
    final_list = []
    driver_path = "/Users/digitastic/Downloads/chromedriver-2"
    browser = webdriver.Chrome(driver_path)
    #browser.get("https://www.sahibinden.com/kategori/otomobil/alfa-romeo")
    browser.get("https://www.sahibinden.com/otomobil")
    
    browser.maximize_window()
    time.sleep(1)
    
    id_ul = browser.find_element_by_id("searchCategoryContainer")
    ul = id_ul.find_element_by_tag_name("ul")
    li = ul.find_elements_by_tag_name("li")
    arac_list = []
    araclink_list =[]
    for i in range(1,len(li)+1):
        araclar = browser.find_element_by_xpath("//*[@id='searchCategoryContainer']/div/div[1]/ul/li[%d]/a"%i)
        araclar.location_once_scrolled_into_view
    
        #browser.execute_script('arguments[0].scrollIntoView(true);', araclar)
        araclink_list.append(araclar.get_attribute("href"))
        arac_list.append(araclar.text)
    time.sleep(1)
    len(arac_list)
    len(araclink_list)
    
    
    for i in range(13,len(araclink_list)):
        while True:
            try:
                secim = Secim.Secim("Benzin","Manuel",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
       
                
        while True:
            try:
                secim = Secim.Secim("Benzin","Yarı Otomatik",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Benzin","Otomatik",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Benzin & LPG","Manuel",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Benzin & LPG","Yarı Otomatik",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Benzin & LPG","Otomatik",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Dizel","Manuel",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Dizel","Yarı Otomatik",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Dizel","Otomatik",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Hybrid","Manuel",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Hybrid","Yarı Otomatik",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Hybrid","Otomatik",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Elektrik","Manuel",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Elektrik","Yarı Otomatik",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
                
        while True:
            try:
                secim = Secim.Secim("Elektrik","Otomatik",browser,arac_list[i],araclink_list[i])
                secim.yakit_vites()
                df = secim.process()
            except(IndexError, NoSuchElementException, StaleElementReferenceException,ElementClickInterceptedException):
                continue
            break
        for j in range(len(df)):
            if len(df) == 0:
                pass
            else:    
                final_list.append(df[j])
    return final_list

#Hata alınırsa 
# =============================================================================
# deneme = []           
# for i in range(len(final_list)):
#     if final_list[i][1] == "Audi":
#         pass
#     else:
#         deneme.append(final_list[i])
# final_list = deneme    
# =============================================================================
    

#for i in range(0,len(araclink_list)+1):
    
# =============================================================================
# araclar = []
# for i in araclar2:
#     a = re.findall(r"(\w+[ ]*[\w+]*)",i)
#     araclar.append(a[0])
# 
# len(araclar)
# =============================================================================
if __name__ == "__main__":
    final_list = main_secim()

