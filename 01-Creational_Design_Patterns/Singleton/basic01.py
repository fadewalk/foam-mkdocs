
class SingletonMeta(type):
    """Metaclass that makes a class a Singleton"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """Call method"""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """Singleton class"""
    
    def some_building_logic(self):
        """Some building logic"""
        pass
    
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1 == s2)
    
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")