import cv2 as cv # import the nessecary package
#reading the image
Image=cv.imread('c:/Users/rssat/Downloads/Gemini_Generated_Image_vv8f44vv8f44vv8f (1).png')# reading the image along the path
cv.imshow('image',Image)# showing the image 

#reading the video
capture=cv.VideoCapture("c:/Users/rssat/OneDrive/Pictures\Camera Roll/Kantara_A_Legend_Chapter_1_(2025)_Kannada_HQ_PreDVD_-_720p_-(1).mkv")#capturing the video from the webcam

while True:
    istrue,frame=capture.read()
    cv.imshow('Video',frame) 
    if cv.waitKey(20) & 0xFF==ord('d'):
        break


    capture.release
    cv.destroyAllWindows

