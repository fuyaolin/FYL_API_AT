### **FYL_API_AT**

1.1 python3+pytest+allure

1.2 目录结构

```
assertfun: 处理断言
    断言
common: 处理数据
    读取yaml
    数据库连接
    读取config参数
    保存公用路径
config：配置
    配置基本数据
    邮件
logs：日志
public：公用
    前置
    后置
report_allure：allure报告
    pytest-allure报告
report_html：html报告
    pytest-html报告
testcase_py：py文件
    单个执行测试用例文件
    每个py与yaml同名
testcase_yaml: yaml文件
    测试用例存放
test_run.py:
    执行整个测试用例
```
