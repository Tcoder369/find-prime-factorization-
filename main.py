from primecheck import Number


def factorize(number):
  prime = []
  factors = []
  for i in range(2, number):
    to_check = Number(i)
    if Number.find_if_prime(to_check) == True:
      prime.append(to_check.number)
  for x in prime:
    if number%x == 0:
      factors.append(x)
  return(factors)
    
while True:
  print(factorize(int(input())))