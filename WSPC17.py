#encoding:gbk
__author__ = 'luoxt'

# 1
a = "python 测试中文"

print a.decode("gbk").encode("gbk")   #输出终端的编码会影响输出的效果，比如终端是utf-8,而a最后是gbk的时候就会乱码
print a.decode("gbk").encode("utf-8")

# 2

# s = "中文测试" + u"chinaese test" #erro
s = "中文测试"  #这个的编码方式有文件开头的encoding指定，如果文件开头没有制定，就有文件类型指定
s = "中文测试".decode("gbk") + u"chinaese test"  # "+" 时需要先把"中文测试"转换为unicode再转utf-8同后面的相加，但是如果没有.decode("gbk")，
# 就会默认用sys.defaultencoding,但默认的defaultencoding是ascii,无法处理中文，所以出错。
print s

# 3
filehandle = open("test.txt", 'r')
print filehandle.read() #如果文件是utf-8保存的，切输出终端也是utf-8的，输出就没有问题，如果输出终端是gbk的，就会乱码
filehandle.close()