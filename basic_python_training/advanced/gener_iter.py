#assign1:
def prime_numbers():
    for num in range(2, 51):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num

print(list(prime_numbers()))  


#assign2:
def even_numbers():
    num = 2
    while True:
        yield num
        num += 2  

even_gen = even_numbers()
for _ in range(10):
    print(next(even_gen), end=" ")


#assign3:
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

fib = Fibonacci(10)
print(list(fib),end=" ")  