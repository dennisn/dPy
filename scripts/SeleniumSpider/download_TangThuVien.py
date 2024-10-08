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
    
    # Cẩu Tại Yêu Võ Loạn Thế Tu Tiên - Văn Sao Công
    # target_url = r"https://truyen.tangthuvien.vn/doc-truyen/cau-tai-yeu-vu-loan-the-tu-tien/chuong-"
    # dest_dir = r"D:\Temp\CauTaiYeuVoLoanTheTuTien"
    
    # Lão Tử Thị Lại Cáp Mô - Phong Hỏa Hí Chư Hầu
    #target_url = r"https://truyen.tangthuvien.vn/doc-truyen/lao-tu-thi-lai-cap-mo---reconvert/chuong-"
    #dest_dir = r"D:\Temp\LaoTuThiLaiCapMo"
    
    # Ác Hán - Canh Tân
    #target_url = r"https://truyen.tangthuvien.vn/doc-truyen/dichac-han-suu-tam/chuong-"
    #dest_dir = r"D:\Temp\AcHan"
    
    # Thịnh Đường Quật Khởi  - Canh Tân
    # target_url = r"https://truyen.tangthuvien.vn/doc-truyen/thinh-duong-quat-khoi/chuong-"
    # dest_dir = r"D:\Temp\CanhTan_ThinhDuongQuatKhoi"
    
   # Chắc Chẳng Có Ai Cảm Thấy Tu Tiên Khó  - Hắc Dạ Di Thiên
    # target_url = r"https://truyen.tangthuvien.vn/doc-truyen/se-khong-thuc-su-co-nguoi-cam-thay-tu-tien-kho-di-bat-hoi-chan-huu-nhan-giac-dac-tu-tien-nan-ba/chuong-"
    # dest_dir = r"D:\Temp\HacDaDiThien_ChacChangCoAiCamThayTuTienKho"
    
    # Bất Phóng Tâm Du Điều - Nhất Phẩm Tu Tiên
    target_url = r"https://truyen.tangthuvien.vn/doc-truyen/nhat-pham-tu-tien/chuong-"
    dest_dir = r"D:\Temp\BatPhongTamDuDieu_NhatPhamTuTien"
    
    os.makedirs(dest_dir, exist_ok=True)
    
    # extracted already downloaded number
    filenames = [x for x in os.listdir(dest_dir) if x.startswith("Chuong_") and x.endswith(".html")]
    nums = []
    for filename in filenames:
        parts = filename.split('_')
        if len(parts) > 2:
            nums.append(parts[1])
        else:
            print("Error: ", filename)

    count = 0

    next_url = target_url + str(count)
    while True and count <= 100000:
        # next chapter
        count = count + 1
        next_url = target_url + str(count)
        
        if str(count) in nums:
            continue
        
        driver.get(next_url)
        
        _ = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[5]/div[1]/div/div[1]/div[2]/div/div[1]')))
        logging.info("Processing location: " + driver.current_url)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        title_ele = driver.find_element(By.TAG_NAME, "title")
        
        
        chapter_ele = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[1]/div[2]/div/h5/a")
        chapter_st = chapter_ele.text if chapter_ele is not None else "Chapter_" + str(count)
        
        # search for content
        content_ele = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[1]/div[2]/div/div[1]")
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
            

if __name__ == '__main__':
    sys.exit(main())
