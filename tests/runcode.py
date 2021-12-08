text = "Sachin Ramesh Tendulkari"
output = "S.R. Tendulkar"

count = 0
out = ''
for char in text:
    if char == ' ':
        count += 1
space = 0
for char in text:

    if char.islower() and space < count:
        pass

    elif char == ' ':
        out += '.'
        space += 1
    else:
        out += char
