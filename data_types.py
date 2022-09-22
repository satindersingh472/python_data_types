string_one = "this is the first string with single quotes test"
string_two = "this is the second string with double quotes"

if (string_one.endswith('test') or string_two.endswith('test')):
    print('found test')
else:
    print('no test')