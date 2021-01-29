import re


def check_strength(password):
    strength = {1: 'Weak', 2: 'Okay', 3: 'Strong', 4: 'Very Strong', 5: 'Excellent'}
    level = 0
    l0 = re.compile(r'.{1,7}')
    l1 = re.compile(r'.{8,}')
    l2 = re.compile(r'(?=.*[a-z])(?=.*[A-Z]).*')
    l3 = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[\W_]).*?')

    if l1.search(password):
        level += 1
    else:
        print('password must be up to 8 characters or more')
        return
    if l2.match(password):
        level += 1
    else:
        print('Password Must include Characters and a mix upper and lower case characters')
        return
    if l3.search(password):
        level += 1
    else:
        print('Password Must include alphanumeric Characters and a mix upper and lower case characters')
        return
    if len(password) > 12:
        level += 1
    print(f'{strength[level]} Password')
    return re.sub(r'.', '*', password)


check_strength('Sa miyohhPlsam78+')
