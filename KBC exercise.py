questions=[
    ["When did Amogh & Vaishali get married?","1st Nov","8th Dec","3rd April","9th March",2],
    ["When is Vasihali\'s birthday?","1st Nov","8th Dec","3rd April","9th March",3],
    ["When is Amogh\'s birthday?","22nd Nov","8th Dec","3rd April","9th March",1],

["When is Amogh\'s birthday?","22nd Nov","8th Dec","3rd April","9th March",1],
["When is Amogh\'s birthday?","22nd Nov","8th Dec","3rd April","9th March",1],
["When is Amogh\'s birthday?","22nd Nov","8th Dec","3rd April","9th March",1],
["When is Amogh\'s birthday?","22nd Nov","8th Dec","3rd April","9th March",1],
["When is Amogh\'s birthday?","22nd Nov","8th Dec","3rd April","9th March",1],
["When is Amogh\'s birthday?","22nd Nov","8th Dec","3rd April","9th March",1],
["When is Amogh\'s birthday?","22nd Nov","8th Dec","3rd April","9th March",1]
]

levels=[10000,20000,50000,100000,2000000,4000000,6000000,8000000,9000000,10000000]      #prize amount at different levels

money=0

for i in range(0,10):   #10 questions

    question=questions[i]

    print(f"\nYour question for Rs{levels[i]} is:\n")
    print(question[0])
    print("Your options are:")
    print(f"1. {question[1]}                                       2.{question[2]}")
    print(f"3. {question[3]}                                       4.{question[4]}")

    try:
        ans=int(input("\nEnter your answer:"))
    except:
        print("\nIncorrect format entered")
        break

    if ans==question[-1]:
        print("Correct Answer")

        conti=int(input("\nDo you want to continue? select 1 for yes and 2 for no:"))

        if conti == 2:
            money = levels[i]       # if user quits in between he takes the cash amount for that level
            break
        else:
            print("")

        if i in (0,3,6):        # if user gives wrong answer in the middle he will be given the base amount set and not the entire cash amount for that level
            money=levels[i]
    else:
        print("Wrong answer")
        break

print(f"\nYou have won total amount of Rs{money}")