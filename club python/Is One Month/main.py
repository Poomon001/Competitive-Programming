def isOneMonth(d1, d2):
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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(isOneMonth([1 ,12,2021], [1 ,1,2022])) # exact
    print(isOneMonth([1, 1, 2022], [1, 12, 2021])) # exact
    print(isOneMonth([1, 1, 2022], [2, 12, 2021]))  # smaller
    print(isOneMonth([2, 1, 2022], [1, 12, 2021]))  # greater
    print(isOneMonth([1, 1, 2021], [1, 2, 2022])) # greater
    print(isOneMonth([2, 1, 2019], [1, 2, 2019])) # smaller
    print(isOneMonth([15, 6, 2020], [15, 5, 2020])) # exact