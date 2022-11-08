i = int(input("请输入一个数字: "))
while i>6:
    print(f"你输入的数字是{i}, {i}大于6,符合计算条件，{i}+8的计算结果为：{i+8}")
    break
else:
    print ("你输入的数字小于6，不符合计算条件，请重新输入")