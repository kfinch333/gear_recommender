# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:52:16 2020

@author: Keith
"""
#Sweetwater scraper
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import pandas as pd

def get_synths(num, verbose):
    #assign chromedriver
    DRIVER_PATH = '/webdrivers/chromedriver'

    #create chrome instance
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    #go to sweetwater website
    driver.get('https://www.sweetwater.com/c510--Synthesizers')
    
    #click on view all
    view_all = '//*[@id="gridTrack"]/div[1]/div[2]/strong/a'
    time.sleep(3)
    driver.find_element_by_xpath(view_all).click()
    
    synths = []
    
    while len(synths) < num:  
        time.sleep(3)     
        
        products = driver.find_elements_by_xpath('//*[@id="gridTrack"]/div[2]/div/div[' + str(len(synths)+1) + ']/div[1]/a')
        for product in products:  
        
            print('Progress: {}'.format('' + str(len(synths)) + '/' + str(num)))
            if len(synths) >= num:
                break

            products[len(synths)].click()
            time.sleep(1)
            collected_successfully = False
            
            while not collected_successfully:
                try:   
                    savings = driver.find_element_by_xpath('//*[@id="product-options"]/div[1]/div/div[2]').text
                except NoSuchElementException:
                    savings = -1
                try:                                    
                    rating = driver.find_element_by_xpath('//*[@id="store-detail"]/div[1]/header/div/div[2]/a[1]/span[1]').text
                except NoSuchElementException:
                    rating = -1    
                try:
                    brand = driver.find_element_by_xpath('/html/head/meta[23]').text
                except NoSuchElementException:
                    brand = -1
                try:
                    tech_specs = driver.find_element_by_xpath('//*[@id="store-detail"]/section[3]/ul').get_attribute('outerHTML')
                except NoSuchElementException:
                    tech_specs = -1
                try:
                    price = driver.find_element_by_xpath('//*[@id="product-options"]/div[1]/div/div[1]/price').text
                    collected_successfully = True
                    # #price: //*[@id="product-options"]/div[1]/div/div[1]
                    # savings: //*[@id="product-options"]/div[1]/div/div[2]/span[1]/price
                    # rating: 
                except:
                    time.sleep(5)
                    
            driver.back()

            # try:
            #     salary_estimate = driver.find_element_by_xpath('.//span[@class="gray small salary"]').text
            # except NoSuchElementException:
            #     salary_estimate = -1 #You need to set a "not found value. It's important."
            
            # try:
            #     rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
            # except NoSuchElementException:
            #     rating = -1 #You need to set a "not found value. It's important."

            #Printing for debugging
            if verbose:
                print("Price: {}".format(price))
                print("Savings: {}".format(savings))
                print("Rating: {}".format(rating))
                print("Brand: {}".format(brand))
                print("Tech Specs: {}".format(tech_specs))
              # print("Location: {}".format(location))    
                    
            synths.append({"Price" : price,
            "Savings" : savings,
            "Rating" : rating,
            "Brand" : brand,
            "Tech Specs" : tech_specs})

    return pd.DataFrame(synths)
        
        
        
        

        
        
        
        
        
        # #click first item
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="gridTrack"]/div[2]/div/div[1]/div[1]/a').click()

# # #shop by category
# by_category = '//*[@id="site-header"]/nav[3]/div/div[1]/a'
# driver.find_element_by_xpath(by_category).click()

# # #
# kbs_synths = '//*[@id="main-content"]/div/section[1]/ul/li[6]/a/div'
# driver.find_element_by_xpath(kbs_synths).click()

# # #synths
# by_sy = '//*[@id="category-filters"]/div[1]/div[1]/a'
# driver.find_element_by_xpath(by_sy).click()

   
    #start scraping

    # cols = (['Price', 'Savings', 'Rating'])
    # tbl = driver.find_element_by_xpath('//*[@id="store-detail"]/section[2]/ul').get_attribute('outerHTML')
    # df_specs  = pd.read_html(tbl)
    # df_synths = pd.DataFrame({'Price': ,
    #                       'Savings': ,
    #                       'Ratings': })[cols]

# #price: //*[@id="product-options"]/div[1]/div/div[1]
# savings: //*[@id="product-options"]/div[1]/div/div[2]/span[1]/price
# rating: 

    #loop through all items


# //*[@id="gridTrack"]/div[2]/div/div[2]
# //*[@id="gridTrack"]/div[2]/div/div[2]/div[1]/a

# //*[@id="gridTrack"]/div[2]/div/div[216]/div[1]/a
# //*[@id="gridTrack"]/div[2]/div/div[113]/iframe

    # driver.back()
    # driver.execute_script("window.history.go(-1)")
