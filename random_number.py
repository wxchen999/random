import random
start = input('請決定起始值')
end = input('請決定最後一個數值')
start = int(start)
end = int(end)
r = random.randint(start, end)

count = 0

while True:
	count = count + 1

	guess = input('請猜一個數字')
	guess = int(guess)
	if guess == r :
		print('終於猜對了')
		print('這是你猜的', count, '次')
		break
	elif guess > r:
		print('比答案大')
		
	elif guess < r:
		print('比答案小')
	print('這是你猜的', count, '次')

		