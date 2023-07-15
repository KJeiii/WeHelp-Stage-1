def find_and_print(messages):
# write down your judgment rules in comments
# 1. Match each word in the message with 17ysr-keyword:
#    > build a keyword list containing strings representing age beyond 17 yrs.
#    > slice message by into sevral strings by blank(" ") and create a list
# 2. Print the key if message is verified as a guy beyond 17 yrs.

# your code here, based on your own rules

    # Build keywords_set
    keywords_set = {'18', 'college', 'legal', 'vote'}

    # Split each message and create sets for them
    new_msg_dict = {}
    for _ in messages:
        new_msg_dict[_] = set(messages[_].split(" "))
    
    # Verify each message with keywords_set
    guy_beyond_17 = []
    for _ in new_msg_dict:
        if len(new_msg_dict[_] & keywords_set) > 0:
            guy_beyond_17.append(_)
    print(guy_beyond_17)


find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."}
    )



