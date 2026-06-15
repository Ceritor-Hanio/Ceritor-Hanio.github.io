---
title: PostgreSQL密码重置方法
description: 
slug: PostgreSQL密码重置方法
date: 2025-09-15 00:00:00+0000
categories:
    - 计算机
tags:
    - Web
weight: 1
---
## 前言

最近接手一个离职同事的电脑，他本地安装了[postgresql](https://zhida.zhihu.com/search?content_id=215602550&content_type=Article&match_order=1&q=postgresql&zhida_source=entity)，并且使用Navicat已经连接上了这个本地postgresql数据库，但是我自己不知道这个数据库的密码，我想用[Jdbc](https://zhida.zhihu.com/search?content_id=215602550&content_type=Article&match_order=1&q=Jdbc&zhida_source=entity)去连接这个数据库就没戏了，我试了postgres,123456这种常见的密码都不正确后，我打算重置这个数据库的密码。

## 密码重置方法汇总

###   **工具已登陆**

  
这个就是最简单的方法，你有工具登陆过，完全可以通过工具来修改（可是我当时完全没想到这个。。。），我是通过Navicat来连接的，可以直接通过Navicat来修改步骤如下：  
1、连接数据库  
2、点击角色  
3、选择角色  
4、填入新密码  
5、保存之后，关闭连接，编辑连接就OK了。  

![4d6d8bb379dc4efa0eb4a78b98aa1a78_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251209220935094.jpg)

![14b2243f9e1e3427270759a862c16ca0_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251209220935095.jpg)

###   **工具未登录**

  
**Windows**  
1、找到Postgresql安装目录下的data，打开文件夹，找到[pg\_hba.conf](https://zhida.zhihu.com/search?content_id=215602550&content_type=Article&match_order=1&q=pg_hba.conf&zhida_source=entity)  
ps：如果大家找不到，那我推荐一个文件搜索神器：[Listary](https://zhida.zhihu.com/search?content_id=215602550&content_type=Article&match_order=1&q=Listary&zhida_source=entity)，大家可以去试试，贼好用  

![70b70de8a1efe9774f6a1b456202e8b6_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251209220935097.jpg)

  
2.用记事本格式打开，拉到最下面，找到所有md5,全都改为trust  

![d18119129bff08ce8c8d0efe4e4e82ce_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251209220935098.jpg)

  
3.重启数据库，然后连接数据库，不输入密码，直接点连接，此时连接成功  
ps：在windows的控制面板中，找到管理工具，然后找到服务：postgresql，点击右键 ,重启就行了。  

![4cb6913b6700505d4fe130d5f1f8a849_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251209220935099.jpg)

  
4.修改密码  
在客户端修改  
alter user postgres with password 'YOUR　PASSWORD'  
5.或者重新打开[pgAdmin](https://zhida.zhihu.com/search?content_id=215602550&content_type=Article&match_order=1&q=pgAdmin&zhida_source=entity)（即数据库）,连接服务器，不输入密码，直接点连接，此时连接成功  
6.修改密码，右键登陆角色中要修改密码的账户，打开属性，点击定义，输入密码，然后确定，此时修改密码成功。如果重新打开定义会发现密码栏里依旧空白，但此时密码已是新密码。  

![1fed32059cc57c8444a08168f17fe300_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251209220935100.jpg)

  
7，最后将第一二步中的trust改回md5。重新启动数据库，输入密码，成功连接服务器。  
参考链接：[https://mp.csdn.net/mdeditor/96288907](https://link.zhihu.com/?target=https%3A//mp.csdn.net/mdeditor/96288907)  
**Linux**  
如果是Linux下的话：  
1、找到pg\_hba.conf路径  
运行  
ps ax | grep postgres | grep -v postgres:  
得到：  
25653 pts/0 S+ 0:00 /usr/lib/postgresql/9.3/bin/psql -h 192.168.10.10 -p 5432 -U postgres -W 26679 ? S 0:00 /usr/lib/postgresql/9.3/bin/postgres -D /var/lib/postgresql/9.3/main -c config\_file=/etc/postgresql/9.3/main/postgresql.conf 26924 pts/7 R+ 0:00 grep --color=auto postgres  
注意结果中有一个config\_file,而config\_file=/etc/postgresql/9.3/main/就是我们配置所在地  
2、无密码postgres登录  
修改pg\_hba.confg  
#原来是 host all all 127.0.0.1/32 md5 # IPv6 local connections: host all all ::1/128 md5 #改成 host all all 127.0.0.1/32 trust # IPv6 local connections: host all all ::1/128 md5  
ps:如果你重启之后还是登陆不了，也可以将全部md5修改为trust  
重启postgresql服务  
sudo service postgresql restart  
登录  
psql -h 127.0.0.1 -U postgres  
3、登录修改密码  
修改密码  
alter user postgres with password 'YOUR　PASSWORD'  
最后将pg\_hba修改回去就好啦，也就是将所有的trust还原为md5。