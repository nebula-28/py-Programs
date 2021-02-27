First, the rows are changed by color channel, where 
the top is the red channel, 
the middle is the green channel, and 
the bottom is the blue channel. 
Wait, why dont the colors look more red, green, and blue, in that order? Because the change you to be making is the ratio, or intensity, or that channel, in relationship to the other channels. 
Were going to use three different intensities, 
0.1 (reduce the channel a lot), 0.5 (reduce the channel in half), and 0.9 (reduce the channel only a little bit).
0.9------->0.5------->0.1
For instance, a pixel represented as (200, 100, 50) is a sort of burnt orange color. 
So the top row of changes would create three alternative pixels, 
varying the first channel (red). one at (20, 100, 50), one at (100, 100, 50), and one at (180, 100, 50). 
The next row would vary the second channel (blue), and would create pixels of color values (200, 10, 50), (200, 50, 50) and (200, 90, 50).

Note: A font is included for your usage if you would like! It's located in the file readonly/fanwood-webfont.ttf


import PIL
from PIL import Image, ImageFont, ImageDraw 
from PIL import ImageColor
from PIL import ImageEnhance

# read image and convert to RGB
im=Image.open("readonly/msi_recruitment.gif").convert('RGB')


colorSet=[0.1,0.5,0.9]
resultSet=[]
for i in range(0,3):
    for j in colorSet: 
        r, g, b = im.split()
        if i==0:
            r = r.point(lambda i: i * j)
            g = g.point(lambda i: i * 1)
            b = b.point(lambda i: i * 1)
            result = Image.merge('RGB', (r, g, b))
            resultSet.append(result)
            d = ImageDraw.Draw(result) 
            #d.text((im.width/2,im.height/2), "Hello World", fill=(255,255,0)) 
            d.text((0,im.height-20), "Hello World", fill=(255,255,0)) 
            display(d)
        elif i==1:
            r = r.point(lambda i: i * 1)
            g = g.point(lambda i: i * j)
            b = b.point(lambda i: i * 1)
            result = Image.merge('RGB', (r, g, b))
            resultSet.append(result)
        else:
            r = r.point(lambda i: i * 1)
            g = g.point(lambda i: i * 1)
            b = b.point(lambda i: i * j)
            result = Image.merge('RGB', (r, g, b))
            resultSet.append(result)


# create a contact sheet
first=resultSet[0]
contact_sheet=PIL.Image.new(first.mode, (first.width*3,first.height*3))
x=0
y=0
for img in resultSet:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    if x+first.width == contact_sheet.width:
        x=0
        y=y+first.height
    else:
        x=x+first.width
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)