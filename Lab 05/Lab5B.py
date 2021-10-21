import random

num = random.randint(1, 50)

count = 1
i = 1
while i != 6:
	user_num = int(input('Guess #{}: '.format(count)))
	if user_num > num:
		print('Too high. Try a lower number.')
	if user_num < num:
		print('Too low. Try a higher number.')
	if count == 5:
		break;
	if user_num == num:
		break;
	count = count + 1
	
if count == 5 and user_num != num:
	print('Sorry you have run out of guesses. The secret number was', num)
else:
	print('Nice job! You guessed my secret number in', count, "guesses!")