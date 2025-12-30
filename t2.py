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
    for i in range(len(calculation)):
        if calculation[i]=="+":
            place=calculation.index("+")
        if calculation[i]=="-":
            place=calculation.index("-")
        if calculation[i]=="*":
            place=calculation.index("*")
        if calculation[i]=="/":
            place=calculation.index("/")
    if calculation[place]=="+":
        print(calculation,"=",calcul.add(int(calculation[0:place]),int(calculation[place+1:])))
    elif calculation[place] == "-":
        print(calculation,"=",calcul.minus(int(calculation[0:place]),int(calculation[place+1:])))
    elif calculation[place]=="*":
        print(calculation,"=",calcul.multiply(int(calculation[0:place]),int(calculation[place+1:])))
    elif calculation[place]=="/":
        print(calculation,"=",calcul.divide(int(calculation[0:place]),int(calculation[place+1:])))
    else:
        print("error")
    
    process=input("continue?(y/n)")
    print("")
print("The calculation had ended.")