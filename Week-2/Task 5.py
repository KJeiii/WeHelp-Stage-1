def find_index_of_car(seats, status, number):
    # your code here
    
    # if car seats is less than pessengers amount, 
    # change value in car list and status list to 0
    check_seats = [car if car >= 2 else 0 for car in seats ]
    ckeck_status = []

    for n in range (len(status)):
        if check_seats[n] == 0:
            ckeck_status.append(0)
        else:
            ckeck_status.append(status[n])

    # if status list equals to 0,
    # change car list to 0

    for n in range (len(status)):
        if ckeck_status[n] == 0:
            check_seats[n] = 0

    # find most fitting choice of car seats
    substraction_seats = []
    for n in range(len(check_seats)):
        substraction = check_seats[n] - number
        if substraction >= 0:
            substraction_seats.append(substraction)
        else:
            substraction_seats.append(-1)

    car_chosen_index = -1
    for n in range(len(substraction_seats)):
        try:
            car_chosen_index = substraction_seats.index(0)

        except:
            new_substraction_list = []
            for n in substraction_seats:
                if n > 0 :
                    new_substraction_list.append(n)
            new_substraction_list.sort()
            if len(new_substraction_list) > 0:
                first_item = new_substraction_list[0]
                car_chosen_index = substraction_seats.index(first_item)


    print(car_chosen_index)


find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
