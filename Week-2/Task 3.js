function func(...data){
    // your code here

    // extact middle and create a list
    const middle_name_list = [];
    for ( let i = 0; i < data.length; i++ ) {
        let middle_name = data[i].slice(1,2);
        middle_name_list.push(middle_name);

    }

    // count amount of each middle name
    // create dict = {amount : middle name}
    const name_amount_list = [];
    const middle_name_set = new Set(middle_name_list);

    const shorter_name_list = [];
    middle_name_set.forEach(function(value) {
        shorter_name_list.push(value);
    })

    const amountNameObj = {};
    shorter_name_list.forEach(calName);

    function calName(shorter_name) {
        let name_list = middle_name_list.filter(cal);
        function cal(middle_name) {
        return middle_name == shorter_name;
        };
        let name_list_length = name_list.length;
        amountNameObj[name_list_length] = shorter_name;
        
    };

   

    // make all keys into a list
    let keys = Object.keys(amountNameObj).sort(function(a, b){return b - a});

    // find unique name
    // match whole name with unique middle name
    let answer = "沒有";
    if (keys.length > 1) {
        if (keys[keys.length-1] == "1") {
            data.forEach(findName);
            function findName(name) {
                let keyToFind = keys[keys.length-1];
                let middleNameToFind = amountNameObj[keyToFind];
                if (name[1] == middleNameToFind){
                    answer = name;
                }
                
            }
        }
    }
    console.log(answer);
}


    func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
    func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
    func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有