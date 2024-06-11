import requests
# import json
#
# url = "https://test-mx-gateway.teemopay.com/api/pay/payment/create/v1"
#
# payload = json.dumps({
#   "merchantOrderNo": "o1t9j3s8x93k512txm268at219v30a00",
#   "realName": "XinXu",
#   "amount": "1000",
#   "callbackUrl": "https://sandbox.presimex.mx/api/user/public/teemopay/payment/callback/78f04feca0c5581628508b156d364fc0",
#   "paymentType": 1,
#   "email": "1015922891@qq.com",
#   "phone": "13175025808",
#   "sign": "QRcD1SNmv9SEQJSJX47fsbfsVDG5hbdg+K/cb3Wa12EBeJR+MTwx0emuBvAxWLQ53tu3QNj0jQAGPInEoCDAJi7TpaIJwtXxtLqGc/elMD/5j6TE3KAWINt5uREGonY8XSesaF7HO63yFuDAd6DBi0a/wYF1eK2eyUQyJC6aeS4="
# })
# headers = {
#   'timestamp': '1709102586001',
#   'nonce': 'jHVtrauIf364QdDRwwrBuFISISyyY6UC',
#   'country': 'MX',
#   'app_code': 'A2404010004MX001',
#   'Content-Type': 'application/json'
# # }
#
# # response = requests.request("POST", url, headers=headers, data=payload)
# response = requests.post(url, headers=headers, data = payload)
# # 打开图片 r---只读，b----二进制格式,上传文件，post(file = data)
# # open("文件路径","rb")
# print(response.text)
import logging
# 设置级别
logging.basicConfig(level=logging.DEBUG)
logging.info("不设置级别默认info")






import base64
import email
from email.header import decode_header
from imapclient import IMAPClient


def decode_str(hs):
    """
    编码处理
    """
    if isinstance(hs, bytes):
        hs = hs.decode()
    if hs:
        if hs[0] == "=":
            s, de = decode_header(hs)[0]
            encoding = de or 'utf-8'
            failout = base64.b64decode(s).decode(encoding, errors='ignore')
            return failout
        else:
            return hs
    return ''


# 邮箱登录
email_address = 'baoshoujia@outlook.com'  # 邮箱地址
password = '1079049924bao'  # 密码

# 连接邮箱服务器
imapObj = IMAPClient('imap.outlook.com', ssl=True)
imapObj.login(email_address, password)

# 选择收件箱并搜索邮件
imapObj.select_folder('INBOX')
UIDs = imapObj.search(['SUBJECT', 'Teemopay'])

data = imapObj.fetch(UIDs[0], ['BODY[]'])
raw_email = data[UIDs[0]][b'BODY[]']
msg = email.message_from_bytes(raw_email)
print(msg)
subject = decode_str(msg.get('Subject'))
sender = decode_str(msg.get('From'))
# # 获取邮件内容
# if UIDs:
#     for uid in UIDs:
#         data = imapObj.fetch(uid, ['BODY[]'])
#         raw_email = data[uid][b'BODY[]']
#         msg = email.message_from_bytes(raw_email)
#
#
#         # 解析邮件内容
#         subject = decode_str(msg.get('Subject'))
#         sender = decode_str(msg.get('From'))
#
#         body = ''
#         if msg.is_multipart():
#             for part in msg.walk():
#                 content_type = part.get_content_type()
#                 content_disposition = str(part.get("Content-Disposition"))
#                 try:
#                     body += part.get_payload(decode=True).decode()
#                 except:
#                     pass
#         else:
#             content_type = msg.get_content_type()
#             body = msg.get_payload(decode=True).decode()
#
#         # 打印邮件内容
#         print("Subject:", subject)
#         print("From:", sender)
#         print("Body:", body)
#
# # 关闭邮箱连接
# imapObj.logout()