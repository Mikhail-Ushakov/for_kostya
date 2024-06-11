import random
def game():
    progress=True
    word=['стол','арбуз','фактор']
    lifes=3
    word_in_play=get_word(word)  
    template=start_template(word_in_play)
    welcome_speech(template)

    while progress:
        user_guess=input('Введите букву')
        template=build_template(template, word_in_play, user_guess)
        print(template)
        progress=check_win(template)
        if user_guess not in word_in_play:
            lifes -= 1
            print(f"К сожалению вы не угади, у вас осталось{lifes} попытки!")
        if lifes == 0:
            print("Вы проиграли!")
            break
        if not progress:
            print("Вы победили!") 

def welcome_speech(t):
    print(f'''Загаданное слово состоит из {len(t)} букв {t}''')

def get_word(w):
    return random.choice(w)

def start_template(w):
    return len(w)*'_'

def build_template(t,w,g=''):
    t=list(t)
    for i in range(len(w)):
        if t[i] == '_':
            if w[i] == g:
                t[i] = w[i]
            else:
                t[i] = '_'
    return t

def check_win(t):
    if '_' in t :
        return True
    else:
        return False

game()

