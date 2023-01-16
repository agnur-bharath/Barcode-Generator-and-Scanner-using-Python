#import the barcode
import barcode

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter
#importing date
from datetime import date
#extracting the date
CurrentDate=date.today()
print(CurrentDate)
opt=input("Enter The Type Of Grain:")
SCurrentDate=(str(CurrentDate))+opt
#using code 39 and making the image
sample_barcode=barcode.get('code39',SCurrentDate,writer=ImageWriter())
filename=sample_barcode.save('barcode')
