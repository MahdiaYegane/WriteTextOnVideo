#write text on video
import cv2 as cv

cap=cv.VideoCapture("E://OpenCV_videos/01.mp4")

while(True):
    ret,frame=cap.read()
    
    #use puttext() method to write text
    cv.putText(frame,"text : maryam mirzakhni",(30,30),cv.FONT_HERSHEY_SIMPLEX,
               0.8,(250,241,23),1,cv.LINE_4)
    
    #disply result
    cv.imshow("video",frame)
    
    #quit button
    if cv.waitKey(1) & 0xFF==ord('a'):
        break
    
#release the cap
cap.release()
cv.destroyAllWindows()


