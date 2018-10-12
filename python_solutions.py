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
