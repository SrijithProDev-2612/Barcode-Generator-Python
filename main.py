from barcode import EAN13
from barcode.writer import ImageWriter
import random

inputnbr = input("Enter 12 digit number: ")
barcodename = input("Enter the name in which i need to save your Barcode: ")

Barcode = EAN13(str(inputnbr) , writer = ImageWriter())

Barcode.save(barcodename)
print("Barcode Saved.....")
