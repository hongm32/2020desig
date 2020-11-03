# 二分法求函数f的近似解
# 4.3.5：P105-拓展练习2-求方程近似值
# 尝试用二分法求解方程x^3-X^2+x-1=0

def f(x):
    return x ** 3 - x ** 2 + x - 1


# 要保证 fun(x1) * fun(x2) < 0 才能确认方程在(x1, x2)内有解
x1 = -100000
x2 = 3000000
x0 = (x1 + x2) / 2
while x2 - x1 >= 1e-13:
    x0 = (x1 + x2) / 2
    if f(x1) * f(x0) < 0:  # 函数f在（x1, x0)有解
        x2 = x0
    elif f(x2) * f(x0) < 0:  # 函数f在（x0, x2)有解
        x1 = x0

print("方程解为：", x0)
input("运行完毕，请按回车键退出...")
