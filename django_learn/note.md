# Django

------

## 下载更新

https://www.djangoproject.com/download/

---------

## 新项目

### 创建

```
django-admin startproject mysite
```

### 运行

```
 python manage.py runserver
```

#### 更改端口

```
python manage.py runserver 8080
#更改监听IP
python manage.py runserver 0:8000 (在云服务器上用这个)
#0->0.0.0.0
```

----------

## 服务器重启

当修改了代码以后不需要重新启动服务器
当添加新文件,新动作以后需要手动重新启动服务器





-----

## 问题DisallowedHost at / Invalid HTTP_HOST header

https://blog.csdn.net/will5451/article/details/53861092

https://stackoverflow.com/questions/61760770/django-invalid-http-host

修改`setting.py`

```
ALLOWED_HOSTS = [] -> ALLOWED_HOSTS = ['*'] 
```

`如果只是写*的话, 还是默认本地主机, 部署的话,需要加上部署的ip, 在您的项目settings.py文件中，设置ALLOWED_HOSTS如下： ALLOWED_HOSTS = ['198.211.99.20', 'localhost', '127.0.0.1']`

`ALLOWED_HOSTS = ['198.168.1.9', 'localhost', '192.168.1.1', '0.0.0.0', ]`

