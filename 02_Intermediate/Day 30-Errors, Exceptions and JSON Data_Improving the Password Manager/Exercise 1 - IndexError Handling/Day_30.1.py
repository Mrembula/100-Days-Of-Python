fruits = ['Apple', 'Pear', 'Orange']

# TODO: Catch the exception and make sure the code runs with crashing


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as e:
        print(f"{e}")
    else:
        print(fruit + ' pie')


make_pie(4)
