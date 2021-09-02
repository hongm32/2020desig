import tkinter
import datetime

root = tkinter.Tk()
root.geometry('300x100')
root.title("数据安全性测试")


def jiemi():
    d1 = datetime.datetime.now()  # 获取当前系统时间d1
    p = varin.get()  # 获取输入文本框的数字密码
    if p.isdigit():
        p = int(p)
    else:
        return
    for i in range(0, p + 1):  # 从0循环到正确密码数值
        if i == p:  # 如果密码相同
            d2 = datetime.datetime.now()  # 获取当前系统时间d2
            d = d2 - d1  # 取得时间差
            # 在输出文本框中显示解密用时
            vartime.set(str(d.seconds) + "秒" + str(d.microseconds / 1000) + "毫秒")
            varout.set(i)


frm = tkinter.Frame(root)
# left
frm_L = tkinter.Frame(frm)
tkinter.Label(frm_L, text='输入密码：', font=('Arial', 10)).pack()
tkinter.Label(frm_L, text='破解用时：', font=('Arial', 10)).pack()
tkinter.Label(frm_L, text='你的密码是：', font=('Arial', 10)).pack()
frm_L.pack(side=tkinter.LEFT)

# right
frm_R = tkinter.Frame(frm)
varin = tkinter.StringVar()
vartime = tkinter.StringVar()
varout = tkinter.StringVar()
tkinter.Entry(frm_R, show='*', textvariable=varin).pack()
tkinter.Entry(frm_R, textvariable=vartime, state="disabled").pack()
tkinter.Entry(frm_R, textvariable=varout, state="disabled").pack()
frm_R.pack(side=tkinter.RIGHT)
frm.pack()

tkinter.Button(root, text="破解", command=jiemi, relief="solid", width=10).pack()
root.mainloop()
