import threading
from time import time
from moviepy.editor import *

def convert(url,audio):
    video = VideoFileClip(url)
    video.audio.write_audiofile(audio)

start_time=time()


t=threading.Thread(target=convert,args=["https://persian2.asset.aparat.com/aparat-video/5ebe0a132df8de4064a8de3d80194fb748135115-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImEyYWMxMGQzYWYzMTU4NjBlMDMwY2IyODIwYWUwMjgxIiwiZXhwIjoxNjc4NDUwMTUzLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.m15XL3qN3faxe3vupFx2KDj9UjqIRB6zdo7B2F1jPw0","audio.mp3"])

t.start()
t.join()

end_time=time()
print(end_time - start_time)


