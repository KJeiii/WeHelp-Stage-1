function findAndPrint(messages){
    // write down your judgment rules in comments
    // 1. Match each word in the message with 17ysr-keyword:
    //     > build a keyword list containing strings representing age beyond 17 yrs.
    //     > slice message by into sevral strings by blank(" ") and create a list
    // 2. Print the key if message is verified as a guy beyond 17 yrs.
    
    // your code here, based on your own rules

    // Build keyWords_array
    let keyWords = ["18", "college", "legal", "vote"];

    // Split each message and create a new object for them
    // new object will be {name : set of string}
    let newObject= {};
    for ( let key in messages ) {
        let msgSet = new Set ( messages[key].split(" ") );
        newObject[key] = msgSet;
    };

    // Verify each msgSet with keywords_array
    let guyBeyond17 = [];
    for ( let i = 0 ; i < 4 ; i++ ) {
        for ( let key in newObject ) {
            if ( newObject[key].has( keyWords[i] ) ) {
                guyBeyond17.push(key);
            }
        } 
    }

    console.log(guyBeyond17);
    }
    
    findAndPrint({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
    });

