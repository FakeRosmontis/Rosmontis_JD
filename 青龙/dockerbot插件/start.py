from telethon import events
from .. import jdbot, chat_id,ch_name


@jdbot.on(events.NewMessage(from_users=chat_id, pattern='/start'))
async def bot_start(event):
    '''接收/start命令后执行程序'''
    msg = '''使用方法如下：
    /help - 帮助
    /a - 快捷命令
    /set - BOT设置
    /bean - 获取收支表格
    /chart - 获取变化图表
    /env - 管理环境变量
    /addenv - 添加环境变量
    /cron - 管理定时设定
    /addcron - 增加定时任务
    /edit - 从目录选择文件并编辑，需要将编辑好信息全部发给BOT，BOT会根据你发的信息进行替换。建议仅编辑config或crontab.list，其他文件慎用！！！
    /log - 查看日志
    /setshort - 快捷按钮设定
    /clearboard - 删除快捷按钮
    /setname - 设置命令别名
    /dl - 下载文件
    /getfile - 获取data目录下文件
    /reboot - 重启BOT
    /start - 开始使用本程序
    /node - 执行js脚本，输入/node xxxxx.js。如执行非scripts目录js，需输入绝对路径执行。node命令会等待脚本执行完，期间不能使用BOT，建议使用snode命令。
    /snode - 选择脚本执行，只能选择/scripts和/own目录下的脚本，选择完后直接后台运行，不影响BOT响应其他命令。 

    此外，直接发送文件至BOT，会让您选择保存到目标文件夹，支持保存并运行。'''
    await jdbot.send_message(chat_id, msg)

if ch_name:
    jdbot.add_event_handler(bot_start,events.NewMessage(from_users=chat_id, pattern='开始'))
