import time

start = time.time()

def recursive_fibonacci(n):
    
    if n <= 1:
        return n
    else:
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))


val = int(input("Shtyp vleren: "))

print(val)
# kontrollo hyrjen n
if val <= 0:
   print("Numri n duhet te jete pozitiv")
else:
   print("Vargu Fibonacci:")
   for i in range(val):
       print(recursive_fibonacci(i))
end = time.time()
print("Koha e kaluar:")
print(end - start)
