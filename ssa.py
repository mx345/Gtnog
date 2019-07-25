#!/usr/bin/env python
#-*- coding: utf-8 -*- 
# File Name: ssa.py
# Author :马勋
# Email:maxunnm12@163.com
# Created Time:Wed 17 Jul 2019 09:04:42 PM CST
# Last Time: Wed 17 Jul 2019 09:04:42 PM CST
import random
import time

n = random.randint(2, 8)
start_time = time.time()  # 获取系统当前时间戳（即距离1970年1月1日0时0分0秒的秒数）
cnt = 1
time_difference=0
while True:
	# 循环体
	if cnt == 1:
		i = int(input("\n请猜一个数字(0-9)："))
	else:
		i = int(input("\n请再猜一个数字(0-9)："))

	if i == n:
		end_time = time.time()
		time_difference=end_time-start_time
		print("恭喜你猜对了!(次数:"+str(cnt)+",耗时:"+str(int(time_difference))+"秒)")
		if 1<=time_difference<=20:
			if 1<=cnt <=3 :
				print("你很棒!")
			elif 4<=cnt<=8:
				print("你还行!") 
			elif 8<=cnt<=15:
				print("继续努力吧")
		elif 20<=time_difference<=100:
			if 1<=cnt<=20:
				print("要加油啊")
			elif cnt>20:
				print("你运气很差") 
		break  # 结束当前循环结构，执行循环的后续语句
		# continue  # 结束本轮循环，继续执行下一轮循环
	elif i > n:
		# 代码块(Code Block)，即若干行语句构成的一个整体，同一个代码块中的语句要使用相同的缩进
		print("偏大")
		#print("你猜错了！")
	else:
		pass  # 空语句，啥也不干，用在这里是为了满足语法规则要求
		pass
		print("偏小")
	
	cnt += 1

pass
print("程序运行结束！")

