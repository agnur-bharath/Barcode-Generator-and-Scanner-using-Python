import cv2
from pyzbar import pyzbar
from datetime import date
from datetime import datetime as dt
from datetime import timedelta
#extracting the date
CurrentDate=date.today()
print("Today's Date is ",CurrentDate)

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        #3
        with open("barcode_result.txt", mode ='w') as file:
            file.write(barcode_info)
        with open("barcode_result.txt", mode ='r') as file:
            data = file.read(10)
            print("Date on Barcode is ",data)
            print(len(data))
            
            Begindate = dt.strptime(str(data), "%Y-%m-%d").date()
            Enddate = Begindate + timedelta(days=30)
            d1 = dt.strptime(str(Enddate), "%Y-%m-%d").date()
            d2 = dt.strptime(str(CurrentDate), "%Y-%m-%d").date()
            ndate=d1-d2
            if(CurrentDate>Enddate):
                print("The grains are Expired\n")
            elif(CurrentDate<Enddate):
                print("Still",ndate,"days are remaining to Expire\n")
            else:
                print("Today is the expiring date\n")
                      
    return frame


def main():
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()
#4
if __name__ == '__main__':
    main()
