from threading import Lock,Thread


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
    
class Singleton(metaclass=SingletonMeta):
    value = None
    
    def __init__(self, value):
        self.value = value
        
    def some_business_logic(self):
        pass
    
def test_singleton(value):
    singleton = Singleton(value)
    
    print(singleton.value)

if __name__ == "__main__":
    
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, then 2 singletons were created (booo!!)\n\n"
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
    

"""

代码解释
这段代码定义了一个名为 SingletonMeta 的元类，用于实现单例模式。具体功能如下：

初始化：_instances 字典用于存储类的实例。
调用方法：__call__ 方法在创建类的实例时被调用。
检查实例：如果类尚未被实例化，则通过 super().__call__(*args, **kwargs) 创建实例并存储在 _instances 字典中。
返回实例：无论是否已经存在实例，都返回 _instances 字典中的实例



__call__ 方法解释
__call__ 是 Python 中的一个特殊方法，当一个对象被调用时，会自动调用这个方法。通常，这个方法用于使一个类的实例像函数一样可调用。在元类 SingletonMeta 中，__call__ 方法被重写，以便控制类实例的创建过程。

参数解释
cls：当前类本身。在元类中，cls 表示的是使用 SingletonMeta 作为元类的类。
*args：位置参数，表示传递给类构造函数的所有位置参数。
**kwargs：关键字参数，表示传递给类构造函数的所有关键字参数。
具体功能
检查实例：if cls not in cls._instances 检查当前类是否已经有一个实例存在于 _instances 字典中。
创建实例：如果类尚未被实例化，调用 super().__call__(*args, **kwargs) 创建一个新的实例。
存储实例：将新创建的实例存储在 _instances 字典中，键为类本身，值为实例。
返回实例：无论是否已经存在实例，都返回 _instances 字典中的实例。

```
flowchart TD
A[开始] --> B{类是否已实例化}
B -->|否| C[创建新实例]
C --> D[存储实例]
B -->|是| D
D --> E[返回实例]
```


详细解释
开始：进入 __call__ 方法。
类是否已实例化：检查当前类是否已经在 _instances 字典中存在实例。
创建新实例：如果类尚未实例化，调用 super().__call__(*args, **kwargs) 创建新实例。
存储实例：将新创建的实例存储在 _instances 字典中。
返回实例：无论是否已经存在实例，都返回 _instances 字典中的实例。



super().__call__(*args, **kwargs) 解释
在 Python 中，super() 函数用于调用父类的方法。在元类 SingletonMeta 的 __call__ 方法中，super().__call__(*args, **kwargs) 的作用是调用父类 type 的 __call__ 方法，从而创建一个新的类实例。

具体功能
调用父类方法：super() 返回一个代理对象，该对象可以用来调用父类的方法。在这里，super().__call__(*args, **kwargs) 调用了 type 类的 __call__ 方法。
传递参数：*args 和 **kwargs 将所有传递给 SingletonMeta.__call__ 的参数原封不动地传递给 type.__call__ 方法。
创建实例：type.__call__(*args, **kwargs) 实际上会调用类的 __new__ 和 __init__ 方法来创建并初始化一个新的实例。
代码解释
python
instance = super().__call__(*args, **kwargs)
super()：返回一个代理对象，代表 SingletonMeta 的父类 type。
__call__(*args, **kwargs)：调用 type 类的 __call__ 方法，传递所有参数。
instance：接收 type.__call__(*args, **kwargs) 返回的新实例。
控制流图
mermaid
100%
否

是

开始

```mermaid
flowchart TD
A[开始] --> B{类是否已实例化}
B -->|否| C[调用父类的 __call__ 方法]
C --> D[创建新实例]
D --> E[存储实例]
B -->|是| E
E --> F[返回实例]
```


详细解释
开始：进入 __call__ 方法。
类是否已实例化：检查当前类是否已经在 _instances 字典中存在实例。
调用父类的 __call__ 方法：如果类尚未实例化，调用 super().__call__(*args, **kwargs) 来创建新实例。
创建新实例：type.__call__(*args, **kwargs) 调用类的 __new__ 和 __init__ 方法，创建并初始化新实例。
存储实例：将新创建的实例存储在 _instances 字典中。
返回实例：无论是否已经存在实例，都返回 _instances 字典中的实例。
"""