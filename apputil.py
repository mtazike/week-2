import numpy as np

#exercise1
def ways(n):
    count = 0
    for nickles in range(n // 5+1):         #from 0 nickels up to max possible
        pennies = n - 5 * nickles           #remaining pennies
        if pennies >= 0:                    
            count += 1
    return count



#exercise2_part1
def lowest_score(names,scores):       #find the index of the lowest score
    index = np.argmin(scores)         #return the student name at the index
    return names[index]




#exercise2_part2
def sort_names(names, scores):
    idx = np.argsort(scores)
    idx = idx[::-1]
    return names[idx]