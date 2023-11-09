'''
第三方配置
'''

# 互亿无限短信配置
HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': 'C62019458',
    'password': '39a676c45cf4a5ec4fab223c7c52a011',
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile': None,
    'format': 'json'
}

# 七牛云配置
QN_ACCESS_KEY = 'Qb_Q9sIhM3dLYcW5L6ITshySnkluI-bRxJHSNXUS'
QN_SECRET_KEY = 'znwOhmZ9R8KWInv1paFRBkyL9gAhZpeDRNe9QcfN'
QN_BUCKET_NAME = 'test159203'
QN_BASE_URL = 'http://s3plf9l1k.hn-bkt.clouddn.com'
