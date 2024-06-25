Python中有多个库可以帮助你实现OAuth2登录授权，以下是一些常用的库：

1. **requests-oauthlib**：这是一个基于`requests`库的OAuth客户端实现，支持OAuth 1.0和OAuth 2。它简化了OAuth的流程，让你可以很容易地与各种OAuth服务提供商集成。使用这个库，你可以快速实现如Google、Facebook等的OAuth2登录。

   安装命令：`pip install requests-oauthlib`

   示例代码：
   ```python
   from requests_oauthlib import OAuth2Session
   from oauthlib.oauth2 import BackendApplicationClient
   import requests

   client_id = 'your_client_id'
   client_secret = 'your_client_secret'

   client = BackendApplicationClient(client_id=client_id)
   oauth = OAuth2Session(client=client)
   token = oauth.fetch_token(token_url='https://example.com/oauth2/token', client_id=client_id, client_secret=client_secret)

   response = oauth.get('https://example.com/api/resource')
   ```

2. **authlib**：Authlib是一个全面的OAuth和OpenID Connect库，支持客户端和服务器端的实现。它不仅支持OAuth 1.0和OAuth 2的各种流程，还提供了Flask、Django等框架的集成，使得在这些框架中实现OAuth认证变得非常简单。

   安装命令：`pip install Authlib`

   示例代码（使用Flask）：
   ```python
   from flask import Flask, redirect, url_for
   from authlib.integrations.flask_client import OAuth

   app = Flask(__name__)
   oauth = OAuth(app)

   google = oauth.register(
       name='google',
       client_id='your_client_id',
       client_secret='your_client_secret',
       access_token_url='https://accounts.google.com/o/oauth2/token',
       access_token_params=None,
       authorize_url='https://accounts.google.com/o/oauth2/auth',
       authorize_params=None,
       api_base_url='https://www.googleapis.com/oauth2/v1/',
       userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
       client_kwargs={'scope': 'openid email profile'},
   )

   @app.route('/')
   def hello_world():
       redirect_uri = url_for('authorize', _external=True)
       return google.authorize_redirect(redirect_uri)

   @app.route('/authorize')
   def authorize():
       token = google.authorize_access_token()
       resp = google.get('userinfo')
       user_info = resp.json()
       # do something with the token and profile
       return redirect('/')
   ```

这两个库都是非常流行的OAuth2实现方案，选择哪个取决于你的具体需求和偏好。`requests-oauthlib`更轻量级，适合简单的客户端应用，而`authlib`则提供了更全面的功能，特别是对于那些需要深度集成到web框架中的应用。