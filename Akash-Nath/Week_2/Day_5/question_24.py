#Task: Write a Python program to implement the Sieve of Eratosthenes algorithm for prime number generation. (Lists)

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    primes = [num for num in range(2, limit + 1) if is_prime[num]]
    return primes

limit = int(input("Enter a limit to find prime numbers up to: "))

result = sieve_of_eratosthenes(limit)
print(f"Prime numbers up to {limit}: {result}")
