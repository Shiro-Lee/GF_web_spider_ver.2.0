INSTRUCTION = \
    "  1.输入萌娘百科（https://zh.moegirl.org）上人形的对应名称（必须相同，如9A91×/9A-91√），点击【确定】开始下载\n" + \
    "  2.为防反爬并避免对萌百服务器造成压力，文件下载速度限制在每4秒下载一次，4秒间可以使用【暂停/继续】（虽然我自己也不知道设置这个有什么用？）\n" + \
    "  3.当下载长时间无反应时会自动更换ua继续尝试下载，若多次无反应可通过【操作->重置】下载另一名人形语音或过一段时间再尝试下载。\n" + \
    "  4.每个人形的语音文件夹存放在【GFL Voice Downloader.exe】所在目录下。\n" + \
    "  5.下载过程中不要改动语音文件夹内【url_finished.txt】以及【url_unfinished.txt】两个文件的内容" + \
    "（除非手动选择下载哪些语音，将其他url从【url_unfinished.txt】删除），下载完成后会自动删除两个文件。" + \
    "只要两个文件还在，下次打开程序下载同一个人形语音文件时会从当前进度继续下载。\n" + \
    "  6.不要删了【head.gif】不然程序启动不了。不管出现了什么错误重启程序避免错误操作应该就没事了（"

ABOUT = \
    "  1.本爬虫程序由【黒雛°】于百度【少女前线】吧发布，仅限个人使用与学习交流，禁止商用（不过做得这么菜应该不会有人商用…吧），可在上述前提下自由传播。\n" + \
    "  2.程序使用纯Python编写，用tkinter模块完成GUI界面，用urllib及re模块进行爬虫处理。\n" + \
    "  3.由于本人能力有限，程序可能还存在一些bug（GUI和多线程是边学边做的…）。" + \
    "源程序py文件已附在【源代码】文件夹内，欢迎各路dalao对程序进行有益的改进。如有相关疑问可在贴吧内私信或本人相关水贴楼内回复。\n" + \
    "  4.感谢各位指挥官的使（shì）用。\n" + \
    "  5.416我老婆，不接受反驳！\n"


welcome = [
    "鼻梁脱销，谢谢你们。",
    "蛇佬今天又双叒叕发情了吗？",
    "天王盖地虎，宝塔镇河妖。416胸口，藏着小怪兽。",
    "YMFM，谁同意，谁反对？",
    "指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官\
指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官\
指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官指挥官",
    "只要不断翀钱，少女前线的末日就不会来临。\n所以说，不要停下来啊……！！",
    "夜は焼き肉っしょ！アッハッハッハッ...",
    "人类的悲欢并不相通,我只觉得他们吵闹。",
    "while True:\n    print(input())",
    "Jμsτ Ｍσηíкǎ",
    "人不能操狗，至少不该操。",
    "大家好，我是本群的提醒红茶小助手。希望此刻看到消息的人可以和我一起来快速泡红茶。及时灌后辈红茶，记得要雷普。\
一小时后我会继续提醒大家泡红茶，和我一起成为一天雷普后辈八次的人吧！"
]

