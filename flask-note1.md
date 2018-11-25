
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





















