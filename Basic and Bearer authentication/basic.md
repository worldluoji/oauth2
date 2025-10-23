# Basic Auth
Basic 认证（基础认证），是最简单的认证方式。当用户尝试访问受保护的资源时，浏览器会弹出对话框要求输入用户名和密码。

它简单地将用户名:密码进行 base64 编码后，放到 HTTP Authorization Header 中。HTTP 请求到达后端服务后，后端服务会解析出 Authorization Header 中的 base64 字符串，解码获取用户名和密码，并将用户名和密码跟数据库中记录的值进行比较，如果匹配则认证通过。例如：
```
$ basic=`echo -n 'admin:Admin@2021'|base64`
$ curl -XPOST -H"Authorization: Basic ${basic}" http://127.0.0.1:8080/login
```
Basic 认证虽然简单，但极不安全。使用 Basic 认证的唯一方式就是将它和 SSL 配合使用，来确保整个认证过程是安全的。在设计系统时，要遵循一个通用的原则：不要在请求参数中使用明文密码，也不要在任何存储中保存明文密码。

---

## Nginx配置basic认证
在 Nginx 中配置基本认证（Basic Authentication）主要是为了保护特定的网站目录或路由，确保只有拥有有效凭证的用户才能访问。以下是配置 Nginx Basic 认证的基本步骤：

1. **安装 httpd-tools**：
   如果你的系统中还没有 `htpasswd` 这个工具，你需要先安装它。`htpasswd` 用于创建和更新储存用户名和加密密码的文件。在基于 Red Hat 的系统上，你可以使用 yum 安装，在 Debian/Ubuntu 系统上则使用 apt。例如：

   ```bash
   # 对于基于 yum 的系统
   yum install -y httpd-tools
   
   # 对于基于 apt 的系统
   apt-get install -y apache2-utils
   ```

2. **创建认证用户文件**：
   使用 `htpasswd` 命令创建一个包含用户名和密码的文件。如果文件不存在，需要使用 `-c` 参数来创建新文件。例如，创建名为 `users.htpasswd` 的文件，并添加用户 `admin`：

   ```bash
   htpasswd -c /path/to/users.htpasswd admin
   ```

   在这个命令执行过程后，系统会交互式地提示用户输入密码。如果你想使用 MD5 加密（默认），可以省略任何选项。对于其他加密方式，请参考 `htpasswd` 的帮助文档。

3. **编辑 Nginx 配置文件**：
   打开 Nginx 的配置文件（通常位于 `/etc/nginx/nginx.conf` 或 `/etc/nginx/sites-available/default`），在你想要保护的 `location` 块内添加以下配置：

   ```nginx
   location /protected_area {
       auth_basic "Protected Zone"; # 弹出框显示的认证提示信息
       auth_basic_user_file /path/to/users.htpasswd; # 用户名密码文件路径
       
       # 其他配置，比如 proxy_pass、root、try_files 等
   }
   ```

   这里，`/protected_area` 是你想要保护的路径，`Protected Zone` 是认证提示信息，`/path/to/users.htpasswd` 是之前创建的用户密码文件的路径。

4. **测试 Nginx 配置并重启**：
   在修改配置后，首先应该测试配置是否正确，使用以下命令：

   ```bash
   nginx -t
   ```

   如果测试成功，再重新加载或重启 Nginx 使更改生效：

   ```bash
   # 重新加载配置（平滑重启，不会中断现有连接）
   nginx -s reload
   
   # 或者完全重启 Nginx（会中断所有连接）
   systemctl restart nginx
   ```

完成以上步骤后，访问受保护的路径时，浏览器会弹出一个认证对话框要求输入用户名和密码。只有输入正确的凭据，用户才能访问该资源。