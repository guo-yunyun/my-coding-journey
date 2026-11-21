def calc_bmi(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        comment = '偏瘦了，多吃点，孩子！'
    elif bmi < 24:
        comment = '正常，很不错哟，继续保持哟！'
    else:
        comment = '超重了，孩子，管住嘴，迈开腿，该减减肥了！'
    return round(bmi, 1), comment  #round(bni,1)保留一位小数


result, comment = calc_bmi(1.63, 45)
print(f'BMI={result},评价:{comment}')
