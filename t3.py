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
calculation=0
place=[]
cal=[]
calcul = Calculator()
import re

def renew():
    place.clear()
    cal.clear()
    for i in re.finditer(r'[+\-*/]', calculation):
        start, end = i.span()
        place.append(hash(start))
        cal.append(i.group())

process="y"
while process=="y":
    calculation=input("calculation:")
    cal2=calculation
    place.clear()
    cal.clear()
    for i in re.finditer(r'[+\-*/]', calculation):
        print("finditer:", i)
        print(i.group())
        start, end = i.span()
        place.append(hash(start))
        cal.append(i.group())
    
    for num in range(len(place)):
        if len(place) > 1:
            if cal[0]=="+":
                calculation=calculation.replace(calculation[0:place[1]], str(calcul.add(int(calculation[0:place[0]]),int(calculation[place[0]+1:place[1]]))))
                print(calculation)
                renew()
            elif cal[0] == "-":
                calculation=calculation.replace(calculation[0:place[1]], str(calcul.minus(int(calculation[0:place[0]]),int(calculation[place[0]+1:place[1]]))))
                print(calculation)
                renew()
            elif cal[0]=="*":
                calculation=calculation.replace(calculation[0:place[1]], str(calcul.multiply(int(calculation[0:place[0]]),int(calculation[place[0]+1:place[1]]))))
                print(calculation)
                renew()
            elif cal[0]=="/":
                calculation=calculation.replace(calculation[0:place[1]], str(calcul.divide(int(calculation[0:place[0]]),int(calculation[place[0]+1:place[1]]))))
                print(calculation)
                renew()
            else:
                print("error")
        else:
            if cal[0]=="+":
                print(calcul.add(int(calculation[0:place[0]]),int(calculation[place[0]+1:])))
            if cal[0]=="-":
                print(calcul.minus(int(calculation[0:place[0]]),int(calculation[place[0]+1:])))
            if cal[0]=="*":
                print(calcul.multiply(int(calculation[0:place[0]]),int(calculation[place[0]+1:])))
            if cal[0]=="/":
                print(calcul.divide(int(calculation[0:place[0]]),int(calculation[place[0]+1:])))
    process=input("continue?(y/n)")
    print("")
    
print("The calculation had ended.")