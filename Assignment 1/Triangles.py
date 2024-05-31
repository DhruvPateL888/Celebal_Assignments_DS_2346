#Username : CT_CSI_DS_2346
#Name : Dhruv Patel

#Taking input from user
n = int(input("Enter the number of lines for getting lower Triangle: "))
print()
#Creating the lower triangle 
print("Lower Triangle :")
print()
#First loop ensures the number of lines
#Nested loop is for the stars in that particular line 
for row in range(n) :
    for j in range(row+1) :
        print("*",end="")
    print()

print()
n = int(input("Enter the number of lines for getting upper Triangle: "))
print()
#Creating the upper triangle 
print("Upper Triangle :")
print()
#outer loop is for number of lines
#inner loop 1 is for adjusting the spaces
#inner loop 2 for drawing the stars
for row in range(n) :
    for j in range(row) :
        print(" ",end="")
    for j in range(n-row) :
        print("*",end="")
    print()
    
    
print()
n = int(input("Enter the number of lines for getting pyramid : "))
print()
#Creating the pyramid 
print("Pyramid :")
print()
#outer loop is for number of lines
#inner loop 1 is for adjusting the spaces
#inner loop 2 for drawing the stars
for row in range(n) :
    for j in range(n-row-1) :
        print(" ",end="")
    for j in range(row+1) :
        print("* ",end="")
    print()

print()
print("End of the Assignment...")
