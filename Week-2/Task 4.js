function getNumber(index){
    // your code here
    
    // set initial number
    const totalArray = [[0,4]];

    // calculate how long the list is  
    let lenArray = 0;
    if ( Number.isInteger((index + 1) / 2)) {
        lenArray = (index + 1) / 2;
    }else{
        lenArray = Math.round((index + 1) / 2);
    }

    // create list 
    for ( let i = 1; i < lenArray; i++ ) {
        let last_term = totalArray[i-1];
        let element_add = [ last_term[0]+3 , last_term[1]+3];
        totalArray.push(element_add);
    };
    
    // find number
    let index_in_element = null;
    if ( Number.isInteger(index / 2)) {
        index_in_element = 0;
    }else{
        index_in_element = 1;
    }

    let array_chosen = totalArray[lenArray-1];
    let num_chosen = array_chosen[index_in_element];

    console.log(num_chosen);
}
    getNumber(1); // print 4
    getNumber(5); // print 10
    getNumber(10); // print 15