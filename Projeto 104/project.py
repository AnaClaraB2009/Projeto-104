import cv2

img = cv2.imread ("solar-system.jpg")

cv2.putText(img,
            "Sol",
            (40,80),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))

cv2.putText(img,
            "Mercurio",
            (60,120),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (160,160),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))

cv2.putText(img,
            "Terra",
            (250,100),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))

cv2.putText(img,
            "Marte"
            ,
            (360,160),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (520,60),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))

cv2.putText(img,
            "Saturno",
            (720,100),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))

cv2.putText(img,
            "Urano",
            (920,120),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))

cv2.putText(img,
            "Netuno",
            (1080,120),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))

cv2.imshow("resultado", img)

cv2.waitKey(0)

