'''
Author: Daylight 
Date: 2021-02-01 20:18:57
LastEditTime: 2021-02-01 20:38:45
LastEditors: Please set LastEditors
Description: Practice for dictionaries in python
FilePath: \python\6_1.py
'''
#todo 字典（简单的字典）
alien_0 = {'color': 'green', 'point': 5} #! 保存两个键值
alien_1 = {'colors': 'red'}              #! 最简单的字典

print(alien_0['color'])   #? 输出字典的某个键值的方法
print(alien_0['point'])

#todo 假设你射杀了一个外星人，将返回你取得的分数(访问字典中的值)
new_points = alien_0['point']
print(f"You just earned {new_points} points!\n")

'''
 添加键值对(往字典中添加一个键值对):例子，假如要显示外星人在屏幕中的位置，而开始一般在屏幕的
 左上方,需要显示x,y的坐标
'''
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
