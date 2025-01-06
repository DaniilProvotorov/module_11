import inspect

def introspection_info(obj):
    print(f'Тип объекта: {type(obj)}')
    print(f'Методы и атрибуты объекта: {dir(obj)}')
    print(f'Модуль объекта: {inspect.getmodule(obj)}')


introspection_info(introspection_info)