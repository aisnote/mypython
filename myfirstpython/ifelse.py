if __name__ == '__main__':
    # print("this is my project")
    age = 24
    if age >= 25:
        print(age)

    elif age < 25:
        print("age < 25\n")
        print("still will print this line\n")
    else:
        print("can not go here!")


    value = None

    if value != None:
        print("value not equal None")
    else:
        print("value is equal None")

    age = 6.594584598948594
    converted_age_float = float(age)

    round_number = round(age, 1)
    print("round_number = " + str(round_number))

    round_number2 = round(age, 2)
    print("round_number2 = " + str(round_number2))

    print("float = " + str(converted_age_float))

    converted_age = int(age)

    print("coverted_age = " + str(converted_age))


