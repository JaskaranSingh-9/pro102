import cv2,dropbox,time,random

startTime=time.time()

def snap_shot():
    number=random.randint(0,100)
    snapshot=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=snapshot.read()
        img="img"+str(number)+".png"
        cv2.imwrite(img,frame)
        startTime=time.time()
        result=False
    return img
    snapshot.release()
    cv2.destroyAllWindows()

def upload_img(img):
    access_token="V1EUCsib7XUAAAAAAAAAAZ8hL9nOL0VjvHebBkJapLGOt7kk_WVvMiVdH4IEQDJB"
    fileFrom=img
    fileTo="/jaskaran/"+img
    dbx=dropbox.Dropbox(access_token)
    with open(fileFrom,"rb") as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)

def main():
    while(True):
        if((time.time()-startTime)>=300):
            name=snap_shot()
            upload_img(name)

main()
