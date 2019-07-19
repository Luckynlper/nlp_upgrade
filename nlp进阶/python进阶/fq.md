## 代码规范篇

> 阅读者的体验 >> 编程者的体验 >> 机器的体验
### 代码书写规范
执行以上代码，输出的结果是　Invalid level
> 缩进规范
1.选择四个空格缩进，不要使用Tab,更不要Tab个空格混着用
2.每行最大长度限制在79个字符
> 空行规范
全局的类和函数的上方需要空两个空行，而类的函数之前需要空一个空行
> 空格规范
1.逗号后要跟一个空格
2.冒号后跟一个空格
3.请记得要在#后、注释前加一个空格
4.例如+，-，*，/，&，|，=，==，!=，请在两边都保留空格
> 换行规范
1.通过括号来将过长的运算进行封装，此时虽然跨行，但是仍处于一个逻辑引用下
2.通过换行符来实现，如'\'
> 文档规范
> 注释规范
> 文档规范
　我们首先用一句话简单说明这个函数做什么，然后跟一段话来详细解释；再往后是参数列表,参数格式,返回值格式
> 命名规范
1.变量使用小写，通过下划线串联起来
2.对于常量，最好的做法是全部大写，例如：WAIT_TIME、SERVER_ADDRESS
3.对于函数名，同样也请使用小写的方式，通过下划线连接起来，例如launch_nuclear_missile()
4.对于函数名，同样也请使用小写的方式，通过下划线连接起来，例如SpatialDropout2D
### 编程规范篇
> 触发异常后，提醒相应的错误
```python
def mye( level ):
    if level < 1:
        raise Exception,"Invalid level!"
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception,err:
    print 1,err
else:
    print 2
```
> 合理使用assert
```python
def apply_discount(price, discount):
    updated_price = price * (1 - discount)
    assert 0 <= updated_price <= price, 'price should be greater or equal to 0 and less or equal to original price'
    return updated_price
```
> 巧用上下文管理器和with语句精简代码
```python
class FileManager:
    def __init__(self, name, mode):
        print('calling __init__ method')
        self.name = name
        self.mode = mode 
        self.file = None
        
    def __enter__(self):
        print('calling __enter__ method')
        self.file = open(self.name, self.mode)
        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        print('calling __exit__ method')
        if self.file:
            self.file.close()
            
with FileManager('test.txt', 'w') as f:
    print('ready to write to file')
    f.write('hello world')   
＃输出
＃calling __init__ method
＃calling __enter__ method
＃ready to write to file
＃calling __exit__ method

class Foo:
    def __init__(self):
        print('__init__ called')        

    def __enter__(self):
        print('__enter__ called')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('__exit__ called')
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_tb}')
            print('exception handled')
        return True
    
with Foo() as obj:
    raise Exception('exception raised').with_traceback(None)
输出
__init__ called
__enter__ called
__exit__ called
exc_type: <class 'Exception'>
exc_value: exception raised
exc_traceback: <traceback object at 0x1046036c8>
exception handled

```
### 单元测试

```python
import unittest

def sort(arr):
    l = len(arr)
    for i in range(0, l):
        for j in range(i + 1, l):
            if arr[i] >= arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp


编写子类继承 unittest.TestCase
class TestSort(unittest.TestCase):
   # 以 test 开头的函数将会被测试
   def test_sort(self):
        arr = [3, 4, 1, 5, 6]
        sort(arr)
        # assert 结果跟我们期待的一样
        self.assertEqual(arr, [1, 3, 4, 5, 6])
if __name__ == '__main__':
    ## 如果在 Jupyter 下，请用如下方式运行单元测试
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    ## 如果是命令行下运行，则：
    ## unittest.main()  
输出
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```
> mock
mock 是单元测试中最核心重要的一环。mock 的意思，便是通过一个虚假对象，来代替被测试函数或模块需要的对象
```python
import unittest
from unittest.mock import MagicMock

class A(unittest.TestCase):
    def m1(self):
        val = self.m2()
        self.m3(val)

    def m2(self):
        pass

    def m3(self, val):
        pass

    def test_m1(self):
        a = A()
        a.m2 = MagicMock(return_value="custom_val")
        a.m3 = MagicMock()
        a.m1()
        self.assertTrue(a.m2.called) # 验证 m2 被 call 过
        a.m3.assert_called_with("custom_val") # 验证 m3 被指定参数 call 过
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
#输出
#..
#----------------------------------------------------------------------
#Ran 2 tests in 0.002s

#OK

```
> mock　Side Effect
第二个我们来看 Mock Side Effect，这个概念很好理解，就是mock函数，属性是根据不同的输入，返回不同的数值，而不只是一个return_value
> patch
至于patch,给开发者提供了非常便利的函数mock方法，它可以应用python的decoration模式或是context manager概念，快速自然地mock所需的函数．

### pdb&cProfile:调试和性能分析的法宝
> 调试和性能分析的主要场景，通常有三个：
1.代码本身问题，需要我么找到root cause并修复
2.代码效率有问题，比如过度浪费资源，增加latency,因此需要我们debug
3.是在开发心的feature时，一般都需要测试

> 利用pdb进行调试
```python
a = 1
b = 2
import pdb
pdb.set_trace()
c = 3
print(a + b +c)
```

> 用cProfile进行性能分析
日常工作中，我们常常会遇到这样的问题：在线上，我发现产品的某个功能模块效率地下，延迟(letency)高，占用资源多，但却不知道哪里出了问题．
所谓的profile，是指对代码的每个部分进行动态分析，比如准确计算每个模块耗时的时间等．
```python
import cProfile
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n-1))
    res.append(fib(n))
    return res
print(fib_seq(30))
cProfile.run('fib_seq(30)')


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq_v1(n):
    res = []
    if n > 0:
        res.extend(fib_seq_v1(n-1))
    res.append(fib(n))
    return res
print(fib_seq_v1(30))
cProfile.run('fib_seq_v1(30)')
```




