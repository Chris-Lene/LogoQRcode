# coding=utf-8
"""
根据链接生成二维码，并在二维码中增添logo.
"""
from PIL import Image
import qrcode

yes=['yes','是','Yes','shi']

while True:
    qr = qrcode.QRCode(
        version=9,error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=30,border=4
        )

    http=input("请输入网站链接：")   
    qr.add_data(http)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")

    #logo"
    path_input = input("请输入Logo图片路径: ")
    icon = Image.open(path_input)

    img_w,img_h = img.size
    factor = 5
    size_w = img_w / factor
    size_h = img_h / factor

    icon_w,icon_h = icon.size
    
    if icon_w > icon_h:
        icon_h = int(icon_h/(icon_w/size_w))
        icon_w = int(size_w)       
    else:
        icon_w = int(icon_w/(icon_h/size_h))
        icon_h = int(size_h)

#解释    
    icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)

    w = int((img_w - icon_w)/2)
    h = int((img_h - icon_h)/2)
    icon = icon.convert("RGBA")
#解释
    img.paste(icon,(w,h),icon)
    #img.show()
    name_output=input("请输入文件名：")
    img.save('{}.png'.format(name_output))
    
    if input("是否继续？(yes or no): ") in yes:
        print('\n')
        continue
    else :
        print("\n谢谢使用，再见！\n")
        break

input("Press any key to exit.")