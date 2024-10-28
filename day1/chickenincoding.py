with open("python\day1\chicken.txt","r",encoding='UTF-8') as file:
    total_revenue = 0
    total_days = 0
    for line in file:
        data = line.strip().split(": ")
        revenue = int(data[1])

        total_revenue += revenue
        total_days += 1
    print(total_revenue / total_days)

        