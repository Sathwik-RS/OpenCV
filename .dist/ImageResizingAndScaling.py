import cv2 as cv

def image_Resized(frame,scale=0.3):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)

    dimensions=(height,width)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture("c:/Users/rssat/OneDrive/Pictures\Camera Roll/Kantara_A_Legend_Chapter_1_(2025)_Kannada_HQ_PreDVD_-_720p_-(1).mkv")
while True:
    isTrue,frames=capture.read()

    cv.imshow('Video',image_Resized(frames))
    
    if cv.waitKey(20) & 0xFF==ord('d')  :
        break


    capture.release
    cv.destroyAllWindows


