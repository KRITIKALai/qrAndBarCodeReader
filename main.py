import cv2
import numpy as np
from pyzbar.pyzbar import decode
import ids

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    if success:
        for info in decode(img):
            data = info.data.decode('utf-8')
            if data in ids.valid_ids:
                message = "Authorized"
                color = (0, 255, 0)
            else:
                message = "Un-Authorized"
                color = (0, 0, 255)

            pts_image = np.array([info.polygon], np.int32)
            pts_image = pts_image.reshape((-1, 1, 2))
            cv2.polylines(img, [pts_image], True, color, 5)
            pts_text = info.rect
            cv2.putText(img, message, (pts_text[0], pts_text[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        key = cv2.waitKey(2)
        if key == ord('q'):
            break

        cv2.imshow('Frame', img)

    else:
        break

cap.release()
cv2.destroyAllWindows()