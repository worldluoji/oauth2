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

<br>

## 降低Token被截取和滥用的风险
为了防止客户端获取的Token（尤其是JWT等敏感信息）被截取，可以采取以下几种策略来提升安全性：

1. **使用HTTPS**：确保所有客户端与服务器之间的通信都通过HTTPS协议进行。HTTPS提供了端到端的数据加密，可以有效防止中间人攻击，确保Token在传输过程中不被窃听。

2. **存储位置选择**：
   - 避免在Cookie中存储未经 HttpOnly 标志保护的Token，以防XSS（跨站脚本攻击）。
   - 不建议将Token存储在LocalStorage或SessionStorage中，因为这两种浏览器存储方式容易受到XSS攻击。如果必须存储在前端，考虑使用Secure Storage API（如果可用）或实施严格的Content Security Policy (CSP)来减轻XSS风险。

3. **使用短生命周期的Token**：缩短Token的有效期可以限制即使Token被窃取，攻击者能利用的时间窗口也会很短。

4. **刷新Token机制**：实现刷新Token（Refresh Token）机制，客户端使用短生命周期的访问Token，并且在Token失效时，使用安全通道向服务器请求新的访问Token。刷新Token需要更加严格地保护，通常不在前端存储，或者如果必须前端存储，则需确保有强大的安全措施。

5. **令牌绑定（Token Binding）**：这是一种标准机制，可以将Token与特定的客户端绑定，即便Token被截取也无法在其他设备或上下文中使用。

6. **实施严格的同源策略**：确保Token只能在预期的源（Origin）使用，防止跨站请求伪造（CSRF）攻击。

7. **验证HTTP头部**：使用如X-Forwarded-For、Referer等HTTP头部进行额外的请求验证，增加攻击难度。

8. **教育用户**：提高用户对于钓鱼攻击、恶意软件的警惕，避免在不安全的网络环境下登录或使用敏感应用。