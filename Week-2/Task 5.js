function findIndexOfCar(seats, status, number){
    // your code here

    // if car seats is less than pessengers amount, 
    // change value in car list and status list to 
    const check_seats = [];
    const check_status = [];

    seats.forEach((seat) => {
        if ( seat < number ) {
            check_seats.push(0);
        }else{
            check_seats.push(seat);
        }
    });

    for ( let i = 0; i < status.length; i++ ) {
        if ( check_seats[i] == 0 ) {
            check_status.push(0);
        }else{
            check_status.push(status[i]);
        }
    };


    // if status list equals to 0,
    // change car list to 0
    for ( let i = 0; i < status.length; i++ ) {
        if ( check_status[i] == 0 ) {
            check_seats[i] = 0;
            
        };
        
    };


    // find most fitting choice of car seats
    const substraction_seats = [];
    check_seats.forEach((seat) => {
        let substraction = seat - number;
        substraction_seats.push(substraction);
    });

    let car_chosen_index = -1;
    if ( substraction_seats.indexOf(0) !== -1 ) {
        car_chosen_index = substraction_seats.indexOf(0);
    }else{
        const new_substraction_list = [];
        substraction_seats.forEach((value) => {
            if ( value >= 0 ) {
                new_substraction_list.push(value);
            }
        });
    
        if ( new_substraction_list.length > 0 ) {
            new_substraction_list.sort(function(a, b){return a-b});
            car_chosen_index = substraction_seats.indexOf(new_substraction_list[0]);
        }
    }

        console.log(car_chosen_index);
    
}


    
    findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4
    findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
    findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2