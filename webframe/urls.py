'''
urls
表达能够进行的数据处理
'''
from views import *

urls =[("/datetime",datetime),
       ("hi",hi)]

if __name__ =="__main__":
    urls[0][1]()