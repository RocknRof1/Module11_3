def introspection_info(obj):
    # Получение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибутов и методов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Получение модуля, к которому принадлежит объект
    obj_module = obj.__class__.__module__

    # Другие свойства объекта
    other_properties = []

    # Если объект имеет длину
    if hasattr(obj, '__len__'):
        other_properties.append(f"length: {len(obj)}")

    # Если объект является числом
    if isinstance(obj, (int, float, complex)):
        other_properties.append(f"Is numeric: True")
        other_properties.append(f"Numeric value: {obj}")

    # Если объект является строкой
    if isinstance(obj, str):
        other_properties.append(f"Is string: True")
        other_properties.append(f"String: {obj}")



    # Создаем строки
    info = f"Type: {obj_type}\n"
    info += f"Module: {obj_module}\n"
    info += f"Attributes: {', '.join(attributes)}\n"
    info += f"Methods: {', '.join(methods)}\n"

    # Добавляем другие свойства
    if other_properties:
        info += "Other Properties:\n" + "\n".join(other_properties)

    return info


# Пример класса
class MyClass:
    def __init__(self, value):
        self.value = value

    def greet(self):
        return f"Hello, {self.value}!"


my_object = MyClass("Python")

object_info = introspection_info(my_object)
print(object_info)

number_info = introspection_info(42)
print(number_info)

