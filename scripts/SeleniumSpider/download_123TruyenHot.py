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
        
    # # Cầu Ma - Nhĩ Căn
    # target_url = r"https://123truyenzz.com/cau-ma/chuong-"
    # dest_dir = r"c:\Temp\CauMa"
    
    # # Ngã Dục Phong Thiên - Nhĩ Căn
    # target_url = r"https://123truyenzz.com/nga-duc-phong-thien/chuong-"
    # dest_dir = r"c:\Temp\NgaDucPhongThien"
    
    # Thần Tú Chi Chủ - Văn Sao Công
    #target_url = r"https://123truyenzzz.com/than-tu-chi-chu/chuong-"
    # dest_dir = r"D:\Temp\ThanTuChiChu"
    
    # TUYẾT TRUNG HÃN ĐAO HÀNH -  Phong Hỏa Hí Chư Hầu
    # target_url = r"https://123truyenzzz.com/index.php/tuyet-trung-han-dao-hanh/chuong-"
    # dest_dir = r"D:\Temp\TuyetTrungHanDaoHanh"
    
    # # Vô Địch Sư Thúc Tổ - Tác giả: Cửu Thứ Tuyệt
    # target_url = r"https://123truyenzzz.com/index.php/vo-dich-su-thuc-to/chuong-"
    # dest_dir = r"D:\Temp\VoDichSuThucTo"
    
    # Đệ Tử Của Ta Đều Có Che Giấu Thân Phận - Tác giả: Lăng Thần Hữu Hắc Miêu
    # target_url = r"https://123truyenzzz.com/de-tu-cua-ta-deu-co-che-giau-than-phan/chuong-"
    # dest_dir = r"D:\Temp\DeTuCuaTaDeuCoCheGiauThanPhan"
    
    # HÀNG LONG GIÁC TỈNH  - Yêu Dạ
    # target_url = r"https://123truyenfull.com/hang-long-giac-tinh/chuong-"
    # dest_dir = r"D:\Temp\YeuDa_HangLongGiacTinh"
    
    # TA THẬT KHÔNG PHẢI ĐẠI MA VƯƠNG  - Yêu Dạ
    # target_url = r"https://123truyenfull.com/ta-that-khong-phai-dai-ma-vuong/chuong-"
    # dest_dir = r"D:\Temp\YeuDa_TaThatKhongPhaiDaiMaVuong"
    
    # DỰ BÁO TƯƠNG LAI: ĂN BÁM! BẮT ĐẦU LẤY NỮ NHÀ GIÀU NHẤT - Băng Đường Hồ Lô
    # target_url = r"https://123truyenfull.com/du-bao-tuong-lai-an-bam-bat-dau-lay-nu-nha-giau-nhat/chuong-"
    # dest_dir = r"D:\Temp\BangDuongHoLo_DuBaoTuongLai-AnBam"
    
    # Trời Sinh Một Đô - Đông Thanh Liễu Diệp
    # target_url = r"https://123truyenfull.com/troi-sinh-mot-doi/chuong-"
    # dest_dir = r"D:\Temp\DongThanhLieuDiep_TroiSinhMotDoi"
    
    # Quỷ Đạo Chi Chủ - Bất Phóng Tâm Du Điều
    # target_url = r"https://123truyenfull.com/quy-dao-chi-chu/chuong-"
    # dest_dir = r"D:\Temp\BatPhongTamDuDieu_QuyDaoChiChu"
    
    # Kiết Dữ 2 - Đường Chuyên
    # target_url = r"https://123truyenfull.com/duong-chuyen/chuong-"
    # dest_dir = r"D:\Temp\KietDu2_DuongChuyen"
    
    # Ngã Thị Chân Kình - Hồng Hoang: Vừa Cưới Vân Tiêu, Nói Cho Ta Biết Đây Là Phong Thần
    #target_url = r"https://123truyenfull.com/hong-hoang-vua-cuoi-van-tieu-noi-cho-ta-biet-day-la-phong-than/chuong-"
    #dest_dir = r"D:\Temp\NgaThiChanKinh-VuaCuoiVanTieuNoiChoTaBietDayLaPhongThan"
    
    #  Ân Tứ Giải Thoát - Bách Luyện Thành Thần
    # target_url = r"https://123truyencv.com/bach-luyen-thanh-than/chuong-"
    # dest_dir = r"D:\Temp\AnTuGiaiThoat-BachLuyenThanhThan"
    
    #  Duy Khách - TA KHÔNG PHẢI LÀ ĐẠI SƯ BẮT QUỶ
    # target_url = r"https://123truyentop.com/ta-khong-phai-la-dai-su-bat-quy/chuong-"
    # dest_dir = r"D:\Temp\DuyKhach-TaKhongPhaiLaDaiSuBatQuy"
    
    #  Kiếm Phi Bạo Vũ Trung - THẦN QUỶ THẾ GIỚI, TA CÓ ĐẶC THÙ NGỘ TÍNH
    #target_url = r"https://123truyentop.com/than-quy-the-gioi-ta-co-dac-thu-ngo-tinh/chuong-"
    #dest_dir = r"D:\Temp\KiemPhiBaoVuTrung-ThanQuyTheGioiTaCoDacThuNgoTinh"
    
    #  Kiếm Phi Bạo Vũ Trung - TA CÙNG TIÊN TỬ TU HÀNH
    # target_url = r"https://123truyentop.com/ta-cung-tien-tu-tu-hanh/chuong-"
    # dest_dir = r"D:\Temp\KiemPhiBaoVuTrung-TaCungTienTuTuHanh"
    
    # Bắc Đằng - THIÊN TÀI NHI TỬ VÀ MẪU THÂN PHÚC HẮC
    # target_url = r"https://123truyentop.com/thien-tai-nhi-tu-va-mau-than-phuc-hac/chuong-"
    # dest_dir = r"D:\Temp\BacDang-ThienTaiNhiTuVaMauThanPhucHac"
    
    # Ngã Gia Ngưu Bào Liễu - Đọc Sách Thành Thánh! Bị Tiểu Sư Muội Lộ Ra Ánh Sáng!
    # target_url = r"https://123truyenx.com/doc-sach-thanh-thanh-bi-tieu-su-muoi-lo-ra-anh-sang/chuong-"
    # dest_dir = r"D:\Temp\NgaGiaNguuBaoLieu-DocSachThanhThanh_BiTieuSuMuoiLoRaAnhSang"
    
    # Ám Ảnh Ngoạn Cụ Xa - Xuyên Qua Ba Năm, Ngươi Liền Cho Ta Cái Này Phá Hệ Thống?
    # target_url = r"https://123truyenx.com/xuyen-qua-ba-nam-nguoi-lien-cho-ta-cai-nay-pha-he-thong/chuong-"
    # dest_dir = r"D:\Temp\AmAnhNgoanCuXa-XuyenQuaBaNamNguoiLienChoTaCaiNayPhaHeThong"
    
    # Phi Điểu Nhập Hải - Mặt Đất Tối Cường Nam Nhân: Từ Bày Hàng Vỉa Hè Bắt Đầu
    # target_url = r"https://123truyenx.com/mat-dat-toi-cuong-nam-nhan-tu-bay-hang-via-he-bat-dau/chuong-"
    # dest_dir = r"D:\Temp\PhiDieuNhapHai_MatDatToiCuongNamNhanTuBayHangViaHe"
    
    # # Bạch Long Thần - Nữ Giả Nam Trang Túc Địch Nữ Đế Luôn Trêu Chọc Ta
    # target_url = r"https://123truyenx.com/nu-gia-nam-trang-tuc-dich-nu-de-luon-treu-choc-ta/chuong-"
    # dest_dir = r"D:\Temp\BachLongThan_NuGiaNamTrangTucDichNuDeLuonTreuChocTa"
    
    # Truy Mộng Huỳnh Hỏa Trùng - Làm Ruộng Hệ Tu Tiên
    # target_url = r"https://123truyenxx.com/lam-ruong-he-tu-tien/chuong-"
    # dest_dir = r"D:\Temp\TruyMongHuynhHoaTrung_LamRuongHeTuTien"
    
    # Cố Mạn - Em Là Niềm Kiêu Hãnh Của Anh
    # target_url = r"https://123truyennn.com/em-la-niem-kieu-hanh-cua-anh/chuong-"
    # dest_dir = r"D:\Temp\CoMan_EmLaNiemKieuHanhCuaAnh"
    
    # Cố Mạn - Bữa Trưa Tình Yêu
    # target_url = r"https://123truyennn.com/bua-trua-tinh-yeu/chuong-"
    # dest_dir = r"D:\Temp\CoMan_BuaTruaTinhYeu"
    
    #  Văn Sao Công - Cẩu Tại Yêu Võ Loạn Thế Tu Tiên
    target_url = r"https://123truyennn.com/cau-tai-yeu-vo-loan-the-tu-tien/chuong-"
    dest_dir = r"D:\Temp\VanSaoCong_CauTaiYeuVoLoanTheTuTien"
    
    os.makedirs(dest_dir, exist_ok=True)

    count = 1
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
