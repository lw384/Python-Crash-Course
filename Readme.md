# PYTHON CRASH COURSE
## 1. Basic knowledge

### string
useful funciton:
* f: f str
* 大小写：str.title() str.upper() str.lower()
* 空格删除：str.rstrip() str.lstrip() str.strip()
* 部分删除：str.removeprefix('前缀') str.removesuffix('后缀')

### number
* 指数： 3**2 = 9
* 浮点数同样有 0.1 + 0.2 不等于 0.3 的问题
* 可以使用_ 下划线 分割长数字，不影响python 的运算
* 除法会返回浮点类型结果
* python 没有 const 关键词，约定全大写的单词作为 const

### comment
* # 表示注释

### list
list 增删改
* python 使用‘-1’可以提取数组最后一个元素 array[-1]
* 入队 array.append(target)  js里是用push
* 指定位置插入元素 array.insert(index,element)
* 指定位置删除元素 del array[index] = 仅仅删除
* 队尾删除：array.pop()
* 特殊：python pop(index) 可以推出指定索引位置的元素 = 推出元素，使用推出的元素
* array.remove(target) 按照值删除元素（删除出现的第一个）
list 排序
* array.sort() 整体排序，改变原数组 参数 reverse = true 可以逆向排序
* sorted(array) 不改变原数组，提供一个排序后的结果
* 逆向数组：array.reverse()
* 长度：len(array)

循环
* for ... in ...
* range(start,end,step) 不包含end
* min(array) max(array) sum(array)
* list comprehensions: (与js不同的简洁语法) squares = [value**2 for value in range(1, 11)]
截取数组
* array[start:end] 返回 start end-1索引位置元素组成的数组 和 js 的slice 一样； end 无数据表示一直到结尾；start是负数表示截取最后几位数据
复制数组
* array = array1[:] python的深拷贝
* array1 = array2 同样是浅拷贝

元组 Tuple: 不可更改其中元素的数组 用（） 包裹
虽然不能对元组内的元素重新负值，但是可以给元组整体重新赋值

### python 风格规范
### if
if xx :
elif xx :
else:

#### 条件判断
* 大小写不能判相等
* 并： and  ；或： or
* in 关键字判断 list 是否含有哪个元素 ； not in 关键字判断不在数组内

### dictionary/list

a key:value pair，操作与Js中操作对象类似，可以用索引取数值，可以使用key取值

* 添加: 直接 dict[x] = y
* 删除：del item
* Dict.get(key,'error message') 可以避免取到不存在的值
* 遍历： 
  * for key, value in dict.**items()**  （和js中遍历不同）  
  * for key in dict.**keys()**（遍历key属于默认，不需要额外的处理,.keys() 可选使用）
  * for value in dict**.values()**
*  Nesting: 嵌套结构 数组的每个对象是一个key:value的dict

### 用户交互

#### input

```python
age = input('How old are you?')
```

#### int : str 转 num

```pyhton
age = int(age)
```

#### Loop

while break continue 用法同js

### Function

* 定义关键字： def funcname(): xxx

* 参数：

  * 按顺序输入函数： func(a, b) 需要注意参数顺序
  * 提供key=value形式：func ( name = a, age = b) 无需注意参数顺序
  * 参数可选，那么某个参数初始 = ‘ ‘ 
  * List 参数传递copy，不想修改原始值： func( list_name[:])
  * 不确定参数个数： func( * parameters) 是list[1,2,3];  func(** parameters) 是 可以传递 key: value 形式

* Return value

* 如何模块化引入函数: 使用与j s 大同小异

  ```
  pizza.py : 函数存放的文件 有函数 make_pizza()
  
  整体引入：
  import pizza as 别名
  pizza.make_pizza()
  
  import module_name as mn
  
  
  局部引入：
  from pizza import make_pizza as 别名
  make_pizza()
  别名（）
  
  from module_name import func_name as fn
  from module_name import *
  ```

  

### Class

#### 声明一个类

__init__ 和 js 中 constructor 用法一样

```python
 class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
      """Initialize name and age attributes."""
      self.name = name
      self.age = age
     
    def sit(self):
      """Simulate a dog sitting in response to a command."""
      print(f"{self.name} is now sitting.")
    def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(f"{self.name} rolled over!")
```

#### 实例化

```python
instance = Dog('Lucy','3')
```

#### 继承

```python
class ElectricCar(Car):
  """Represent aspects of a car, specific to electric vehicles."""
  def __init__(self, make, model, year):
    """Initialize attributes of the parent class."""
    super().__init__(make, model, year)
    self.child_attributes = 40/其他Class
    
    
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

### 文件操作

#### 取

```python
from pathlib import Path
path = Path('pi_digits.txt')
```

#### 读

```python
contents = path.read_text()
contents = contents.rstrip()
```

```python
行读取
lines = contents.splitlines()
```

#### 相对路径，绝对路径

```
path = Path('text_files/filename.txt') // 相对
path = Path('/home/eric/data_files/text_files/filename.txt') // 绝对
```

避免路径错误的方法: 获取当前文件所在目录

```python
base_path = Path(__file__).parent
```

### 异常抓取

什么错误需要阻断执行并上报？

什么错误

```python
try:
  // 执行过程
expect 具体错误：
  pass // fail silently
else: 
  执行其他
```

### JSON

此处的用途是讲用户输入的暂时数据以json形式存储在文件中做数据持久化

* 转为json格式：json.dumps()
* 读取json: json.loads()

### test

插件： pytest

test开头的文件会作为测试文件运行

assert 写断言
