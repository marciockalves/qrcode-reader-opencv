import cv2

from app.screen_capture import screen_capture


def main():

    screen_capture()

    img = cv2.imread("./app/img.png")

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    decode = cv2.QRCodeDetector()

    retval, decoded_info, points, straight_qrcode = decode.detectAndDecodeMulti(img)

    print(decoded_info)


if __name__ == "__main__":
    main()

