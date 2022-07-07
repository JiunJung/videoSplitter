import cv2
import os

def video_splitter(filename,foldername):

    videoname = filename.split("/")[-1].split(".")[0] # 경로와 확장자를 제외한 비디오의 이름.
    create_path = os.path.join(foldername,videoname) # 캡쳐 이미지를 생성할 디렉토리.
    try:
        if not os.path.exists(create_path):
            os.makedirs(create_path)
    except OSError:
        print(f"videoname : {videoname}")
        print(f"error : can't make {create_path}") #오류가 발생했을 때 처리

    cap = cv2.VideoCapture(filename) # 지정한 경로에 해당하는 비디오를 불러옴.
    i = 0 # 캡쳐된 이미지에 부여될 번호(이미지 파일명).
    # count = 0 # 캡쳐될 이미지 수를 제어하기 위함.

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret == False:
            break

        #if count % 14 == 0 :
        cv2.imwrite(os.path.join(create_path , str(i)+'.jpg') , frame) # 각 프레임을 지정된 경로에 저장
        i += 1
        # count += 1
  
    cap.release()
    cv2.destroyAllWindows()