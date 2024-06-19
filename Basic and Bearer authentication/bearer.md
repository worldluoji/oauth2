# Bearer
## 什么是Bearer认证
- Bearer 认证，也称为令牌认证，是一种 HTTP 身份验证方法;
- Bearer 认证的核心是 bearer token。bearer token 是一个加密字符串，通常由服务端根据密钥生成;
- 客户端在请求服务端时，必须在请求头中包含Authorization: Bearer <token>。服务端收到请求后，解析出 <token> ，并校验 <token> 的合法性，如果校验通过，则认证通过;
- 跟基本认证一样，Bearer 认证需要配合 HTTPS 一起使用，来保证认证安全性;
- 目前最流行的token一般使用JWT，JWT 是 Bearer Token 的一个具体实现。

## JWT token认证流程
<img src="./Bearer JWT token auth flow.PNG"/>

如图所示，认证过程分为4步：
- 客户端使用用户名和密码请求登录。
- 服务端收到请求后，会去验证用户名和密码。如果用户名和密码跟数据库记录不一致，则验证失败；如果一致则验证通过，服务端会签发一个 Token 返回给客户端。
- 客户端收到请求后会将 Token 缓存起来，比如放在浏览器 Cookie 中或者 LocalStorage 中，之后每次请求都会携带该 Token。
- 服务端收到请求后，会验证请求中的 Token，验证通过则进行业务逻辑处理，处理完后返回处理后的结果。