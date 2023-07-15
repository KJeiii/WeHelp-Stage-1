def func(*data):
# your code here
    # make tuple to be list
    name_list = list(data)
    
    # extact middle and create a list
    middle_name_list = []
    for name in name_list:
        middle_name_list.append(name[1])

    # count amount of each middle name
    name_amount_list = []
    for middle_name in middle_name_list:
        amount = middle_name_list.count(middle_name)
        name_amount_list.append(amount)

    # create dict = {amount : middle name}
    amount_middle_name_dict = {} 
    for _ in range(len(middle_name_list)):
        amount_middle_name_dict[name_amount_list[_]] = middle_name_list[_]

    # make all keys into a list
    amount_keys = list(amount_middle_name_dict.keys())
    amount_keys.sort()

    # find unique name
    unique_middle_name = None
    if len(amount_keys) > 1:
        if amount_keys[0] == 1:
            unique_middle_name = amount_middle_name_dict[amount_keys[0]]

    # match whole name with unique middle name
    answer = "沒有"
    for n in range(len(middle_name_list)):
        if middle_name_list[n] == unique_middle_name:
            answer = name_list[n]

    print(answer)

func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有