import math


def paint_calc(height, width, cover):
    number_cans = (height * width) / cover
    # number_cans = int(round(number_cans)) -> wrong
    number_cans = math.ceil(number_cans)
    print(f"You'll need {number_cans} of paint")


test_h = int(input("Height  of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
