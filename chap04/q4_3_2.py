#numbers = [1,2,3,4]
#def func_hint(*args):
#    print("args:",args)
#    print("len(args):",len(args))
#
#func_hint(*numbers)
#
#many_numbers = list(range(100))
#print(many_numbers)

def func_spuare(*args):
    results = []
    for n in args:
        results.append(n * n)
    return results

numbers = [1, 2, 3, 4]
print(func_spuare(*numbers))

a = list(range(100))
print(func_spuare(*a))
