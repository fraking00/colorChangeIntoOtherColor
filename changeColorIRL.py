import numpy as np
import cv2 as cv 

cap = cv.VideoCapture(0)

print("chose your hsv color range to create your green screen \n")
print("red-scale: low(155,25,0),up(179,255,255) \n")
print("yellow-scale: low(20, 100, 100), up(30, 255, 255)\n")
print("blue-scale: low(78, 158, 124), up(138, 255,255)\n")
print("this are example of colors but you can choose which color you want")

color_low1 = int(input('color lower first position (coordinate): '))
color_low2 = int(input('color lower second position (coordinate): '))
color_low3 = int(input('color lower third position (coordinate): '))

color_up1 = int(input('color upper first position (coordinate): '))
color_up2 = int(input('color upper second position (coordinate): '))
color_up3 = int(input('color upper third position (coordinate): '))

print("\n and in what color also hsv do you what it")

color_des1 = int(input('color desired first position (coordinate): '))
color_des2 = int(input('color desired second position (coordinate): '))
color_des3 = int(input('color desired third position (coordinate): '))

print("press q to exit")

while True:
    ret, frame = cap.read()
    result = frame.copy()
    frame2 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower = np.array([color_low1,color_low2,color_low3])
    upper = np.array([color_up1,color_up2,color_up3])
    mask = cv.inRange(frame2, lower, upper)
    result = cv.bitwise_or(result, result, mask=mask)

    for i in zip(*np.where(frame == result)):
                frame[i[0], i[1], 0] = color_des1
                frame[i[0], i[1], 1] = color_des2
                frame[i[0], i[1], 2] = color_des3

    cv.imshow('frame', frame)
    cv.imshow('result', result)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
