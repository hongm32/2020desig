def match_num(num):
    f = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]  # 0-9的数字分别需要多少根小棒
    if num == 0:  # 火柴棒总数变量赋初值
        total = f[0]
    else:
        total = 0
    while num > 0:
        x = num % 10  # 取num除以10的余数，即num的个位数
        total = total + f[x]  # 所需火柴棒数累加
        num = num // 10	 # num整除10，即去掉num的个位数
    return total  # 返回需要多少根火柴棒数


# 以下为主程序
snum = 6  # 6根火柴棒
print("你可以拼出这些数字：")
for i in range(112):
    if match_num(i) == snum:  # 如果i需要的火柴棒数等于现有火柴棒数
        print(i)

input("运行完毕，请按回车键退出...")
