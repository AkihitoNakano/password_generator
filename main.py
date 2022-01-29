import random, string
import secrets
from datetime import datetime

number_of_digits = 12

def gen_password(number_of_digits: int) -> str:
    l, u, d, p = divide_area(number_of_digits)
    lower_text = [secrets.choice(string.ascii_lowercase) for i in range(l)]
    upper_text = [secrets.choice(string.ascii_uppercase) for i in range(u)]
    digit = [secrets.choice(string.digits) for i in range(d)]
    punctuation = [secrets.choice('_-') for i in range(p)]

    word_list = lower_text + upper_text + digit + punctuation
    random.shuffle(word_list)

    password =  "".join(word_list)
    print(password)
    return password


def divide_area(num: int) -> int:
    l = num // 2
    u = l // 2
    d = u // 2
    p = num - (l+u+d)

    _ = random.randint(0,2)
    if _ == 1:
        u, d, p = d, p, u
    elif _ == 2:
        u, d, p = p, u, d
    return (l,u,d,p)

def save_pass(password):
    today = datetime.now()
    with open('secrets.txt', mode='a') as f:
        f.writelines(f'\n\n{today}')
        f.writelines(f'\n{password}')


if __name__ == "__main__":
    p = gen_password(number_of_digits)
    save_pass(p)


'''
print('ascii_lowercase: ' + string.ascii_lowercase)
print('ascii_lowercase: ' + string.ascii_uppercase)
print('ascii_letters: ' + string.ascii_letters)
print('digits: ' + string.digits)
print('punctuation: ' + string.punctuation)
print(len(string.ascii_letters))
'''
