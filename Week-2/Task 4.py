def get_number(index):
    # your code here

    # set initial number
    tuple_list = [(0,4)]

    # calculate how long the list is  
    lenth_tuple_list = None
    if (index + 1) % 2 == 0:
        lenth_tuple_list = int((index + 1) / 2)
    else:
        lenth_tuple_list = (index + 1)//2 + 1

    # create list 
    for n in range(1,lenth_tuple_list):
        tuple_last_term = tuple_list[n-1]
        tuple_add = (tuple_last_term[0]+3, tuple_last_term[1]+3)
        tuple_list.append(tuple_add)

    # find number
    index_in_tuple = None
    if index % 2 == 0:
        index_in_tuple = 0
    else:
        index_in_tuple = 1
    
    tuple_chosen = tuple_list[lenth_tuple_list-1]
    num_chosen = tuple_chosen[index_in_tuple]

    print(num_chosen)


get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15
