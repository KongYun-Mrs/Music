from itsdangerous import URLSafeTimedSerializer as utsr, SignatureExpired, BadSignature
import base64
import re

class Token:
    def __init__(self,secret_key):
        self.secret_key = secret_key
        self.salt = base64.encodebytes(self.secret_key.encode('utf8')).decode('utf8')
    def generate_validate_token(self,uid):
        #序列化对象
        serilizer = utsr(self.secret_key)
        #返回token值
        return serilizer.dumps(uid,self.salt)

    def confirm_validate_token(self,token,expiration=3600):
        # 序列化对象
        serilizer = utsr(self.secret_key)
        try:
            res = serilizer.loads(token, salt=self.salt, max_age=expiration)
        except SignatureExpired:  #token过期
            return -1
        except BadSignature:
            return -2
        except:
            return -3
        return res

if __name__ == "__main__":
    token = Token('9jpj+-tv$-ycufkvdh=x#)m#tv+m%m895kogwuo&%xqd$j3y8s')
    print(token.salt)
    s = token.generate_validate_token(10)
    print(s)
    res = token.confirm_validate_token(s)
    print(res)
