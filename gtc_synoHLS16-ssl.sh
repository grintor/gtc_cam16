#!/bin/bash

USERNAME="admin"
PASSWORD="abc123"
ADDRESS="192.168.0.1:5001"

SID="null"


while [ $SID == "null" ]
do
	SID=$(curl -s -k --max-time 30 "https://$ADDRESS/webapi/auth.cgi?api=SYNO.API.Auth&method=Login&version=2&account=$USERNAME&passwd=$PASSWORD&session=SurveillanceStation&format=sid" | jq -r '.data.sid')
done

play_stream () {
	CAMERAID=$1
	POS=$2
	while true; do
		curl -s -k --max-time 30 "https://$ADDRESS/webapi/SurveillanceStation/videoStreaming.cgi?api=SYNO.SurveillanceStation.VideoStream&method=Open&version=1&cameraId=$CAMERAID&format=hls&_sid=$SID"
		livestreamer --http-no-ssl-verify "hls://https://$ADDRESS/webapi/SurveillanceStation/videoStreaming.cgi?api=SYNO.SurveillanceStation.VideoStream&method=Stream&version=1&cameraId=$CAMERAID&format=hls&_sid=$SID" worst  --fifo --player "omxplayer --win $POS --timeout 30"
	done
}

play_stream 5 0,0,320,180 &
play_stream 6 0,180,320,360 &
play_stream 3 0,360,320,540 &
play_stream 4 0,540,320,720 &

play_stream 7 320,0,640,180 &
play_stream 8 320,180,640,360 &
play_stream 9 320,360,640,540 &
play_stream 10 320,540,640,720 &

play_stream 11 640,0,960,180 &
play_stream 12 640,180,960,360 &
play_stream 13 640,360,960,540 &
play_stream 14 640,540,960,720 &

play_stream 15 960,0,1280,180 &
play_stream 16 960,180,1280,360 &
play_stream 17 960,360,1280,540 &
play_stream 19 960,540,1280,720 &
