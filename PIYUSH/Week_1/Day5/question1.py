String2 = input('Enter the string :')
count = 0
String = String2.lower()
for i in String2:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count+=1
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))
