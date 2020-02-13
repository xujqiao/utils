# python编程总结

> python相关组件包装，专注实际内容，避免重复编码，提高编程效率

## 工程结构

    |- jxuao/
    |   |- dao/
    |   |   |- base.py          # entity的入口
    |   |   |- dbconfig.py      # db相关的配置类
    |   |   |- dbgateway.py     # db操作类
    |   |   |- exceptions.py    # 异常类
    |   |   |- utils.py         # db部分的工具类
    |   |   |- boot.py          # 业务代码的入口
    |   |- log/
    |   |   |- config.py        # log配置读取的入口
    |   |   |- logging.conf     # log的配置
    |   |   |- log/
    |   |- utils/
    |   |   |- CryptoUtil.py    # 加解密工具
    |   |   |- DateTmeUtil.py   # 日期时间处理工具
    |   |- app/                 # 业务代码目录
    |   |   |- ...
    |   |   |- log/             # 日志内容 
    
预留沙发
