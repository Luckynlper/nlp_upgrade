# -*- coding : UTF-8 -*-

import re
# re.findall(pattern=,string=)
'''
pattern:以字符串的形式传入一个正则表达式
string:要匹配的目标字符串
'''
# 普通字符串　匹配规则：每个普通自负匹配其对应的字符
re.findall('ab', "abcdefabcd")
# ['ab', 'ab']
# 或元字符｜
# 匹配规则：匹配｜两侧的正则表达式
re.findall('com|cn', "www.baidu.com/www.tmooc.cn")
# ['com', 'cn']
# 匹配单个字符
# 元字符： .
# 匹配规则：匹配除 \n外任意一个字符
re.findall('张.丰',"张三丰,张四丰,张五丰")
# ['张三丰', '张四丰', '张五丰']
# 匹配字符集
'''元字符: [字符集]

匹配规则: 匹配字符集中的任意一个字符

表达形式:

[abc#!好] 表示 [ ] 中的任意一个字符
[0-9], [a-z], [A-Z] 表示区间内的任意一
[_#?0-9a-z] 混合书写,一般区间表达写在后面
'''
re.findall('[aeiou]',"How are you!")
# ['o', 'a', 'e', 'o', 'u']
#　匹配字符集反集
'''
元字符: [^字符集]

匹配规则: 匹配除了字符集以外的任意一个字符
'''
re.findall('[^0-9]',"Use 007 port")
# ['U', 's', 'e', ' ', ' ', 'p', 'o', 'r', 't']

# 匹配结束位置
'''
元字符：$
匹配规则：匹配目标字符串的结束位置
'''
re.findall('Jame$',"Hi,Jame")
# ['Jame']

# 匹配字符重复
'''
元字符:  *
匹配规则: 匹配前面的字符出现0次或多次
'''
re.findall("wo*", "woooo~~w!")
# w后面o出现多次的情况和出现０次的情况
#　['woooo', 'w']
# 大写字母后面跟小写之母出现０次或多次
re.findall("[A-Z][a-z]*", "How ary you? Finf Ha")
# ['How', 'Finf', 'Ha']

'''
元字符:　+
匹配规则: 匹配前面的字符出现后面的字符的次数1次或多次的情况
'''
# 大写之母后面跟小写之母出现１次或多次
re.findall('[A-Z][a-z]+',"Hello World")
# ['Hello', 'World']

'''
元字符:　?
匹配规则: 匹配前面的字符出现0次或1次
'''
# 匹配整数
re.findall('-?[0-9]+',"Jame,age:18, -26")
# ['18', '-26']

'''
元字符:　{n}
匹配规则: 匹配前面的字符出现n次
'''
# 匹配手机号码
re.findall('1[0-9]{10}',"Jame:13886495728")
# ['13886495728']


'''
元字符:　{m,n}
匹配规则: 匹配前面的字符出现 [m-n] 次
'''
# 匹配qq号
re.findall('[1-9][0-9]{5,10}',"Baron:1259296994")
# ['1259296994']

# 匹配任意（非）数字字符
'''元字符: \d \D
匹配规则: \d 匹配任意数字字符, \D 匹配任意非数字字符
'''
# 匹配端口
re.findall('\d{1,5}',"Mysql: 3306, http:80")
# ['3306', '80']

# 匹配任意（非）普通字符
'''
元字符: \w  \W
匹配规则: \w 匹配普通字符, \W 匹配非普通字符
说明: 普通字符指 数字, 字母, 下划线, 汉字。
'''
re.findall('\w+',"server_port = 8888")
# ['server_port', '8888']
# 匹配非空字符
'''
元字符: \s \S
匹配规则: \s 匹配空字符, \S 匹配非空字符
说明:空字符指 空格 \r \n \t \v \f 字符
'''
re.findall('\w+\s+\w+',"hello    world")
# ['hello world']

# 匹配开头结尾位置
'''
元字符: \A \Z
匹配规则: \A 表示开头位置, \Z 表示结尾位置
'''
re.findall("\Ahello","hello world")
# ['hello']
re.findall("world\Z","hello world")
# ['world']
# 匹配(非)单词的边界位置
'''
元字符: \b \B
匹配规则: \b 表示单词边界, \B 表示非单词边界
说明:单词边界指数字字母(汉字)下划线与其他字符的交界位置。
'''
re.findall(r'\bis\b',"This is a test.")
# ['is']

# 如果使用正则表达式匹配特殊字符则需要加 \ 表示转义。 特殊字符: . * + ? ^ $ [] () {} | \
# 匹配特殊字符 . 时使用 \. 表示本身含义
re.findall('-?\d+\.?\d*',"123,-123,1.23,-1.23")
# ['123', '-123', '1.23', '-1.23']

# *******贪婪模式和非贪婪模式*********
'''
贪婪模式: 默认情况下,匹配重复的元字符总是尽可能多的向后匹配内容。比如: * + ? {m,n}

非贪婪模式(懒惰模式): 让匹配重复的元字符尽可能少的向后匹配内容。

贪婪模式转换为非贪婪模式: 在匹配重复元字符后加  '?'  号即可

　　　　* ---> *?　　;         + ---> +?　　;       ? ---> ??　　{m,n} ---> {m,n}?
'''
re.findall("ab*", "abbbbb") # ['abbbbb']
re.findall("ab*?", "abbbbb")  # ['a']

