### 准备上线
1. 上线前的检查工作。

   ```Shell
   python manage.py check --deploy
   ```

2. 将DEBUG设置为False并配置ALLOWED_HOSTS。

   ```Python
   DEBUG = False
   ALLOWED_HOSTS = ['*']
   ```

3. 安全相关的配置。

   ```Python
   # 保持HTTPS连接的时间
   SECURE_HSTS_SECONDS = 3600
   SECURE_HSTS_INCLUDE_SUBDOMAINS = True
   SECURE_HSTS_PRELOAD = True
   
   # 自动重定向到安全连接
   SECURE_SSL_REDIRECT = True
   
   # 避免浏览器自作聪明推断内容类型
   SECURE_CONTENT_TYPE_NOSNIFF = True
   
   # 避免跨站脚本攻击
   SECURE_BROWSER_XSS_FILTER = True
   
   # COOKIE只能通过HTTPS进行传输
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   
   # 防止点击劫持攻击手段 - 修改HTTP协议响应头
   # 当前网站是不允许使用<iframe>标签进行加载的
   X_FRAME_OPTIONS = 'DENY'
   ```
 
### 更新服务器Python环境到3.x
略

### 准备域名
略

### uWSGI的配置

1. 安装。

2. 修改配置文件
   ```INI
   举例：

   # 配置前导路径
   base=/root/project
   # 配置项目名称
   name=teamproject
   # 守护进程
   master=true
   # 进程个数
   processes=4
   # 虚拟环境
   pythonhome=%(base)/venv
   # 项目地址
   chdir=%(base)/code/%(name)
   # 指定python解释器
   pythonpath=%(pythonhome)/bin/python
   # 指定uwsgi文件
   module=%(name).wsgi
   # 通信的地址和端口(自己服务器的IP地址和端口)
   socket=IP:port
   # 日志文件地址
   logto=%(base)/logs/uwsgi.log
   ```
   
3. 启动服务器

   
### Nginx的配置
1. 安装Nginx

2. 修改全局配置文件

    ```
    举例：
    
    # 进程数(可以CPU的核数量一样)
    worker_processes auto;
    # 错误日志
    error_log /var/log/nginx/error.log;
    # 进程文件
    pid /run/nginx.pid;
    # 包含其他的配置
    include /usr/share/nginx/modules/*.conf;
    # 工作模式(多路IO复用方式)和连接上限
    events {
        use epoll;
        worker_connections 1024;
    }
    # HTTP服务器相关配置
    http {
        # 日志格式
        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                          '$status $body_bytes_sent "$http_referer" '
                          '"$http_user_agent" "$http_x_forwarded_for"';
        # 访问日志
        access_log  /var/log/nginx/access.log  main;
        # 开启高效文件传输模式
        sendfile            on;
        # 用sendfile传输文件时有利于改善性能
        tcp_nopush          on;
        # 禁用Nagle来解决交互性问题
        tcp_nodelay         on;
        # 客户端保持连接时间
        keepalive_timeout   30;
        types_hash_max_size 2048;
        # 包含MIME类型的配置
        include             /etc/nginx/mime.types;
        # 默认使用二进制流格式
        default_type        application/octet-stream;
        # 包含其他配置文件
        include /etc/nginx/conf.d/*.conf;
        # 包含项目的Nginx配置文件
        include /root/project/conf/*.conf;
    }
    ```
   
3. 编辑局部配置文件（自己创建conf）

    ```
    举例：
    
    server {
        listen      80;
        server_name _;
        access_log /root/project/logs/access.log;
        error_log /root/project/logs/error.log;
        location / {
            include uwsgi_params;
            uwsgi_pass IP:port;
        }
        location /static/ {
            alias /root/project/stat/;
            expires 30d;
        }
    }
    server {
        listen      443;
        server_name _;
        ssl         on;
        access_log /root/project/logs/access.log;
        error_log /root/project/logs/error.log;
        ssl_certificate     /root/project/conf/cert/xxxx.pem;
        ssl_certificate_key /root/project/conf/cert/xxxx.key;
        ssl_session_timeout 5m;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:xxxxxxxxxxxxx;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;
        location / {
            include uwsgi_params;
            uwsgi_pass IP:port;
        }
        location /static/ {
            alias /root/project/static/;
            expires 30d;
        }
    }
    ```
   
4. 重启Nginx服务器

#### 负载均衡

   ```
    用docker创建
    
    举例：
    
    docker run -d -p 801:80 --name nginx1 nginx:latest
    docker run -d -p 802:80 --name nginx2 nginx:latest
    docker run -d -p 803:80 --name nginx3 nginx:latest
   ```

   ```
    配置负载均衡

    举例：
    
    http {   
    upstream xxx {
        server IP:port1 weight=4;
        server IP:port2 weight=2;
        server IP:port3 weight=2;
    }
   ```
