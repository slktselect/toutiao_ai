# 头条自动发文工具
`目前市面上的AI工具很多，他们可以生成文章和视频但是没有发布功能，一些网站不开放他们的发布接口，本项目致力于改变这一现状。实现自动发布功能`

`工作流: 使用爬虫获取热门文章 -> 使用AI重新或者扩写文章 -> 使用自定义的头条sdk发送`

## 1.文章获取

## 2.AI扩写/二创

## 3.头条SDK

## 4.系统工具类
### 4.1 任务调度

### 4.2 日志保存

### 4.3 系统配置

### 4.4 工作流可视化

## 5.部署

### 5.1 Docker部署

### 5.2 本地直接部署

```` shell
# 安装项目依赖
pip install -r requirements.txt

# 迁移数据
python manage.py migrate
# 会创建一个默认用户 用户名: admin 密码: passwd 
python manage.py load_default_data

# 运行后台
python manage.py runserver
````

## 打开后台

http://127.0.0.1:8000/admin/

