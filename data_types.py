string_one = "this is the first string with single quotes"
string_two = "this is the second string with double quotes test"
list_numbers = [11,10,33,54,44,5454,34,66,433,677,5,534,4453,454556,2,5,0,]

if (string_one.endswith("test") or string_two.endswith('test')):
    print('found test')
else:
    print('no test')

for each_number in list_numbers:
    if(each_number > 10):
        print(each_number, ': Large')
    elif(each_number <= 10):
        print(each_number,':Not Large')
