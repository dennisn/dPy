from selenium import webdriver
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import UnexpectedAlertPresentException


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
    return filename + extension

def convert_title_to_filename(title_st):
    #title_st = title_st.split("(")[0].strip()
    #title_st = title_st.replace("?", "").replace(".", "").replace("*", "").replace('"', '')
    #title_st =  title_st.replace(" ", "_").replace(":", "_").replace(r"/", "")
    #return unidecode(title_st)+ ".html"
    return format_filename(unidecode(title_st), ".html")


def main():
    driver = webdriver.Firefox()
    
    #target_url = r"https://truyen.tangthuvien.vn/doc-truyen/khoa-ky-luyen-khi-su--khoa-hoc-ky-thuat-luyen-khi-su/chuong-"
    #dest_dir = r"C:\Temp\KhoaKyLuyenKhiSu"
    
    #target_url = r"https://truyen.tangthuvien.vn/doc-truyen/6931-dichtao-tac-suu-tam/chuong-"
    #dest_dir = r"c:\Temp\TaoTac"
    
    #target_url = r"https://truyen.tangthuvien.vn/doc-truyen/dichsay-mong-giang-son-suu-tam/chuong-"
    #target_url = r"https://truyen.tangthuvien.vn/doc-truyen/tuy-cham-giang-son/chuong-"
    #dest_dir = r"c:\Temp\TuyChamGiangSon"
    
    #target_url = r"https://truyen.tangthuvien.vn/doc-truyen/thanh-binh/chuong-"
    #dest_dir = r"c:\Temp\ThanhBinh"
    
    #target_url = r"https://truyen.tangthuvien.vn/doc-truyen/cau-tai-yeu-vu-loan-the-tu-tien/chuong-"
    #dest_dir = r"c:\Temp\CauTaiYeuVoLoanTheTuTien"
    
    
    
    # target_url = r"https://truyen.tangthuvien.vn/doc-truyen/dichtap-do-suu-tam/chuong-"
    # dest_dir = r"c:\Temp\TapDo"
    
    # Tiêu Dao Mộng Lộ - Văn Sao Công
    target_url = r"https://truyen.tangthuvien.vn/doc-truyen/tieu-dao-mong-lo/3521996-chuong-1"
    dest_dir = r"c:\Temp\TieuDaoMongLo"
    
    
    os.makedirs(dest_dir, exist_ok=True)

    count = 1
    # next_url = target_url
    driver.get(target_url)
    
    
    while True:
        
        # Wait for loading
        _ = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[5]/div/div[1]/div[2]/div/div[1]')))
        logging.info("Processing location: " + driver.current_url)
        
        # Scrolling to end so we have everything
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        title_ele = driver.find_element(By.TAG_NAME, "title")
        
        chapter_ele = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/h2")
        chapter_st = chapter_ele.text if chapter_ele is not None else "Chapter_" + str(count)
        
        # search for content
        content_ele = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div[2]/div/div[1]")
        #content_st = content_ele.text if content_ele is not None else None
        
        # write file out
        file_name = convert_title_to_filename(chapter_st)
        print("Write to file: ", file_name)
        with open(os.path.join(dest_dir, file_name), "wb") as fout:
            fout.write(r"<?xml version='1.0' encoding='utf-8'?>".encode("UTF-8"))
            fout.write(r'<html xmlns=\"http://www.w3.org/1999/xhtml\">'.encode("UTF-8"))
            fout.write("<head>".encode("UTF-8"))
            fout.write(title_ele.get_attribute("outerHTML").encode("UTF-8"))
            fout.write("</head><body>".encode("UTF-8"))
            fout.write(chapter_ele.get_attribute("outerHTML").encode("UTF-8"))
            
            #fout.write(content_ele.get_attribute("outerHTML").encode("UTF-8"))
            content = content_ele.get_attribute("outerHTML")
            content = content.replace("\n\n", "<P/>\n")
            fout.write(content.encode("UTF-8"))
            
            fout.write("</body></html>".encode("UTF-8"))
        
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

if __name__ == '__main__':
    sys.exit(main())
