# csv文件行转列


## csv文件形式如下


每行中的字段采用制表符分割

```
用户名	时长	数值
a	时间1	v1
a	时间2	v2
a	时间3	v3
b	时间1	v4
b	时间2	v5
c	时间1	v6
c	时间2	v7
c	时间3	v8
c	时间4	v9
```

## 需要转换的形式如下

```
用户名	时间1	时间2	时间3	时间4
a	v1	v2	v3	
b	v4	v5		
c	v6	v7	v8	v9
```

## 使用方法

运行命令：`python trans_row2col.py xxx.txt`


程序运行成功后，会生成名称类似 xxx.export.txt 的文件
