---
title: "Flow Matching & Diffusion"
description: ""
slug: "Flow-Matching-Diffusion"
date: 2025-09-15 00:00:00+0000
categories:
    - 计算机
tags:
    - 视觉生成
weight: 1
---

## 1. 数学基础
### 1.0  生成与采样
1. 一个数据可以被投影到高维空间的一个点
	1. 图像
	2. 视频
	3. 蛋白质结构
2. 我们想要生成的东西（比如狗的图片），在高维空间符合某个概率密度函数 $p_{data}:\mathbb{R}^d \to \mathbb{R}_{\geq 0}$ 
3. 那么生成一张狗的图片，约等于对 $p_{data}$ 进行采样：$z∼p_{data}$ 
### 1.1 流模型
#### 1. 轨迹函数
 -    $X:[0,1]\to \mathbb{R}^d,t \mapsto X(t)$粒子在时间 $t$ 时的位置。
#### 2. 向量场 (Vector Field) 
*   **直观理解**：向量场就是空间中每个点上的“速度指示器”。你可以把它想象成天气预报里的**风向图**，或者水流的**漩涡图**。
*   **数学定义**：在数学上，向量场是一个函数 $v(x)$。它接收一个位置坐标 $x$（比如二维平面上的 $(x_1, x_2)$），输出一个向量（比如 $(v_1, v_2)$）。这个输出向量代表了在该位置粒子的**瞬时速度**（包含大小和方向）。
*   **关键点**：向量场本身是**静态**的。它只是把规则摆在那里，并没有发生实际的移动。
#### 3. 常微分方程 (ODE) 
*   **直观理解**：ODE 是连接“位置”和“速度”的桥梁。它描述了事物**如何随时间变化**。
*   **数学定义**：最基础的 ODE 形式如下：
	$$ \frac{dX(t)}{dt} = v(x(t)) $$
	*   $\frac{dx(t)}{dt}$：位置随时间的变化率，也就是**速度**。
	*   $v(x(t))$：粒子在当前位置 $x(t)$ 时，向量场给它的速度指令。
	*   **关键点**：这个方程在说：“你下一瞬间的移动速度，完全由你当前所在位置的向量场决定。”
#### 4. 流 (Flow) 
*   **直观理解**：流就是许多粒子顺着向量场的指引，随时间推移画出的那条**曲线（轨迹）**。在生成模型中，我们常说的“流”，就是指数据从噪声分布“流动”到真实数据分布的整个过程。
*   **数学定义**：流通常用 $\psi_t(x_0)$ 或 $\phi_t(x_0)$ 表示。它是一个**映射函数**，告诉你：如果一个粒子在初始时刻 $t=0$ 位于 $x_0$，那么在时间 $t$ 时，它会到达哪里。
*   **关键点**：流是 ODE 的**解**。它必须满足两个条件：
	1. **初始条件**：$\psi_0(x_0) = x_0$ （时间没开始动，位置不变）。
	2. **满足 ODE**：$\frac{d}{dt}\psi_t(x_0) = v(\psi_t(x_0))$ （轨迹上每一点的切线方向，必须和该点的向量场方向一致）。
- ==在流体力学中，这对应着两种观察世界的视角==：
	*   **欧拉视角 (Eulerian)**：你站在河边，观察水流过你面前时的速度。你关注的是空间中的固定点 -> **这就是向量场**。
	*   **拉格朗日视角 (Lagrangian)**：你跳进河里，顺流而下，记录自己随时间变化的位置。你关注的是单个粒子的轨迹 -> **这就是流**。
	*   **ODE** 则是连接这两种视角的数学语言：它告诉你，拉格朗日视角下的轨迹切线（速度），等于欧拉视角下该点的向量场。
#### 5. 流模型
1. 流模型的条件
	- $X_{0}∼p_{init}$ 
	- $\frac{d}{dt}X_{t}=u_{t}^\theta(X_{t})$
	- $X_{1}∼p_{data} \Leftrightarrow \psi_{1}^\theta(X_{0})∼p_{data}$
2. 流模型的采样过程
	![image.png|668x181](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20260611193000682.png)

### 1.2 扩散模型
#### 1. 布朗运动
满足的条件：
- 从零开始 $W_{0}=0$ 
- 增量符合正态分布 $W_{n}-W_{t} ∼\mathcal{N}(0, (t-s)I_d)$
- 增量之间互相独立
$W_{t+h}=W_{t}+\sqrt{h}\varepsilon_{t}$
#### 2. 从ODE到SDE
*   **ODE 的离散化：**
	原本 $X$ 的变化率是 $u_t(X_t)$。写成差分形式就是：
