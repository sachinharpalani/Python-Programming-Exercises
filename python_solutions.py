def divisible_by_7_and_not_5():
    ans = [i for i in range(2000,3201) if i % 7 == 0 and i % 5 != 0]
    print(*ans,sep=',')


def calculate_factorial():
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n-1)

    n = int(input('Enter a number'))
    print(fact(n))


def dict_square():
    n = int(input('Enter a number'))
    print({i:i*i for i in range(1,n+1)})


def list_and_tuple():
    seq = input('Enter a comma seperated sequence')
    seq_split = seq.split(',')

    print(seq_split)
    print(tuple(seq_split))


class StringManipulator():

    def getString(self):
        self.seq = input('Enter a string')

    def printString(self):
        print(self.seq.upper())


def seq_custom_formula():
    def compute(D):
        import math
        C = 50
        H = 30
        return int(math.sqrt((2*C*D)/H))

    seq = input('Enter a sequence')
    ans = [compute(int(e)) for e in seq.split(',')]
    print(*ans,sep=',')


def matrix_2d():
    x,y = input('Enter x and y').split(',')
    ans = [[i*j for j in range(int(y))] for i in range(int(x))]
    print(ans)


def seq_sort():
    seq = input('Enter comma seperated words')
    seq_split = seq.split(',')
    print(sorted(seq_split,key=lambda x:x[0]))


def seq_unique_sorted():
    seq = input('Enter comma seperated words')
    seq_split = seq.split(' ')
    ans = ' '.join(sorted(set(seq_split),key=lambda x:x[0]))
    print(ans)


def binary_divisible_by_5():
    seq = input('Enter comma seperated sequence of binary digits: \n')
    seq_int = map(lambda x: int(x,2),seq.split(','))
    ans = [bin(i).replace('0b','') for i in seq_int if i % 5 == 0]
    print(*ans, sep=',')


def even_comma_sep():
    ans = [i for i in range(1000,3001) if i % 2 == 0]
    print(*ans,sep=',')


def letters_and_digits_counter():
    import string
    sentence = input('Enter a sentence \n')
    l_count = 0
    d_count = 0
    for c in sentence:
        if c in string.ascii_letters:
            l_count +=1
        elif c in string.digits:
            d_count +=1
    print('Letters: {} \nDigits: {}'.format(l_count,d_count))


def upper_lower_case_counter():
    import string
    sentence = input('Enter a sentence \n')
    l_count = 0
    u_count = 0
    for c in sentence:
        if c in string.ascii_uppercase:
            u_count +=1
        elif c in string.ascii_lowercase:
            l_count +=1
    print('Upper Case: {} \nLower Case: {}'.format(u_count,l_count))


def custom_a_formula():
    a = int(input('Enter a number:\n'))
    n1 = int("%s%s"% (a,a))
    n2 = int("%s%s%s"% (a,a,a))
    n3 = int("%s%s%s%s"% (a,a,a,a))

    print(a+n1+n2+n3)


def square_odd_index():
    seq = input('Enter a comma seperated number sequence')
    seq_split = map(int, seq.split(','))
    seq_square = [i**2 for i in seq_split if i % 2 == 1]
    print(*seq_square, sep=',')


class InsufficientAmount(Exception):
    def __str__(self):
        return 'Balance is insufficient'

class BankAccount():

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientAmount
        else:
            self.balance -= amount


    @property
    def bal(self):
        return self.balance

def bank_transactions():
    account = BankAccount()
    while True:
        ip_seq = input('Enter D to deposit, or W for withdraw, or anything to cancel: \n')
        if not ip_seq:
            print(account.bal)
            break
        try:
            action, amount = ip_seq.split(' ')
            if action == 'D':
                account.deposit(int(amount))
            elif action == 'W':
                account.withdraw(int(amount))
        except ValueError:
            print(account.bal)
            break


