#!/usr/bin/python3

import tkinter
from PIL import Image, ImageTk
import requests
from io import BytesIO
from threading import Timer


rootWindow = tkinter.Tk()

# the following makes the program full-screen
RWidth = rootWindow.winfo_screenwidth()
RHeight = rootWindow.winfo_screenheight()
#
rootWindow.overrideredirect(True)	# without a close option
rootWindow.geometry(("%dx%d")%(RWidth,RHeight))

cameraURL01="http://209.251.247.251:82/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507301122"
cameraURL02="http://108.209.209.13/webcapture.jpg?command=snap&amp;channel=1?1507300788"
cameraURL03="http://72.81.132.14:60001/SnapshotJPEG?Resolution=640x480&amp;amp;Quality=Clarity&amp;amp;1507300872"
cameraURL04="http://24.98.52.12:8082/cgi-bin/viewer/video.jpg?r=1507300889"
cameraURL05="http://73.239.2.12:86/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507300909"
cameraURL06="http://24.23.232.13:50001/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507300932"
cameraURL07="http://72.24.25.12/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507300941"
cameraURL08="http://72.67.198.9:8080/cgi-bin/viewer/video.jpg?r=1507300960"
cameraURL09="http://63.172.41.245/webcapture.jpg?command=snap&amp;channel=1?1508162812"
cameraURL10="http://73.204.60.243:83/webcapture.jpg?command=snap&amp;channel=1?1508162842"
cameraURL11="http://69.29.46.9:50000/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507300992"
cameraURL12="http://166.251.210.244:81/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507302299"
cameraURL13="http://208.83.194.7/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507301058"
cameraURL14="http://166.251.210.239:81/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507302581"
cameraURL15="http://76.76.72.210/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507303549"
cameraURL16="http://70.167.85.194:81/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507297041"


image01_label = tkinter.Label()
image02_label = tkinter.Label()
image03_label = tkinter.Label()
image04_label = tkinter.Label()
image05_label = tkinter.Label()
image06_label = tkinter.Label()
image07_label = tkinter.Label()
image08_label = tkinter.Label()
image09_label = tkinter.Label()
image10_label = tkinter.Label()
image11_label = tkinter.Label()
image12_label = tkinter.Label()
image13_label = tkinter.Label()
image14_label = tkinter.Label()
image15_label = tkinter.Label()
image16_label = tkinter.Label()
image01_label.grid(row=0, column=0)
image02_label.grid(row=0, column=1)
image03_label.grid(row=0, column=2)
image04_label.grid(row=0, column=3)
image05_label.grid(row=1, column=0)
image06_label.grid(row=1, column=1)
image07_label.grid(row=1, column=2)
image08_label.grid(row=1, column=3)
image09_label.grid(row=2, column=0)
image10_label.grid(row=2, column=1)
image11_label.grid(row=2, column=2)
image12_label.grid(row=2, column=3)
image13_label.grid(row=3, column=0)
image14_label.grid(row=3, column=1)
image15_label.grid(row=3, column=2)
image16_label.grid(row=3, column=3)
	
def main():
	rootWindow.bind('<Escape>', close)
	Timer(0.1, refreshCam01).start()
	Timer(0.1, refreshCam02).start()
	Timer(0.1, refreshCam03).start()
	Timer(0.1, refreshCam04).start()
	Timer(0.1, refreshCam05).start()
	Timer(0.1, refreshCam06).start()
	Timer(0.1, refreshCam07).start()
	Timer(0.1, refreshCam08).start()
	Timer(0.1, refreshCam09).start()
	Timer(0.1, refreshCam10).start()
	Timer(0.1, refreshCam11).start()
	Timer(0.1, refreshCam12).start()
	Timer(0.1, refreshCam13).start()
	Timer(0.1, refreshCam14).start()
	Timer(0.1, refreshCam15).start()
	Timer(0.1, refreshCam16).start()

def refreshCam01():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL01, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image01_label.configure(image=tmp_photo)
		image01_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#Timer(50, refreshCam02)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam01).start()

def refreshCam02():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL02, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image02_label.configure(image=tmp_photo)
		image02_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam03)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam02).start()
	
def refreshCam03():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL03, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image03_label.configure(image=tmp_photo)
		image03_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam04)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam03).start()
	
def refreshCam04():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL04, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image04_label.configure(image=tmp_photo)
		image04_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam05)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam04).start()
	
def refreshCam05():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL05, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image05_label.configure(image=tmp_photo)
		image05_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam06)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam05).start()
	
def refreshCam06():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL06, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image06_label.configure(image=tmp_photo)
		image06_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam07)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam06).start()
	
def refreshCam07():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL07, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image07_label.configure(image=tmp_photo)
		image07_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam08)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam07).start()
	
def refreshCam08():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL08, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image08_label.configure(image=tmp_photo)
		image08_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam09)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam08).start()
	
def refreshCam09():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL09, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image09_label.configure(image=tmp_photo)
		image09_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam10)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam09).start()
	
def refreshCam10():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL10, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image10_label.configure(image=tmp_photo)
		image10_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam11)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam10).start()
	
def refreshCam11():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL11, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image11_label.configure(image=tmp_photo)
		image11_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam12)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam11).start()
	
def refreshCam12():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL12, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image12_label.configure(image=tmp_photo)
		image12_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam13)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam12).start()
	
def refreshCam13():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL13, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image13_label.configure(image=tmp_photo)
		image13_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam14)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam13).start()
	
def refreshCam14():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL14, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image14_label.configure(image=tmp_photo)
		image14_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam15)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam14).start()
	
def refreshCam15():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL15, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image15_label.configure(image=tmp_photo)
		image15_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam16)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam15).start()
	
def refreshCam16():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL16, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
		image16_label.configure(image=tmp_photo)
		image16_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	#rootWindow.after(50, refreshCam01)
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam16).start()


def close(event=None):
	rootWindow.quit()
		
# start the subprocess, main loop, and gui
if __name__ == '__main__':
	main()
	rootWindow.mainloop()
	
