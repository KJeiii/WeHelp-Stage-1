def calculate_sum_of_bonus(data):
    # write down your bonus rules in comments   
    # 1. Total bonus is 10,000 TWD.
    # 2. Basic bonus fraction of 3 employees : 1/3 for each one.

    # 3. Performance weighting :
    #   below average :  + 1,000 TWD
    #   average : + 2,000 TWD
    #   above average : + 3,000 TWD  
    # 
    # 4. Role weighting :
    #   engineer : + 800 TWD
    #   sales : + 800 TWD
    #   CEO : + 1,000 TWD

    # 5. Salary weighting： 
    #   salary > NT 30,000：+ 300 TWD
    #   salary <= NT 30,000：+ 800 TWD

    # your code here, based on your own rules

    total_bonus = 0

    # weighting performance
    for employee in data["employees"]:
        if employee['performance'] == "below average":
            total_bonus += 1000
        elif employee['performance'] == "average":
            total_bonus += 2000
        else:
            total_bonus += 3000

    # weighting role 
    for employee in data["employees"]:
        if employee['role'] == "CEO":
            total_bonus += 1000
        else:
            total_bonus += 800

    # weighting salary
    number_set = {str(n) for n in range(10)}
    new_salary_dict = {}
    salary_for_bonus = []

    # check salary datatype: if not int, proceed str > int
    for employee in data["employees"]:
        if type(employee['salary']) == int:
            new_salary_dict[employee['salary']] = ""

        else:
            salary_str_list = list(employee["salary"])
            salary_str = []
            not_int_str = []

            for _ in salary_str_list:
                if _ in number_set:
                    salary_str.append(_)
                else:
                    not_int_str.append(_)   
            salary = int("".join(salary_str))
            not_int = "".join(not_int_str)
            new_salary_dict[salary] = not_int  


    # check salary unit: if it is USD, proceed USD > TWD
    for salary in new_salary_dict:
        if new_salary_dict[salary] == "USD":
            salary_USDtoTWD = salary*30
            salary_for_bonus.append(salary_USDtoTWD)
        else:
            salary_for_bonus.append(salary)



    # calculate bonus
    for salary in salary_for_bonus:
        if salary > 30000:
            total_bonus += 300
        else:
            total_bonus += 800

     
    print(total_bonus)

calculate_sum_of_bonus({
    "employees":[
        {
        "name":"John",
        "salary":"1000USD",
        "performance":"above average",
        "role":"Engineer"
        },
        {
        "name":"Bob",
        "salary":60000,
        "performance":"average",
        "role":"CEO"
        },
        {
        "name":"Jenny",
        "salary":"50,000",
        "performance":"below average",
        "role":"Sales"
        }
    ]
}) # call calculate_sum_of_bonus function

