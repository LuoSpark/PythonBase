#encoding:gbk
__author__ = 'luoxt'

# 1
a = "python ��������"

print a.decode("gbk").encode("gbk")   #����ն˵ı����Ӱ�������Ч���������ն���utf-8,��a�����gbk��ʱ��ͻ�����
print a.decode("gbk").encode("utf-8")

# 2

# s = "���Ĳ���" + u"chinaese test" #erro
s = "���Ĳ���"  #����ı��뷽ʽ���ļ���ͷ��encodingָ��������ļ���ͷû���ƶ��������ļ�����ָ��
s = "���Ĳ���".decode("gbk") + u"chinaese test"  # "+" ʱ��Ҫ�Ȱ�"���Ĳ���"ת��Ϊunicode��תutf-8ͬ�������ӣ��������û��.decode("gbk")��
# �ͻ�Ĭ����sys.defaultencoding,��Ĭ�ϵ�defaultencoding��ascii,�޷��������ģ����Գ���
print s

# 3
filehandle = open("test.txt", 'r')
print filehandle.read() #����ļ���utf-8����ģ�������ն�Ҳ��utf-8�ģ������û�����⣬�������ն���gbk�ģ��ͻ�����
filehandle.close()