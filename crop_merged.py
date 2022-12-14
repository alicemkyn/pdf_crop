from PyPDF2 import PdfFileReader, PdfFileWriter

reader = PdfFileReader('/dest/merged.pdf','r') #from merged Pdf File 

# returns the points(pt) 1 inch = 72pt and 1 inch = 2.54 cm
''' 
page = reader.getPage(5)
print(page.cropBox.getLowerLeft()) 
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())
print(page.cropBox.getLowerRight())
'''
writer = PdfFileWriter()
for i in range(reader.getNumPages()):
    page = reader.getPage(i)
    page.cropBox.setLowerLeft((15,50))
    page.cropBox.setUpperLeft((15,842))
    page.cropBox.setLowerRight((580,50))
    page.cropBox.setUpperRight((580,842))
    writer.addPage(page) 
    
# to merged pdf file
outstream = open("/home/user/Desktop/cropped.pdf","wb")
writer.write(outstream)
outstream.close()