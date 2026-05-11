import os
import re
import sys

DUP_PATTERN = re.compile(r"(chương \d*?:.*?)<", flags=re.MULTILINE | re.IGNORECASE)

def fix_filename(base_dir:str):
    for name in os.listdir(base_dir):
        if ".." in name:
            print(name)
            new_name = name.replace("..html", ".html")
            os.rename(os.path.join(base_dir, name), os.path.join(base_dir, new_name))


def remove_duplicate(content: str) -> str:
    matches = DUP_PATTERN.finditer(content)

    found: dict[str, list[tuple[int, int]]] = {}
    for _, match in enumerate(matches, start=1):
        for group_num, group in enumerate(match.groups(), start=1):
            start:int = match.start(group_num)
            end:int = match.end(group_num)
            if group in found:
                found[group].append((start, end))
            else:
                found[group] = [(start, end)]

    for _, group in found.items():
        if len(group) <= 0:
            continue
        group.reverse()
        for start, end in group[1:]:
            content = content[:start] + content[end:]

    return content

# def remove_spam_1(base_dir:str, truncates:list):
#     count = 0
#     for name in os.listdir(base_dir):
#         full_name = os.path.join(base_dir, name)
#         with open(full_name, mode="r", encoding="utf-8") as read_file:
#             content = read_file.read()
#         for truncate_st in truncates:
#             content = content.replace(truncate_st, "")
#         with open(full_name, mode="w", encoding="utf-8") as write_file:
#             write_file.write(content)
#
#         count += 1
#         if count % 100 == 0:
#             print(count, "::", name)

def remove_spam(base_dir: str, literals: list[str], regex_strs: list[str]):
    count = 0
    regex_compiled = [re.compile(x) for x in regex_strs]
    for name in os.listdir(base_dir):
        # if not name.startswith("Chuong_102_"):
        #     continue
        full_name = os.path.join(base_dir, name)
        with open(full_name, mode="r", encoding="utf-8") as read_file:
            content = read_file.read()
        content = remove_duplicate(content)
        for literal_st in literals:
            content = content.replace(literal_st, "")
        for regex in regex_compiled:
            content = regex.sub("", content, re.M | re.U | re.S)
        with open(full_name, mode="w", encoding="utf-8") as write_file:
            write_file.write(content)

        count += 1
        if count % 100 == 0:
            print(count, "::", name)


