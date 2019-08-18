# Realtime QR Code decoder
> lets play with QR codes

This project is about decode QR Codes in realtime using pyzbar and OpenCV.
You have to call qr_decode_video.py and you will see the video recorded from your camera (tested in MacOS Mojave). When a QR Code is detected it will be surrounded in red and the code printed in console.

It needs OpenCV and imutils. We suggest to use python virtual envs. Steps are given below. 

This project was possible thanks to Adrian at pyImageSearch (https://www.pyimagesearch.com) 

## Getting started

```shell
git clone https://github.com/rejamen/realtime_qr_decode.git
cd realtime_qr_decode
python qr_decode_video.py
```

## Using virtual envs

```shell
pip install virtualenv virtualenvwrapper (to install virtualenv)
virtualenv venv (create venv)
source /bin/activate (to activate it)
'Once in venv'
(venv) pip install opencv-contrib-python
(venv) pip install imutils
```

You will see a window with QRCode surrounded in red (if found) and data decoded in terminal.
