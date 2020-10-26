from tkinter import *
from tkinter.messagebox import *
from function import *
from message import *
from threading import *
from time import sleep
from flags import Flags

flags = Flags()


def refresh():
    """更换ua"""
    flags.ua = get_ua()
    insert_info(info_box, '\n下载重置。\n')
    insert_info(info_box, '更换ua为：' + flags.ua + '\n\n')


def reset():
    """重置下载状态"""
    name_ent.config(state=NORMAL)
    confirm_but.config(state=NORMAL)
    con_pau_but.config(state=DISABLED)
    info_box.config(fg='springgreen', selectforeground='red')
    con_pau_but.config(text='-暂停-', state=DISABLED)
    if not flags.downloading:
        insert_info(info_box, '\n下载重置。\n\n')
    flags.con_pau_flag = False
    flags.downloading = False
    flags.exit_thread_flag = True


def instruction():
    """弹出使用说明消息框"""
    inst_win = Toplevel(root)
    inst_win.title('操作说明')
    inst_win.geometry('+520+220')
    inst_win.minsize(450, 320)
    inst_win.maxsize(450, 320)
    inst_lb = Label(inst_win, text=INSTRUCTION, width=55, wraplength=390, justify=LEFT, font=('黑体', 11))
    inst_lb.place(x=5, y=10)


def about():
    """弹出关于消息框"""
    ab_win = Toplevel(root)
    ab_win.title('关于')
    ab_win.geometry('+560+220')
    ab_win.minsize(450, 225)
    ab_win.maxsize(450, 225)
    ab_lb = Label(ab_win, text=ABOUT, width=55, wraplength=390, justify=LEFT, font=('黑体', 11))
    ab_lb.place(x=5, y=10)


def insert_info(info_box, info):
    """向文本消息框中添加信息"""
    info_box.config(state=NORMAL)
    info_box.insert(END, info)
    info_box.config(state=DISABLED)
    info_box.see(END)


def download_end(fin_file_name, unfin_file_name):
    """下载正常终止"""
    if os.path.exists(fin_file_name):
        os.remove(fin_file_name)
    if os.path.exists(unfin_file_name):
        os.remove(unfin_file_name)
    reset()
    exit()


def chg_state():
    """暂停/继续"""
    flags.con_pau_flag = not flags.con_pau_flag
    if flags.con_pau_flag:
        con_pau_but.config(text='-暂停-')
        info_box.config(fg='springgreen', selectforeground='red')
        insert_info(info_box, '「そして、時は動き出す——」\n\n')
    else:
        con_pau_but.config(text='-继续-')
        info_box.config(fg='red', selectforeground='green')
        insert_info(info_box, '\n「The world！時よ止まれ！」\n\n')


def get_all_voice(ua, folder_name):
    """下载存储于voice_url.txt中url指向的文件"""
    headers = {'User-Agent': ua}
    fin_file_name = folder_name + '/' + "url_finished.txt"
    unfin_file_name = folder_name + '/' + "url_unfinished.txt"

    with open(unfin_file_name, 'r+') as unfinished, open(fin_file_name, 'r') as finished:
        url = unfinished.readline().rstrip()
        i = len(finished.readlines())+1  # 当前下载文件序号
        count = len(unfinished.readlines())+i  # 所需下载文件总数

    while url:
        if flags.exit_thread_flag:
            flags.exit_thread_flag = False
            exit()
        if not flags.con_pau_flag:
            sleep(2)
            continue
        file_name = url.split('/')[-1]  # 取处于url最后位置的文件名
        con_pau_but.config(state=DISABLED)
        flags.downloading = True  # 标识开始下载
        info = '(' + str(i) + '/' + str(count) + ')' + '-下载文件：' + file_name
        insert_info(info_box, info)
        result = get_voice(url, headers, folder_name, file_name, flags)
        if not result:  # 下载异常（反爬）时更换ua
            refresh()
            continue
        if flags.exit_thread_flag:  # 判断下载过程中重置否
            con_pau_but.config(state=DISABLED)
            insert_info(info_box, '下载重置。\n\n')
            con_pau_but.config(state=DISABLED)
        else:
            insert_info(info_box, '  下载完成\n')
            con_pau_but.config(state=NORMAL)
        flags.downloading = False
        if flags.exit_thread_flag:  # 若重置标识为True，退出当前线程
            exit()
        i += 1
        with open(fin_file_name, 'a') as fin:  # 写入已下载文件url
            fin.write(url + '\n')
        update(unfin_file_name)  # 从voice_unfinished.txt中删去第一行（即刚下载好的文件的url）
        with open(unfin_file_name, 'r+') as unfinished:  # 读取下一条待下载文件的url
            url = unfinished.readline().rstrip()
        if flags.exit_thread_flag:
            exit()
        sleep(4)  # 暂停4秒防反爬

    insert_info(info_box, '\n下载结束。\n')
    download_end(fin_file_name, unfin_file_name)


