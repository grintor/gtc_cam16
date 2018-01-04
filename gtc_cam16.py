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
cameraURL05="http://80.24.185.230:86/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1515078226"
cameraURL06="http://24.23.232.13:50001/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1507300932"
cameraURL07="http://80.24.185.230:81/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1515078327"
cameraURL08="http://80.24.185.230:82/cgi-bin/camera?resolution=640&amp;amp;quality=1&amp;amp;Language=0&amp;amp;1515078336"
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

def URL2PhotoImage(URL):
	return ImageTk.PhotoImage(Image.open(BytesIO(requests.get(URL, timeout=4).content)).resize((int(RWidth/4),int(RHeight/4)), Image.ANTIALIAS))
	
def refreshCam01():
	try:
		tmp_photo = URL2PhotoImage(cameraURL01)
		image01_label.configure(image=tmp_photo)
		image01_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam01).start()

def refreshCam02():
	try:
		tmp_photo = URL2PhotoImage(cameraURL02)
		image02_label.configure(image=tmp_photo)
		image02_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam02).start()
	
def refreshCam03():
	try:
		tmp_photo = URL2PhotoImage(cameraURL03)
		image03_label.configure(image=tmp_photo)
		image03_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam03).start()
	
def refreshCam04():
	try:
		tmp_photo = URL2PhotoImage(cameraURL04)
		image04_label.configure(image=tmp_photo)
		image04_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam04).start()
	
def refreshCam05():
	try:
		tmp_photo = URL2PhotoImage(cameraURL05)
		image05_label.configure(image=tmp_photo)
		image05_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam05).start()
	
def refreshCam06():
	try:
		tmp_photo = URL2PhotoImage(cameraURL06)
		image06_label.configure(image=tmp_photo)
		image06_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam06).start()
	
def refreshCam07():
	try:
		tmp_photo = URL2PhotoImage(cameraURL07)
		image07_label.configure(image=tmp_photo)
		image07_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam07).start()
	
def refreshCam08():
	try:
		tmp_photo = URL2PhotoImage(cameraURL08)
		image08_label.configure(image=tmp_photo)
		image08_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam08).start()
	
def refreshCam09():
	try:
		tmp_photo = URL2PhotoImage(cameraURL09)
		image09_label.configure(image=tmp_photo)
		image09_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam09).start()
	
def refreshCam10():
	try:
		tmp_photo = URL2PhotoImage(cameraURL10)
		image10_label.configure(image=tmp_photo)
		image10_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam10).start()
	
def refreshCam11():
	try:
		tmp_photo = URL2PhotoImage(cameraURL11)
		image11_label.configure(image=tmp_photo)
		image11_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam11).start()
	
def refreshCam12():
	try:
		tmp_photo = URL2PhotoImage(cameraURL12)
		image12_label.configure(image=tmp_photo)
		image12_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam12).start()
	
def refreshCam13():
	try:
		tmp_photo = URL2PhotoImage(cameraURL13)
		image13_label.configure(image=tmp_photo)
		image13_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam13).start()
	
def refreshCam14():
	try:
		tmp_photo = URL2PhotoImage(cameraURL14)
		image14_label.configure(image=tmp_photo)
		image14_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam14).start()
	
def refreshCam15():
	try:
		tmp_photo = URL2PhotoImage(cameraURL15)
		image15_label.configure(image=tmp_photo)
		image15_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam15).start()
	
def refreshCam16():
	try:
		tmp_photo = URL2PhotoImage(cameraURL16)
		image16_label.configure(image=tmp_photo)
		image16_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.05, refreshCam16).start()


def close(event=None):
	rootWindow.quit()

# start the subprocess, main loop, and gui
if __name__ == '__main__':
	main()
	rootWindow.mainloop()
	
