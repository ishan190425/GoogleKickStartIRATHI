"""
A Template based on google kickstarts input/output
"""

def func(self,params):
    return 0

def main():
    tests = int(input()) #amount of testcases
    for i in range(1,tests + 1):
        answer = func(0) #return function
        print("Case #{}: {}".format(i, answer)) #output


if __name__ == "__main__":
    main()