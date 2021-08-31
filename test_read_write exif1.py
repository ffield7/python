import pyexiv2
import glob
for name in glob.glob('./*.jpg'):
    img = pyexiv2.Image(name)
    metadata = img.read_exif()
    str1=name.split('_')[1]
    str2=str1[0:4]+':'+str1[4:6]+':'+str1[6:8]+' '+str1[9:11]+':'+str1[11:13]+':'+str1[13:15]
    print(str2)
    dict1 = {'Exif.Image.DateTime': str2}
    img.modify_exif(dict1)
    img.close()
