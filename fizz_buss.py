#4 check fizz,buzz,fizzbuzz
def checkb(num):
    if num%3==0 and num%5==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    elif num%3==0:
        print("fsizzbuzz")
    else:
        print(num)

num=int(input("Enter a number:"))
checkb(num)
