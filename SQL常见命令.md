SHOW databases; 显示所有库
USE the_database; 使用某个库
CREATE DATABASE database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci; 创建库
DROP database the_name;  删除库


SHOW TABLES;

创建表 和 字段
CREATE TABLE `product_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amis_user` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `product` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_del` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4

展示表结构
SHOW CREATE TABLE your_table_name;
字段信息
DESCRIBE your_table_name;

增加字段
ALTER TABLE example_table
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

修改 自动更新时间 字段
ALTER TABLE your_table_name
MODIFY COLUMN update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

删除表数据
delete from mytable where name='';

重置表
truncate table mytable;

删除表
drop table table_name;

查询
select * from students where 1=1 and id<10 or age>20 join score on score.stu_id=students.id group by class order by name;

** 插入数据 **
insert into table_name(列名) values(值)


# ON
ON DELETE 和 ON UPDATE（用于外键约束）
用于定义外键约束时，指定当相关联的记录被删除或更新时的行为，比如 CASCADE、SET NULL、NO ACTION 等。

主键约束：primary key
唯一约束：unique
非空约束：not null
默认约束：default
外键约束：foreign key（外键）references主表（主键）




