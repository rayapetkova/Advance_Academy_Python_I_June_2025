age = int(input("На колко си години?: "))

if age < 10:
    print("Ти си още дете!")
elif age == 10:
    print("На точно 10 си - страхотно!")
else:  # същото като elif age > 10
    print("Ти си по-голяма от 10!")
