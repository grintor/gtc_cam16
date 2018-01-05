#!/usr/bin/python3

import tkinter
from PIL import Image, ImageTk
import requests
from io import BytesIO
from threading import Timer
import json
import os

SID=None
while SID is None:
	try:
		SIDJson = requests.get("http://10.123.45.210:5002/webapi/auth.cgi?api=SYNO.API.Auth&method=Login&version=2&account=admin&passwd=abc123&session=SurveillanceStation&format=sid", timeout=4).content
		SIDArr = json.loads(str(SIDJson,'utf-8'))
		SID=SIDArr['data']['sid']
	except:
		pass

camSession = requests.Session()

rootWindow = tkinter.Tk()

# the following makes the program full-screen
RWidth = rootWindow.winfo_screenwidth()
RHeight = rootWindow.winfo_screenheight()
#
rootWindow.overrideredirect(True)	# without a close option
rootWindow.geometry(("%dx%d")%(RWidth,RHeight))

cameraURL01="http://10.123.45.210:5002/webapi/entry.cgi?camStm=1&version=%228%22&cameraId=15&api=%22SYNO.SurveillanceStation.Camera%22&preview=true&method=%22GetSnapshot%22&_sid=" + SID
cameraURL02="http://10.123.45.210:5002/webapi/entry.cgi?camStm=2&version=%228%22&cameraId=22&api=%22SYNO.SurveillanceStation.Camera%22&preview=true&method=%22GetSnapshot%22&_sid=" + SID
cameraURL03="http://10.123.45.210:5002/webapi/entry.cgi?camStm=2&version=%228%22&cameraId=23&api=%22SYNO.SurveillanceStation.Camera%22&preview=true&method=%22GetSnapshot%22&_sid=" + SID
cameraURL04=""
cameraURL05="http://10.123.45.210:5002/webapi/entry.cgi?camStm=2&version=%228%22&cameraId=24&api=%22SYNO.SurveillanceStation.Camera%22&preview=true&method=%22GetSnapshot%22&_sid=" + SID
cameraURL06="http://10.123.45.210:5002/webapi/entry.cgi?camStm=2&version=%228%22&cameraId=11&api=%22SYNO.SurveillanceStation.Camera%22&preview=true&method=%22GetSnapshot%22&_sid=" + SID


image01_label = tkinter.Label()
image02_label = tkinter.Label()
image03_label = tkinter.Label()
image04_label = tkinter.Label()
image05_label = tkinter.Label()
image06_label = tkinter.Label()

image01_label.grid(row=0, column=0)
image01_label.grid(columnspan=2)
image01_label.grid(rowspan=2)

image02_label.grid(row=0, column=2)
image03_label.grid(row=1, column=2)
image04_label.grid(row=2, column=2)
image05_label.grid(row=2, column=1)
image06_label.grid(row=2, column=0)

	
def main():
	rootWindow.bind('<Escape>', close)
	rootWindow.bind('q', close)
	Timer(0, refreshCam01).start()
	Timer(0, refreshCam02).start()
	Timer(0, refreshCam03).start()
	Timer(0, refreshCam04).start()
	Timer(0, refreshCam05).start()
	Timer(0, refreshCam06).start()
	Timer(0, refreshCam07).start()
	Timer(0, refreshCam08).start()
	Timer(0, refreshCam09).start()


def refreshCam01():
	
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL01, timeout=4).content)).resize((int(RWidth/3*2),int(RHeight/3*2)), Image.ANTIALIAS))
		image01_label.configure(image=tmp_photo)
		image01_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(0.1, refreshCam01).start() # biger camera, slower download, refresh sooner

def refreshCam02():
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL02, timeout=4).content)).resize((int(RWidth/3),int(RHeight/3)), Image.ANTIALIAS))
		image02_label.configure(image=tmp_photo)
		image02_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(1, refreshCam02).start()
def refreshCam03():
	
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL03, timeout=4).content)).resize((int(RWidth/3),int(RHeight/3)), Image.ANTIALIAS))
		image03_label.configure(image=tmp_photo)
		image03_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(1, refreshCam03).start()
	
def refreshCam04():
	
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL04, timeout=4).content)).resize((int(RWidth/3),int(RHeight/3)), Image.ANTIALIAS))
		image04_label.configure(image=tmp_photo)
		image04_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(1, refreshCam04).start()
	
def refreshCam05():
	
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL05, timeout=4).content)).resize((int(RWidth/3),int(RHeight/3)), Image.ANTIALIAS))
		image05_label.configure(image=tmp_photo)
		image05_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(1, refreshCam05).start()
	
def refreshCam06():
	
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL06, timeout=4).content)).resize((int(RWidth/3),int(RHeight/3)), Image.ANTIALIAS))
		image06_label.configure(image=tmp_photo)
		image06_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(1, refreshCam06).start()
	
def refreshCam07():
	
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL07, timeout=4).content)).resize((int(RWidth/3),int(RHeight/3)), Image.ANTIALIAS))
		image07_label.configure(image=tmp_photo)
		image07_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(1, refreshCam07).start()
	
def refreshCam08():
	
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL08, timeout=4).content)).resize((int(RWidth/3),int(RHeight/3)), Image.ANTIALIAS))
		image08_label.configure(image=tmp_photo)
		image08_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(1, refreshCam08).start()
	
def refreshCam09():
	
	try:
		tmp_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(cameraURL09, timeout=4).content)).resize((int(RWidth/3),int(RHeight/3)), Image.ANTIALIAS))
		image09_label.configure(image=tmp_photo)
		image09_label.image = tmp_photo # keep a reference to prevent tkinter garbage collection
	except:
		pass
	if rootWindow.state() == 'normal': Timer(1, refreshCam09).start()

def close(event=None):
	os._exit(1)

# start the subprocess, main loop, and gui
if __name__ == '__main__':
	main()
	rootWindow.mainloop()
	
