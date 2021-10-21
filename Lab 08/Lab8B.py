import Lab8A

def replace_word(sentence, target, replace):
    split_sentence = sentence.split()
    i = 0
    while i < len(split_sentence):
        if split_sentence[i] == target:
            split_sentence.remove(target)
            split_sentence.insert(i, replace)
        i += 1
    joined_sentence = ' '.join(split_sentence)
    return joined_sentence

user_sentence = input('Enter a sentence: ')
user_target = input('Enter a word in sentence to replace: ')
user_replace = input('Enter a replacement word: ')
print('Here is the new sentence: ', replace_word(user_sentence, user_target, user_replace))
user_letter = input('Enter letter to remove from sentence: ')
Lab8A.remove_letter(replace_word(user_sentence, user_target, user_replace), user_letter)