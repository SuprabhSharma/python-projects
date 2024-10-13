

print("select the operation you want to perform :\n 1) addition\n 2) subtraction\n 3)division\n 4) multiplication\n ")   
def calc():
   

     
    select = int(input("select the operation to perform:"))
    match select:
           case 1|2|3|4:

            num1 = float(input("enter the value of num1:"))
            num2 = float(input("enter the value of num2:"))
   

            match select:
                case 1:
                    print(f"sum is {num1+num2}")
                case 2:
                    print(f"subtraction is {num1-num2}")
                case 3:
                    if num2 != 0:
                        print(f"div is {num1/num2}")
                    else:
                         print("division by zero is not possible")
                case 4:
                        print(f"multiplication is {num1*num2}")
                case _:
                        print("invalid case")               
calc()



        
