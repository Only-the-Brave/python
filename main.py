# 用户输入判断和pass关键字
import zds_02tool名片
while True:
    zds_02tool名片.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("你的选择是【%s】" % action_str)
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            zds_02tool名片.new_card()
        # 显示全部
        elif action_str == "2":
            zds_02tool名片.show_all()
        # 查询名片
        elif action_str == "3":
            zds_02tool名片.search_card()
    elif action_str == "0":
        print("退出系统，欢迎再次使用名片管理系统")
        break
    else:
        print("输入错误，请输入正确的步骤代号")

