"""Python module to check if a string is palindrome"""

def is_palindrome(string :str) -> bool:
    """Returns if the string is palindrome (True or False)"""
    string = string.replace(" ","").replace(",","").lower()
    return string == string[::-1]

def run():
    print(is_palindrome('A ti no, bonita'))
    
def is_prime(number: int) -> bool:
    """Returns True if number is prime or False if the number is not prime"""
    results_list = [x for x in range(2, number) if number % x == 0]
    return len(results_list) == 0


def run2():
    number: int = 73
    number_is_prime: bool = is_prime(number)
    print(f'Is {number} a prime number? {number_is_prime}')    
    
    
    
    

if __name__ == "__main__":
    run()