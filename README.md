# blibili_wallpaper_spider

> 本项目使用`Python`编写，采用`requests`库爬取`bilibili`官方壁纸并保存到本地。
>
> 思路来源于[bilibili-wallpaper](https://github.com/zhaoolee/bilibili-wallpaper)，在此表示感谢。

# 运行

>+ 命令行执行
>
>`python bilibili_wallpaper_spider.py`
>
>+ IDE中执行即可

### 方式1：使用cookie直接请求json数据

+ 复制链接 `https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=6823116&page_num=0&page_size=10000&biz=all` 到浏览器打开
+ 按`F12`打开开发者工具，在`Network`那里找到请求的`Header`，再在里面找到对应的`cookie`，选中复制粘贴到代码中`Headers`的`Cookie`中，首尾添加`'`即可。

![image-20220703112245398](https://cdn.jsdelivr.net/gh/Thee24LYJ/Pic_Image/images/image-20220703112245398.png)

### 方式2：直接读取json文件

+ 浏览器打开 https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=6823116&page_num=0&page_size=10000&biz=all 并将其内容保存成`json`文件
+ 取消直接读取`json`文件的代码注释并修改`json_path`为保存的`json`文件路径
+ 注释`URL`请求得到`json`数据

# 精美壁纸

+ 哔哩哔哩 春

![e0a9f20fcdf2977dadef521f02b0465004cafee6](https://cdn.jsdelivr.net/gh/Thee24LYJ/Pic_Image/images/e0a9f20fcdf2977dadef521f02b0465004cafee6.jpg)

+ bilibili盛夏

![](https://cdn.jsdelivr.net/gh/Thee24LYJ/Pic_Image/images/bilibili盛夏.png)

+ 哔哩哔哩 秋

![3f3986e2e781a521e8b9be7d9df068bf99f4b389](https://cdn.jsdelivr.net/gh/Thee24LYJ/Pic_Image/images/3f3986e2e781a521e8b9be7d9df068bf99f4b389.jpg)

+ 哔哩哔哩 冬

![022c23204ba7816e279cc352e332b74b6f656da2](https://cdn.jsdelivr.net/gh/Thee24LYJ/Pic_Image/images/022c23204ba7816e279cc352e332b74b6f656da2.png)