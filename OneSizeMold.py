# フォルダ内の画像を同一サイズのpngファイルに一斉変換
import glob
from PIL import Image, ImageFilter

ReSize = (350,350)  # サイズ指定

Folder = 'd:/tmp/tmp/'

# jpgファイルをpng化    ※ただpngに変換して保存するだけ
files = glob.glob(Folder+ "*.jpg")
for file in files:
    print(file)
    im = Image.open(file)
    pngFile = file[:-4]+'.png'
    im.save(pngFile)

files = glob.glob(Folder+ "*.png")
for file in files:
    print(file)


