import random

r = random.randint(1, 100)
i = []

while True:
	user = int(input('請猜數字: '))
	if r == user:
		print('你猜對了')
		break
	elif user > r:
		print('數字太大')
		continue
	else:
		print('數字太小')
		continue	
