import copy

class SelfReferencingEntity:
    def __init__(self):
        self.parent = None
        
    def set_parent(self, parent):
        self.parent = parent
        
        
class SomeCompont:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref
        
    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        
        
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        
        new.__dict__.update(self.__dict__)
        return new
    def __deepcopy__(self,memo=None):
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )

        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new
    
if __name__ == "__main__":
    list_of_objects = [1, {1,2,3},[1,2,3]]
    circular_ref = SelfReferencingEntity()
    component = SomeCompont(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)
    
    shallow_copied_component = copy.copy(component)
    # Let's change the list in shallow_copied_component and see if it changes in
    # component.
    shallow_copied_component.some_list_of_objects.append("another object")
    if component.some_list_of_objects[-1] == "another object":
        print(
            "Adding elements to `shallow_copied_component`'s "
            "some_list_of_objects adds it to `component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Adding elements to `shallow_copied_component`'s "
            "some_list_of_objects doesn't add it to `component`'s "
            "some_list_of_objects."
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "changes that object in `shallow_copied_component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "doesn't change that object in `shallow_copied_component`'s "
            "some_list_of_objects."
        )

    deep_copied_component = copy.deepcopy(component)

    # Let's change the list in deep_copied_component and see if it changes in
    # component.
    deep_copied_component.some_list_of_objects.append("one more object")
    if component.some_list_of_objects[-1] == "one more object":
        print(
            "Adding elements to `deep_copied_component`'s "
            "some_list_of_objects adds it to `component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Adding elements to `deep_copied_component`'s "
            "some_list_of_objects doesn't add it to `component`'s "
            "some_list_of_objects."
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "changes that object in `deep_copied_component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "doesn't change that object in `deep_copied_component`'s "
            "some_list_of_objects."
        )

    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )

    print(
        "^^ This shows that deepcopied objects contain same reference, they "
        "are not cloned repeatedly."
    )

"""
这句话的意思是：

深拷贝的对象包含相同的引用：在进行深拷贝时，某些对象的引用可能没有被克隆，而是直接复制了引用。
它们不会被重复克隆：这意味着在深拷贝过程中，某些对象不会被多次克隆，而是共享同一个引用。
这句话通常用来解释深拷贝和浅拷贝的区别。
在某些情况下，即使进行了深拷贝，某些复杂的对象或嵌套对象的引用可能仍然会被共享，而不是完全独立的副本。
这有助于减少内存占用和提高性能。

"""

#########################################

"""
识别方法
clone 或 copy 方法：原型模式通常通过 clone 或 copy 方法来识别。在 Python 中，这些方法通常命名为 __copy__ 和 __deepcopy__。
自定义拷贝行为：通过重写 __copy__ 和 __deepcopy__ 方法，可以自定义对象的拷贝行为，确保对象的正确性和一致性。
总结
原型模式通过复制现有对象来创建新的对象，避免了复杂的构造过程。
在 Python 中，可以通过实现 __copy__ 和 __deepcopy__ 方法来支持对象的浅拷贝和深拷贝，从而实现原型模式。
"""



"""
在 Python 中，__class__ 是一个特殊的属性，用于访问对象的类。每个对象都有一个 __class__ 属性，它指向创建该对象的类。这个属性在多种情况下非常有用，例如：

动态创建对象：可以使用 __class__ 来创建与当前对象相同类型的新的对象实例。
类信息查询：可以用来获取对象所属的类的信息。
元编程：在元编程中，__class__ 可以用于动态地修改类的行为。

__class__ 是一个非常有用的属性，它提供了对象与其类之间的链接。
通过 __class__，你可以动态地创建新的对象实例、查询对象的类信息，以及在元编程中动态地修改类的行为。
"""


"""
在 Python 中，__dict__ 是一个特殊属性，用于存储对象的所有属性（即实例变量）及其对应的值。
每个对象都有一个 __dict__ 属性，它是一个字典，键是属性名，值是属性的值。
通过 __dict__，你可以动态地访问和修改对象的属性。

__dict__ 的用途
动态访问和修改属性：可以直接通过 __dict__ 访问和修改对象的属性。
查看对象的所有属性：可以查看对象的所有实例变量及其值。
序列化和反序列化：在对象的序列化和反序列化过程中，__dict__ 非常有用。
示例

"""



"""
new.__dict__ = copy.deepcopy(self.__dict__, memo)
在这段代码中，new 是一个新创建的对象实例，self 是当前对象实例。self.__dict__ 包含了当前对象的所有属性及其值。copy.deepcopy 方法用于创建一个深拷贝，确保新对象的属性与当前对象的属性完全独立。

详细解释
self.__dict__：

self.__dict__ 是一个字典，包含了当前对象的所有实例变量及其值。例如，如果 self 有一个属性 value，那么 self.__dict__ 中会有一个键值对 'value': value。
copy.deepcopy：

copy.deepcopy 是 Python 标准库中的一个函数，用于创建一个对象的深拷贝。深拷贝不仅复制对象本身，还会递归地复制对象中的所有子对象，确保新对象与原对象完全独立。
memo 参数是一个字典，用于记录已经拷贝过的对象，防止在递归拷贝过程中出现无限循环或重复拷贝。这对于处理包含循环引用的对象特别有用。
new.__dict__ = copy.deepcopy(self.__dict__, memo)：

这行代码将 self.__dict__ 的深拷贝赋值给 new.__dict__。这意味着 new 对象的属性及其值与 self 对象的属性及其值完全相同，但它们是独立的，互不影响。
使用 copy.deepcopy 确保了即使 self 对象的属性中包含复杂的数据结构（如列表、字典或其他对象），这些数据结构也会被完全复制，而不是仅仅复制引用。
为什么要这样做？
避免引用共享：

如果使用浅拷贝（如 copy.copy），则 new 对象的属性会引用 self 对象的属性。如果 self 对象的属性是可变对象（如列表、字典），对 new 对象的属性进行修改会影响 self 对象的属性。
使用深拷贝可以确保 new 对象的属性与 self 对象的属性完全独立，互不影响。
处理循环引用：

在处理包含循环引用的对象时，使用 copy.deepcopy 并传递 memo 参数可以避免无限递归和重复拷贝，确保拷贝过程的正确性和效率。



总结
不可变对象：深拷贝和浅拷贝行为相同，因为不可变对象不能被修改。
1. 不可变对象
对于不可变对象（如整数、字符串、元组等），深拷贝和浅拷贝的行为是一样的，因为不可变对象在 Python 中是不可修改的。因此，即使它们被共享，也不会影响其他对象。



自定义对象：如果自定义对象没有正确实现 __deepcopy__ 方法，可能会导致部分对象没有被真正独立拷贝。
循环引用：深拷贝会使用 memo 参数来记录已经拷贝过的对象，防止无限递归。
对于包含循环引用的对象，深拷贝会使用 memo 参数来记录已经拷贝过的对象，防止无限递归。
但是，如果对象的结构非常复杂，可能会有一些特殊情况需要特别处理。


为了确保深拷贝的正确性，建议在自定义对象中实现 __deepcopy__ 方法，以确保所有子对象都被正确地深拷贝。

总结
浅拷贝：创建一个新对象，但嵌套的可变对象仍然是引用。对嵌套对象的修改会影响到原始对象。
深拷贝：创建一个新对象，并递归地复制所有嵌套的可变对象。对新对象的修改不会影响原始对象。
在处理包含可变对象的复杂数据结构时，深拷贝可以确保对象的完全独立性，避免意外的副作用。










"""