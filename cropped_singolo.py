from PyPDF2 import PdfFileWriter, PdfFileReader
import os 

dest1 = os.listdir("/dest1/")
dest2 = os.listdir("/dest2/")
dest3 = os.listdir("/dest3/")
dest4 = os.listdir("/dest4/")
base = "/home/user/Desktop/folder/"

# specific x,y coordinates(pt) to remove watermark of CS
def fonk(folder_name,i):
    reader = PdfFileReader(base+folder_name+i)
    writer = PdfFileWriter()
    page = reader.getPage(0)
    page.cropBox.setLowerLeft((15,50))
    page.cropBox.setUpperLeft((15,842))
    page.cropBox.setLowerRight((580,50))
    page.cropBox.setUpperRight((580,842))
    writer.addPage(page)
    outstream = open(f"{base}{folder_name}c_{i}","wb")
    writer.write(outstream)
    outstream.close()
    

for i in dest1:
    fonk("dest1/",i)

for i in dest2:
    fonk("dest2/",i)

for i in dest3:
    fonk("dest3/",i)

for i in dest4:
    fonk("dest4/",i)
