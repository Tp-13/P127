from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/WhiteHatJunior/HomeWork/P 127/chromedriver")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers = ["proper_name", "distance", "mass", "radius"]
    star_data = []
    for i in range(0, 1):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("tr", attrs={"class", "headerSort"}):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("span")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            
            star_data.append(temp_list)
        
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    
    with open("scraper.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(star_data)

scrape()