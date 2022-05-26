# Basic Auth
Basic 认证（基础认证），是最简单的认证方式。它简单地将用户名:密码进行 base64 编码后，放到 HTTP Authorization Header 中。HTTP 请求到达后端服务后，后端服务会解析出 Authorization Header 中的 base64 字符串，解码获取用户名和密码，并将用户名和密码跟数据库中记录的值进行比较，如果匹配则认证通过。例如：
```
$ basic=`echo -n 'admin:Admin@2021'|base64`
$ curl -XPOST -H"Authorization: Basic ${basic}" http://127.0.0.1:8080/login
```
Basic 认证虽然简单，但极不安全。使用 Basic 认证的唯一方式就是将它和 SSL 配合使用，来确保整个认证过程是安全的。在设计系统时，要遵循一个通用的原则：不要在请求参数中使用明文密码，也不要在任何存储中保存明文密码。