
import jwt
import time
import os
from jwt import algorithms

# 秘钥，用于签名和验证JWT
# SECRET_KEY = "your-secret-key"
SECRET_KEY = os.urandom(32)

# 载荷数据，通常包含关于用户的信息
payload = {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": int(time.time()),  # 发布时间
    "exp": int(time.time()) + 60*60  # 过期时间，设置为1小时后
}

# 使用HS256算法创建JWT
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("Encoded JWT:", token)


try:
    # 解码并验证JWT
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print("Decoded Payload:", decoded_payload)
except jwt.ExpiredSignatureError:
    print("Token has expired.")
except jwt.InvalidTokenError:
    print("Invalid token.")