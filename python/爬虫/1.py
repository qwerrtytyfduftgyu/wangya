'''
pytho爬取网易云歌曲
'''
import requests
a = 'https://m801.music.126.net/20240416211516/313fb25f2489bac89932a4bf2818a734/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/35163575262/dff9/ca14/6380/34fdcc5f8f536f37f768ce5a49162433.m4a'

b = requests.get(a)
c = b.content
# 在尾部添加wb创建一个没有的文件
d = open('歌曲.mp3','wb')
d.write(c)
