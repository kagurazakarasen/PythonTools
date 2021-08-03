# Usage:　python3 resizeimgs.py <riseze.csv> in_image.png
# 　　　　イメージをresize.csv の内容に合わせてリサイズする。結果はimage_x_y.pngとして保存
#

from PIL import Image, ImageFilter
import csv
import sys

ImgFileName = 'test.png'
CsvFileName = 'test.csv'

#print(len(sys.argv))

if(len(sys.argv)==1):
    print('Usage: > python3 resizeImgs.py risezeXY.csv inImage.png')
    sys.exit()

if(len(sys.argv)>1):
    CsvFileName = sys.argv[1]

if(len(sys.argv)>2):
    ImgFileName = sys.argv[2]

print('CSV FILE:',CsvFileName)
with open(CsvFileName) as f:
    r = csv.reader(f)
    # next(r) # 見出し行を飛ばす
    size_tuple=[tuple(map(int,line)) for line in r] # lineの各要素の文字列をintに変換してtupleにする

print(size_tuple)

#print(size_tuple[0])


print('In Image FILE:',ImgFileName)
im = Image.open(ImgFileName)

for siz in size_tuple:
    print(siz)
    img_resize = im.resize(siz)
    st=str(siz[0])+'x'+str(siz[1])
    outFile = ImgFileName[:-4]  + st +'.png'
    print(outFile)
    img_resize.save(outFile)

