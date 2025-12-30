class Calculator:
    name="Good calculator"
    def add(self,x,y):
        result = x + y
        return(result)
    def minus(self,x,y):
        result = x - y
        return(result)
    def multiply(self,x,y):
        result = x * y
        return(result)
    def divide(self,x,y):
        result = x / y
        return(result)

calcul = Calculator()

process="y"
while process=="y":
    calculation=input("calculation:")
    if len(calculation)==3:
        if calculation[1]=="+":
            print(calculation,"=",calcul.add(int(calculation[0]),int(calculation[2])))
        elif calculation[1] == "-":
            print(calculation,"=",calcul.minus(int(calculation[0]),int(calculation[2])))
        elif calculation[1]=="*":
            print(calculation,"=",calcul.multiply(int(calculation[0]),int(calculation[2])))
        elif calculation[1]=="/":
            print(calculation,"=",calcul.divide(int(calculation[0]),int(calculation[2])))
        else:
            print("error")
    else:
        print("error")
    process=input("continue?(y/n)")
    print("")
print("The calculation had ended.")

