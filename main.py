import random, string

number_of_digits = 12

def gen_password(number_of_digits: int) -> str:
    l, u, d, p = divide_area(number_of_digits)
    lower_text = random.choices(string.ascii_lowercase,k=l)
    upper_text = random.choices(string.ascii_uppercase, k=u)
    digit = random.choices(string.digits, k=d)
    punctuation = random.choices('_-', k=2)

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
