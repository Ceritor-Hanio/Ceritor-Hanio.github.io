---
title: c语言程序设计简单复习
description: 
slug: c语言程序设计简单复习
date: 2025-09-15 00:00:00+0000
categories:
    - 计算机
tags:
    - C语言
weight: 1
---
给老手的复习地图，忽略程序理解，注重复习某些小知识点。
# 第一章
## C程序的构成
- 引入文件
- 主函数
- 返回值

## 常见标识
1. 关键字
	1. 数据类型关键字
		- char	        声明字符变量
		- double	声明双精度变量
		- float  	声明浮点型变量
		- int	        声明整型变量
		- short	声明短整型变量
		- long	        声明长整型变量
		- unsigned	声明无符号类型变量
		- signed	声明有符号类型变量
		- struct	声明结构体变量
		- union	声明共用体或联合数据类型
		- void	        声明函数无返回值或无参数，声明无类型指针
		- enum	声明枚举类型
	- ==进制转换！==
	1. 控制语句类型关键字（5个）
		1. 循环语句
			1. for	        遍历循环
			2. do	        其后紧跟循环体
			3. while	条件循环或死循环
			4. break	跳出当前循环
			5. continue	终止本次循环，开始下次循环
		2. 条件语句类型关键字
			1. if	        条件语句
			2. else	        条件语句否定分支
			3. goto	无条件跳转语句
	2. 返回语句类型关键字
		1. return
	3.  存储类型关键字	

| 序号  | 关键字      | 说明                            |
| --- | -------- | ----------------------------- |
| 1   | auto     | 声明自动变量                        |
| 2   | extern   | 声明变量是在其他文件定义                  |
| 3   | register | 声明寄存器变量                       |
| 4   | static   | 声明静态变量（1. 隐藏，2. 持久 3.默认初始化为零） |
4. 其它关键字

| 序号  | 关键字      | 说明             |
| --- | -------- | -------------- |
| 1   | const    | 声明只读变量         |
| 2   | sizeof   | 计算数据类型长度（字节数）  |
| 3   | typedef  | 给数据类型取别名       |
| 4   | volatile | 所修饰的对象不能被编译器优化 |
2. 标识符
	1. ![image.png](https://s2.loli.net/2024/11/23/mgI9KHxYyUqrSQT.png)
		![image.png](https://s2.loli.net/2024/11/23/RgtNDoka3yl68sm.png)
		![image.png](https://s2.loli.net/2024/11/23/xI8ohpcYzFXfKZO.png)
		- i++表示i参与运算后，i的值再自增1。
		- ++i表示i自增1后，再参与其它运算。
1. 分隔符
## 数据类型
![image.png](https://s2.loli.net/2024/11/23/I9Oo6BVDthHcLZm.png)

### **结构体** 
![image.png](https://s2.loli.net/2024/11/23/3Sigd6mhP8rDxoy.png)


### 数组


### 共用体


## 格式化输入输出

- printf("%?",?);
- scanf("%?",&?);
		![image.png](https://s2.loli.net/2024/11/23/zhryPBa2Cgtj841.png)

## 书写规则

- C语句都是以分号作为结束标志的
- C程序的书写格式比较自由（建议一行只写一条语句）
- C语言代码划分段落。"段"是以"{}"来进行划分的
- 为了对程序进行必要的说明，可以添加注释，它有两种方式/* ...  * /和//...。


## 流程图
![image.png](https://s2.loli.net/2024/11/23/Tl87kphBFJXLICz.png)


## 进制

![image.png](https://s2.loli.net/2024/11/23/eIMSTlsQF3WkOHE.png)

- ![image.png](https://s2.loli.net/2024/11/23/bvrq2A5Ro8JXPsI.png)

## 正负数的存储
- 正数的原码，反码和补码相同
- 负数的补码可以由原码取反+1获得


# 第二章 · 选择结构

![image.png](https://s2.loli.net/2024/11/23/wxm5g7Lct84dKei.png)


## 表达式的返回值

- 赋值表达式
	- 或、与、非
	![image.png](https://s2.loli.net/2024/11/23/8gGaYXudPEC3zSy.png)

- 逻辑运算
- 

## switch

![image.png](https://s2.loli.net/2024/11/23/Qbm7JYPp82Ug9h1.png)

```c
int main(void)
{
      int nDay;
      printf("input integer number: ");
      scanf("%d",&nDay);
      switch (nDay)	/*判定表达式*/
     { 
	case 1: 
                      printf("Monday\n");
                      break;
	case 2:printf("Tuesday\n");break;
	case 3:printf("Wednesday\n");break;
	case 4:printf("Thursday\n");break;
	case 5:printf("Friday\n");break;
	case 6:printf("Saturday\n");break;
	case 7:printf("Sunday\n");break;
	default:printf("Error!\n");
    }
    return 1;
}

```
# 第三章·循环控制结构

## for
![image.png](https://s2.loli.net/2024/11/23/JmPguzcbi73kNwO.png)


## do-while
![image.png](https://s2.loli.net/2024/11/23/u3C5RizBs2OA7cb.png)

![image.png](https://s2.loli.net/2024/11/23/JdrmVnczqN2Z6AD.png)


- break
	- 直接退出循环
- continue
	- 跳出这层循环，进入下一层循环



# 第四章·模块化设计

## 函数
![image.png](https://s2.loli.net/2024/11/23/Uv2jyQZuONAfxIz.png)

- 函数声明
- 函数调用
	- 传参
		- ![image.png](https://s2.loli.net/2024/11/23/raZ6KPIC9UzNSTk.png)
			**将实参的值传给形参而已！**
			- 形参在被调用之前不会分配内存空间
		
		- 指针
			- 'int max(int * x)'
				- 可以通过给形参传实参的地址来修改实参的值
			- 数组的名字相当于数组的数组的首地址
			- 结构体的数组

## 宏定义

