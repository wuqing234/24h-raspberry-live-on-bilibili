#coding:utf-8

#需要修改的值

path = '24h-raspberry-live-on-bilibili/'
#本文件的路径，请修改

roomid = '205175'
#房间id（真实id，不一定是网址里的那个数）

cookie = '_uuid=050AA2B2-05D9-D02D-E49E-F5998E3A7FBF33197infoc; buvid3=0D5EDA9F-17C4-41FD-97FC-EA93BF34106C190980infoc; LIVE_BUVID=AUTO4515661229332616; sid=a3ttkc14; DedeUserID=18085741; DedeUserID__ckMd5=3bb4e60e31692881; bili_jct=43594b165fc75e1ef64778ce9f565a34; finger=b3372c5f; im_notify_type_18085741=0; CURRENT_FNVAL=16; stardustvideo=1; rpdid=|(Y|)uYummu0J'ulYYuJumlY; UM_distinctid=16ca4c9cddc783-0b616f76e84c74-7373e61-1fa400-16ca4c9cdddbf6; fts=1566136868; CURRENT_QUALITY=112; bp_t_offset_18085741=292378739037423188; GIFT_BLOCK_COOKIE=GIFT_BLOCK_COOKIE; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1566122954,1566573328,1566991687; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1566991885'
#发送弹幕用的cookie
csrf_token = '43594b165fc75e1ef64778ce9f565a34'
#发送弹幕用的csrf_token

download_api_url = 'https://qq.papapoi.com/163music/'
#获取音乐链接的api网址，服务器性能有限，尽量请换成自己的，php文件在php文件夹

rtmp = 'rtmp://txy.live-send.acg.tv/live-txy/'
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
