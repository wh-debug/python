'''
Author: Daylight
Date: 2021-02-13 21:22:48
LastEditTime: 2021-02-13 21:32:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_4_1.py
'''
'''在函数中修改列表'''

'''
2021年2月13日21:31:19
下面的代码输出：
Printing model: dodecahedron.
Printing model: robot pendant.
Printing model: phone case.

The following models have been printed:
dodecahedron
robot pendant
phone case

主要是修改列表，具体是将一个列表复制到另一个列表

'''
unprinted_desingns = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_desingns:
    current_design = unprinted_desingns.pop()
    print(f"Printing model: {current_design}.")
    completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)