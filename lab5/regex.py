#ex1
import re
pattern = 'ab*'
x = input()
if re.fullmatch(pattern, x):
    print(x)
#ex2
import re
pattern = 'ab{2,3}'
x = input()
if re.fullmatch(pattern, x):
    print(x)
#ex3
import re
pattern = '\b[a-z]+_[a-z]+\b'
x = input()
matches = re.findall(pattern, x)
print(x)
#ex4
import re
pattern = '\b[A-Z][a-z]+\b'
x = input()
matches = re.findall(pattern, x)
print(x)
#ex5
import re
pattern = 'a.*b$'
x = input()
matches = re.findall(pattern, x)
print(x)
#ex6
import re
text = input()
pattern = '[ ,.]'
replaced_text = re.sub(pattern, ':', text)
print(replaced_text)
#ex7
import re
snake = input()
pattern = re.compile(r'(_\w)')
camel = re.sub(pattern, lambda x: x.group(1)[1:].upper(), snake)
print(camel)
#ex8
import re
x = input()
pattern = '[A-Z][^A-Z]*'
split_strings = re.findall(pattern, x)
print(' '.join(split_strings))
#ex9
import re
x = input()
pattern = re.compile(r'(?<=[a-z])([A-Z])')
space = re.sub(pattern, r' \1', x)
print(space)
#ex10
import re
camel = input()
pattern = re.compile(r'(?<!^)(?=[A-Z])')
snake_case_string = re.sub(pattern, '_', camel).lower()
print(snake)