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




size = 500
text_color = (0, 0, 0)
bg_color = (255, 251, 247)

font_arial = ImageFont.truetype('arial.ttf', 14)

text = '''Якщо потребуєте тимчасового розміщення, харчування слід звертатися до приймальних пунктів, які знаходяться у прикордонній зоні та у містах Польщі. Вони розташовані на всіх пунктах перетину українсько-польського кордону та вокзалах (dworzec). Як правило, інформаційні афіші про такі пункти виконані на тлі кольорів українського прапора і його назва зазначена українською та польською мовами. У таких пунктах Вас можуть направити до Центрів з прийняття українців у потребі, де Вам нададуть можливість перепочити, їжу, можливість заночувати у теплому місці (на добу або більший строк). Їх перелік знаходиться тут https://www.gov.pl/web/ua/-2. Звертаємо увагу, що цей перелік не є вичерпний. ЇХ може бути більше за рахунок пунктів відкритих владою міст. Про них Ви можете дізнатися на офіційному сайті такого міста (як правило, сайт міста виглядає так: «назва міста».pl).'''



new = Image.new('RGB',(size, size),color=bg_color)

d = ImageDraw.Draw(new)
for index, row in enumerate(temp_result):

    d.text((10,209*index+10), ''.join(row), fill=text_color, font=font_arial, spacing=6)

new.show()