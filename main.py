from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pkg_resources import WorkingSet

font_arial = ImageFont.truetype('arial.ttf', 12)

text = input('Give text: ').split()

word_counter = 0
temp = []
result = []
for i in text:
    if word_counter % 5 != 0 or word_counter == 0:
        temp.append(i)
    else:
        result.append(temp)
        temp = []
    word_counter += 1
try:
    print(result)
    result.pop()
    print(result)
except IndexError:
    pass
finally:
    result.append(temp)
    


new = Image.new('RGB',(300,300),color=(0, 0, 0))

d = ImageDraw.Draw(new)

for index, row in enumerate(result):
    text = ' '.join(row)
    d.text((10,15*(index+1)), text, fill=(255, 255, 255), font=font_arial)

new.show()