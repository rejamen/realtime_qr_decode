# import the necessary packages
from datetime import datetime
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2
import psycopg2


# testing connection with DB
cursor = None
conn = None
# save to DB if different code.
# If the same code detected then it must be
# in different datetime.
last_login = last_code = None

try:
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        database='aidooit',
        user='postgres',
        password='postgres'
    )
    print('Database Connection success!!!')
    cursor = conn.cursor()
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

# initialize the video stream and allow the camera sensor to warm up
# loop over the frames from the video stream
# only when connection success
if conn:
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    # vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)
    while True:
        # grab the frame from the threaded video stream and resize it to
        # have a maximum width of 400 pixels
        text = 'None'
        frame = vs.read()

        frame = imutils.resize(frame, width=400)

        # find the barcodes in the frame and decode each of the barcodes
        barcodes = pyzbar.decode(frame)
        # loop over the detected barcodes
        for barcode in barcodes:
            # extract the bounding box location of the barcode and draw
            # the bounding box surrounding the barcode on the image
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # the barcode data is a bytes object so if we want to draw it
            # on our output image we need to convert it to a string first
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type

            # draw the barcode data and barcode type on the image
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(frame, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # save it to DB
            insert_query = '''INSERT INTO login_data(code, login_date) VALUES (%s,%s)'''

            # date checking
            dt_fm = '%Y-%m-%d %H:%M:%S'
            now = datetime.now()
            now_db = datetime.strftime(now, dt_fm)  # adjust to save to DB

            if last_login:
                seconds = (now - last_login).total_seconds()
                if barcodeData == last_code:
                    if seconds >= 60:
                        # the same QR code can only be saved
                        # every 1 minute
                        values = (barcodeData, now_db)
                        cursor.execute(insert_query, values)
                        conn.commit()
                        last_login = now
                else:
                    values = (barcodeData, now_db)
                    cursor.execute(insert_query, values)
                    conn.commit()
                    last_login = now
                    last_code = barcodeData
            else:  # first time login
                values = (barcodeData, now_db)
                cursor.execute(insert_query, values)
                conn.commit()
                last_login = now
                last_code = barcodeData

        cv2.imshow("Frame", frame)
        print(text)
        key = cv2.waitKey(1) & 0xFF
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
