#coding:utf-8

#需要修改的值

path = '/home/pi/live'
#本文件的路径，请修改

roomid = '205175'
#房间id（真实id，不一定是网址里的那个数）

cookie = 'im_notify_type_287990140=0; buvid3=A33D94EB-1970-4F70-810A-A5A88F225B0E16065infoc; LIVE_BUVID=2f650f6c76ac2829f0f391a4f2eb1e71; sid=8525ub9l; DedeUserID=287990140; DedeUserID__ckMd5=c828c660f915a2c8; SESSDATA=0f497c2f%2C1539846725%2Cb24a836c; bili_jct=0e764ad33be2bc01dda32f92dc0bbb52; finger=edc6ecda; bp_t_offset_287990140=165039706103486238; fts=1537254904; UM_distinctid=165eb884f6b37-0fced4333db1f-9393265-144000-165eb884f6c409; LIVE_BUVID__ckMd5=c6498ab0b5d2fe94; GIFT_BLOCK_COOKIE=GIFT_BLOCK_COOKIE; GIFT_BLOCK_COOKIE=GIFT_BLOCK_COOKIE; _dfcaptcha=54c5eaf5f2378a4e3aa0f75d5887cc29'
#发送弹幕用的cookie
csrf_token = '0e764ad33be2bc01dda32f92dc0bbb52'
#发送弹幕用的csrf_token

download_api_url = 'https://qq.papapoi.com/163music/'
#获取音乐链接的api网址，服务器性能有限，尽量请换成自己的，php文件在php文件夹

rtmp = 'rtmp://qn.live-send.acg.tv/live-qn/'
#直播给的两个码，填在这里
live_code = '?streamname=live_18085741_9906629&key=f61ebeb4e725ffed876575c3ebcd06d9'

free_space=15360
#允许download/default_mp3文件夹占用空间大小，超过时自动按时间顺序删除视频/音乐，单位：MiB

maxbitrate='3000'
#允许的最大码率，单位k，字符串类型，切勿改成数值型

dm_size=20
#每段弹幕的最大长度（20级以后可发30字）

use_dht11 = False
#是否使用dht11温湿度传感器

use_gift_check = False
#是否使用投礼物才让点歌的设定

play_videos_when_night = False
#是否播放晚间专属视频？
