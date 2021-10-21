def remove_letter(sentence, letter):
    new_sentence = ''
    i = 0
    while i < len(sentence):
        if sentence[i] == letter:
            new_sentence += ''
        else:
            new_sentence += sentence[i]
        i += 1
    if len(sentence) == len(new_sentence):
        print('No letter', letter, 'removed from:', sentence)
    else:
        print('New sentence with letter', letter, 'removed:', new_sentence)

if __name__ == "__main__":
    user_sentence = input('Enter a sentence: ')
    user_letter = input('Enter letter to remove from sentence: ')
    remove_letter(user_sentence, user_letter)