
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

hello = []
#your code go here:
for value in my_list:
    if type(value) is list or type(value) is dict:
        hello.append(value)


print(hello)
