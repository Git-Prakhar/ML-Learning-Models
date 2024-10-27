import re

# expression = r"(^|\W)\$[0-9]+(\.[0-9][0-9])?\b"
# text = '$99'
# match = re.search(expression, text)
# print(match)

pattern = r'([0-9]+)'
replacement = r'<\1>'
text = '1 added by 10 is equal to 11'

replaced = re.sub(pattern, replacement, text)

print(replaced)