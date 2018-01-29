#!/bin/bash

USERNAME="admin"
PASSWORD="abc123"
ADDRESS="192.168.1.10:5000"

SID="null"
while [ $SID == "null" ]
do
	SID=$(curl -s --max-time 30 "http://$ADDRESS/webapi/auth.cgi?api=SYNO.API.Auth&method=Login&version=2&account=$USERNAME&passwd=$PASSWORD&session=SurveillanceStation&format=sid" | jq -r '.data.sid')
done

play_stream () {
	CAMERAID=$1
	POS=$2
	while true; do
		curl -s --max-time 30 "http://$ADDRESS/webapi/SurveillanceStation/videoStreaming.cgi?api=SYNO.SurveillanceStation.VideoStream&method=Open&version=1&cameraId=$CAMERAID&format=hls&_sid=$SID"
		livestreamer "hls://http://$ADDRESS/webapi/SurveillanceStation/videoStreaming.cgi?api=SYNO.SurveillanceStation.VideoStream&method=Stream&version=1&cameraId=$CAMERAID&format=hls&_sid=$SID" worst  --fifo --player "omxplayer --win $POS --timeout 30"
	done
}

play_stream 15 0,0,853,480 &
play_stream 22 853,0,1280,240 &
play_stream 23 853,240,1280,480 &
play_stream 24 0,480,426,720 &
play_stream 11 426,480,853,720 &
