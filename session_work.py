def avg(*args):
    return sum(args) / len(args)

def longest(l: list):
    m = 0
    w = ""
    for word in l:
        if len(word) > m:
            m, w = len(word), word
    return w
    
def is_prime(N: int):
    for i in range(2, N+1):
        if N%i == 0:
            return False
    return True
    
def celsius_to_fahrenheit(t): # t in celsius
    return (t * 9/5) + 32

def square(*args):
    return [n**2 for n in args]

def to_upper(l: list):
    return [w.upper() for w in l]

def calculate_price(amount):
    # for every 100 apply 10 tax (10% tax)
    tax = 0
    for i in range(10, amount+1, 10):
        if i % 100 == 0:
            tax+=10
    return f"Price = {amount + tax}. Tax = {tax}"

def max_and_min(l: list):
    minimum = l[0]
    maximum = l[0]
    for n in l:
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n
    return f"Max = {maximum}, Min = {minimum}"

def validate_email(email: str) -> bool:
    at = False
    dot_com = False
    for c in email:
        if c == "@":
            at = True
            break
    if at:
        for c in email[email.index('@'):]:
            if c == ".":
                if email[email.index("."):] == '.com':
                    dot_com = True
    return at and dot_com

def freq_of_chars(s: str):
    freqs = dict()
    for c in s:
        if c == ' ':
            continue
        if c not in freqs:
            freqs.update({c: 0})
        freqs[c] += 1
    return freqs

print(freq_of_chars("ali amr"))
  
