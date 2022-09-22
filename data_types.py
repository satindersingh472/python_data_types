string_one = "this is the first string with single quotes"
string_two = "this is the second string with double quotes test"

if (string_one.endswith("test") or string_two.endswith('test')):
    print('found test')
else:
    print('no test')