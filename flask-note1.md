
> 为了避免大量的可有可无的参数把师徒函数弄得一团糟， `Flask` 使用上下文临时把某些对象变成全局对象。有了上下文
，就可以写出下面的试图函数

```python
from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {} </p>'.format(user_agent)
```

事实上`request` 不可能是全局变量，在多线程服务器中，多个线程同时处理不同客户端发送的不同请求时，每个线程看到的`request`
对象必然不同， `Flask` 使用上下文特定的变量在一个线程中全局可访问，于此同时却不会干扰其他线程。 

在 `Flask` 中上下文有两种： 程序上下文和请求上下文

- `current_app` 程序上下文 当前激活程序的实例 
- `g` 程序上下文 处理请求时作用临时存储对象，每次请求都会重设这个变量
- `request` 请求上下文  请求对象封装了客户端发出的HTTP请求中的内容
- `session` 请求上下文  用户存储请求之间需要"记住"的值得词典


### 请求调度 

`Flask` 会在程序的 `URL` 映射中查找请求的 `URL` . `URL` 映射是 `URL` 和试图函数之间的对应关系。 `Flask` 使用
`app.route` 修饰器或者非修饰器形式的 `app.add_url_rule()` 生成映射 


##### 请求钩子 

有时在处理请求之前或之后执行代码会很有用。如请求开始时创建数据库连接或者认证发起请求的用户。为了避免每个试图函数都时候用
重复代码，Flask提供了注册通用函数的功能。注册的函数可在请求被分发到试图函数之前或之后调用。 

请求钩子使用装饰器实现，`Flask` 支持4中钩子

- `before_first_request`: 处理第一个请求之前运行
- `before_request`: 每次请求之前运行
- `after_reques`: 如果没有未处理的异常抛出，在每次请求之后运行
- `teardown_request`: 即使有未处理的异常，也在每次请求之后执行


在请求钩子函数和试图函数之间共享数据一般使用上下文全局变量`g` . 

### 响应 

返回状态码可以作为第二个参数

```python
@app.route('/')
     def index():
         return '<h1>Bad Request</h1>', 400
```

或者使用 `make_response` 

```python
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
```

后者使用重定向 `redirect`

```python
@app.route('/')
def index():
    return redirect('http://www.example.com')
```

还有一种特殊的响应由 `abort` 函数生成，用于处理错误

```python
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name
```

### Jinjia2 模板引擎 

`Jinjia2` 能识别所有类型的变量，甚至是一些复杂的类型，例如列表，字典和对象。在模板中使用变量如下所示

```python
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
```

可以使用过滤器修改变量，过滤器名添加在变量名之后，中间使用竖线分隔。例如，下述 模板以首字母大写形式显示变量 name 的值

```python
Hello, {{ name|capitalize }}
```

常用过滤器

- `safe` 渲染值时不转义
- `capitalize` 把值的首字母转换成大写，其他字母转换成小写
- `lower` 把值转换成小写形式
- `upper` 把值转换成大写形式
- `title` 把值中每个单词的首字母都转换成大写
- `trim`  把值的首尾空格去掉 
- `striptags` 渲染之前把值中所有的 HTML 标签都删掉
  
> safe 过滤器值得特别说明一下。默认情况下，出于安全考虑，Jinja2 会转义所有变量。例 如，
如果一个变量的值为 '<h1>Hello</h1>'，Jinja2 会将其渲染成 '&lt;h1&gt;Hello&lt;/ h1&gt;'，
浏览器能显示这个 h1 元素，但不会进行解释。很多情况下需要显示变量中存储 的 HTML 代码，这时就可使用 safe 过滤器。


需要在多处重复使用的模板代码片段可以写入单独的文件，再包含在所有模板中，以避免 重复:

```python
{% include 'common.html' %}
```

`Flask-Bootstrap` 基模板中定义的块
 

- `doc`: 整个 `HTML` 文档 
- `html_attribs`: `<html>` 标签中的属性 
- `html`: `<html>` 标签中的内容
- `head`: `<head>` 标签中的内容
- `title`: `<title>` 标签中的内容
- `metas`: 一组 `<meta>` 标签
- `styles`: 层叠样式表定义 
- `body_attribs`: `<body>` 标签的属性
- `body`: `<body>` 标签中的内容
- `navbar`: 用户定义的导航条
- `content`: 用户定义的页面内容
- `scripts`: 文档底部的 `JavaScript` 声明 

### 自定义错误页面 

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

### 链接 

`url_for('index')`
`url_for('user',name='john')`
调用 `url_for('index', _external=True)` 返回的则是绝对地 址，在这个示例中是 `http://localhost:5000/`
调用 `url_for('static', filename='css/styles.css', _external=True)` 得到的结果是 `http:// localhost:5000/static/css/styles.css`

默认设置下，Flask 在程序根目录中名为 static 的子目录中寻找静态文件。如果需要，可在 static 文件夹中使用子文件夹存放文件。
服务器收到前面那个 URL 后，会生成一个响应， 包含文件系统中 static/css/styles.css 文件的内容。


### `Flask-Moment` 本地化日期和时间

统一使用`utc`时间

安装： `pip install flask-moment`


```python
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }} 
{{ moment.lang('zh_cn') }}
{% endblock %}
```

还可以格式化各种时间格式。 

### 表单 


`request.form` 能获取 `POST` 请求中提交的表单数据。

`Flask-WTF` 协助处理表单










     