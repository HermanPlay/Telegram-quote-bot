text = '''1 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok 2 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok 3 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok 4 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok 5 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok 6 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok 7 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok 8 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok 9 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok 10 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok 11 linijka zawiera w sobie rozne slowa ktore nie mozna rozdzielic ok ostatnia linijka ma.
'''

temp = ''
result = ''
temp_result = []
bool_variable = False
line_counter = 0
for index, char in enumerate(text):

    if index % 758 != 0 or index == 0:

        if bool_variable:

            bool_variable = False
            continue

        elif index % 67 == 0 and index != 0:

            result += temp
            line_counter += 1

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

print(temp_result)