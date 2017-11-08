list1 = []
enter = input('Enter name: ')
list1.append(enter)
print(list1)
#change it so it prints the list to a text file
with open ('test_git.txt', 'w'):
    for line in list1:
        a.write(list1)
