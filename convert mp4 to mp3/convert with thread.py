from threading import*
from time import time
from moviepy.editor import *

def convert(url,audio):
    video = VideoFileClip(url)
    video.audio.write_audiofile(audio)

start_time=time()

urls=[["https://persian2.asset.aparat.com/aparat-video/5ebe0a132df8de4064a8de3d80194fb748135115-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImEyYWMxMGQzYWYzMTU4NjBlMDMwY2IyODIwYWUwMjgxIiwiZXhwIjoxNjc4NDUwMTUzLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.m15XL3qN3faxe3vupFx2KDj9UjqIRB6zdo7B2F1jPw0","audio1.mp3"],
["https://caspian3.asset.aparat.com/aparat-video/823efad8f6933673d0cf5ee72827cee245938447-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImRiN2ZmMjhmOWIyMDk1YTU1ZDZlNjlmZGFlNzJmNDIwIiwiZXhwIjoxNjc4NDUyNTExLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.d-3h4ySH0XFutkJOPf7PzIGt4MumpROTVxCK4MV6zuA","audio2.mp3"],
["https://persian5.asset.aparat.com/aparat-video/9b2007e5f9e1a52cced920914abd60d144132357-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6Ijk0NzQ4OTkyNDM1ODI1M2VmZTQxMWZkZGQzYTQ4NDMyIiwiZXhwIjoxNjc4NDUyNjUzLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.T2cAkBc2Bsx7bil68ODoh0LiczdB_R6Z8krYrNGgkS8","audio3.mp3"]
]

threads=[]
for url,audio in urls:
    new_thread=Thread(target=convert,args=[url,audio])
    threads.append(new_thread)

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time=time()
print(end_time - start_time)