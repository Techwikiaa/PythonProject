#write your code below:


def primeNumCheck(number):
  is_prime = True
  if num == 2 or number == 3:
    print(f"{num} prime number!")
  elif num < 0 or num == 0 or num == 1:
    print("please enter a correct value!")
  else:
    for i in range(2, num):
      if num % i == 0:
        is_prime = False
    if is_prime == True:
      print(f"{num} is prime number.")
    else:
      print(f"{num} isn't a prime number. ")


num = int(input("enter a number to check: "))
primeNumCheck(num)
