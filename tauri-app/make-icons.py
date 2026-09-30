# 由 tauri-app/icon.png（1024x1024）生成 Tauri 需要的图标：
#   icons/32x32.png, icons/128x128.png, icons/icon.png, icons/icon.ico, icons/icon.icns
# 说明：正式全套图标建议用 `npx tauri icon icon.png -o src-tauri/icons` 生成；
#       本脚本是不依赖 npm 的备用方案（其中 icns 由 Pillow 写出）。
# 用法：C:/Python314/python.exe tauri-app/make-icons.py
from PIL import Image
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'icon.png')
OUT = os.path.join(HERE, 'src-tauri', 'icons')
os.makedirs(OUT, exist_ok=True)

img = Image.open(SRC).convert('RGBA')
img.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, 'icon.png'))
img.resize((128, 128), Image.LANCZOS).save(os.path.join(OUT, '128x128.png'))
img.resize((32, 32), Image.LANCZOS).save(os.path.join(OUT, '32x32.png'))

# ICO 内嵌多尺寸 PNG（Vista+ 格式）
img.save(os.path.join(OUT, 'icon.ico'),
         sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print('icons ->', OUT)
for f in sorted(os.listdir(OUT)):
    print('  ', f, os.path.getsize(os.path.join(OUT, f)), 'bytes')
