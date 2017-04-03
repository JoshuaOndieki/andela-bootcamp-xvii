#prime numbers generator

def prime_numbers(upper_limit):
    prime_list=[]
    def is_prime(n):
        if n in [0,1,2]:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    try:
        if upper_limit<0:
            return 0
        for number in range(upper_limit+1):
            if is_prime(number):
                prime_list.append(number)
        return prime_list
    except TypeError:
        raise TypeError


