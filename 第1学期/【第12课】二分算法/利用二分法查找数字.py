# CH4.3-P101利用二分法查数字
x = int(input("请输入要查找的1000以内的整数:"))
step = 0  # 查找次数
flag1 = 1  # 目标区域左边界
flag2 = 1000  # 目标区域右边界
while flag1 <= flag2:  # 区间左边界不大于右边界则执行
    mid = (flag1 + flag2) // 2  # 表示区间中间值
    step = step + 1  # 查找次数加1
    if mid > x:  # 区域中间值大于目标数
        flag2 = mid - 1  # 范围往左侧区域找···右边界前移
    elif mid < x:  # 区域中间值大于目标数
        flag1 = mid + 1  # 范围往右侧区域找···左边界后移
    else:
        break
print("查找次数为：", step)
input("运行完毕，请按回车键退出...")