$$X_{t+h} = X_t + h \cdot u_t(X_t)+hR_{t}(h)$$
	(意思是：新位置 = 旧位置 + 步长 $\times$ 速度 + 步长 $\times$ 误差)
*   **ODE加入随机性 ：**
$$X_{t+h} = X_t + \underbrace{h u_t(X_t)}_{\text{确定性部分 (Drift)}} + \underbrace{\sigma_t (W_{t+h} - W_t)}_{\text{随机部分 (Diffusion)}} + \underbrace{hR_{t}(h)}_{\text{误差 (error term)}}$$
*   **符号表示 (Equation 7a)：**
	这就是 SDE 的标准写法：
$$\mathrm{d}X_t = u_t(X_t)\mathrm{d}t + \sigma_t \mathrm{d}W_t$$
	*   $u_t$ 是漂移系数（决定趋势）。
	*   $\sigma_t$ 是扩散系数（决定随机波动的强度）。
#### 3. 如何模拟 SDE？(Euler-Maruyama 方法)
既然电脑不能处理连续的微分 $\mathrm{d}t$，我们需要用离散的方法来模拟。这就用到了 **Euler-Maruyama 方法**（你可以把它理解为欧拉法的随机版本）。
*   **公式 ：**
$$X_{t+h} = X_t + h u_t(X_t) + \sqrt{h} \sigma_t \epsilon_t$$
	*   注意这里有个 **$\sqrt{h}$**。这是因为布朗运动的性质：时间间隔 $h$ 内的噪声方差是 $h$，所以标准差（噪声幅度）是 $\sqrt{h}$。
	*   $\epsilon_t$ 是从标准正态分布 $\mathcal{N}(0, I)$ 采样的随机数。
	![image.png](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20260611202217764.png)


### 1.3 Flow Matching

#### 1. 什么是概率路径 (Probability Path)?
*   我们要构建一个随时间 $t$ 变化的分布序列 $p_t$。
*   **起点 ($t=0$)**：$p_0$ 是初始噪声分布（比如标准高斯分布 $p_{\text{init}}$）。
*   **终点 ($t=1$)**：$p_1$ 是真实数据分布 $p_{\text{data}}$。
*   **中间过程**：我们需要定义 $0 < t < 1$ 时分布长什么样。

#### 2. 条件概率路径 (Conditional Probability Path) 
定义一个条件概率路径 $p_t(x|z)$。
*   **含义**：假设我们的目标仅仅是生成**某一个特定的数据点 $z$**（比如一张特定的猫的图片）。
*   **起点**：$p_0(\cdot|z) = p_{\text{init}}$（还是从噪声开始）。
*   **终点**：$p_1(\cdot|z) = \delta_z$。这里的 $\delta_z$ 是 Dirac delta 分布，意思是“确定性地在点 $z$ 处”。

#### 3. 边缘概率路径 (Marginal Probability Path)
*   **定义**：它是所有“条件概率路径”的加权平均。
*   **采样过程**：
    1. 先从真实数据集中随机抽一个点 $z \sim p_{\text{data}}$。
    2. 然后沿着这个点 $z$ 对应的条件路径 $p_t(\cdot|z)$ 采样 $x$。
- 
  $$
  	p_{t}(x)=\int p_{t}(x|z)p_{data}(z)dz
  $$
*   **结论 (公式 14)**：这样构造出来的总路径 $p_t$，在 $t=0$ 时是噪声，在 $t=1$ 时就是真实数据分布 $p_{\text{data}}$。

#### 4. 具体例子：高斯条件路径 (Example 8)
这是目前最常用的一种路径定义（公式 15）：
$$ p_t(\cdot|z) = \mathcal{N}(\alpha_t z, \beta_t^2 I_d) $$
*   这意味着，在时间 $t$，分布是一个高斯分布。
*   $\alpha_t = t$  **均值**是 $\alpha_t z$：随着 $t$ 从 0 变到 1，均值从 0 慢慢移向 $z$ ,
*   $\beta_t = 1-t$  **方差**是 $\beta_t^2$：随着 $t$ 从 0 变到 1，方差慢慢缩小到 0（从一团模糊的噪声收缩成一个点）。

