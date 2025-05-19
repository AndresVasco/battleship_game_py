def my_generator():
    yield 1    #El yield se usa para decir que queremos retornar cierto valor
    yield 2
    yield 3

for value in my_generator():
    print(value)