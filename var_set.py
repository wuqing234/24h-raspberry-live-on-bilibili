#coding:utf-8

#需要修改的值

path = '/home/pi/live'
#本文件的路径，请修改

roomid = '205175'
#房间id（真实id，不一定是网址里的那个数）

cookie = 'finger=edc6ecda; buvid3=20A59A66-E31C-4516-9DA5-BF5332B9A3DC16095infoc; sid=aetvmslp; DedeUserID=287990140; DedeUserID__ckMd5=c828c660f915a2c8; SESSDATA=0f497c2f%2C1539135531%2Cb468664a; bili_jct=9ec17bd356ca26dd06b0ff6331ffb292; LIVE_BUVID=c2d2c7b75eac7fda9b1f0e6497816aa1; _dfcaptcha=e02671b87f963cb1d37e761021a17027; fts=1536543547; UM_distinctid=165c121df41158-0e8495d3cd41d4-9393265-144000-165c121df435b9; bp_t_offset_287990140=161703268132895259; LIVE_BUVID__ckMd5=472280cec355fd6c'
#发送弹幕用的cookie
csrf_token = '9ec17bd356ca26dd06b0ff6331ffb292'
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
