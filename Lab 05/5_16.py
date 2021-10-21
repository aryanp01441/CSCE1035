word = input()
password = ''

''' Type your code here. '''
password = word.replace("i", "1")
password = password.replace("a", "@")
password = password.replace("m", "M")
password = password.replace("B", "8")
password = password.replace("s", "$")
print(password + "!")