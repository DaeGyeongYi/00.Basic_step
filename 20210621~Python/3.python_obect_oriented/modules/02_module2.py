# 02_module2

from module import a #a 모듈명만 import - a.함수명()
from module import b #b 모듈명만 import - b.함수명()
from module.b import * #모든 함수 까지 import  -함수명()

a.hello("홍길동")
b.hello_1()
hello_1()