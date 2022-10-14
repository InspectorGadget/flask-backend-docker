var = [{'a' : 1}, {'b' : 2}]
var2 = [{'c' : 3}, {'d' : 4}, {'raeveen': 2}]


result = [
    *var,
    *var2
] # [{'a' : 1}, {'b' : 2}, {'c' : 3}, {'d' : 4}]

# All in one dict
res = {
    key: value 
    for element in result
    for (key, value )
    in element.items()
}

# print(res)