### 1.4 条件向量场和边缘向量场
#### 1. 条件向量场 (Conditional Vector Field) 
*   对于每一个去特定点 $z$ 的流，都有一个对应的速度场 $u_t^{\text{target}}(x|z)$。
*   如果我们解这个 ODE（常微分方程）：$\frac{d}{dt}X_t = u_t^{\text{target}}(X_t|z)$，粒子就会沿着条件路径走到 $z$。

#### 2. 边缘向量场 (Marginal Vector Field) 
这是全篇最重要的结论，被称为**“边缘化技巧 (Marginalization trick)”**。
*   **问题**：我们想要一个总的速度场 $u_t^{\text{target}}(x)$，让噪声变成整个数据集。直接求很难。
*   **答案**：总的速度场 = 所有条件速度场的**期望（加权平均）**。
    $$ u_t^{\text{target}}(x) = \int u_t^{\text{target}}(x|z) \frac{p_t(x|z)p_{\text{data}}(z)}{p_t(x)} dz $$
    这个积分项 $\frac{p_t(x|z)p_{\text{data}}(z)}{p_t(x)}$ 其实就是后验概率 $p(z|x)$。
*   **直观解释**：
    假设你在位置 $x$，你该往哪个方向走？
    *   如果你要去点 $z_1$，速度场告诉你往左。
    *   如果你要去点 $z_2$，速度场告诉你往右。
    *   **最终的速度**就是这些方向的**平均值**（根据 $z$ 的可能性加权）。 ==使用连续性方程可以验证这是正确的！==
#### 4. 结论 
只要我们用这个算出来的总速度场 $u_t^{\text{target}}(x)$ 来跑 ODE，我们就可以成功地把初始噪声 $p_{\text{init}}$ 转换成真实数据 $p_{\text{data}}$。

#### 5. 高斯概率向量场公式推导
定义一个条件流 $\psi_t^{\text{target}}(x_0|z) = \alpha_t z + \beta_t x$
 1. 利用速度场的定义
速度场 $u_t$ 的定义是位置随时间的变化率 $\frac{\mathrm{d}}{\mathrm{d}t} x_t = u_t^{\text{target}}(x_t | z)$
我们先计算左边 $\frac{\mathrm{d}}{\mathrm{d}t} x_t$：$x_t = \alpha_t z + \beta_t x_0$
对 $t$ 求导（$z$ 和 $x_0$ 是常数，不随时间变化）：$\frac{\mathrm{d}}{\mathrm{d}t} x_t = \dot{\alpha}_t z + \dot{\beta}_t x_0$
根据定义，这等于速度场在位置 $x_t$ 处的值：
$$ u_t^{\text{target}}(x_t | z) = \dot{\alpha}_t z + \dot{\beta}_t x_0 \quad $$
 2. 第二步：变量代换
$x_t = \alpha_t z + \beta_t x_0$ 
反解出 $x_0$：
- $\beta_t x_0 = x_t - \alpha_t z$
- $x_0 = \frac{x_t - \alpha_t z}{\beta_t}$

现在，把这个 $x_0$ 的表达式代入：
$$ u_t^{\text{target}}(x_t | z) = \dot{\alpha}_t z + \dot{\beta}_t \left( \frac{x_t - \alpha_t z}{\beta_t} \right) $$
$$ u_t^{\text{target}}(x|z) = \left(\dot{\alpha}_t - \frac{\dot{\beta}_t}{\beta_t}\alpha_t\right)z + \frac{\dot{\beta}_t}{\beta_t}x $$


### 1.5 训练模型以模拟概率向量场
损失函数
$$\mathcal{L}_{FM}(\theta) = \mathbb{E}_{t \sim \text{Unif}, x \sim p_t} [\|u_t^\theta(x) - u_t^{\text{target}}(x)\|^2]$$



**公式 (26) - 条件流匹配损失:**
$$\mathcal{L}_{CFM}(\theta) = \mathbb{E}_{t \sim \text{Unif}, z \sim p_{\text{data}}, x \sim p_t(\cdot|z)} [\|u_t^\theta(x) - u_t^{\text{target}}(x|z)\|^2]$$




### 1.6 分数函数和分数匹配
#### 1.6.0 什么是分数函数 (Score Function)？

