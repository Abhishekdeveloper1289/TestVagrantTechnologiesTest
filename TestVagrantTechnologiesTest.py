def subscriptionperweek():
    for i, j in plans.items():
        total = 0
        items.append(i)
        for k in j.values():
            total = total + k
        weektotal[i] = total
    print(weektotal)


plans = {"TOI": {"Monday": 3, "Tuesday": 3, "Wednesday": 3, "Thursday": 3, "Friday": 3, "Saturday": 5, "Sunday": 6},
         "Hindu": {"Monday": 2.5, "Tuesday": 2.5, "Wednesday": 2.5, "Thursday": 2.5, "Friday": 2.5, "Saturday": 4,
                   "Sunday": 4},
         "ET": {"Monday": 4, "Tuesday": 4, "Wednesday": 4, "Thursday": 4, "Friday": 4, "Saturday": 4, "Sunday": 10},
         "BM": {"Monday": 1.5, "Tuesday": 1.5, "Wednesday": 1.5, "Thursday": 1.5, "Friday": 1.5, "Saturday": 1.5,
                "Sunday": 1.5},
         "HT": {"Monday": 2, "Tuesday": 2, "Wednesday": 2, "Thursday": 2, "Friday": 2, "Saturday": 4, "Sunday": 4}
         }
items = []
weektotal = {}
subscriptionperweek()
budget = int(input("Enter the Budget: "))

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        expence = weektotal[items[i]] + weektotal[items[j]]
        if expence <= budget:
            print('{"', items[i], '","', items[j], '"}, ')
