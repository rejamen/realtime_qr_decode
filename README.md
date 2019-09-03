# Realtime QR Code decoder
> lets play with QR codes

This project is about decode QR Codes in realtime using pyzbar and OpenCV.
You have to call qr_decode_video.py and you will see the video recorded from your camera (tested in MacOS Mojave). When a QR Code is detected it will be surrounded in red and the code saved to a postgres database.

It has a docker ready configuration, so you do not need to install anything but Docker and Docker Compose into your computer.

The decoding was possible thanks to Adrian at pyImageSearch (https://www.pyimagesearch.com)

## Getting started

```shell
git clone https://github.com/rejamen/realtime_qr_decode.git
cd realtime_qr_decode
docker-compose up -d
```

You will see a window with QRCode surrounded in red (if found). Everytime a new QR Code is decoded, it is saved into the aidooit_login database.

## Database specs

When 'docker-compose up -d' its done, a PostgreSQL container is created and automatically creates the aidooit_login database with the login_data table. This table has the following columns:
 - id: Records ID
 - code: QR Code content
 - login_date: Datetime when the record was saved to DB

## How it works?

The same QR Code will be store on database only every 1 minutes. Different QR codes can be store no matter time.

## Using venvs

Unfortunately, its not possible to record video on Mac from inside a Docker container (if it does please let me know). That's why I had to use venv to install pyzbar and OpenCV and run the code. Just pip install requirements.txt in your venv.