**定义：** 分数函数是概率分布的对数关于输入的梯度：$\text{Score} = \nabla \log q(x)$
**直观理解：**
- 想象一个山地地形图，高度代表概率密度 $q(x)$
- $\log q(x)$ 就是对高度取对数
- $\nabla \log q(x)$ 告诉你：**在当前位置，往哪个方向走能最快爬上概率高峰**
- 它像一个指南针，总是指向概率密度更高的地方
	![image.png|420x214](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20260613134622975.png)
	- 左图：概率分布 $q(x)$ 的等高线图（红色是高概率区域）
	- 右图：分数函数 $\nabla \log q(x)$ 用箭头表示，箭头指向概率增加最快的方向
1. 条件与边缘分数函数

到目前为止，我们关注的核心对象是向量场 $u_t(x)$。扩散模型采用了不同的视角，专注于**分数函数 (score functions)**。因此，在本节中，我们将用分数函数的语言来重述我们在这里学到的内容——提供一个新颖的视角。

设 $q(x)$ 为任意概率分布。那么 $q$ 的**分数函数 (score function)** 定义为 $\nabla \log q(x)$，即 $q$ 的对数似然关于 $x$ 的梯度。分数具有直观的含义：$\nabla \log q(x)$ 是对数似然上升最陡的方向。图 8 说明了这一点。

让我们回到条件概率路径 $p_t(x|z)$ 和边缘概率路径 $p_t(x)$ 的设定（如第 3 节所述）。那么我们可以等价地定义**条件分数函数 (conditional score function)** 为 $\nabla \log p_t(x|z)$，**边缘分数函数 (marginal score function)** 为 $\nabla \log p_t(x)$。边缘分数可以通过条件分数函数 $\nabla \log p_t(x|z)$ 表达为：

$$\nabla \log p_t(x) = \int \nabla \log p_t(x|z) \frac{p_t(x|z)p_{\text{data}}(z)}{p_t(x)} dz \quad (38)$$

因此，**条件分数与边缘分数的关系类似于条件向量场与边缘向量场的关系**。注意我们可以通过以下方式证明公式 (38)：

$$\nabla \log p_t(x) = \frac{\nabla p_t(x)}{p_t(x)} = \frac{\nabla \int p_t(x|z)p_{\text{data}}(z)dz}{p_t(x)} = \frac{\int \nabla p_t(x|z)p_{\text{data}}(z)dz}{p_t(x)} = \int \nabla \log p_t(x|z) \frac{p_t(x|z)p_{\text{data}}(z)}{p_t(x)} dz \quad (39)$$

其中我们使用了规则 $\partial_y \log y = 1/y$ 并结合了两次链式法则。
#### 1.6.1 推导SDE
我们的目的是类比ODE，使用SDE从 $p_{init}$ 到 $p_{data}$ 

1. 假设我们有一个普通的 ODE，它的向量场是 $u_t^{\text{target}}(x)$：$\frac{dx}{dt} = u_t^{\text{target}}(x)$
	根据**连续性方程**（这是 FP 方程在 $\sigma=0$ 时的特例），这个 ODE 产生的概率分布 $p_t(x)$ 满足：
$$ \partial_t p_t = -\nabla \cdot (p_t u_t^{\text{target}}) \quad \text{--- (式 A)} $$
2. 我们想给这个系统加入随机噪声 $\sigma_t dW_t$。
	假设新的 SDE 形式为：$dX_t = v_t(X_t)dt + \sigma_t dW_t$ ，其中 $v_t$ 是我们需要重新设计的**新漂移项**（为了抵消噪声带来的影响）。
	根据**Fokker-Planck 方程**，这个 SDE 产生的概率分布 $p_t(x)$ 必须满足FP方程：
$$ \partial_t p_t = -\nabla \cdot (p_t v_t) + \frac{\sigma_t^2}{2} \Delta p_t \quad \text{--- (式 B)} $$

3. 强制分布一致（核心步骤）
	我们的目标是：**让加了噪声的 SDE (式 B) 产生的分布，和没加噪声的 ODE (式 A) 产生的分布完全一样。**
	既然 $p_t$ 是一样的，$\partial_t p_t$ 也是一样的，那么 (式 A) 的右边必须等于 (式 B) 的右边：
