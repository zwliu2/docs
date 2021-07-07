## sql注入基础
### 1. sql布尔型blind注入
当页面不返回任何数据库查询信息时，比如只返回操作正确或者错误，此时需要选择盲注来确定数据的内容和长度。

#### 确定内容长度
`1' and if(length(database())=5,1,0)--`
此语句表示如果database()的长度为5 则返回1 反之返回0。
如果需要快速得到内容长度，可以通过burpsuite抓包后直接进行爆破。





SCHEMATA 表
INNODB_SYS_TABLES 
INNODB_SYS_COLUMNS  

** 判断字段数

\# 备注 table1中有3个字段,如果order by后不是3 语句都会报错
select * from table1 where id='1' order by 3;
1' union select 1,2,3 --