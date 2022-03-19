from copy import copy
from typing import final
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def check_length(text, screen):  # First argument is string. Second is draw object, on which we put text
    global font  # Will be resolved if done in OOP
    global side_length  # Will be resolved if done in OOP
    size = screen.textsize(text, font)
    if size[0] > side_length - 15:
        return False
    return True

side_length = 500
text_color = (0, 0, 0)
bg_color = (255, 251, 247)
font = ImageFont.truetype('arial.ttf', 15)



new = Image.new('RGB',(side_length, side_length),color=bg_color)

draw = ImageDraw.Draw(new)

text = 'Zdanie wielokortnie zlozone zawiera w sobie wiele roznych slow w tym tez slog g g g g g g g g g g g gg g g gg g g  g wa mi nie znane. Ja kocham kingusie najbardziej na swiecei i nic nie zmieni mojego zdania nigdy.'
copy_text = ''
final_row = ''
rows = []

text_list = text.split(' ')

for i in text_list:
    copy_text += (i + ' ') 
    if check_length(copy_text, draw):
        final_row += (i + ' ')
    else:
        rows.append(final_row)
        copy_text = i + ' '
        final_row = i + ' '

if final_row:
    rows.append(final_row)

text = '\n'.join(rows)        

draw.multiline_text((10,10), text, fill=text_color, font=font)
new.show()
# for index, row in enumerate(text_rows):

#     d.text((10,10*index+10), ''.join(row), fill=text_color, font=font_arial, spacing=6)

# new.show()