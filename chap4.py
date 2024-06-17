'''
# strings and methods

s = "374"
print(int(s)*2)

s = "374"
print(float(s)*2)

one = int(input('please input a number: '))
two = int(input('please input another number: '))
print (float(one * two))

weight = float(.2)
animal = 'newt'
print(f'{weight} is the weight of a {animal}')
print('{} is the weight of a {}'.format(weight, animal))
 
print('AAA'.find('a'))
print('Somebody said something to Samantha.'.replace('s', 'x'))

inp = input('please writhe something: ')
print(inp.find('e'))

text = input('Enter some text: ')
text = text.replace('a', '4')
text = text.replace('b', '8')
text = text.replace('e', '3')
text = text.replace('l', '1')
text = text.replace('o', '0')
text = text.replace('s', '5')
text = text.replace('t', '7')
print(text)

text = input('Enter some text: ')
print(text.replace('a', '4').replace('b', '8'))
#oder
text = input('Enter some text: ')
letters = ['a', 'b', 'e', 'l', 'o', 's', 't']
numbers = ['4', '8', '3', '1', '0', '5', '7']

for i in range(len(letters)):
    text = text.replace(letters[i], str(numbers[i])) #fixable
print(text)
'''