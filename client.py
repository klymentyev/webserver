import requests
import json

data = {'UK': 'London'}

#добавляем элемент
res = requests.post('http://127.0.0.1:5000/save/second', json=data)
print('Данные сервера после добавления элемента second:')
print(res.json())

#смотрим значение элемента
res = requests.get('http://127.0.0.1:5000/show/second')
print('Значение second:')
print(res.json())

#смотрим значение несуществующего элемента
res = requests.get('http://127.0.0.1:5000/show/third')
print('Смотрим несуществующий элемент:')
print(res.json())

#смотрим значение начального элемента
res = requests.get('http://127.0.0.1:5000/show/first')
print('Значение first:')
print(res.json())


#пытаемся удалить несуществующий элемент
res = requests.delete('http://127.0.0.1:5000/del/firt')
print('Удаляем несуществующий элемент:')
print(res.json())

#удаляем первый элемент
res = requests.delete('http://127.0.0.1:5000/del/first')
print('Удаляем first:')
print(res.json())