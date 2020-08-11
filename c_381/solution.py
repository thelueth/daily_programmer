def yahtzee_upper(rolls):
    score = [0] * max(rolls)
    for num in rolls:
        score[num-1] = score[num-1]+num
    
    return score

print(max(yahtzee_upper([2, 3, 5, 5, 6])))
print(max(yahtzee_upper([1, 1, 1, 1, 3])))
print(max(yahtzee_upper([1, 1, 1, 3, 3])))
print(max(yahtzee_upper([1, 2, 3, 4, 5])))
print(max(yahtzee_upper([6, 6, 6, 6, 6])))
print(max(yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747,
    1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
    30864, 4868, 30864])))