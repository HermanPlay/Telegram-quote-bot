from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

size = 500
text_color = (0, 0, 0)
bg_color = (255, 251, 247)
font = ImageFont.truetype('arial.ttf', 15)

text = 'Zdanie wielokortnie zlozone zawiera w sobie wiele roznych slow w tym tez slowa mi nie znane'
copy_text = ''




new = Image.new('RGB',(size, size),color=bg_color)

draw = ImageDraw.Draw(new)
hello = draw.textbbox((10,10), 'Zdanie wielokortnie zlozone zawiera w sobie wiele roznych slow w tym tez slowa mi nie znane', font)
draw.text((10,10), text, fill=text_color, font=font, spacing=6)
print(hello)
new.show()
# for index, row in enumerate(text_rows):

#     d.text((10,10*index+10), ''.join(row), fill=text_color, font=font_arial, spacing=6)

# new.show()