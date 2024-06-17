'''
for n in range(2, 11):
    print(n)

m = 2
while m <= 10:
    print(m)
    m += 1

def doubles(inp):
    return [x * 2 for x in inp] # interesting code suggestion -> was gelernt
print(doubles([3,4,5]))

def doubles(inp):
    return(inp * 2)
k = 2
for i in range(3):
    print(doubles(k))
    # list comprehension is a way to create lists based on existing lists. It's like a loop inside the brackets of square brackets.
    k = doubles(k)
'''
def cube()