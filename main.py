from PIL import Image, ImageDraw,ImageFont
print('генератор мемов запущен')
top_text = input('ведите верхний текст ')
bottom_text = input('ведите нижний текст ')
print(top_text,bottom_text)
print('список картинок')
print('1.кот открыл банку')
print('2.кот переел валерьянки')
img_num = int(input('ведите номер картинки '))
if img_num == 1:
    img_file = 'cat1.jpg'
elif img_num == 2:
    img_file = "cat.jpg"
img = Image.open(img_file)
width,height = img.size
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf',size=100)
text = draw.textbbox((0,0),top_text,font)
draw.text(((width - text[2]) / 2, 10), top_text,font = font,fill="white")
text = draw.textbbox((0,0),bottom_text,font)
draw.text(((width - text[2]) / 2, height - text[3] - 10), bottom_text,font = font,fill="white")
img.save('mem.jpg')