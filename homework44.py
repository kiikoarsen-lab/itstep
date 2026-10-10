class MyNumbers:
    def __iter__(self):
        yield 1
        yield 2
        yield 3

numbers = MyNumbers()

for number in numbers:
    print(number)