re.findall("ab+", "abbbbb") # ['abbbbb']
re.findall("ab+?", "abbbbb") # ['ab']

# 练习
# 把数字匹配出来
re.findall("[^ ]+", "12 -36 28 1.34 -3.8")
# ['12', '-36', '28', '1.34', '-3.8']

re.findall("-?\d+\.?\d*", "12 -36 28 1.34 -3.8")
# ['12', '-36', '28', '1.34', '-3.8']

# 匹配一个.com邮箱格式字符串
print(re.findall(r"\w+@\w+", "lvze@163.com"))
# 匹配一个密码 8-12位数字字母下划线构成
print(re.findall(r"\w{8,12}", "Tedu023256"))
# 匹配一个数字 正数,负数,整数,小数,分数1/2,百分数45%
print(re.findall(r"-?\d+/?\.?\d*%?", "12 -3 3.5 5.45 42% 1/3"))
# 匹配一段文字中以大写字母开头的单词,注意文字中可能有ipython(不算)H-base(算),单词可能有大写字母小写之母 -_
print(re.findall(r"\b[A-Z][-_a-zA-Z]*", "Hello ipython H-base BSD"))

# 分组
'''
在正则表达式中, 以 () 建立正则表达式的内部分组,子组是正则表达式的一部分,可以作为内部整体操作对象。

可以被作为整体操作, 改变元字符的操作对象
'''
# 改变 +号 重复的对象
re.search(r'(ab)+',"ababababab").group()
#  'ababababab'
# 改变 |号 操作对象
re.search(r'(王|李)\w{1,3}',"王者荣耀").group()
# '王者荣耀'

# 可以通过编程语言某些接口获取匹配内容中,子组对应的内容部分
# 获取url协议类型
re.search(r'(https|http|ftp|file)://\S+',"https://www.baidu.com").group(1)
# 'https'

# *******捕获组******
'''
可以给正则表达式的子组起一个名字,表达该子组的意义。这种有名称的子组即为捕获组。

格式: (?P<name>pattern)
'''
# 给子组命名为 "pig"
re.search(r'(?P<pig>ab)+',"ababababab").group('pig')
# 'ab'
'''
注意事项

一个正则表达式中可以包含多个子组
子组可以嵌套,但是不要重叠或者嵌套结构复杂
子组序列号一般从外到内,从左到右计数
'''
# python re模块
# regex = compile(pattern,flags = 0)
'''
参数:

pattern 正则表达式
flags 功能标志位,扩展正则表达式的匹配
返回值:  正则表达式对象
'''
# regex.findall(string,pos,endpos)
'''
参数:

string 目标字符串
pos 截取目标字符串的开始匹配位置
endpos 截取目标字符串的结束匹配位置
返回值: 匹配到的内容列表, 如果正则表达式有子组则只能获取到子组对应的内容
'''
s = "Alex:1994,Sunny:1993"
pattern = r"(\w+):(\d+)"
regex = re.compile(pattern)
l = regex.findall(s, 0, 10)
print(l)        # [('Alex', '1994')]

# re.split(pattern,string,flags = 0)　　使用正则表达式匹配内容,切割目标字符串
'''
参数:

pattern 正则表达式
string 目标字符串
flags 功能标志位,扩展正则表达式的匹配
返回值: 切割后的内容列表
'''
s = "Alex:1994,Sunny:1993"
# 按照匹配内容切割字符串
l = re.split(r'[:,]', s)
print(l)        # ['Alex', '1994', 'Sunny', '1993']

# re.sub(pattern,replace,string,max,flags = 0)　和 re.subn(pattern,replace,string,max,flags = 0)

'''
使用一个字符串替换正则表达式匹配到的内容

参数:

pattern 正则表达式
replace 替换的字符串
string 目标字符串
max 最多替换几处, 默认替换全部
flags 功能标志位,扩展正则表达式的匹配
返回值: 替换后的字符串
'''
# 替换匹配到的内容
s = re.subn(r'\s+','#',"This is a test",2)
print(s)        # ('This#is#a test', 2)

# re.finditer(pattern,string,flags = 0)　　根据正则表达式匹配目标字符串内容
'''
参数:

pattern 正则表达式
string 目标字符串
flags 功能标志位,扩展正则表达式的匹配
'''
import re

s = "2019年,建国70年"
pattern = r'\d+'

# 返回迭代器
it = re.finditer(pattern,s)
for i in it:
  print(i)  # 获取match对象对应内容
  # <_sre.SRE_Match object; span=(0, 4), match='2019'>
  # <_sre.SRE_Match object; span=(0, 4), match='70'>


# re.fullmatch(pattern,string,flags=0)　　
'''
参数:

pattern 正则
string 目标字符串
返回值:完全匹配某个目标字符串 object
'''
# 完全匹配
print(re.fullmatch("[,\w]+", s).group())    # 2019年,建国70年

# re.match(pattern,string,flags=0)　
'''
参数:

pattern 正则
string 目标字符串
返回值:匹配内容match 对象
'''
# 匹配开始位置
m = re.match(r"[A-Z]\w*", "Hello World")
print(m.group())    # Hello