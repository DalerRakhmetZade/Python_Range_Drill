def start():
    first = no1()
    second = no2()
    third = no3()
    print ("\nI hope it's a 'PASS' :) Thank you for your time and HAPPY FRIDAY!")

# one parameter to display 0,1,2,3
def no1():
    run = True
    while run:
        choice = input("\nWould you like to run a range() function with one parameter that will display: 0, 1, 2, 3? \ny/n:").lower()
        if choice == "y":
            print ("Pretty easy :)")
            for i in range(4):
                print (i)
            run = False
        elif choice == "n":
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', 'n' for 'NO'...")    

# three parameters to display 3,2,1,0
def no2():
    run = True
    while run:
        choice = input("\n\n\nNow let's check my range() function with three parameters that displays: 3, 2, 1, 0. \nJust say 'GO' when ready:").lower()
        print ("Here you go!")
        if choice == "go":   
            for i in range(3,-1,-1):
                print (i)
                run = False
        else:
            print("\nPlease enter 'GO' to proceed...")   

# three parameters to display 8,6,4,2
def no3():
    run = True
    while run:
        choice = input("\n\n\nSo far so good! Let's check the third range() function that should display: 8, 6, 4, 2. \nSay 'Daler is the best student to see results!' - Kidding :). \nJust enter 'Check' :").lower()
        if choice == "check":
            for i in range(8,0,-2):
                print (i)
                run = False
        else:
            print("\nPlease enter 'Check' to proceed...")         
    


    
if __name__ == "__main__":
    start()
