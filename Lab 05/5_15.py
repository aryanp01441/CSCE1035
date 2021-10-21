user_text = input()

''' Type your code here. '''
text = ""

text = user_text.replace(" ", "")
text = text.replace(",", "")
text = text.replace(" ", "")
text = text.replace(".", "")
text = text.replace("!", "")
print(len(text))