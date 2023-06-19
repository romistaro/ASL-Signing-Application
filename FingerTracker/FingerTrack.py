import cv2
import time
import os

import FingerTracker.TrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "ASL"
myList = os.listdir("ASL")
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

pTime = 0

detector = htm.handDetector(detectionCon=1)

tipIds = [4, 8, 12, 16, 20]

score = 0
total_letters = 5
current_letter = 0
show_timer = time.time()
show_duration = 5  # Adjust this value to change the duration to display each letter (in seconds)

while True:
    success, img = cap.read()

    img = detector.findHands(img)

    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 3][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        totalFingers = fingers.count(1)

        
        if current_letter < total_letters:
            current_overlay = overlayList[current_letter]
            current_letter_name = chr(ord('A') + current_letter)
            cv2.putText(img, "Show: " + current_letter_name, (45, 375), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            
            if fingers == [1, 0, 0, 0, 0] and lmList[1][2] > lmList[0][2]:
                if current_letter == 2:
                    cv2.putText(img, "Correct!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                    score += 1
                    current_letter += 1
                    show_timer = time.time()
                else:  
                    cv2.putText(img, "Incorrect!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            elif fingers == [0, 1, 1, 1, 1]:
                if current_letter == 1:
                    cv2.putText(img, "Correct!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                    score += 1
                    current_letter += 1
                    show_timer = time.time()
                else:
                    cv2.putText(img, "Incorrect!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                
            elif fingers == [0, 1, 0, 0, 0]:
                if current_letter == 3:
                    cv2.putText(img, "Correct!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                    score += 1
                    current_letter += 1
                    show_timer = time.time()
                else:
                    cv2.putText(img, "Incorrect!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            elif fingers == [0, 0, 0, 0, 0] and lmList[12][2] > lmList[4][2]:
                if current_letter == 0:
                    cv2.putText(img, "Correct!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                    score += 1
                    current_letter += 1
                    show_timer = time.time()
                else:
                    cv2.putText(img, "Incorrect!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            elif fingers == [0, 0, 0, 0, 0]:
                if current_letter == 4:
                    cv2.putText(img, "Correct!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                    score += 1
                    current_letter += 1
                    show_timer = time.time()
                else:
                    cv2.putText(img, "Incorrect!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:   
                if time.time() - show_timer > show_duration:
                    cv2.putText(img, "Incorrect!", (45, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                    current_letter += 1
                    show_timer = time.time()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow("Image", img)

    # Check for user input to quit
    key = cv2.waitKey(1)
    if key == ord('q') or current_letter == total_letters:
        break

cap.release()
cv2.destroyAllWindows()


with open("score.txt", "w") as file:
    file.write(f"{score}")