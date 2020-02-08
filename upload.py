import upload.file as f
import upload.upload as upload

cookies = ""

json = {
    "copyright": 2,  # 1自治，2搬运
    "videos": [{
        "filename": 0,  # 别管
        "title": "日常第二十一话",  # 分p标题
        "desc": ""  # 不知道
    }],
    "source": "测试投稿",  # 转载地址
    "tid": 21,  # 分类
    "cover": "",  # 封面图  可以不管
    "title": "日常第二十一话",  # 总标题
    "tag": "日漫",  # 标签
    "desc_format_id": 0,  # 不知道
    "desc": "测试投稿",  # 简介
    "dynamic": "#日漫#",  # 粉丝动态
    "subtitle": {"open": 0, "lan": ""}  # 不知道
}

# 视频文件
f = f.File('1.mp4')

# print(f.read(2500))

upload = upload.Upload()
upload.init('23333.mp4', f.size, cookies)  # '23333.mp4' 可以随便填，但必须有相应的视频格式后缀
upload.set_post_json(json)
upload.run(f)

f.close()
