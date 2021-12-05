import cv2

def image_to_cartoon(path):

    ''' A program that imitates Cel-Shading technology used in video games '''

    base_image = cv2.imread(path)

    gray = cv2.cvtColor(base_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)
    edge = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 255, 18)

    color = cv2.bilateralFilter(base_image, 15, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edge)

    cv2.imwrite('Cartoon.jpg', cartoon)

image_to_cartoon('test.jpg')