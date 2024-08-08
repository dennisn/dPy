from selenium import webdriver
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException

import csv
import importlib
import sys
import string
from pathlib import Path

# make sure the root of the developing library is in the path
module_path=r"C:\Dev\Github\dPy"
if module_path not in sys.path:
    sys.path.append(module_path)

# normal import
from dpy import LogHelper
LogManager = LogHelper.LogConfigurator("./Log/download_TangThuVien.txt")

import logging
import os
from unidecode import unidecode



def format_filename(s, extension=".html"):
    """Take a string and return a valid filename constructed from the string.
    Uses a whitelist approach: any characters not present in valid_chars are
    removed. Also spaces are replaced with underscores.
    """
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    filename = filename.replace("..", "")
    return (filename + extension).replace("..", ".")


def convert_title_to_filename(title_st):
    #title_st = title_st.split("(")[0].strip()
    #title_st = title_st.replace("?", "").replace(".", "").replace("*", "").replace('"', '')
    #title_st =  title_st.replace(" ", "_").replace(":", "_").replace(r"/", "")
    #return unidecode(title_st)+ ".html"
    return format_filename(unidecode(title_st), ".html")


def retrieve_chapter_list(driver, target_url, chapter_list_file):

    driver.get(target_url)
    results = []
    
    
    # Wait for loading
    _ = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[5]/div[2]/div/ul/li[2]/a')))
    logging.info("Processing location: " + driver.current_url)
    
    # Scrolling to end so we have everything
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Move the table of content
    toc_link = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/ul/li[2]/a")
    driver.execute_script("arguments[0].click();", toc_link)
    
    _ = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/nav/ul')))
    
    count = 1
    while True:

        chapter_items = driver.find_elements(By.XPATH, "/html/body/div[5]/div[3]/div/div[2]/ul/li")
        for chapter_item in chapter_items:
            try:
                chapter_link = chapter_item.find_element(By.XPATH, ".//a")
                title_st = unidecode(chapter_link.get_attribute("title"))
                href_st = chapter_link.get_attribute("href")
                results.append([title_st, href_st])
            except NoSuchElementException:
                # ignore
                continue
            
        
        next_link = None
        try:
            next_link = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/nav/ul/li/a[@aria-label="Next"]')
            logging.info("Next link: " + next_link.text)
        except NoSuchElementException:
            # ignore
            next_link = None
        
        if next_link is None:
            break
        driver.execute_script("arguments[0].click();", next_link)
        _ = WebDriverWait(driver, 3).until(EC.staleness_of(chapter_link))
       
    
    with open(chapter_list_file, mode="w",newline='') as toc_file:
        csv_writer = csv.writer(toc_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for res in results:
            logging.info(res[0] + "," + res[1])
            csv_writer.writerow(res)
    return results

def read_chapter_list(chapter_list_file):
    res = []
    with open(chapter_list_file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            res.append(row)
    return res

def retrieve_pages(driver, dest_dir, chapter_list, skip_count=0):
    count = 0
    for chapter_st, url_st in chapter_list:
        # print(convert_title_to_filename(title_st), "::", url_st)
        
        count += 1
        if count < skip_count:
            continue
        driver.get(url_st)
        _ = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[5]/div/div[1]/div[2]/div/div[1]')))
        logging.info("Processing location: " + str(count) + "==" + driver.current_url)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # search for content
        title_ele = driver.find_element(By.TAG_NAME, "title")
        chapter_ele = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/h2")
        
        # next chapter button
        # count = count + 1
        # next_url = target_url + str(count)
        _ = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[5]/div/div[1]/div[4]/div/div/a[2]')))
        logging.info("Wait for next button ")
        
        next_btn = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div[4]/div/div/a[2]")
        # next_btn.click()
        driver.execute_script("arguments[0].click();", next_btn)
        # driver.implicitly_wait(10)
        
        # Wait for loading
        # _ = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[5]/div/div[1]/div[2]/div/div[1]')))
        count += 1
        
        retry = 3
        while retry > 0:
            try:
                _ = WebDriverWait(driver, 5).until(EC.url_contains("chuong-" + str(count)))
                break
            except UnexpectedAlertPresentException:
                retry -= 1
                driver.implicitly_wait(5)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
        logging.info("Wait for: " + driver.current_url)


def main():
    driver = webdriver.Firefox()
    skip_count = 0
    
    # target_url = r"https://truyen.tangthuvien.vn/doc-truyen/dichtap-do-suu-tam"
    # dest_dir = r"D:\Temp\TapDo"
    
    # Tiêu Dao Mộng Lộ - Văn Sao Công
    # target_url = r"https://truyen.tangthuvien.vn/doc-truyen/tieu-dao-mong-lo/3521996-chuong-1"
    # target_url = r"https://truyen.tangthuvien.vn/doc-truyen/tieu-dao-mong-lo"
    # dest_dir = r"D:\Temp\TieuDaoMongLo"
    
    # Lão Tử Thị Lại Cáp Mô - Phong Hỏa Hí Chư Hầu
    target_url = r"https://truyen.tangthuvien.vn/doc-truyen/lao-tu-thi-lai-cap-mo---reconvert"
    dest_dir = r"D:\Temp\LaoTuThiLaiCapMo"
    skip_count=310
    
    
    os.makedirs(dest_dir, exist_ok=True)
    
    # retrieve the chapter list
    chapter_list_file = os.path.join(dest_dir, "TOC.csv")
    chapter_list = None
    #chapter_list = retrieve_chapter_list(driver, target_url, chapter_list_file)
    
    if chapter_list is None:
        chapter_list = read_chapter_list(chapter_list_file)
        
    if chapter_list is not None:
        retrieve_pages(driver, dest_dir, chapter_list, skip_count)


if __name__ == '__main__':
    sys.exit(main())
