import re

document = input()
expression = re.compile(input())

matches = expression.findall(document)

print(len(matches))
