import random, os, time
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

'''menu code'''

def xunhuan():
    os.system('cls')
    forif = input('''root@main > 测试类型:(for/while/exit)''')
    if forif == 'for':
        inp = 0
        for i in range(3):
            print('''
            for 循环测试
            次数 %s''' %inp)
            inp = inp + 1
            time.sleep(0.5)
        print('''
        循环了3次
        语法:
        
        for <变量> in range(<次数>):
            <code>
            ''')
        xunhuanin = input('''按Enter继续''')
        os.system('cls')
        xunhuan()
    elif forif == 'while':
        inp = 0
        while inp <= 2:
            inp = inp + 1
            print('''
            while 循环测试
            次数 %s''' %inp)
            time.sleep(0.5)
        print('''
        循环了%s次
        语法:
        
        while <方法>
            <code>
            ''' %inp)
        xunhuan()
    elif forif == 'exit':
        main()


def jsq():
    os.system('cls')
    hight = float(input('root@jsq> 你的身高（M ）:'))
    wight = float(input('root@jsq> 你的体重（KG）:'))
    total = wight/(hight*hight)
    input('你的BMI值约为{:.2f}'.format(total))

def dint():
    def rebackrest():
        os.system('cls')
        print('信息科好玩吗\n')
        for i in range(4):
            dinto = ['好玩', '不好玩', '还行']
            result = random.choice(dinto)
            print(result)
            time.sleep(0.5)
        print('''
        语法: 
        <变量> = ['<内容>']
        <变量> = random.choice(<字典>)''')
        reback = input('\n按Enter继续 输入re继续> ')
        if reback == 're':
            rebackrest()
        else:
            main()
    rebackrest()

def game():
    os.system('cls')
    all_choice = ['石头', '剪刀', '布']
    win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
    prompt = """
    [1] 石头
    [2] 剪刀
    [3] 布

    root@game1 >选项（0/1/2）:
    """
    player_win = 0
    pc_win = 0
    while player_win < 2 and pc_win < 2:
        pc = random.choice(all_choice)
        ind = int(input(prompt))
        player = all_choice[ind]

        print("你出的拳是：%s,计算机出的拳是： %s" % (player, pc))
        if player == pc:
            print('\033[32m平局\033[0m')
        elif [player, pc] in win_list:
            print('\033[32m你赢了\033[0m')
            player_win += 1
        else:
            print('\033[31m你输了\033[0m')
            pc_win += 1
            
def gui():
    print('''
    GUI开发需要tkinter库
    基本组件有Label,Button,Menu,Fram
    可以通过pip install tkinter安装
    这里不行多说''')
    message.showinfo('须知', 'GUI开发需要tkinter库\n基本组件有Label,Button,Menu,Fram\n可以通过pip install tkinter安装\ng这里不行多说')
    
    def button1com():
        message.showinfo('你好', '这将会是你的第一个Windows窗口')
    
    tk = Tk()
    tk.maxsize()
    tk.title('gui窗口')
    
    Label1 = tk.Label(tk, text='非常简单的一个Windows窗口')
    Label1.pack
    
    Button1 = tk.Button(tk, text='按钮能干啥', command=button1com)
    Button1.pack
    
    tk.mainloop()


def importa():
    print('这不能告诉你')

def main():
    os.system('cls')
    menu1 = print('''
    信息科内容
    [1]for 与 while循环
    [2]计算器
    [3]字典与随机
    [4]终端交互
    [5]可视化交互
    [6]库的原理
    [7]须知
    [8]python之父的话
    ''')

    menu = input('root@main>')

    if menu == '1':
        xunhuan()
    
    elif menu == '2':
        jsq()

    elif menu == '3':
        dint()
        
    elif menu == '4':
        game()
        
    elif menu == '5':
        gui()
    
    elif menu == '7':
        message.showinfo('警告', "该程序使用原生库，方便易学\n总结了该学期所学课程，不要盗代码！！！")
        
    elif menu == '8':
        import this
        
    else:
        print('\033[31m error 1\033[0m')
        main()
    
main()