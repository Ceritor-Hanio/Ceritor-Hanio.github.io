---
title: 博客部署-hugo博客云服务器部署
description: 
slug: 博客部署-hugo博客云服务器部署
date: 2025-09-15 00:00:00+0000
categories:
    - 计算机
tags:
    - Web
weight: 1
---
 经过好长一段时间的折腾，终于搭建了一个自己看上去舒服的博客，现在可以写一下博客，为大家自建博客扫除困难。

不同人选择自建博客的路径不同，会遇到的bug不尽相同，所以自建博客的过程必然困难重重。我的博文只能指明一条清晰明了的路径，并且尽力扫除这条路径的所有阻碍。不过一些较基础的操作，我会交给你去自己搜索学习。

## 1. 本地部署hugo
### 1.1 安装hugo
1. 到 [github](https://github.com/gohugoio/hugo/releases) 下载适合你电脑的版本，解压到合适的位置
2. 将解压出来的文件加入环境变量
3. 找个合适的地方，打开命令行，并输入
```bash
hugo new site xxx # xxx是随便一个名字
```
4. 打开 $xxx$ 文件夹，你会看到很多文件，我会向你介绍比较重要的：
	- config.yaml或config.toml               配置文件
	- content                                           内容文件夹，你的文章将被存放在这
	- themes                                            主题文件夹
	- public                                              静态网站文件（现在没看见不要紧）

### 1.2 加载主题
1. 访问[官方主题市场](https://themes.gohugo.io/) ，选择自己喜欢的主题
2. 点进去，点 $Download$ ，进入该主题的 $github$ 主页
3. 根据 $github$ 上介绍的方法安装该主题
	
	这里我展示一下主题 $stack$ 的安装方法。（因为它的配置文档写得很差）
	1. 命令行输入
	```bash
	cd /xxx/themes
	git submodule add https://github.com/CaiJimmy/hugo-theme-stack/ hugo-theme-stack
	#如果git失败，复制错误输出，到浏览器搜索解决方法
	```
	2. 将 $themes/hugo-theme-stack/exsampleSite$  里面的所有文件复制并粘贴到 $xxx$ ，替换原有文件
4. 建立第一篇文章
	```bash
	hugo new post/my-first-post.md
	```
	所有的文章都建立在 $/xxx/content/post$ ，可以删除自带的默认文章

### 1.3 本地网站建立
1. 可以自己编辑 `config.yaml` ，自定义网站外观
2. 在命令行输入 `hugo server` ，$ctrl +$ 鼠标点击出现的网址，你就可以看到自己的网站了！

### 1.4 个性化部署（待建）
这部分比较复制，有时间再单开一篇博客

### 1.5 obsidian 部署
如果你喜欢用 $obsidian$ ，你可以直接把 $post$ 定成 $obsidian$ 的仓库.

3.  如果你有了解插件 $Templater$ 甚至直接把 `my-first-post.md` 定成模板,我的模板是这样写的：
```markdown
---
title: 模板
description: 
date: <% tp.date.now("YYYY-MM-DDTHH:mm:ssZ") %>
image: 
math: true
license: 
hidden: true
comments: true
draft: true
tags:

---
```
可以在  `config.yaml`  添加以下代码，将模板隐藏，避免出错。

```yaml
module:

  mounts:

  - excludeFiles: post/模板/模板.md

    source: content

    target: content
```
4. 这里是插件 Shell  command 配置的代码，后面部署会用到
```bash
cd D:\Internet-blog\codingxiaoma
hugo
cd .\public\
git add .
git commit -m 'first commit'
git push server main
git push git main -f
```
## 2. 部署github页面
### 2.1 连接GitHub
1. 登录GitHub账号
2. 命令行输入 `ssh-keygen -t rsa -C "xxx@xxx.com" # 填写你的github邮箱地址`，一路$enter$
3. 然后在 `C:\Users\你的账户\.ssh` 里面，记事本打开公钥，并复制
	-  `id_rsa` 私钥
	- `id_rsa.pub` 公钥
4. 登录GitHub，Settings->SSH and GPG Keys->add SSH Key,将公钥粘贴进去

### 2.2 建立GitHub页面
1. 建立新仓库
	登录后，在左上角，点击绿色`New`，建立新仓库
	![image.png](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20250211182133072.png)
2. 然后像下面这样书写和勾选
![image.png](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20250211182510150.png)
3. 然后直接点击最下面的 `create repository`


### 2.3 将静态页面发布至GitHub

1. 准备工作 命令行输入
	```bash
	cd xxx/public #进入存放静态文件的位置
	git init#将public设为本地的repo
	git branch -m main #将本地分支改名为main

	git remote add server git@github.com:xxx/xxx #在下图的位置复制

	```
![image.png](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20250211183342596.png)
2. 推送 命令行同位置输入
	```bash
	git add . #将public的内容加入分支
	git commit -m 'first commit'
	git push server main -f#-f表示强制覆盖
```

3. 然后你就可以访问到你自己的网站了
![image.png](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20250211183823118.png)

## 3. 部署云服务器页面

### 3.1 购买服务器和域名

可以到[便宜服务器](https://kubk.net/800.html)上面买个便宜服务器。
### 3.2 安装docker

1. 防火墙端口开放
	1. 在阿里云轻量应用服务器的控制页面，点击防火墙模板
		![image.png](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20250213001240385.png)
	2. 点击创建模板，创建三个开放22、80和443端口的模板，然后将模板应用到我们的服务器

2. 远程连接服务器
	可以用`xshell`和 `WinScp` 远程连接服务器，不过因为阿里云提供相应的工具，我就不使用了。
	阿里云的控制账户需要重置密码，没有初始密码的。
3. [docker部署](https://help.aliyun.com/zh/simple-application-server/use-cases/manually-deploy-docker?spm=a2c4g.11186623.help-menu-58607.d_3_0_1_4_1.1c8a112deLyOQT&scm=20140722.H_2842479._.OR_help-T_cn~zh-V_1#2054cb93deu58)
	这个不难，直接根据你服务器的系统去搜索如何安装 $docker$ 就行
### 3.3 git 将 public 静态文件同步到服务器
1. 安装 $git$ 
	这个也是根据你服务器的系统去搜索。
2. 如果你的系统是 $Linux$ ，就可以在
## 4. 搜索引擎收录

## 参考
- [搭建hugo](https://hyrtee.github.io/2023/start-blog/#%E5%AE%89%E8%A3%85-hugo)
- [bing收录图标](https://blog.reincarnatey.net/2024/0802-bing-crawl-website-icon/)
- [便宜服务器](https://kubk.net/800.html)
- [docker部署](https://help.aliyun.com/zh/simple-application-server/use-cases/manually-deploy-docker?spm=a2c4g.11186623.help-menu-58607.d_3_0_1_4_1.1c8a112deLyOQT&scm=20140722.H_2842479._.OR_help-T_cn~zh-V_1#2054cb93deu58)
- [dockerCompose安装nginx部署hugo静态博客](https://blog.5zx.top/posts/myblog27/)
- [域名部署](https://www.dianbanjiu.com/post/%E6%90%AD%E5%BB%BAmemos/)
- [hugo添加备案号](https://laosji.net/p/hugo-stack%E5%A6%82%E4%BD%95%E6%B7%BB%E5%8A%A0%E5%A4%87%E6%A1%88%E5%8F%B7/)