# 用户输入判断和pass关键字
while True:
    # 显示功能菜单
    action_str = input("请选择希望执行的操作：")
    print("你的选择是【%s】" % action_str)
    if int(action_str) == 0:
        print("退出系统,欢迎再次使用")
        break
    elif int(action_str) == 1:
        print("新建名片")
    elif int(action_str) == 2:
        print("显示全部")
    elif int(action_str) == 3:
        print("查询名片")
    else
        print("输入错误，请输入正确的步骤代号")

# OPENCV\numpy\shut