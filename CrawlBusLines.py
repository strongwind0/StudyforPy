import requests
from bs4 import BeautifulSoup
import re
import csv


class Data:
    def __init__(self, name, duration, volume, barrage, upload):
        self.name = name
        self.duration = duration
        self.volume = volume
        self.barrage = barrage
        self.upload = upload

    def to_info(self, row=0):
        print("第{:}名".format(row))
        print("名称:{:}".format(self.name))
        print("时长:{:}".format(self.duration))
        print("播放数:{:}".format(self.volume))
        print("弹幕数:{:}".format(self.barrage))
        print("上传时间:{:}".format(self.upload))
        return [self.name, self.duration, self.volume, self.barrage, self.upload]


def parsing(item):
    # 截取视频名称
    video_name = str(test.a)
    intercept_name = re.compile('title=\\".*\\"><div')
    video_name = intercept_name.findall(video_name)[0]
    video_name = video_name[7:]
    video_name = video_name[:-23]

    # 截取视频时长
    video_duration = str(test.a.div.div.find_next_sibling())
    intercept_duration = re.compile('>.*<')
    video_duration = intercept_duration.findall(video_duration)[0]
    video_duration = video_duration[1:]
    video_duration = video_duration[:-1]

    # 截取观看数、弹幕数、上传时间
    play_volume = test.a.find_next_sibling().div.find_next_sibling().find_next_sibling().span
    barrage_number = play_volume.find_next_sibling()
    upload_time = barrage_number.find_next_sibling()
    play_volume = str(play_volume)
    barrage_number = str(barrage_number)
    upload_time = str(upload_time)
    intercept1 = re.compile(".*万")
    play_volume = intercept1.findall(play_volume)[0][-7:]
    barrage_number = intercept1.findall(barrage_number)[0][-5:]
    intercept2 = re.compile("....-..-..")
    upload_time = intercept2.findall(upload_time)[0]
    data = Data(video_name,video_duration,play_volume,barrage_number,upload_time)
    return data


kv = {"keyword": '老番茄', "order": 'click'}
r = requests.get("https://search.bilibili.com/all?", kv)
print(r.status_code)
p = r.text
soup = BeautifulSoup(p, 'html.parser')
test = soup.body.contents[2].div.contents[1].li
datas = []
print("老番茄视频点击量前10")
for i in range(10):
    datas.append(parsing(test))
    test = test.find_next_sibling()
f = open('老番茄B站视频点击量前10.csv', 'w', encoding='utf-8', newline="")
writer = csv.writer(f)
writer.writerow(['视频名称', '视频时长', '观看数', '弹幕数', '上传时间'])
row = 1
for i in datas:
    writer.writerow(i.to_info(row))
    row += 1
print("已写入文件")
