import re
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


size = 500
text_color = (0, 0, 0)
bg_color = (255, 251, 247)

font_arial = ImageFont.truetype('arial.ttf', 14)

text = '''Якщо потребуєте тимчасового розміщення, харчування слід звертатися до приймальних пунктів, які знаходяться у прикордонній зоні та у містах Польщі. Вони розташовані на всіх пунктах перетину українсько-польського кордону та вокзалах (dworzec). Як правило, інформаційні афіші про такі пункти виконані на тлі кольорів українського прапора і його назва зазначена українською та польською мовами. У таких пунктах Вас можуть направити до Центрів з прийняття українців у потребі, де Вам нададуть можливість перепочити, їжу, можливість заночувати у теплому місці (на добу або більший строк). Їх перелік знаходиться тут https://www.gov.pl/web/ua/-2. Звертаємо увагу, що цей перелік не є вичерпний. ЇХ може бути більше за рахунок пунктів відкритих владою міст. Про них Ви можете дізнатися на офіційному сайті такого міста (як правило, сайт міста виглядає так: «назва міста».pl).'''

temp = ''
result = ''
temp_result = []
bool_variable = False
for index, char in enumerate(text):

    if index % 758 != 0 or index == 0:

        if bool_variable:

            bool_variable = False
            continue

        elif index % 67 == 0 and index != 0:

            result += temp

            if text[index+1] == ' ':
                print(text[index+1])

                bool_variable = True

            result += '\n'
            temp = '' + char

        else:

            temp += char
        
        if index == len(text) - 1:
            result += temp
            temp_result.append(result)

    else:
        temp_result.append(result)
        result = ''
        temp = ''

text = result

new = Image.new('RGB',(size, size),color=bg_color)

d = ImageDraw.Draw(new)
for index, row in enumerate(temp_result):

    d.text((10,209*index+10), ''.join(row), fill=text_color, font=font_arial, spacing=6)

new.show()