# フォルダ内の画像を同一サイズのpngファイルに一斉変換
# https://note.nkmk.me/python-pillow-image-resize/ 　参考

import os
import glob
from PIL import Image, ImageFilter

ReSize = (408,408)  # サイズ指定

inFolder = 'd:/tmp/inImages/'    # 元画像入れてあるフォルダ
outFolder = 'd:/tmp/outImages/'   # 変換後の画像が入るフォルダ

files = glob.glob( inFolder +'*')

for f in files:
    try:
        img = Image.open(f)
        img_resize = img.resize(ReSize)
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        st=str(ReSize[0])+'x'+str(ReSize[1])
        img_resize.save(os.path.join(outFolder, basename + '_' + st +'.png'))
    except OSError as e:
        pass
