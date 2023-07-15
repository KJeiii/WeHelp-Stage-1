function calculateSumOfBonus(data){
    // write down your bonus rule in comments
    //  1. Total bonus is 10,000 TWD.
    //  2. Basic bonus fraction of 3 employees : 1/3 for each one.
    //  3. Performance weighting :
    //    below average :  + 1,000 TWD
    //    average : + 2,000 TWD
    //    above average : + 3,000 TWD  
     
    //  4. Role weighting :
    //    engineer : + 800 TWD
    //    sales : + 800 TWD
    //    CEO : + 1,000 TWD

    //  5. Salary weighting： 
    //    salary > NT 30,000：+ 300 TWD
    //    salary <= NT 30,000：+ 800 TWD

    // your code here, based on your own rules
    let totalBonus = 0;

    // weighting performance
    for ( let i = 0; i < data["employees"].length; i++ ) {
        let staffPerformace = data["employees"][i]["performance"];
        if ( staffPerformace == "below average" ) {
            totalBonus += 1000;
        }else if ( staffPerformace == "average" ) {
            totalBonus += 2000;
        }else {
            totalBonus +=3000;
        }
    }

    // weighting role 
    for ( let i = 0; i < data["employees"].length; i++ ) {
        let staffRole = data["employees"][i]["role"];
        if ( staffRole == "CEO" ) {
            totalBonus += 1000;
        }else {
            totalBonus += 800;
        }
    }

    // weighting salary
    // check salary datatype: 
    // if it is not number, proceed str > int
    // if it is number, calulation bonus
    let salaryObj = {};
    const numberSet = new Set(["0","1","2","3","4","5","6","7","8","9"]);
    for ( let i = 0; i < data["employees"].length; i++ ) {
        let rawSalary = data["employees"][i]["salary"];
        if ( typeof(rawSalary) == "number" ) {
            if ( rawSalary > 30000 ) {
                totalBonus += 300;
            }else{
                totalBonus += 800;
            }
        }else{
            const salaryArray = rawSalary.split("");
            let salary_num_array = [];
            let salary_text_array = [];
            for ( let i = 0; i < salaryArray.length; i++) {
                if ( numberSet.has(salaryArray[i]) ) {
                    salary_num_array.push(salaryArray[i]);
                }else{
                    salary_text_array.push(salaryArray[i]);
                }
            }
            salaryObj[salary_num_array.join("")] = salary_text_array.join("");
        }
    }

    // check salary unit: if it is USD, proceed USD > TWD
    let otherSalaryArray = [];
    for ( let key in salaryObj ) {
        if ( salaryObj[key] == "USD" ) {
            otherSalaryArray.push(key*30);
        }else{
            otherSalaryArray.push(key*1);
        }
    }

    // calculate bonus
    for ( let i = 0 ; i < otherSalaryArray.length; i++ ) {
        if ( otherSalaryArray[i] > 30000 ) {
            totalBonus += 300;
        }else{
            totalBonus += 800;
        }
    }
    console.log(totalBonus);
    }


    calculateSumOfBonus({
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
    }); // call calculateSumOfBonus function