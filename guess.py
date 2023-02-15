import random

min = int(input('請決定隨機數字範圍開始值'))
max = int(input('請決定隨機數字範圍結束值'))
r = random.randint(min, max)
i = 0

while True:
	user = int(input('請猜數字: '))
	i = i + 1 
	if r == user:
		print('你猜對了!')
		print('這是你猜的第', i, '次')
		break
	elif user > r:
		print('數字太大')
	else:
		print('數字太小')
	print('這是你猜的第', i, '次')	