def password_validity():

    def check_pass(password):
        import re
        lower_case_valid = bool(re.findall(r'[a-z]+',password))
        upper_case_valid = bool(re.findall(r'[A-Z]+',password))
        digits_valid = bool(re.findall(r'[0-9]+',password))
        special_char_valid = bool(re.findall(r'[$#@]+',password))
        len_valid = True if 6 <= len(password) <= 12 else False
        return (lower_case_valid and upper_case_valid and digits_valid and special_char_valid and len_valid)

    seq = input('Enter comma seperated passwords')
    valid_pass = [password for password in seq.split(',') if check_pass(password)]
    print(*valid_pass, sep=',')


def name_age_height_sort():
    ip_seq = []
    while True:
        try:
            name, age, score = input('Enter name, age, score').split(',')
            ip_seq.append((name, int(age), int(score)))
        except:
            import operator
            print(sorted(ip_seq, key=operator.itemgetter(0,1,2)))
            break


def div_by_6_gen(n):
    for i in range(1,n):
        if i % 6 == 0:
            yield i


def word_freq():
    import collections
    sentence = input('Enter a sentence')
    sentence_count = collections.Counter(sentence.split(' '))
    for k,v in sorted(sentence_count.items()):
        print('{}:{}'.format(k,v))


def even_no_gen(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

def even_no_gen_helper():
    n = int(input('Enter n'))
    gen = even_no_gen(n)
    ans = []
    while True:
        try:
            ans.append(next(gen))
        except StopIteration:
            print(*ans, sep=',')
            break


def even_nos_assertion(nos):
    for no in nos:
        assert(no%2==0) , 'Only even no allowed'


def basic_expressions():
    exp = input('Enter basic mathematic expressions')
    print(eval(exp))


def list_shuffle(nos):
    import random
    random.shuffle(nos)
    print(nos)


def sentences_combination():
    subject = ["I", "You"]
    verb = ["Play", "Love"]
    object = ["Hockey","Football"]

    sentences = [' '.join([s,v,o]) for s in subject
                 for v in verb
                 for o in object]

    print(sentences)


def remove_index_list_comp():
    nos = [12,24,35,70,88,120,155]
    ans = [num for idx, num in enumerate(nos) if not idx in [0,2,4,6]]
    print(ans)


def matrix_3d(i=3,j=5,k=8):
    print([[[0 for _ in range(k)] for _ in range(j)] for _ in range(i)])


def list_intersection(a,b):
    print(list(set(a).intersection(set(b))))


def character_occurences():
    import collections
    sentence = input('Enter a sentence')
    sentence_count = collections.Counter(sentence)
    for ch, cnt in sorted(sentence_count.items()):
        print('{},{}'.format(ch,cnt))


def sentence_reversed():
    sentence = input('Enter a sentence')
    sentence_reverse = [word[::-1] for word in sentence.split(' ')]
    print(' '.join(sentence_reverse[::-1]))


def list_permutations(nos):
    import itertools
    print(list(itertools.permutations(nos)))


class Person():

    def __init__(self, gender=None):
        self.gender = gender

    def getGender(self):
        return self.gender

class Male(Person):
    def __init__(self):
        super().__init__('Male')

    def getGender(self):
        return super().getGender()


class Female(Person):
    def __init__(self):
        super().__init__('Female')

    def getGender(self):
        return super().getGender()


def binary_search(key, nos):
    nos_back = nos[:]
    nos_back.sort()
    index=-1

    for _ in nos_back:
        nos_back_len = len(nos_back)
        middle = nos_back[nos_back_len//2]

        if key == middle:
            index=middle
            print('{} found at index {}'.format(key, middle-1))
            break

        elif key < middle:
            nos_back = nos_back[:nos_back_len//2]

        else:
            nos_back = nos_back[nos_back_len//2:]

    if index == -1:
        print(key, 'not found')


def robot_move():
    x, y = 0, 0
    while True:
        ip_seq = input('Enter direction with steps \n')
        if not ip_seq:
            import math
            print(x,y)
            print(math.floor(math.sqrt(x**2 + y**2)))
            break
        else:
            direction, steps = ip_seq.split(' ')
            if direction == 'UP':
                x += int(steps)
            elif direction == 'DOWN':
                x -= int(steps)
            elif direction == 'LEFT':
                y -= int(steps)
            elif direction == 'RIGHT':
                y += int(steps)
            else:
                print('Wrong key try again')
                continue
