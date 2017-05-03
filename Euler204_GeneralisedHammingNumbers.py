"""
Euler204_Generalised Hamming Numbers
Problem 204 
A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?



PSEUDO OUTLINE:
    1) list all the primes between 100 and 1,000,000,000
    2) for each of these, list all its multiples that are below 1,000,000,000
    3) remove all duplicates from this list
    4) subtract the length of this set from 1,000,000,000, then add 100 to have answer
"""


import math

def is_prime(x):
    for i in range(2,math.floor(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

def main(maxi):
    not_gen_hamm_hundred=[]; 
    j=101
    while j<=maxi:
        if (j-1)%(10**6)==0:
            print('passing through j being',j,'so another million')
        if is_prime(j):
            for k in range(1,math.floor((maxi)/j)+1):
                not_gen_hamm_hundred.append(k*j)
            #print('not_gen_hamm_hundred is now', not_gen_hamm_hundred)
        j+=2
    not_gen_hamm_hundred=list(set(not_gen_hamm_hundred)) #remove duplicates
    not_count=len(not_gen_hamm_hundred)
    print('not count is',not_count)
    #print(not_gen_hamm_hundred)
    print('final answer should be maxi minus this plus 100, which is',maxi-not_count+100)
    return maxi-not_count+100

#main(10**7) #--> final answer should be maxi minus this plus 100, which is 269982
main(10**9)


#this algo needs to be streamlined. If I could somehow import the primes trough one billion as a list,
#I could solve this much more efficiently...