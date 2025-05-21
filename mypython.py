#if 5 > 2:
 #  print("false")


#YOB = input('When were you born?/n')
#YOB = int(YOB)
#AGE = 2024 - YOB
#print(f"You are {AGE} years old")

def main():
    positive_sum = 0
    negative_sum = 0

    print("Please enter 10 integers:")

    for _ in range(10):
        num = int(input("Enter an integer: "))
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num

    print(f"Sum of positive integers: {positive_sum}")
    print(f"Sum of negative integers: {negative_sum}")

    
    num = list(range(1,10))
    print("num")



if __name__ == "__main__":
    main()


