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

def split_text_in_rows(text, screen):  # Takes one long string for one page

    copy_text = ''
    final_row = ''
    rows = []

    text_list = text.split(' ')

    for i in text_list:
        copy_text += (i + ' ') 
        if check_length(copy_text, screen):
            final_row += (i + ' ')
        else:
            rows.append(final_row)
            copy_text = i + ' '
            final_row = i + ' '

    if final_row:
        rows.append(final_row)

    text = '\n'.join(rows)        
    return text  # Returns string for one photo

side_length = 500
text_color = (0, 0, 0)
bg_color = (255, 251, 247)
font = ImageFont.truetype('arial.ttf', 14)

def draw_image(text):
    
    new = Image.new('RGB',(side_length, side_length),color=bg_color)

    d = ImageDraw.Draw(new)

    d.multiline_text((10,10), split_text_in_rows(text, d), fill=text_color, font=font)

    new.show()