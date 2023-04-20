"""
Write a function that takes an integer as input, 
and returns the number of bits that are equal to 
one in the binary representation of that number. 
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, 
so the function should return 5 in this case
"""

def count_bits(n):
    if type(n) == int and n > 0:
        bits = []
        while n//2 >= 1:
            bits.append(n%2)
            n //= 2
        return bits.count(1) + 1
    if n == 0:
        return 0

# otra solucion con la funcion bin()
def countBits_2(n):
    return bin(n).count("1")

# otra solucion con operador de bit
def countBits_3(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total

print(count_bits(10))


