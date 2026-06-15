---
title: VS Code 配置 CC++ 编程运行环境（保姆级教程）
description: 
slug: VS Code 配置 CC++ 编程运行环境（保姆级教程）
date: 2025-09-15 00:00:00+0000
categories:
    - 计算机
tags:
    - IDE
weight: 1
---
#### 文章目录

在本教程中，将会安装 Visual Studio Code（后简称 VS Code），并在 VS Code 中安装 C/C++ 相关插件， 同时也将 VS Code 配置为使用 MinGW-W64 中的 GCC C/C++ 编译器（gcc/g++）和 GDB 调试器来创建在 Windows 上运行的程序。配置 VS Code 后，你将编写、编译、运行和调试大多数的 C/C++ 程序。

本教程所有参考内容均来自[Documentation for Visual Studio Code](https://code.visualstudio.com/docs)。

## 一、软件下载

### 1\. 下载 [VS Code](https://so.csdn.net/so/search?q=VS%20Code&spm=1001.2101.3001.7020) 安装工具

官方下载链接：[Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)

![7f80c3eec60906ceb43f56e369563f74_MD5|1541x1111](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515213.png)

直接点"Download for Windows"就可以进行下载。

## 2\. 下载 [MinGW-W64](https://so.csdn.net/so/search?q=MinGW-W64&spm=1001.2101.3001.7020)

MinGW-W64 可以去[MinGW-w64](https://www.mingw-w64.org/)的官网下载，也就可以直接去 MinGW-W64 的 [GitHub](https://so.csdn.net/so/search?q=GitHub&spm=1001.2101.3001.7020) 上下载。由于在官网下载容易下错，所以我这里给一个 GitHub 的链接，也是在 VS Code 上提供的链接。（官方认证，绝对没错！）

**MinGW-W64下载链接：**[Releases · msys2/msys2-installer (github.com)](https://github.com/msys2/msys2-installer/releases/)

进入链接后，可以看到历史版本的更替，截至本教程编写日期，最新版本为 [2024-01-13](https://github.com/msys2/msys2-installer/releases/tag/2024-01-13) 的版本，单击日期跳转至下载窗口。

![476aecba1ab747ee5a55ed1d9b498ce1_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515214.png)

如下图所示，选择`msys2-x86_64-20240113.exe`（记住前缀是 msys2-x86\_64 就行，后面是日期），点击后面的下载标志。

![5b9c8be152990abc65291bc835bb9820_MD5|1587x1086](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515215.png)

## 二、安装 VS Code

双击运行`VSCodeUserSetup-x64-1.87.2.exe`。

![c3558dbd1087b58d7eecd572ef9e2c4d_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515216.png)

如果出现如下弹窗，单击`运行`即可。

![7bb69409b266c1ec18e6243d4c970b02_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515217.png)

选择`我同意此协议`并单击`下一步`。

![6f14e8d313267fc3e30f29dc6085da24_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515218.png)

这里提示 VS Code 的安装位置，我只有一个 C 盘（现在的固态硬盘可以选择不分区），所以选择默认默认路径，直接点击`下一步`。当然，你的电脑硬盘要是有分区的话，可以选择其他路径。

![48bb6bfa0b0293e725dafdae6c414731_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515219.png)

这一步是创建快捷方式的名字，可以输入其他名字，下面的选项如果不勾选，就会把快捷方式添加到开始菜单中。我选择默认，直接点`下一步`。

![f9ecfaf8dc0cec7788bf1ad0e5896644_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515220.png)

默认只有最后两项被选中，我全部选上，单击`下一步`。![43b164df51f33c05422be28fee868679_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515221.png)

最后再确认一下信息，确认之后直接安装即可。

![cdea826d422202f6ae58b27f598bf3b8_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515222.png)

大概一分钟左右就可以安装完成。

![5bcfe256171638b72e430557d07b2014_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515223.png)

安装完成后，先暂时不运行 VS Code，把勾选去掉，点击`完成`。

![e8c688066064b714ebfd4fdda0c9f70d_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515224.png)

## 三、安装 MinGW-W64 及配置环境变量

双击`msys2-x86_64-20240113.exe`运行安装程序。

![7a08104b558e0cfb80d3eb10f435a004_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515225.png)

> \[!CAUTION\]
> 
> **请注意，MSYS2 需要 64 位 Windows 8.1 及以上版本。**

此界面直接点击`下一步`。

![a75e42f8a4cb267d484f44f2f3e3ef0b_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515226.png)

选择安装的路径，我这里选择默认，同学们可以根据自己的情况修改路径，之后点击`下一步`。

![89e409b9131ad4b3ad5e5b002d551c11_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515227.png)

开始菜单中的名字，这个还是可以直接默认，点击`下一步`。

![b08ce9d98436dec01679de4d8a444530_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515228.png)

开始安装。

![a712abaa52eba8dbd0fc917ed42a3496_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515229.png)

待进度条走完，直接点击`下一步`。

![53fb3a4986a6013a2670830a25d32871_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515230.png)

默认勾选`立即运行MSYS2`，单击`完成`。

![6f400a95da7815ba8fc5ce73dc036815_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515231.png)

当按下`完成`之后，会弹出打开一个 MSYS2 终端窗口。

![8027ef2765d2e00c620dbcda97aae614_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515233.png)

在此终端中，通过输入以下命令并按回车键，安装 MinGW-w64 工具链：

```csharp
pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain
```

出现这个界面，直接按回车键，默认接受所有的安装包。

![9823bfa0befec0b87d51bf628de04152_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515234.png)

当系统提示是否继续安装时，请输入`y`并回车。

![b1654425a4dbce88358e9defd2a7e12c_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515235.png)

之后就进入安装过程，稍等片刻。

![5d00d30f826899f80e7b14b2fde36b90_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515236.png)

当所有的包都安装好后，直接关闭终端。

![ab7cfe998419f9fd366100f207d59d90_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515237.png)

打开安装 MSYS2 的目录，先找到`ucrt64`文件夹并进入，再找到`bin`文件夹并进入，然后在地址栏中，复制路径。

如果一开始用默认路径，那路径就是`C:\msys64\ucrt64\bin`。

![4b5eec374402b6eae4bf8407b69ca698_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515238.png)

然后在搜索框中输入 `编辑系统环境变量`，并打开编辑系统环境变量的设置界面。

![312dc92013c55e5178f5e24b1ebc59d2_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515239.png)

在系统属性的弹窗中，点击`环境变量`。

![97c513a1c96d5011f5ca54ea9fae0896_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515240.png)

在弹出的环境变量弹窗中，找到用户变量的`Path`，并双击打开。

![8dccb7cddf189bd4759a43aa9e636628_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515241.png)

此时会弹出编辑环境变量的窗口，先点击`新建`按钮，然后会在空白行中出现一个输入框和一个闪烁的光标，在这里粘贴上广告复制的路径，最后点击`确定`按钮回到上层弹窗。

![6834c8aaae61b914296284da922e5010_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515242.png)

最后逐层弹窗点击`确定`按钮退出即可。

![d4e9d4c44a696f4d563ae72ebea2f297_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515243.png)

最后做一下测试，按组合键`Win + r`之后，输入`cmd`回车。

![bf2c6719825581295347e585c9f68b08_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515244.png)

回车之后，就可以调出 CMD 的终端窗口了，然后分别输入下面的命令，每输入一次命令后回车一次。

```css
gcc --version
g++ --version
gdb --version
```

出现如下图一样的信息，就说明 C/C++ 的编译环境已经安装好。

![f29705d5d328800bd016f0560ff25958_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515245.png)

## 四、配置 VS Code 的 C/C++ 编程运行环境

### 1\. 汉化 VS Code（选做）

这个配置环节并不属于 C/C++ 编程运行环境的配置必要环节，先挑战或想适应英文开发环境的同学可以跳过。

考虑到很多同学的英文水平可能不是很好，对于全英文的开发环境会犯难，这里可以使用 VS Code 自带的汉化插件来解决这个问题。

首先启动 VS Code 软件，按下组合键`Ctrl + Shift + x`，或者直接点击左边的第五个小图标，进入`Extensions`。

![97687893ef833db88cca51ed07c0e26d_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515246.png)

在上方输入框中键入`Chinese`，扩展插件的列表会刷新出汉化插件，点击对应的`Install`按钮进行安装。

![2e3cac2e74d3e678033fc43ba1cbc6a1_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515247.png)

安装好后，软件界面的右下角会弹出通知，并附带`Change Language and Restart`的按钮，点击这个按钮，即可重启软件。

![dbfffddf56c487fa1430661eeb761ee5_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515248.png)

软件重启后，就是中文的界面了。

![c44954b29f84c088e321ddd50648d886_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515249.png)

### 2\. 安装 C/C++ 扩展包

在`Extensions`中搜索"C++"，列表第一个扩展包就是我们要的，点击`安装`即可。

![5e3b0b59b52aa19a49e4ffc4f6ef46a1_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515250.png)

> \[!TIP\]
> 
> 上图中的`C/C++ Extension Pack`是 C/C++ 的扩展功能包，里面包含了一些项目管理和代码构建的工具，不是必要的扩展包，可以选择性安装。

## 五、测试 VS Code 的 C/C++ 编程环境

### 1\. 创建代码文件夹

VS Code 是一款基于文件夹进行代码编辑和管理的编辑器，通常我们会把新建一个文件夹来管理同一个项目的代码，并在 VS Code 中打开。

我新建了一个名为`Code`的文件夹，并在里面新建了一个用于专门放 C 语言代码的文件夹。

![cd55390993c53442897b921b67237b52_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515251.png)

> \[!WARNING\]
> 
> 需要注意的是，这个路径最好不要存在中文，否则会出现编译失败等问题。

打开 VS Code，点击`打开文件夹`的按钮。

![2cc9210fad7e25e31d607d16d75ece88_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515252.png)

在弹窗中找到刚刚新建的`C`文件夹，选中文件夹，再点`选择文件夹`。

![fe5bb2c117114cd2513280a9c088b8cd_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515253.png)

选中文件夹后，在新弹出的窗口中，勾选上`信任父文件夹"Documents"中所有文件的作者`，再点`是，我信任此作者`。

![a7b62d617a2c5d449a7e127627edb1e8_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515254.png)

文件添加好后，在左边的资源管理器中会出现`CODE`文件夹以及子文件夹`C`，把鼠标放在文件夹上面，会出现四个小图标。四个小图标从左往右的作用分别是**新建文件**、**新建文件夹**、**刷新资源管理器**以及**在资源管理器中折叠文件夹**。

![b6d18bd3dafe34f495fb50cdf2e843f4_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515255.png)

好了，做到这一步，接下来就可以进行代码的运行和调试了。

### 2\. 单个 .c 文件的运行和调试

为了方便管理代码，我们先选中`C`文件夹，再点击`新建文件夹`按钮。

![3049bb1999cb8a079c1889a6d55bf847_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515256.png)

此时会在`C`文件夹的下级出现一个输入框，我们新建一个名为`test`的文件夹。

![005450174abf7d2ca4479f46944c01dc_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515257.png)

鼠标右键`test`文件夹，在弹出的菜单中选择`新建文件`。

![ee520d29fa0d2caf8c1f3904c23f6220_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515258.png)

在输入框中输入我们接下来要进行调试代码文件名，命名为`test.c`，注意，一定要是 .c 结尾。

![d7c45bcf89b0b7641f97cb08d44b738d_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515259.png)

接下来就可以输入一个调试程序了，我的代码如下：

```cpp
#include <stdio.h>

int main()
{
    for (int i = 0; i < 5; i++)
        printf("Hello Grayson~%d\n", i); 

    return 0;
}
```

写好测试代码后，点击右上角的调试按钮，这时会弹出调试程序的选项，选择第一个，也是本教程前面安装的 gcc 编译工具。

![bd3c7e038f48478d9e23bbae152302e3_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515260.png)

这时文件就被编译并执行，如果在右下角弹出如下窗口，点击`是`即可。

![898745034a873352d6150489220e49ca_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515261.png)

运行结果如图所示。

![fa1dfa632b5a4d050dd195af06b9e536_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515262.png)

如果要进行简单的断点调试，可以在行号前加一个断点，操作也很简单，只需用鼠标左键点一下行号左边的空白处即可。如下图所示，是在第六行处加了一个断点。

![349f17b2acd2531f6bfe1b5e99dddde2_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515263.png)

这时再去运行程序，搜索框下面就会出现调试的面板，面板上有六个按钮，分别是**继续**、**逐过程**、**单步调试**、**单步跳出**、**重启**和**停止**。

![1e85a3aabb92a5dd981968dc850cfd54_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515264.png)

> \[!IMPORTANT\]
> 
> 以下是 VS Code 中的 C 语言代码调试面板功能的解释：
> 
> 1.  **继续**（Continue）：继续执行程序，直到遇到下一个断点或程序结束。
> 2.  **逐过程**（Step Over）：逐行执行当前行，如果当前行是函数调用，则进入该函数并执行完毕。
> 3.  **单步调试**（Step Into）：逐行执行当前行，如果当前行是函数调用，则进入该函数并停在函数内的第一行。
> 4.  **单步跳出**（Step Out）：执行完当前函数的剩余部分，并停在当前函数被调用的下一行。
> 5.  **重启**（Restart）：重新启动程序的调试会话，即从程序的起点开始执行。
> 6.  **停止**（Stop）：停止程序的调试会话，结束调试过程并关闭程序执行。

目前这个程序还不能很好说明以上的调试功能（至少**逐过程**、**单步调试**和**单步跳出**这三个并不明显），所以在后面的内容将以另一个代码进行演示。

### 3\. 多个 .c 文件的运行与调试

如果想要进行多个 .c 文件编译后的调试，就需要进行一些配置修改。如果进行过一次编译运行，我们会发现在资源管理器的`C`文件夹下，多出一个`.vscode`的文件夹，这个文件夹里面有个`tasks.json`的文件

![9ccdf1e271086dc88a8eef24489f27eb_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515265.png)

这个文件是用于定义任务配置，这些任务可以在 VS Code 中运行，例如编译代码、运行测试、启动调试器等。`tasks.json`文件是一个 JSON 格式的文件，其中包含了任务的配置信息，包括任务名称、命令、参数等。通过编辑`tasks.json`文件，我们可以自定义项目中的各种任务，并在 VS Code 中方便地执行这些任务。

当前的 VS Code 的运行效果还不是很理想，双击打开`tasks.json`文件修改一下编译运行功能。下图是对该 JSON 文件做了部分解释。

![2059bc4eb5fec28d9ed942bf26a2f25f_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515266.png)

具体修改如下图所示，我注释掉了原来的`"${file}"`，并新增一行`"*.c"`，表示并非指定某一个 .c 文件，而是当前文件夹下所有的 .c 文件。同时也把`"${fileDirname}\\${fileBasenameNoExtension}.exe"`注释掉，改成`"${fileDirname}\\program.exe"`，那么多个 .c 文件编译之后的可执行文件就是`program.exe`。

![fd57ca87ceefff41b4d30d27db97b1b4_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515267.png)

修改好后，按组合键`Ctrl + s`保存即可。

然后点击左侧的`运行与调试`，再点击`创建launch.json文件`。

![5634ee29a496721a544540bfa904e4f9_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515268.png)

搜索框会弹出选项，选择`C++(GDB/LLDB)`。

![fff193696fb51eb87f25cab86706bd86_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515269.png)

然后 VS Code 会新建一个 JSON 文件，点击右下角的`添加配置`，在弹出的下拉菜单中选择`C/C++：（gdb）启动`。

![bd8ac500f7d2a2886afaa0ef8ecbebed_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515270.png)

此时，JSON 文件会多出一些配置信息，需要我们修改的内容如下图所示的红框标志内容。

![e2ba54d179f710a0d999bd62f5a3571d_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515271.png)

修改为下图红框所示内容，`"program"`后的内容就是前面提到的`tasks.json`文件中的编译后产生的可执行文件。`"miDebuggerPath"`后面的则是前面安装的 MinGW-W64 的 gdb 工具的路径。修改后保持关闭。

![7664d828b6ac9435d896ac11f022ef17_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515272.png)

> \[!NOTE\]
> 
> 在复制粘贴 gdb 的路径时，不少小伙伴会忽略掉下图所示的问题。反斜杠是转义字符的作用，应该像上图一样多加一个一个反斜杠才表示路径。
> 
> ![6d4c6c66bef37d79f3e584e3b5b921b2_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515273.png)

之后，我们进行多文件的编译调试，先在`C`文件夹下新建一个新的文件夹，我这里命名为`test2`，并在这个文件夹里面新建三个文件，分别是`test.c`、`max.h`和`max.c`。

![3eb1d7560c53486e592b3caa7f8e0d63_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515274.png)

代码如下：

max.h

```cpp
#ifndef __MAX_H__
#define __MAX_H__
#include <stdio.h>

int findMaxNum(int num1, int num2);

#endif // __MAX_H__
```

max.c

```cpp
#include "max.h"

int findMaxNum(int num1, int num2)
{
    return num1 > num2 ? num1 : num2;
}
```

test2.c

```cpp
#include <stdio.h>
#include "max.h"

int main()
{
    int a = 10;
    int b = 20;
    int c = findMaxNum(a, b);
    printf("%d\n", c);
    return 0;
}
```

代码写好后，给`test2.c`的第 8 行代码打一个断点，再点调试按钮旁边的小三角形，在下拉菜单中选择`调试C/C++文件`。

![c895b446212dc210961f5ee0a789dea1_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515275.png)

调试面板依旧是之前的那个。如果点击`继续`，调试过程会跳到下一个断点，不过我们这个程序只打了一个断点，所以会直接运行到程序结束并退出调试。

![616baeed0dd989b5df01114d6c53277d_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515276.png)

如果点击`逐过程`，则在不进入函数内部，而是直接输出函数的运行结果，然后跳到下一行。

![78d224f1e79b4dcafeb062c084c06c5d_MD5](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515278.png)

如果点击`单步调试`，则会进入被调用函数的内部，继续点击`单步调试`会一步一步执行并返回。如果进入函数后，点击`单步跳出`则直接带着函数的执行结果返回被调用处。

![b66b44759fc3585fdf18761046aac7e0_MD5|1227x380](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20251206143515279.png)

___

## 参考资料

[《Running Visual Studio Code on Windows》](https://code.visualstudio.com/docs/setup/windows)

[《C++ programming with Visual Studio Code》](https://code.visualstudio.com/docs/languages/cpp)

[《Get Started with C++ and MinGW-w64 in Visual Studio Code》](https://code.visualstudio.com/docs/cpp/config-mingw)