def main():
    truncates = [
        r'<p style="margin-bottom: 25px;"><a style="font-size: 26px; color: #000; " href="https://www.facebook.com/123Truyen" target="_blank">Click Theo Dõi -&gt; <span style="color: red;">Fanpage</span> Để Cập Nhật Truyện Ta Thành Tân Thủ Thôn BOSS</a></p>',
        r'<p style="font-size: 0.8em; font-style: italic;">Bạn đang đọc truyện trên 123truyenx.vip , Chúc bạn đọc truyện vui vẻ!</p>',
        r'<p style="margin-bottom: 25px;"><a style="font-size: 26px; color: #000; " href="https://www.facebook.com/123Truyen" target="_blank">Click Theo Dõi -&gt; <span style="color: red;">Fanpage</span> Để Cập Nhật Truyện Lại Giết Ta Thêm Mấy Lần, Ta Liền Vô Địch</a></p>',
        r'<br> Main tính cách dung hòa giữa cực độ cẩu , vô sỉ , sát phạt quyết đoán và rất là sợ chết.',
        r'<br>CHỔI QUÉT RÁC, thanh lọc tinh thần, thổi bay mệt mỏi. Nhân phẩm đảm bảo, chất lượng khỏi bàn, đọc liền biết… ',
        r'Bạn có thể tìm kiếm truyện với các từ khóa sau:',
        r'<p style="font-size: 0.8em; font-style: italic;">Bạn có thể tìm kiếm truyện với các từ khóa sau:',
        r'<a href="https://123truyenh.xyz/boss-1#ta-thanh-tan-thu-thon-boss"><span style="font-weight:bold">Ta Thành Tân Thủ Thôn BOSS</span></a>',
        r'<a href="https://123truyenh.xyz/boss-1#truyen-ta-thanh-tan-thu-thon-boss"><span style="font-weight:bold">truyện Ta Thành Tân Thủ Thôn BOSS</span></a>', 
        r'<a href="https://123truyenh.xyz/boss-1#doc-truyen-ta-thanh-tan-thu-thon-boss-full"><span style="font-weight:bold">đọc truyện Ta Thành Tân Thủ Thôn BOSS</span></a>', 
        r'<a href="https://123truyenh.xyz/boss-1#ta-thanh-tan-thu-thon-boss-full"><span style="font-weight:bold">Ta Thành Tân Thủ Thôn BOSS full</span></a>', 
        r'<a href="https://123truyenh.xyz/boss-1#ta-thanh-tan-thu-thon-boss-chuong-moi"><span style="font-weight:bold">Ta Thành Tân Thủ Thôn BOSS chương mới</span> </a></p>',
        r'<p style="margin: 15px 0;"><a style="font-size: 35px; color: #000; " href="https://www.facebook.com/123Truyen" target="_blank">Click Theo Dõi -&gt; <span style="color: red;">Fanpage</span> để cập nhật website</a></p>',
        r'<p style="font-size: 0.8em; font-style: italic;">Bạn đang đọc truyện trên 123truyend.xyz , Chúc bạn đọc truyện vui vẻ!</p>',
        r'---',
        r'<p style="margin: 15px 0;"><a style="font-size: 35px; color: #000; " href="https://www.facebook.com/123Truyen" target="_blank">Click Theo Dõi -&gt; <span style="color: red;">Fanpage</span> để cập nhật website</a></p>',
        r'Truyện quân sự đã hoàn, đi từ thời cổ đại đến hiện đại, nhiều nhân vật lịch sử xuất hiện, chiến trường khốc liệt đến từng chi tiết.  Hàm Ngư xuất phẩm đương nhiên là tinh phẩm. ',
        r'Truyện hài, sảng văn, tấu hài là chính, tu luyện và cày map là phụ, hợp gu thì nhảy hố!!!',
        r'Tay phải đánh võ, tay trái chơi ngải, chân gác tiền tài, đầu gối đài cao. Mời các đạo hữu ghé thăm',
        r'===',
    ]
    
    literal_truncate = [
        r'Bạn có thể tìm kiếm truyện với các từ khóa sau:',
        #r"Bạn đang đọc truyện trên 123truyend.xyz , Chúc bạn đọc truyện vui vẻ!",
        r"  ,",
        r"  ",
         r'Hạo Kiếp Kết Thúc, Diệt Kiếp Tái Hiện!',
        r'Minh Tộc Xâm Lấn, Tiên Ma Đại Loạn!',
        r'Đại Năng Trọng Sinh, Quỷ Tài Xuất Thế!',
        r'Tiên Lộ Hiện, Yêu Nghiệt Tranh Phong!',
        r'Main dân thổ địa, bán cẩu lưu, hệ thống',
        r'Bố cục thế giới rộng, các nhân vật đều cơ trí không não tàn. Mời các bạn đón đọc truyện Việt thể loại Huyền Huyễn',
        r'============================',
        r'==',
        r'INDEX',
        r'END',
        r'Hãy nhấn like ở mỗi chương để ủng hộ tinh thần các dịch giả bạn nhé!',
        r'Độc Y, có thể hồi máu, có thể kèm độc trong kỹ năng, võng du giải trí cực tốt, truyện đã full, bạo chương nhanh'
        r'"Núi La Sơn, mười năm có một đêm trăng tỏ.',
        r'Biển Vô Lượng, trăm năm có một đợt thủy triều',
        r'Sương mù Thương Mang, ngàn năm có một lần lui tán',
        r'Mà ta chờ đợi mấy vạn năm, chỉ để được hướng về quân nở một nụ cười!"',
        r'Võ lộ thênh thang không bờ bến, quay đầu chợt hiện bóng hồng nhan',
        r'Mời đọc:'
    ]
    
    regex_truncate = [
        r"Converter.*?cầu ủng hộ.*?\n",
        r"<a.*>.*?</a>",
        r"<script>.*?</script>",
        r"\s*,\s*,",
        r"<p style=\"font-size: 0.8em; font-style: italic;\">Bạn đang đọc truyện.*?</p>",
        r"Bạn đang đọc truyện trên 123truyen.*? , Chúc bạn đọc truyện vui vẻ!",
        r"\n\s*?,\s*?\n",
        r"<p .*?>\s*?,\s*?\n",
        r"<iframe .*?</iframe>",
        r"Truyện được đăng bởi.*?vn"
    ]
    
    base_dir = r"D:\Temp\DaoAnDat_BanTangKhongMuonLamAnhDe"
    fix_filename(base_dir)
    remove_spam(base_dir, literal_truncate, regex_truncate)
    
            
if __name__ == '__main__':
    sys.exit(main())