import yagmail

#链接邮箱服务器
yag = yagmail.SMTP(
    user="zhuhuilingisman@sina.com",
    password="cbab7c5961b80f65",#授权码
    host='smtp.sina.com'
)

#邮件正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']

#发送邮件
yag.send(
    #如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='123@qq.com'
    to=['zhu_huiling.pfu@cn.fujitsu.com', '841940856@qq.com', 'zhuhuilingisman@126.com'],
    #抄送
    cc='zhuhuilingisman@126.com',
    #邮件标题
    subject='学习发送邮件',
    #邮件正文
    contents=contents,
    #附件
    attachments=[r"F://test1.txt", r"F://test2.txt"]
)

#关闭
yag.close()