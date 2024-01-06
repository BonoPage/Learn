#章节--字符串
course = "Python's for Beginners"
        # 0123456789
print(course)
print(course[0])#输出字符串"python's for Beginners"的第0个字符即  P
print(course[-2])#输出字符串"python's for Beginners"的倒数第2个字符即  r
print(course[0:3])#：冒号就是索引，输出字符串"python's for Beginners"的第0到3个字符即  Pyt
print(course[2:])#排除"python's for Beginners"的第2个字符之前的字符即  thon's for Beginners
print(course[:5])#排除"python's for Beginners"的第5个字符之后的字符即  Pytho
another = course[:]
print(another)#打印一个course的副本
 
    #练习
name = 'Bono'
print(name[1:-1])
print(course.upper())#转换为大写
print(course.lower())#转换为小写 
print(course.find('g'))#用find在字符串中查找字符或者字符序列，输出结果为：15
print(course.find('ginner'))#用方法语法--find在字符串中查找字符或者字符序列，输出结果为：15，因为g是第15个字符
print(course.replace('P','J'))# replace  把字符串中的P替换成J，输出结果：Jython's for Beginners
print('Python' in course)#in 查询Python这个字符串是否在course这个变量里，输出结果将返回布尔值，输出结果：Ture


#章节--格式化了的字符串
first = 'Bono'
last = 'Page'
msg = f'{first}[{last}] is a coder'#花括号是将值动态地插入到字符串中，输出结果：Bono[Page] is a coder
print(msg)
print(len(msg))#查询并打印msg这个变量的字符长度，输出结果：21

x= 10
x-=3
print(x)#输出结果：7

y=-2.9
print(round(y))#对y这个变量四舍五入，输出结果：-3
print(abs(y))#对y这个变量取绝对值，输出结果：2.9

#写一个小程序，如果天气很热，提醒用户多喝水;如果天气很冷，提醒用户多穿点衣服;如果天气平常，就跟用户说今天是一个不错的一天
is_hot=True
is_cold=False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:print("It's a lovely day")


#写一个小程序，你是银行代理人，如果客户来买房，查看他的信用，如果信用好并且有高收入，则符合贷款条件，允许贷款。如果两个条件任意一个不符合，则不予贷款
has_good_credit=True
has_high_income=True
if has_good_credit and has_high_income:
   print('Eligible for loan')


#whlie循环
i=1
while i <=5:
    print(i)
    i=i+1
print('Done')

o=1
while o <=5:
    print('*'*o)
    o=o+1
print("Done")
