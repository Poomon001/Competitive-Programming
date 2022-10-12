def isOneMonth_M1(d1, d2):
    dayInMonth = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    date1 = d1[0]
    date2 = d2[0]
    month1 = d1[1]
    month2 = d2[1]
    year1 = d1[2]
    year2 = d2[2]

    daysInYear = 0
    totalDay1 = date1
    totalDay2 = date2

    for key, value in dayInMonth.items():
        if month1 > key:
            totalDay1 += value

    for key, value in dayInMonth.items():
        if month2 > key:
            totalDay2 += value

    for key, value in dayInMonth.items():
        daysInYear += value

    diff = (totalDay1-totalDay2 + (year1-year2)*daysInYear)

    if abs(diff) > 30+1:
        return "greater"
    elif abs(diff) < 30+1:
        return "smaller"
    else:
        return "exact"


def isOneMonth_M2(d1, d2):
    totalDay1 = countDays(d1)
    totalDay2 = countDays(d2)

    diff = totalDay1 - totalDay2

    if abs(diff) > 30+1:
        return "greater"
    elif abs(diff) < 30+1:
        return "smaller"
    else:
        return "exact"

def countDays(date):
    day = date[0]
    month = date[1]
    year = date[2]

    dayInMonth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    dayInMonth[2] = 29 if isLeaf(year) else 28

    thisYearDays = day
    passYearDays = ((year - 1) * 365) + totalLeaf(year)

    for i in range(1, month):
        thisYearDays += dayInMonth[i]

    return thisYearDays + passYearDays

def totalLeaf(year):
    return (year - 1)//4

def isLeaf(year):
    return (year%4 == 0 and year%100 != 0) or (year%400 == 0)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== solution m1===+\n")
    print(isOneMonth_M1([1 ,12,2021], [1 ,1,2022])) # exact
    print(isOneMonth_M1([1, 1, 2022], [1, 12, 2021])) # exact
    print(isOneMonth_M1([1, 1, 2022], [2, 12, 2021]))  # smaller
    print(isOneMonth_M1([2, 1, 2022], [1, 12, 2021]))  # greater
    print(isOneMonth_M1([1, 1, 2021], [1, 2, 2022])) # greater
    print(isOneMonth_M1([2, 1, 2019], [1, 2, 2019])) # smaller
    print(isOneMonth_M1([15, 6, 2020], [15, 5, 2020])) # exact
    print(isOneMonth_M1([28, 2, 2020], [30, 3, 2020]))  # smaller (incorrect) -> leaf (doesn't support)

    print("\n+=== solution m3===+\n")
    print(isOneMonth_M2([1, 12, 2021], [1, 1, 2022]))  # exact
    print(isOneMonth_M2([1, 1, 2022], [1, 12, 2021]))  # exact
    print(isOneMonth_M2([1, 1, 2022], [2, 12, 2021]))  # smaller
    print(isOneMonth_M2([2, 1, 2022], [1, 12, 2021]))  # greater
    print(isOneMonth_M2([1, 1, 2021], [1, 2, 2022]))  # greater
    print(isOneMonth_M2([2, 1, 2019], [1, 2, 2019]))  # smaller
    print(isOneMonth_M2([15, 6, 2020], [15, 5, 2020]))  # exact
    print(isOneMonth_M2([28, 2, 2020], [30, 3, 2020]))  # exact (correct) -> leaf (does support)