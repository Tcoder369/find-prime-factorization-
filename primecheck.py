class Number:
    def __init__(self, number):
        self.primality = False
        self.number = number

    def find_if_prime(self):
        if self.number == 1 or self.number == 2:
            self.primality = True
      
        for i in range(2, int(self.number)):
            if int(self.number) % i == 0:
              self.primality = False
              break
            else:
              self.primality = True
        return self.primality