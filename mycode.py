x = 90
print(x)

def main():
	print("Sonali")
	
print("Connection lost for Chandrayana-2")
print("it's raining"+str(1230))
print("it's raining"+"1230")

def summation():
	x = "Dream Girl releasing on 13th september 2019"
	print(x)

main()   
""" if __name__ == "__main__":
	main()                                           // it was the syntax to call main funtion before Python version--3  // """
summation()
print(x) # output -> 90 

#------------------------------------------------------------
var1= "Sonali Satarupa Patra"
var2 = "78135"
print(var1+ var2)
print(var1[0])
#------------------------------------------------------------
print("var1[0:9]:" ,var1[0:9] )                      # output is var1[0:9]: Sonali Sa
print(var2[1])                                       # output is 8

print ("a" in var1)                                  # output is True
print ("m" in var1)                                  # output is false
#------------------------------------------------------------
print (var1)
a= var1.replace("Sonali","Mitali")
print (a)                                            # output is Mitali Satarupa Patra
print(var1.upper())                                  # output is SONALI SATARUPA PATRA

print("".join(reversed(var2)))                       # output is 53187
print(var1.split(' '))                               # output is ['Sonali', 'Satarupa', 'Patra']

#------------------------------------------------------------
tup1 =('Sonali',26,'Bhubanesawr','AM(it)')           # Tuples
tup2 = (91,90,11240,8254,55101)

print(tup1[3])
print(tup2[1:3])

(name,age,place,profile) = tup1                      # Unpacking Tuples
print(place)


x ={'a':100,'d':400}                                  # Dictionary example
y = x.items()
print(y)                                              # output is dict_items([('a', 100), ('d', 400)])

z= list(x.items())
print(y)
#------------------------------------------------------------
# Dictinary {'key': value }
x1= {'Sonali':(26,'IT',78135),'Mitali':(29,'IT -analyst','NA'),'Sipra':(48,'IT',75135),'mitali':(29,'IPS',670)} #,('amir','kumar'):(59,'ias','GL-58')}
print(len(x1))
print(x1['mitali'])                                    # output is (29, 'IPS', 670)

#print(x1[('amir','kumar')])                            # Output is (59, 'ias', 'GL-58')

x1.update({'Sonali':(25,'AM-IT',2)})                   # Updating the Dictinary x1
print(x1)
print(x1['Sonali'])
print(x1.items())
print(list(x1.items()))

print(x1.keys())
print(list(x1.keys()))

x3 = list(x1.keys())
x3.sort()                                              # Sorting of Dictinary
for n in x3:
	print(n)

print(len(x1))                                         #Output is 4
print("variable is %s"% type(x1))                      
print("variable is %s" %type(y))                       # Output is variable is <class 'dict'>
print("Printable String is %s" %str (x1))

def mult(x,y=0):
	#y =x*x
	#print(y)
	return (x*y)
	
	
print(mult(4,y=5))
