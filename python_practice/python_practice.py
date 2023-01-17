def hello():
    print('python sayssssss wassssssssup')

def pack(a,b,c):
    return [a, b, c]

def eat_lunch(food):
        if len(food) == 0:
            print('i have no food'),
        else:
            for i in range(len(food)):
                if i == 0:
                    print(f'first i eat {food[0]}')
                else:
                    print(f'next i eat {food[i]}')


hello()

print(pack('ham', 'egg', 'cheese'))

eat_lunch(['ham', 'egg', 'cheese'])

eat_lunch([])
        