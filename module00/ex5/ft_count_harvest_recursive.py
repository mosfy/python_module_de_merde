def ft_count_harvest_recursive(x=-1, days=-1):
    if x == -1:
        days = int(input("Days until harvest: "))
        if days == 0:
            print("Harvest time!")
            return
        x = 1
    print(f"Day {x}")
    x = x + 1
    if x == days+1:
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(x, days)
