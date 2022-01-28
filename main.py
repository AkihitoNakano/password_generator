import random, string

number_of_digits = 12

def gen_password(number_of_digits: int):
    l, u, d, p = divide_area(number_of_digits)
    print(l, u, d, p)
    lower_text = [pick_one(string.ascii_lowercase) for i in range(l)]
    upper_text = [pick_one(string.ascii_uppercase) for i in range(u)]
    digit = [pick_one(string.digits) for i in range(d)]
    punctuation = [pick_one('_-') for i in range(p)]
    word_list = lower_text + upper_text + digit + punctuation
    random.shuffle(word_list)

    password =  "".join(word_list)
    print(password)
    return password

def pick_one(strings: str) -> str:
    return strings[random.randint(0, len(strings)-1)]

def divide_area(num: int) -> int:
    l = num//2
    b = l // 2
    c = b // 2
    d = num - (l+b+c)
    _ = random.randint(0,2)
    if _ == 0:
        u, d, p = b, c, d
    elif _ == 1:
        u, d, p = c, d, b
    else:
        u, d, p = d, b, c
    return (l,u,d,p)


if __name__ == "__main__":
    gen_password(number_of_digits)


'''
print('ascii_lowercase: ' + string.ascii_lowercase)
print('ascii_lowercase: ' + string.ascii_uppercase)
print('ascii_letters: ' + string.ascii_letters)
print('digits: ' + string.digits)
print('punctuation: ' + string.punctuation)
print(len(string.ascii_letters))
'''
