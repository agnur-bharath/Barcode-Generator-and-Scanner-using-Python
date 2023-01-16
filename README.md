# Barcode-Generator-and-Scanner-using-Python

Libraries used : 1. barcode
                 2. datetime
                 3. opencv
                 4. pyzbar

This project is designed to maintain a wearhouse of grains.

The barcodegenerator.py program creates a barcode with the date and type of grain which has come to wearhouse in png format.

The generated barcode is of CODE39 type.

The barcodescanner.py program scans the barcode through camera and compares the date on the barcode with the date on which the scan has been taking place and displays how many days are still remaining for the expiry of the grain and if it crosees the expiry date then it displays that the grain has expired.
