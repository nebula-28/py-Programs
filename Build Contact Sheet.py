import PIL
from PIL import Image, ImageFont, ImageDraw 
from PIL import ImageColor
from PIL import ImageEnhance

# read image and convert to RGB
im=Image.open("readonly/msi_recruitment.gif").convert('RGB')
colorSet=[0.1,0.5,0.9]
resultSet=[]
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 60)
for i in range(0,3):
    for j in colorSet: 
        r, g, b = im.split()
        if i==0:
            r = r.point(lambda i: i * j)
            g = g.point(lambda i: i * 1)
            b = b.point(lambda i: i * 1)
            result = Image.merge('RGB', (r, g, b))
            rect = Image.new('RGB', (result.width, 80), color = (0, 0, 0))
            d = ImageDraw.Draw(rect)
            d.text((10,10), 'channel 0 intensity {}'.format(j), font = fnt, fill = result.getpixel((0, 50)))
            
            #display(sheet)
        elif i==1:
            r = r.point(lambda i: i * 1)
            g = g.point(lambda i: i * j)
            b = b.point(lambda i: i * 1)
            result = Image.merge('RGB', (r, g, b))
            rect = Image.new('RGB', (result.width, 80), color = (0, 0, 0))
            d = ImageDraw.Draw(rect)
            fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 70)
            d.text((10,10), 'channel 1 intensity {}'.format(j), font = fnt, fill = result.getpixel((0, 50)))
        else:
            r = r.point(lambda i: i * 1)
            g = g.point(lambda i: i * 1)
            b = b.point(lambda i: i * j)
            result = Image.merge('RGB', (r, g, b))
            rect = Image.new('RGB', (result.width, 80), color = (0, 0, 0))
            d = ImageDraw.Draw(rect)
            fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 70)
            d.text((10,10), 'channel 2 intensity {}'.format(j), font = fnt, fill = result.getpixel((0, 50)))
        sheet = PIL.Image.new(result.mode, (result.width, result.height + rect.height))
        sheet.paste(rect, (0, result.height))
        sheet.paste(result, (0, 0))
        resultSet.append(sheet)

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