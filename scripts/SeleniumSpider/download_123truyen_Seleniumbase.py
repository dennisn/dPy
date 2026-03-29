from seleniumbase import Driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import importlib
import sys
import string
import time

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
    
    count = 1
    
    # Trạch Trư - Mục Thần Ký
    # target_url = r"https://123truyensss.vip/muc-than-ky/chuong-"
    # dest_dir = r"D:\Temp\TrachTru_MucThanKy"
    
    # Ngọc Cẩm Kiếm - Lưỡng Giới: Đừng Gọi Ta Tà Ma!
    # target_url = r"https://123truyenx.vip/luong-gioi-dung-goi-ta-ta-ma/chuong-"
    # dest_dir = r"D:\Temp\NgocCamKiem_LuongGioi_DungGoiTaTaMa"
    
    # Tân Mã Giáp - Thổ Lộ Thất Bại Liền Mạnh Lên
    # target_url = r"https://123truyenx.vip/tho-lo-that-bai-lien-manh-len/chuong-"
    # dest_dir = r"D:\Temp\TanMaGiap_ThoLoThatBaiLienManhLen"
    
    # Xuân Phong Tiểu Ngọc Lang - Ta Bị Quỷ Dị Công Kích Liền Biến Cường
    # target_url = r"https://123truyenxx.vip/ta-bi-quy-di-cong-kich-lien-bien-cuong/chuong-"
    # dest_dir = r"D:\Temp\XuanPhongTieuNgocLang_TaBiQuyDiCongKichLienBienCuong"
    
    # Ngân Sương Kỵ Sĩ - Bí Thuật Chi Chủ
    # target_url = r"https://123truyena.vip/bi-thuat-chi-chu/chuong-"
    # dest_dir = r"D:\Temp\NganSuongKySi_BiThuatChiChu"
    
    # Ngân Sương Kỵ Sĩ - Ma Vật Tế Đàn
    # target_url = r"https://123truyena.vip/ma-vat-te-dan/chuong-"
    # dest_dir = r"D:\Temp\NganSuongKySi_MaVatTeDan"
    
    # Loạn Thế Cuồng Đao - Kiếm Tiên Ở Đây
    # target_url = r"https://123truyena.vip/kiem-tien-o-day/chuong-"
    # dest_dir = r"D:\Temp\LoanTheCuongDao_KiemTienODay"
    
    # Hà Tả - Tối Tiên Du
    # target_url = r"https://123truyena.vip/toi-tien-du/chuong-"
    # dest_dir = r"D:\Temp\HaTa_ToiTienDu"
    
    # # Tiềm Thủy Đích Oa Ba - Toàn Dân Lĩnh Chủ: Ta Binh Chủng Biến Dị
    # target_url = r"https://123truyen.xyz/toan-dan-linh-chu-ta-binh-chung-bien-di/chuong-"
    # dest_dir = r"D:\Temp\TiemThuyDichOaBa_ToanDanLinhChu_TaBinhChungBienDi"
    
    # # Kiện Bàn Đại Đế - Lại Giết Ta Thêm Mấy Lần, Ta Liền Vô Địch
    # target_url = r"https://123truyen.xyz/lai-giet-ta-them-may-lan-ta-lien-vo-dich/chuong-"
    # dest_dir = r"D:\Temp\KienBanDaiDe_GietTaMayLan_TaLienVoDich"
    
    # Nhất Quyền Manh Vương -  Nữ Đế: Phu Quân Ẩn Cư Mười Năm, Một Kiếm Trảm Tiên Đế
    # target_url = r"https://123truyena.xyz/nu-de-phu-quan-an-cu-muoi-nam-mot-kiem-tram-tien-de/chuong-"
    # dest_dir = r"D:\Temp\NhatQuyenManhVuong_NuDePhuQuan_AnCuMuoiNam_MotKiemTramTienDe"
    
    # # Lăng Nhược Tỳ - Trực Tiếp Đoán Mệnh: Thủy Hữu Trên Đầu Ngươi Có Chút Xanh
    # target_url = r"https://123truyena.xyz/truc-tiep-doan-menh-thuy-huu-tren-dau-nguoi-co-chut-xanh/chuong-"
    # dest_dir = r"D:\Temp\LangNhuocTy_TrucTiepDoanMenh_ThuyHuuTrenDauNguoiCoChutXanh"
    
    # Liễu Ngạn Hoa Hựu Minh - Ta Thật Không Muốn Trọng Sinh A
    # target_url = r"https://123truyena.xyz/ta-that-khong-muon-trong-sinh-a/chuong-"
    # dest_dir = r"D:\Temp\LieuNganHoaHuuMinh_TaThatKhongMuonTrongSinh"
    
    # Vinh Tiểu Vinh - Yêu Nữ Dừng Tay
    # target_url = r"https://123truyena.xyz/yeu-nu-dung-tay/chuong-"
    # dest_dir = r"D:\Temp\VinhTieuVinh_YeuNuDungTay"
    
    # Vinh Tiểu Vinh - Tiêu Dao Tiểu Thư Sinh
    # target_url = r"https://123truyena.xyz/tieu-dao-tieu-thu-sinh/chuong-"
    # dest_dir = r"D:\Temp\VinhTieuVinh_TieuDaoTieuThuSinh"
    
    # Vinh Tiểu Vinh - Như Ý Tiểu Lang Quân
    # target_url = r"https://123truyena.xyz/nhu-y-tieu-lang-quan/chuong-"
    # dest_dir = r"D:\Temp\VinhTieuVinh_NhuYTieuLangQuan"
    
    # Vinh Tiểu Vinh - Đại Chu Tiên Lại
    # target_url = r"https://123truyena.xyz/dai-chu-tien-lai/chuong-"
    # dest_dir = r"D:\Temp\VinhTieuVinh_DaiChuTienLai"
    
    # Vinh Tiểu Vinh - Công Tử Đừng Tú
    # target_url = r"https://123truyena.xyz/cong-tu-dung-tu/chuong-"
    # dest_dir = r"D:\Temp\VinhTieuVinh_CongTuDungTu"
    
    # Đổ Thượng Tây Lâu - Công Tử Hung Mãnh
    # target_url = r"https://123truyena.xyz/cong-tu-hung-manh/chuong-"
    # dest_dir = r"D:\Temp\DoThuongTayLau_CongTuHungManh"
    
     # Đổ Thượng Tây Lâu - Nhất Phẩm Tể Phụ
    # target_url = r"https://123truyena.xyz/nhat-pham-te-phu/chuong-"
    # dest_dir = r"D:\Temp\DoThuongTayLau_NhatPhamTePhu"
    
    # Vân Điên Cổn Lãnh Nguyệt - Ta Từ Trên Thân Quỷ Xoát Thuộc Tính
    # target_url = r"https://123truyenb.xyz/ta-tu-tren-than-quy-xoat-thuoc-tinh/chuong-"
    # dest_dir = r"D:\Temp\VanDienConLanhNguyen_TaTuTrenQuyXoatThuocTinh"
    
    # Hoa Lý Tầm Hoan - Bổn Vương Muốn Thanh Tịnh
    # target_url = r"https://123truyenb.xyz/bon-vuong-muon-thanh-tinh/chuong-"
    # dest_dir = r"D:\Temp\HoaLyTamHoan_BonVuongMuonThanhTinh"
    
    # # Hoa Lý Tầm Hoan - Phong Cách Yêu Thầm Của Nhà Giàu Mới Nổi
    # target_url = r"https://123truyenb.xyz/phong-cach-yeu-tham-cua-nha-giau-moi-noi/chuong-"
    # dest_dir = r"D:\Temp\HoaLyTamHoan_PhongCachYeuThamCuaNhaGiauMoiNoi"
    
    # Dư Lão Cửu - Lấn Đệ Tử Ta, Ngươi Thật Sự Cho Rằng Ta Chỉ Biết Dạy Học?
    # target_url = r"https://123truyenc.xyz/lan-de-tu-ta-nguoi-that-su-cho-rang-ta-chi-biet-day-hoc/chuong-"
    # dest_dir = r"D:\Temp\DuLaoCuu_LanDeTuTaNguoiThatSuChoRangTaChiBietDayHoc"
    
    #  Ly Ca A - Toàn Cầu Cao Võ: Cày Quái Thành Thần, Ta Đánh Xuyên Qua Nhân Loại Cấm Khu
    # target_url = r"https://123truyenc.xyz/toan-cau-cao-vo-cay-quai-thanh-than-ta-danh-xuyen-qua-nhan-loai-cam-khu/chuong-"
    # dest_dir = r"D:\Temp\LyCaA_ToanCauCaoVo_CayQuaiThanhThan"
    
    #  Ngôn Quy Chính Truyện - Người Này Tu Tiên Quá Mức Đứng Đắn
    # target_url = r"https://123truyend.xyz/nguoi-nay-tu-tien-qua-muc-dung-dan/chuong-"
    # dest_dir = r"D:\Temp\NgonQuyChinhTruyen_NguoiNayTuTienQuaMucDungDan"
    
    #  Nhâm Thu Minh - Cái Này Thích Khách Có Bệnh
    # target_url = r"https://123truyend.xyz/cai-nay-thich-khach-co-benh/chuong-"
    # dest_dir = r"D:\Temp\NhamThuMinh_CaiNayThichKhachCoBenh"
    
    #  Ngao Dạ Cật Bình Quả - Ta Có Một Thân Bị Động Kỹ
    # target_url = r"https://123truyend.xyz/ta-co-mot-than-bi-dong-ky/chuong-"
    # dest_dir = r"D:\Temp\NgaoDaCatBinhQua_TaCoMotThanBiDongKy"
    
    #  Thiên Hương Đồng - Đế Quốc Bại Gia Tử
    # target_url = r"https://123truyend.xyz/de-quoc-bai-gia-tu/chuong-"
    # dest_dir = r"D:\Temp\ThienHuongDong_DeQuocBaiGiaTu"
    
    #  Lý Tiếu Tà - Đỉnh Cấp Lưu Manh
    # target_url = r"https://123truyene.xyz/dinh-cap-luu-manh/chuong-"
    # dest_dir = r"D:\Temp\LyTieuTa_DinhCapLuuManh"
    
    #  Túy Ngọa Cửu Trọng Vân - Bắt Đầu Một Đám Người Nguyên Thủy
    # target_url = r"https://123truyene.xyz/bat-dau-mot-dam-nguoi-nguyen-thuy/chuong-"
    # dest_dir = r"D:\Temp\TuyNgoaCuuTrongVan_BatDauMotDamNguoiNguyenThuy"
    
    # Bộ Hành Thiên Hạ - Ta Chỉ Có Hai Ngàn Năm Trăm Tuổi
    # target_url = r"https://123truyene.xyz/ta-chi-co-hai-ngan-nam-tram-tuoi/chuong-"
    # dest_dir = r"D:\Temp\BoHanhThienHa_TaChiCoHaiNganNamTramTuoi"
    
    # Mục Tam Hà - Hệ Thống Để Ta Đi Đoán Mệnh
    # target_url = r"https://123truyeng.xyz/he-thong-de-ta-di-doan-menh/chuong-"
    # dest_dir = r"D:\Temp\MucTamHa_HeThongDeTaDiDoanMenh"
    
    # Thất Nhị Linh Linh - Ta Thành Tân Thủ Thôn BOSS
    # target_url = r"https://123truyenh.xyz/boss-1/chuong-"
    # dest_dir = r"D:\Temp\ThatNhiLinhLinh_TaThanhTanThuThonBoss"
    
    # Diêm Gia Tam Chước - Mạt Thế: Ta Linh Thực Không Gian Thực Vật Biến Dị Rồi
    # target_url = r"https://123truyenh.xyz/mat-the-ta-linh-thuc-khong-gian-thuc-vat-bien-di-roi/chuong-"
    # dest_dir = r"D:\Temp\DiemGiaTamChuoc_MatThe_TaLinhThucKhongGian"
    
    # # Tần Tiểu Từ - Mạt Thế Chi Toàn Năng Đại Sư
    # target_url = r"https://123truyenh.xyz/mat-the-chi-toan-nang-dai-su/chuong-"
    # dest_dir = r"D:\Temp\TanTieuTu_MatTheChiToanNangDaiSu"
    
    # Thần Tinh LL -  Ta Ở Tận Thế Có Căn Phòng
    # target_url = r"https://123truyenh.xyz/ta-o-tan-the-co-can-phong/chuong-"
    # dest_dir = r"D:\Temp\ThanTinh_TaTanTheCoCanPhong"
    
    # Vương Bất Quá Bá - Thứ Tộc Vô Danh
    # target_url = r"https://123truyenh.xyz/thu-toc-vo-danh/chuong-"
    # dest_dir = r"D:\Temp\VuongBatQuaBa_ThuTocVoDanh"
    
    # # Tích Thủy Yêm Thành - Từ Huyện Lệnh Bắt Đầu Đánh Dấu Sinh Hoạt
    # target_url = r"https://123truyenh.xyz/tu-huyen-lenh-bat-dau-danh-dau-sinh-hoat/chuong-"
    # dest_dir = r"D:\Temp\TichThuyYemThanh_TuHuyenLenhBatDauDanhDauSinhHoat"
    
    # # Khinh Tuyền Lưu Hưởng - Không Khoa Học Ngự Thú
    # target_url = r"https://123truyenh.xyz/khong-khoa-hoc-ngu-thu/chuong-"
    # dest_dir = r"D:\Temp\KhinhTuyenLuuHuong_KhongKhoaHocNguThu"
    
    # # Chân Đích Thụy Bất Cú - Nương Tử, Long Bào Mời Mặc, Ta Muốn Đọc Sách!
    # target_url = r"https://123truyenh.xyz/nuong-tu-long-bao-moi-mac-ta-muon-doc-sach/chuong-"
    # dest_dir = r"D:\Temp\ChanDichThuyBatCu_NuongTuLongBaoMoiMac_TaMuonDocSach"
    
    # Kiếm Tâm Cửu Vạn Trọng -  Võng Du: Cái Này Độc Y Ức Điểm Mạnh Mẽ
    # target_url = r"https://123truyenh.xyz/vong-du-cai-nay-doc-y-uc-diem-manh-me/chuong-"
    # dest_dir = r"D:\Temp\KiemTamCuuVanTrong_VongDu_CaiNayDocYUcDiemManhMe"
    
    # Thanh Chưng-  Ta Là Tham Quan, Các Nàng Lại Nói Ta Là Trung Thần!
    # target_url = r"https://123truyenh.xyz/ta-la-tham-quan-cac-nang-lai-noi-ta-la-trung-than/chuong-"
    # dest_dir = r"D:\Temp\ThanhChung_TaLaThamQuan_CacNangLaiNoiTaLaTrungThan"
    
    # # Tối Bạch Đích Ô Nha - Ai Bảo Hắn Tu Tiên!
    # target_url = r"https://123truyenh.xyz/ai-bao-han-tu-tien/chuong-"
    # dest_dir = r"D:\Temp\ToiBachDichONha_AiBaoHanTuTien"
    
    # Tiểu Bàn Hùng Miêu - Ta Mở Tửu Quán Ở Đại Đường
    # target_url = r"https://123truyenh.xyz/ta-mo-tuu-quan-o-dai-duong/chuong-"
    # dest_dir = r"D:\Temp\TieuBanHungMieu_TaMoTuuQuanODaiDuong"
    
    # Phong Hội Tiếu - Đô Thị Cực Phẩm Y Thần (Up to 4105 chuong)
    target_url = r"https://123truyenh.xyz/do-thi-cuc-pham-y-than/chuong-"
    dest_dir = r"D:\Temp\PhongHoiTieu_DoThiCucPhamYThan"
    count = 4105
    
    # Thần Đông - Thế Giới Hoàn Mỹ
    # target_url = r"https://123truyenh.xyz/the-gioi-hoan-my/chuong-"
    # dest_dir = r"D:\Temp\ThanDong_TheGioiHoanMy"
    
    # Ngoạn Bất Khởi - Linh Khí Sống Lại: Từ Hạ Đẳng Thợ Rèn Đến Tạo Hóa Chi Chủ
    #target_url = r"https://123truyenh.xyz/linh-khi-song-lai-tu-ha-dang-tho-ren-den-tao-hoa-chi-chu/chuong-"
    #dest_dir = r"D:\Temp\NgoanBatKhoi_LinhKhiSongLaiTuHaDangThoRenDenTaoHoaChiChu"

    # initialize the driver in GUI mode with UC enabled
    driver = Driver(uc=True, headless=False)
    
    
    os.makedirs(dest_dir, exist_ok=True)

    #count = 523
    next_url = target_url + str(count)
    while True and count < 40000:
        retry = 3
        while retry > 0:
            try:
                # open URL using UC mode with 6 second reconnect time to bypass initial detection
                driver.uc_open_with_reconnect(next_url, reconnect_time=6) # type: ignore
                
                # attempt to click the CAPTCHA checkbox if present
                driver.uc_gui_click_captcha() # type: ignore
                
                _ = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]')))
                logging.info("Processing location: " + driver.current_url)
                break
            except TimeoutException:
                retry -= 1
                driver.implicitly_wait(5)
                logging.info("Retry: " + str(retry) + " for location: " + driver.current_url)
                
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
            fout.write(content.encode("UTF-8"))
            
            fout.write("</body></html>".encode("UTF-8"))
        
        # next chapter button
        count = count + 1
        next_url = target_url + str(count)
            

if __name__ == '__main__':
    sys.exit(main())