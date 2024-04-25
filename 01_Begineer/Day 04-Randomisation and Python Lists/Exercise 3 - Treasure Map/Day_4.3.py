row1 = ['O', 'O', 'O']
row2 = ['O', 'O', 'O']
row3 = ['O', 'O', 'O']

Map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

Map[1][1] = 'X'     # center
print(f"\n{row1}\n{row2}\n{row3}")

Map[0][0] = 'X'     # top-left
print(f"\n{row1}\n{row2}\n{row3}")

Map[2][0] = 'X'     # bottom-left
print(f"\n{row1}\n{row2}\n{row3}")

Map[1][2] = 'X'     # center-right
print(f"\n{row1}\n{row2}\n{row3}")