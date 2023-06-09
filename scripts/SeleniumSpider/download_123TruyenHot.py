from selenium import webdriver
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
LogManager = LogHelper.LogConfigurator("./Log/download_123TruyenHot.txt")

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
    return format_filename(unidecode(title_st), "_.html")


def main():
    truncate_st_1 = "Thông Báo: Website chuyển qua sử dụng tên miền mới <a href=\"https://123truyenzz.com/\">123truyenzz.com</a> , Chúc bạn đọc truyện vui vẻ!</p>"
    truncate_st_2 = "<p>Nếu bạn không load được website hãy cài đặt app 1.1.1.1 để truy cập website."
    driver = webdriver.Firefox()
    
    #target_url = r"https://123truyenzz.com/than-cap-van-minh/chuong-"
    #dest_dir = r"c:\Temp\ThanCapVanMinh"
    
    #target_url = r"https://123truyenzz.com/ngu-thu-than-cap-ngu-thu-su/chuong-"
    #dest_dir = r"c:\Temp\ThanCapNguThuSu"
    
    #target_url = r"https://123truyenzz.com/tri-tue-dai-tong/chuong-"
    #dest_dir = r"c:\Temp\TriTueDaiTong"
    
    target_url = r"https://123truyenzz.com/bach-luyen-thanh-than/chuong-"
    dest_dir = r"c:\Temp\BachLuyenThanhThan"
    
    os.makedirs(dest_dir, exist_ok=True)

    count = 1549
    next_url = target_url + str(count)
    while True and count < 4000:
        driver.get(next_url)
        _ = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]')))
        logging.info("Processing location: " + driver.current_url)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        title_ele = driver.find_element(By.CLASS_NAME, "truyen-title")
        
        chapter_ele = driver.find_element(By.CLASS_NAME, "chapter-title")
        chapter_st = chapter_ele.text if chapter_ele is not None else "Chapter_" + str(count)
        
        # search for content
        content_ele = driver.find_element(By.ID, "js-truyenkk-read-content")
        
        #content_st = content_ele.text if content_ele is not None else None
        
        # write file out
        file_name = convert_title_to_filename(chapter_st)
        print("Write to file: ", file_name)
        with open(os.path.join(dest_dir, file_name), "wb") as fout:
            fout.write(r"<?xml version='1.0' encoding='utf-8'?>".encode("UTF-8"))
            fout.write(r'<html xmlns=\"http://www.w3.org/1999/xhtml\">'.encode("UTF-8"))
            fout.write("<head>".encode("UTF-8"))
            fout.write(chapter_st.encode("UTF-8"))
            fout.write("</head><body>".encode("UTF-8"))
            fout.write(chapter_ele.get_attribute("outerHTML").encode("UTF-8"))
            
            #fout.write(content_ele.get_attribute("outerHTML").encode("UTF-8"))
            content = content_ele.get_attribute("outerHTML")
            content = content.replace("\n\n", "<P/>\n")
            content = content.replace(truncate_st_1, "")
            content = content.replace(truncate_st_2, "")
            fout.write(content.encode("UTF-8"))
            
            fout.write("</body></html>".encode("UTF-8"))
        
        # next chapter button
        count = count + 1
        next_url = target_url + str(count)
            

if __name__ == '__main__':
    sys.exit(main())
