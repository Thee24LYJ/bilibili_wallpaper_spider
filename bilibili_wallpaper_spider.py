# bilibili爬虫 version 2.1
# 参考：https://github.com/zhaoolee/bilibili-wallpaper

import os
import re
import json
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie': 'l=v; buvid3=B0D74F08-D07F-404E-39D7-E8A2FE4D1A9153222infoc; CURRENT_FNVAL=80; _uuid=E06523AC-FA4F-18DB-0833-BD15DC71236553757infoc; blackside_state=1; rpdid=|(kRu)~RRkl0J\'uYkRk)kJl); buvid_fp=B0D74F08-D07F-404E-39D7-E8A2FE4D1A9153222infoc; buvid_fp_plain=B0D74F08-D07F-404E-39D7-E8A2FE4D1A9153222infoc; SESSDATA=4a480e95,1639884061,5f394*61; bili_jct=20caaccb9a577494ebfff10d8794b309; DedeUserID=435070009; DedeUserID__ckMd5=794ce27c5f185238; sid=66crlaql; fingerprint3=dc07b734860f34040b7892876e6862c5; fingerprint=76bd2c43c7f94fa7eeee73ec281992de; fingerprint_s=89c3f98022ac9cd6deee25db6ee1bbe9; CURRENT_QUALITY=80; CURRENT_BLACKGAP=1; bp_t_offset_435070009=558404898775372079; LIVE_BUVID=AUTO4816288591592746; bp_video_offset_435070009=558676761610835843; innersign=1; PVID=1'}  # 设置访问头
path = r'C:\Users\G3\Desktop\壁纸'
url=r'https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=6823116&page_num=0&page_size=10000&biz=all'

# 直接读取json文件
# json_path = r'E:\IDMDownload\bilibili-wallpaper-master\doc_list.json'
# with open(json_path, 'r', encoding='utf-8-sig') as json_file:
#     json_content = json.load(json_file)
# print(jsoncontent.keys())
# print(jsoncontent["data"])

# URL请求得到json数据
json_text=requests.get(url,headers=headers).text
json_content=json.loads(json_text)  #data属性的值为json格式，需进行转换
print(json_content["data"])


linkre = re.compile(r'https://i0.hdslb.com/bfs/.{46,48}.jpg|https://i0.hdslb.com/bfs/.{46,48}.png')  # 图片链接正则表达式匹配
result = linkre.findall(str(json_content["data"]))
result=list(set(result))    # 去除重复元素并转换为列表
print("图片数:{0}张".format(len(result)))
print("图片链接:{0}".format(result))


try:
    # 如果根目录不存在就创建该根目录
    if not os.path.exists(path):
        os.makedirs(path)

    if os.path.exists(path):
        for i in range(len(result)):
            img_name = result[i].split('/')[-1]    # 获取图片文件名
            img_path = path + r'\{0}'.format(img_name)
            if os.path.exists(img_path):
                print("第{0}张已存在--->跳过".format(str(i + 1)))
            else:
                img = requests.get(result[i], headers=headers)
                with open(img_path, 'wb') as f:
                    f.write(img.content)
                    print("第{0}张保存成功!".format(str(i + 1)))

except Exception as e:
    print("执行出错")
    print("错误原因:{0}".format(e))