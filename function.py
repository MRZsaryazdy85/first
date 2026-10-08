import random

my_numbers = [] 
for i in range(1,11):
    my_numbers.append(i)
    
   
    
    
for item in my_numbers:
    if item == 5 :
        continue
    elif item == 8 :
        break
    else:
        print(item)


def sort_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(i,len(numbers)) :
            if numbers[j] > numbers[i]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers
sort_numbers(my_numbers)
print(my_numbers )

                
 
                
    

    
          
        