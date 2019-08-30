# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2
import psycopg2


# testing connection with DB
'''try:
    conn = psycopg2.connect(host = "localhost",
                            port = "5432",
                            database = "aidooit_login",
                            user = "postgres",
                            password = "postgres")
    print('Connection success!!!')
except (Exception, psycopg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)'''

# initialize the video stream and allow the camera sensor to warm up
# loop over the frames from the video stream
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

    cv2.imshow("Frame", frame)
    print(text)
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
