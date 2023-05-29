numberofterms=int(input("Please enter the number of terms:"))

n1=0
n2=1
count=0

if numberofterms<=0:
    print("Please enter a positive integer")

elif numberofterms==1:
    print("Fibbonacci sequence upto:")
    print (n2)

else:
     print("Fibonacci sequence:")
     while count<numberofterms:
         print(n1)
         nth=n1+n2
         n1=n2
         n2=nth
         count+=1
    
    

    
          


    