$$ -\nabla \cdot (p_t u_t^{\text{target}}) = -\nabla \cdot (p_t v_t) + \frac{\sigma_t^2}{2} \Delta p_t $$
4. 我们需要解出 $v_t$。利用拉普拉斯算子的性质 $\Delta p_t = \nabla \cdot (\nabla p_t)$，把方程右边合并：$-\nabla \cdot (p_t u_t^{\text{target}}) = -\nabla \cdot (p_t v_t) + \frac{\sigma_t^2}{2} \nabla \cdot (\nabla p_t)$
	提取公因式 $-\nabla \cdot$：$-\nabla \cdot (p_t u_t^{\text{target}}) = -\nabla \cdot \left( p_t v_t - \frac{\sigma_t^2}{2} \nabla p_t \right)$
	去掉两边的散度符号 $\nabla \cdot$（在物理上这意味着概率流相等）：
		$p_t u_t^{\text{target}} = p_t v_t - \frac{\sigma_t^2}{2} \nabla p_t$
	移项，解出 $p_t v_t$：$p_t v_t = p_t u_t^{\text{target}} + \frac{\sigma_t^2}{2} \nabla p_t$
	两边同时除以 $p_t$： $v_t = u_t^{\text{target}} + \frac{\sigma_t^2}{2} \frac{\nabla p_t}{p_t}$
	利用对数求导法则 $\nabla \log p_t = \frac{\nabla p_t}{p_t}$（这就是 Score Function）：
		$v_t = u_t^{\text{target}} + \frac{\sigma_t^2}{2} \nabla \log p_t$
	把求出的新漂移项 $v_t$ 代回第二步的 SDE 公式中：

$$ dX_t = v_t dt + \sigma_t dW_t $$
$$ dX_t = \left[ u_t^{\text{target}}(X_t) + \frac{\sigma_t^2}{2} \nabla \log p_t(X_t) \right] dt + \sigma_t dW_t $$
#### 1.6.2 
因为SDE存在分数函数，为了避免训练两个模型，我们将向量场转化成分数函数的形式（反之也可以）


对于高斯路径 $p_t(x|z) = \mathcal{N}(x; \alpha_t z, \beta_t^2 I_d)$，我们可以使用高斯概率密度的形式（见公式 (97)）得到：

$$\nabla \log p_t(x|z) = \nabla \log \mathcal{N}(x; \alpha_t z, \beta_t^2 I_d) = -\frac{x - \alpha_t z}{\beta_t^2} \quad (40)$$

**命题 1（高斯概率路径的转换公式）**

对于高斯概率路径 $p_t(x|z) = \mathcal{N}(\alpha_t z, \beta_t^2 I_d)$，条件向量场和条件分数，边缘向量场和边缘分数存在以下恒等式：
- $u_t^{\text{target}}(x|z) = a_t \nabla \log p_t(x|z) + b_t x, \quad a_t = \left(\beta_t^2 \frac{\dot{\alpha}_t}{\alpha_t} - \dot{\beta}_t \beta_t\right), \quad b_t = \frac{\dot{\alpha}_t}{\alpha_t} \quad (41)$
- $u_t^{\text{target}}(x) = a_t \nabla \log p_t(x) + b_t x \quad (42)$

**证明：** 对于条件向量场和条件分数，我们可以推导：

$$u_t^{\text{target}}(x|z) = \left(\dot{\alpha}_t - \frac{\dot{\beta}_t}{\beta_t} \alpha_t\right) z + \frac{\dot{\beta}_t}{\beta_t} x \stackrel{\text{代数变形}}{=} \left(\beta_t^2 \frac{\dot{\alpha}_t}{\alpha_t} - \dot{\beta}_t \beta_t\right) \left(\frac{\alpha_t z - x}{\beta_t^2}\right) + \frac{\dot{\alpha}_t}{\alpha_t} x \stackrel{\text{使用公式40}}{=} \left(\beta_t^2 \frac{\dot{\alpha}_t}{\alpha_t} - \dot{\beta}_t \beta_t\right) \nabla \log p_t(x|z) + \frac{\dot{\alpha}_t}{\alpha_t} x$$

通过取积分，同样的恒等式对边缘流向量场和边缘分数函数成立：

$$u_t^{\text{target}}(x) = \int u_t^{\text{target}}(x|z) \frac{p_t(x|z)p_{\text{data}}(z)}{p_t(x)} dz = \int [a_t \nabla \log p_t(x|z) + b_t x] \frac{p_t(x|z)p_{\text{data}}(z)}{p_t(x)} dz$$

$$\stackrel{(i)}{=} a_t \nabla \log p_t(x) + b_t x$$
#### 1.6.3 训练
- ![image.png](https://raw.githubusercontent.com/Ceritor-Hanio/Pictures/main/20260613150028583.png)