def run():
    flags.con_pau_flag = False
    flags.exit_thread_flag = False
    name = name_ent.get()
    if name == '':
        return
    try:
        confirm_but.config(state=DISABLED)
        name_ent.config(state=DISABLED)
        page_url = get_page_url(name)
        flags.ua = get_ua()
        page_html = get_page_html(page_url, flags.ua)
    except urllib.request.HTTPError:
        showwarning('错误', '人形名称不正确（或者该人形页面暂不存在）')
        name_ent.config(state=NORMAL)
        confirm_but.config(state=NORMAL)
    else:
        info = '\n-找到萌百人形页面url：' + page_url + '\n\n' + \
            '-使用UA：' + flags.ua + '\n\n'
        confirm_but.config(state=DISABLED)
        con_pau_but.config(state=NORMAL)
        flags.con_pau_flag = True
        insert_info(info_box, info)
        # 新建人形语音存放文件夹
        is_exists = os.path.exists(name + '/url_unfinished.txt')
        if not is_exists:
            html_code = page_html.decode('utf-8')
            mkdir(name)
            get_voice_url(html_code, name)   # 获取所有语音地址，存入voice_url.txt
        get_all_voice(flags.ua, name)


def new_thread():
    flags.t = Thread(target=run)
    flags.t.setDaemon(True)
    flags.t.start()


# 主窗口
root = Tk()
root.title('少前语音爬虫ver.2.0')
root.config(bg='#2b2b2b')
# 设定主窗体相对于屏幕的初始位置
root.geometry('+540+200')
# 设定最小尺寸等于最大尺寸，使主窗体大小不可变
root.minsize(520, 330)
root.maxsize(520, 330)

# 菜单栏
main_menu = Menu(root)
menu_fun = Menu(main_menu, tearoff=False)
menu_help = Menu(main_menu, tearoff=False)
# 子菜单-操作
main_menu.add_cascade(label='操作', menu=menu_fun)
menu_fun.add_command(label='重置', command=reset)
# 子菜单-帮助
main_menu.add_cascade(label='帮助', menu=menu_help)
menu_help.add_command(label='操作说明', command=instruction)
menu_help.add_command(label='关于', command=about)
# 加入菜单栏
root.config(menu=main_menu)

# 窗体内的标题
head_img = PhotoImage(file='head.gif')
head = Label(root, image=head_img)
head.place(x=-2, y=0)

# 文本标签-人形名称
name_lb = Label(root, text='人形名称：', font=('方正姚体', 14), bg='#2b2b2b', fg='white')
name_lb.place(x=90, y=84)

# 输入框-人形名称
name_ent = Entry(font=('黑体', 16), width=15)
name_ent.place(x=185, y=86)

# 按钮-人形确认
confirm_but = Button(text='确定', font=('方正姚体', 12), bd=1, relief=RIDGE, command=new_thread, bg='#f7b022')
confirm_but.place(x=365, y=84)

# 按钮-暂停/继续
con_pau_but = Button(text='-暂停-', font=('方正姚体', 12), width=18, bd=1, relief=RIDGE, state=DISABLED, command=chg_state, bg='#f7b022')
con_pau_but.place(x=185, y=123)

# 文本框-输出信息
welcome_msg = welcome[randint(0, len(welcome) - 1)]
info_box = Text(root, width=60, height=10, font=('黑体', 11), bg='black', fg='springgreen',
                selectbackground='white', selectforeground='red')
info_box.place(x=18, y=160)
insert_info(info_box, welcome_msg + '\n')

root.mainloop()
