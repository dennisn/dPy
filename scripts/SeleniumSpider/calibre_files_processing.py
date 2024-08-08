import codecs
import os
import sys


def fix_filename(base_dir:str):
    for name in os.listdir(base_dir):
        if ".." in name:
            print(name)
            new_name = name.replace("..html", ".html")
            os.rename(os.path.join(base_dir, name), os.path.join(base_dir, new_name))
            
def remove_spam(base_dir:str, truncates:list):
    count = 0
    for name in os.listdir(base_dir):
        full_name = os.path.join(base_dir, name)
        with codecs.open(full_name, "r", "utf-8") as read_file:
            content = read_file.read()
        for truncate_st in truncates:
            content = content.replace(truncate_st, "")
        with codecs.open(full_name, "w", "utf-8") as write_file:
            write_file.write(content)
        
        count += 1
        if count % 100 == 0:
            print(count, "::", name)
           
def main():
    truncates = [
        r'<p style="margin-bottom: 25px;"><a style="font-size: 26px; color: #000; " href="https://www.facebook.com/123Truyen" target="_blank">Click Theo Dõi -&gt; <span style="color: red;">Fanpage</span> Để Cập Nhật Truyện Cẩu Tại Yêu Võ Loạn Thế Tu Tiên</a></p>',
        r'<p style="font-size: 0.8em; font-style: italic;">Thông Báo: Website chuyển qua sử dụng tên miền mới <a href="https://123truyennn.com/">123truyennn.com</a> , Chúc bạn đọc truyện vui vẻ!</p>',
        r'<p></p><br>Truyện việt, cẩu đạo, top1 nhân khí cách top2 gần 20% số điểm! <p></p>',
        r'<p style="margin-bottom: 25px;"><a style="font-size: 26px; color: #000; " href="https://www.facebook.com/123Truyen" target="_blank">Click Theo Dõi -&gt; <span style="color: red;">Fanpage</span> Để Cập Nhật Truyện Tu Tiên: Cẩu Tại Dược Viên Làm Ruộng Cầu Trường Sinh</a></p>',
        r'<p style="font-size: 0.8em; font-style: italic;">Thông Báo: Website chuyển qua sử dụng tên miền mới <a href="https://123truyenii.com/">123truyenii.com</a> , Chúc bạn đọc truyện vui vẻ!</p>',
        r'<p></p><br>Độc Y, có thể hồi máu, có thể kèm độc trong kỹ năng, võng du giải trí cực tốt, truyện đã full, bạo chương nhanh <p></p>                    <p style="margin-bottom: 25px;"><a style="font-size: 35px; color: #000; " href="https://www.facebook.com/123Truyen" target="_blank">Click Theo Dõi -&gt; <span style="color: red;">Fanpage</span> để cập nhật website</a></p>',
    ]
    
    base_dir = r"D:\Temp\VanSaoCong_CauTaiYeuVoLoanTheTuTien"
    fix_filename(base_dir)
    remove_spam(base_dir, truncates)
            
if __name__ == '__main__':
    sys.exit(main())