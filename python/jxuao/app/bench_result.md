# 性能测试结果

## 数据库性能

* 运行环境
PostgreSQL-10.9, Windows 10 [WSL](https://docs.microsoft.com/en-us/windows/wsl/about) Ubuntu 10.9-0ubuntu0.18.04.1

* 压测命令
```bash
pgbench -b simple-update -h 127.0.0.1 -U postgres -d spring
```

* 运行结果
```bash
latency average = 16.975 ms
tps = 58.909156 (including connections establishing)
tps = 64.477068 (excluding connections establishing)
```

> 由于在WSL里搭建，本身性能不高

## 读

* 代码片段
```python
def query(session, id) -> str:
    rs = session.query(Resource).filter_by(id=id).one()
    return obj2json(rs)

for id in range(0, 10000):
    db.execute(query, id)
```

* 运行结果

10000条查询记录，消耗30 s
340 tps


## 写

* 代码片段
```python
def insert(session, id) -> None:
    r = Resource(id=id, authors="你好", title="我了个去", url="www.baidu.com")
    session.add(r)
    session.commit()

for id in range(0, 10000):
    db.execute(insert, id)
```

* 运行结果

10000条插入记录，消耗35 s
285 tps
