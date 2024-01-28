感觉 ZKP 实在是很难用英文写笔记，太累了。。脑子跟不上，还是中文吧。

## Week 1 Intro & Basic Definition

Interactive proof 通俗的说就是两个人聊天，一个人试图向另一个人证明自己知道一个事，但是又不想透露其中的信息。一个简单的例子是一个人试图向另一个人证明 1000000016000000063 是一个合数，但是并不想透露它能分解成哪两个数。这非常有用，它可以让你显得很厉害的同时也不会泄露信息使得别人听了之后也能显得很厉害。

正经的来说，传统证明只有一个参与者，而 interactive proof 则有 prover 和 verifier 两个部分组成，比较好的刻画了很多场景，例如身份验证、区块链验证等等。prover 和 verifier 之间会进行通信，最终 verifier 会根据他所看到的内容给出最终的判断，1 表示接受，0 表示拒绝，分别对应相信/不相信对方真的知道这件事。
 
更正经的来说，一个 interactive proof 针对的是一个 language，给定一个 instance 对双方都可见，一个 witness 仅对 prover 可见，verifier 根据 prover 发送的过往信息和 instance 以及自己的随机性给出回复；prover 根据 verifier 过往的回复和 instance、witness 以及自己的随机性给出新的回复，并循环反复直到有限步后 verifier 输出 1 或 0。

一个好的 interactive proof 应该满足三个性质：

+ completeness
+ soundness
+ zero-knowledge

这三个性质分别描述了：

+ completeness：如果 prover 真的知道这个知识，也即 instance 真的在 language 里，verifier 应该相信，也即输出 1。
+ soundness：如果 prover 不知道这个知识，也即 instance 并不在 language 里，verifier 不应该盲目相信，也即输出 0。
+ zero-knowledge：verifier 不应该从证明过程中获得任何『知识』。想要定义什么是知识比较困难，我们稍后讲解。

正经的来说，我们对 completeness 和 soundness 的定义为：

!!! note "completeness"
	$\forall x \in \mathcal{L}, \text{Pr}_{r,s}[\langle P(r), V(s) \rangle (x)=1] \ge \frac{3}{4}$  

!!! note "soundness"
	$\forall x \notin \mathcal{L}, \forall P^*, \text{Pr}_{r,s}[\langle P^*(r), V(s) \rangle (x)=0] \le \frac{1}{2}$

For zero knowledge we have a brilliant idea: if verifier could produce the *proof* by itself then we can say there is zero knowledge gained by verifier. So what's the definition of the proof? A proof for verifier consists of all the *view* that verifier *sees*. If there is a **efficient** simulator $S$ such that for $\forall x \in \mathcal{L}$, we have $\{\text{View}_{V^*}^P\}=\{S(V^*,x)\}$, then we say $(P, V)$ is a perfect zero-knowledge proof, here the brace means the probability distribution.

A classical example for perfect ZKP is Graph Isomorphism ZKP.

图同构问题本身显然是 NP 问题，但是是否是 NP-Complete 暂时还不知道，有可能是 P 问题。这里只是举例说明什么是 zero-knowledge，实际上 IP 的计算能力是很强的。

![Graph_Isomorphism](assets/zkp_GI.png)

这里 Prover 将原图 $G_0$ 打乱得到 $H$ 并发送给 Verifier，然后由 Verifier 选择一个 01 随机数 $b$ 发回 Prover。如果两个图真的同构，那么不管 Verifier 的随机数是什么，Prover 都应该能找到一种排列使得 $\sigma(G_b) = H$。所以 Prover 把这个排列发送给 Verifier 去验证。

如果两个图真的同构，显然这个过程会顺利通过；如果两个图不同构，那么 V 有 50% 的概率 reject（如果不同构，随机到另一个图 P 就没办法发送回正确的排列了）。所以我们就证明了这个协议的 Completeness 和 Soundness。

Zero-knowledge 也是很显然的，从 V 的视角来看，他看到了 $H, b, \tau$，而他自己也可以随即打乱 $G_0$ 得到 $H$，由于这是他自己打乱的，所以 $\tau$ 也是容易得到的。故而存在一个 simulator 模拟出 V 的视角，也就证明 V 从这个证明中得不到任何信息。

zero-knowledge 的定义也有一些变种：

!!! note "black-box zero-knowledge"
	If exist efficient simulator $S$ s.t. $\forall V^*, \forall x \in \mathcal{L}$, we have $\{\text{View}_{V^*}^P\} = \{S_{V^*}(x)\}$

!!! note "honest verifier zero-knowledge (HVZK)"
	If exist simulator $S$ for honest verifier $V$ s.t. $\{\text{View}_{V}^P\}=\{S(V,x)\}$ 

!!! note "special/semi honest verifier zero-knowledge (SHVZK)"
	If exist efficient simulator $S$ s.t. $\forall x \in \mathcal{L}, s \in \{0,1\}^*$, we have $\{\text{View}_{V(s)}^P\}=\{S(V(s),x)\}$

Here black-box zero-knowledge is a stricter definition of zero-knowledge, and I didn't see any rationale behind this definition.

HVZK means when constructing simulator, we can assume that V is honest, instead of malicious. Choosing HVZK instead of ZK doesn't mean that we already know there is some malicious V that could extract knowledge, sometimes it's just that we don't know how to prove ZK. 

SHVZK stands for semi or special HVZK. **Special xxx** under this context means it's a special form of **xxx** and it's sufficient for **xxx**. We usually use SHVZK with regard of sigma protocol because in that sense SHVZK is enough for HVZK and it's easier to analyse.

A classical example for HVZK is Graph 3-coloring ZKP.

The protocol operates as follows:

+ P randomly permutates the coloring and commits it.
+ V chooses arandom edge $(i, j)$ and send this choice
+ P reveals to V only the color of $i$ and $j$
+ V checks if commitment is correct and if the colors are different.

It's easy to construct simulator for honest verifier, using the similar tech in GI ZKP, but it's not trivial to analyse the malicious case. If a V is malicious, it might send $(i, j)$ while the two vertices aren't adjacent. In this case how to simulate the view of V if we don't actually know the correct coloring? So here we choose HVZK over ZK.

Let us move on to another topic: **indistinguishability**.

+ *Perfectly indistinguishable* if for any algorithm $D$, parameter $\lambda$, $|\text{Pr}[D(1^\lambda, X) = 1] - \text{Pr}[D(1^\lambda, Y) = 1]| = 0$
+ *Statistically indistinguishable* if for any algorithm $D$, parameter $\lambda$, $|\text{Pr}[D(1^\lambda, X) = 1] - \text{Pr}[D(1^\lambda, Y) = 1]| \le \text{negl}(\lambda)$
+ *Computationally indistinguishable* if for any efficient algorithm $D$, parameter $\lambda$, $|\text{Pr}[D(1^\lambda, X) = 1] - \text{Pr}[D(1^\lambda, Y) = 1]| \le \text{negl}(\lambda)$

These are three types of indistinguishability. The perfect one means the two distributions really have no difference.; the statistical one means you need to be very lucky to find some difference; the computational one means you need to be very lucky and work very hard to find some difference.

Based on different indistinguishability, we can define different zero-knowledge properties: to what extent does the generated view looks like the real view.

Accordingly, we have perfect one, statistical one, and computational one.

Put zero-knowledge aside we have some variants of soundness.

We call protocols whose soundness only holds against *efficient* provers (so we can prove soundness using cryptographic assumptions) **Interactive Arguments**. It's a strange name, we could just call it computationally sound proof system. The only difference is that we only require *computationally* soundness. In particular, perfect ZK **arguments** are known to exist for every language in NP, it is considered unlikely that perfect ZK **proofs**.

Another variant is knowledge soundness, which assures when V accepts, then we can extract the witness from the messages sent by P. Note that normal soundness requirement only ensures V to know there exist a witness (because $x$ is in the language, thus a witness exists), but V can't be sure about whether P has this witness. This would not be strong enough in some cases, like login protocol.

!!! note "Proof of Knowledge"
	(adapted from https://crypto.stanford.edu/cs355/19sp/lec5.pdf, I think this definition is better than that shown in slide)
	An IP $(P, V)$ for language $L$ is a **proof of knowledge** with **knowledge error** $\epsilon$, if there exists an efficient (expected polynomial running time) algorithm $E$, called an extractor, s.t. for every instance $x$ and every prover $P$: $\text{Pr}[(x, w) \in L: w = E^P(x)] \ge \text{Pr}[(P,V)(x)=1] - \epsilon$.

Some explanations about the definition: The probability of V accepts is $\text{Pr}[(P,V)(x)=1]$ and we can always extract a correct witness except small probability (knowledge error). It doesn't matter P really knows the witness, if we can extract witness from P's messages, P itself could extract witness from messages as well. So this is our definition of "*knows*": you knows everything that you could efficiently compute.

Knowledge error $\epsilon$ directly implies soundness error $\epsilon$.

Now some more definitions in order to introduce sigma-protocol.

We define an IP $(P, V)$ is public coin if V's messages are exactly random bits and nothing else. In this case, V's messages are also called *challenges*. For example, GI ZKP is a public coin IP because the only message sent by V is a random bit; while the trivial GNI (Graph Not Isomorphism) ZKP is not a public coin because its random bit must not be leaked otherwise P could cheat V. However, [GS1986](https://pages.cs.wisc.edu/~jyc/710/Goldwasser-Sipser.pdf) proves every language with an IP has a public coin IP, by proving public coins and private coins the same complexity class as **Probabilistic, nondeterministic, polynomial time Turing machine**.

Here's another concept called **Trees of transcipts**. 

An $(n_1, \cdots, n_k)$ tree of transcripts for a public coin IP is a set of $\Pi_{i=1}^{k} n_i$ transcipts arranged in a tree s.t.:

+ Vertices correspond to P messages.
+ Edges correspond to V challenges.
+ Each node at depth $i$ has $n_i$ child edges labelled with distinct challenges.
+ Each transcript corresponds to one root-to-leaf path.
+ The tree is *accepting* if V would accept every transcript.

Finally we can define another soundness: **Special soundness**.

A public coin IP is $(n_1, \cdots, n_k)$-*special sound* if exist an efficient extractor $E$ takes instance and a $(n_1, \cdots, n_k)$-tree of *accepting* transcripts and produces a witness $w$ with $(x, w) \in \mathcal{R}$.

We've already known that special xxx means it's a special form of xxx, and it's sufficient for xxx. So here special soundness implies knowledge soundness, which further implies soundness.

!!! note "Theorem Attema, Cramer, Kohl 2021"
	Let $(P,V) be (n_1, \cdots, n_k)$-special sound with uniformly random V messages from set of size $N$, and $\Pi_{i=1}^k n_i$ be polynomially bounded in $|x|$. Then $(P,V)$ is knowledge sound with knowledge error: $k = \frac{N^k - \Pi_{i=1}^k(N-n_i - 1)}{N^k} \le \frac{\sum_{i=1}^k(n_i - 1)}{N}$

The proof could be found here: https://eprint.iacr.org/2021/307.pdf, section 3.

The results could be concluded as:

|           |   Soundness   |       ZK      |
|:---------:|:-------------:|:-------------:|
|   Proofs  |  Perfect/Sta  | Computational |
| Arguments | Computational |  Perfect/Sta  |

## Sigma-Protocol

Finally we get here, sigma-protocol.

A **sigma-protocol** is an 3-move, public coin IP satisfying:

+ completeness with no errors
+ $k$-special soundness
+ SHZVK

By definition, GI ZKP is a sigma-protocol.

Now we introduce another important concept: **commitment schemes**.

A **commitment scheme** is a collection of 3 PPT algos (Setup, Commit, Verify) s.t. for any parameter $\lambda$:

+ Setup($1^\lambda$) outputs public parameters $pp$ describing message space $M$, randomness space $R$, decommitment space $D$ and commitment space $C$.
+ Commit($pp, m \in M, r \leftarrow_\$ R$) outputs a pair $(c, d) \in C \times D$, where $c$ is the commitment, $d$ is the secret de-commitment, normally $d$ won't be sent to others unless Verify requires it.
+ Verify($pp, c \in C, d \in D, m \in M) outputs a bit $b \in \{0, 1\}$, where $b$ is the verifying result, $0, 1$ stands for failiure and success respectively.

There are two important properties for commitment scheme: **hiding** and **binding**.

Hiding means it's difficult to determine the original message only from the commitment. Given the commitment and public parameter, how much does the original message distribution differs from uniform distribution implies how difficult it is to extract original message from commitment and $pp$.

Perfectly hiding indicates the message distribution given commitment and $pp$ is exactly the uniform distribution; computationally hiding indicates unless you work very hard (using unbounded time to crack) or very lucky (i.e. something with negelectable probability happens), you can't tell the difference, i.e. you can't extract message from commitment.

Binding means it's difficult to change the message after committed. 

Perfectly binding means the original message is unique; computationally binding means it needs hard work or huge luck to find another message which could generate the same commitment.

Again, $\text{Perfect Hiding} \& \text{Perfect Binding} = False$.

|                         | Perfect Hiding | Compuatationally Hiding |
|:-----------------------:|:--------------:|:-----------------------:|
|     Perfect Binding     |      False     |           True          |
| Computationally Binding |      True      |           True          |


Here we introduce two famous commitment scheme: Elgamal Commitment and Pedersen Commitment.

![Elgamal Commitment](assets/zkp_elgamal_commitment.png)

Elgamal Commitment is based on Elgamal encryption (https://en.wikipedia.org/wiki/ElGamal_encryption), so it inherits the security assumption: Decisional Deffie-Hellman assumption (https://en.wikipedia.org/wiki/Decisional_Diffie%E2%80%93Hellman_assumption).

It's computationally hiding and perfectly binding.

![Pedersen Commitment](assets/zkp_pederson_commitment.png)

The setup is the same as Elgamal commitment, the difference lies in commit function. In Elgamal commitment, we need to send $c2 = r \cdot h$ so as to ensure $r$ won't be changed easily afterwards. If we don't send $rh$ then malicous commit-er could change $r$ to another value $r'$ and calculate corresponding $r'g$ and then eventually open a different value to original message $m$.

In Pedersen commitment, however, we send $mg + rh$, and we no longer need $rh$ in this case because if we want to open another value for $m$, we have to solver DLOG to get a corresponding $g$.

It's perfectly hiding and computationally binding.

Sigma protocol together with commitment scheme could be used for NP-complete problem, as we've already seen: Graph 3-coloring problem.

Consider composition of sigma-protocol, we have this table:

| Preserved? |               Soundness              |   ZK  |
|:----------:|:------------------------------------:|:-----:|
| Sequential |                 True                 |  True |
|  Parallel  | True for proofs; False for arguments | False |

## Week 7 Sumcheck Protocol
### 1 Sumcheck Protocol Itself
这个 protocol 的 instance 是 $p(X_1, \cdots, X_l)$ over $\mathbb{F}$ 和 $u \in \mathbb{F}$，子集 $H \subset \mathbb{F}$。想要检验的是多项式 $p$ 在 $H^l$ 上求值然后全加起来是不是等于 $u$。在这里并没有 witness，那 verifier 到底想知道啥？他自己其实本来就可以验证，因为你自己把所有的值都加起来算算就知道了。但是他并不想花这么多时间，他只是想借助 prover 确认这件事是真的。

这个协议是这样工作的：

![sumcheck_protocol](assets/sumcheck1.png)

简单来说就是 prover 负责把后面的 $l-1$ 个变量都枚举了，相当于把多项式后面的变量都消除了，留给 verifier 自己枚举第一个变量所有可能的取值，然后检查和是不是 $u$。

这样 verifier 肯定不能轻信，否则 soundness 就炸了。verifier 继续出题，那我把多项式的第一个值固定（这就是我的第一个 challenge！），这样就是一个新的多项式了，现在压力回到 prover 这边，你继续递归地用这个多项式做一下 sumcheck。

这样做显然 verifier 的计算压力减小了，主要的计算由 prover 承担，同时 verifier 也能确定 prover 没有骗人。同时协议的 communication cost 也变小了，因为我们只传递单变量的多项式。

completeness 非常显然，如果 instance 本身就在 language 里，没有任何可能 verifier 会 reject。

soundness 建立在『域上多项式的根的数量不会超过 degree』这一事实上。即使prover 提供了一个假的多项式骗过了第一道检查（求和之后确实等于 $u$），verifier 想要验证你提供的多项式和真实的多项式确实是同一个多项式，它的方法是在随机一个点上取值，因为随机一个点两个多项式取值相等的概率其实就是随机点是两个多项式的差的根的概率，而这个不超过 $\frac{d}{|\mathbb{F}|}$。如果不巧随机取值两个多项式的值就是一样的，那么递归的子问题就在 language 中，所以 verifier 就没办法分辨了；但是如果取值不同，那么递归的子问题的 instance 也不在 language 里，这样就很容易使用归纳法了。最终可以说明 soundness error（也就是当 instance 不在 language 的时候 verifier 依然 accept 的概率）不超过 $(l-1)d/|\mathbb{F}|$。
### 2 coNP Is in IP
coNP 里的语言满足：其补语言在 NP 中。所以概念其实很好理解。比如说图同构显然是 NP 的，你给我两个图作为 instance 和一个映射作为 witness，我很简单就能验证你说的对不对。但是图不同构就没有这么简单，你很难让我确信你给我的两个图不同构。显然图不同构的补语言就是图同构，所以图不同构是 coNP 的。

现在我们希望得到下图这样的关系：
![[coNP1.png.png]]
这就需要我们找到一个 coNP-Complete 的语言，然后说明它是 IP 的就可以了。

比较经典的一个 NP-Complete 的问题是 3-SAT 问题（一些 clause 取交集，问能否使得这个逻辑表达式为真），它的补问题 3-UNSAT 问题就是一个 coNP-Complete 问题。

挑选这个逻辑表达式相关的问题是有用意的，因为逻辑表达式很容易用加减乘法拓展到域 $\mathbb{F}$ 上进而变成一个 sumcheck 问题。

比如 $x \wedge y$ 可以变成 $x \cdot y$，$x \vee y$ 可以变成 $1 - (1 - x)(1 - y)$。这样的话我们就可以把一个逻辑表达式变成一个多项式，而且多项式的阶不超过 $3m$，其中 $m$ 是 clause 的个数。

巧妙的是，如果一个逻辑表达式是不可能满足的（UNSAT），就意味着它对应的多项式在 $\{0,1\}^l$ 上求和依然是 0。这样的话就变成了一个 sumcheck 问题。

这里我们需要一个域，所以就找 $\mathbb{Z}_p$ 即可，只要 $2^l < p < 2^{l+1}$。

最终的 protocol 如下：
![[coNP2.png.png]]
### 3 GKR Protocol
GKR protocol 是一个纯人名协议，真是可恶啊看不出来是干啥的。T-T

这个协议一般表述为一个运算门阵列求值问题：给定一系列 add 门和 mul 门，分别对应加法和乘法；门是层级排列的，第 $i$ 层门的输入来自两个 $i+1$ 层的门，输出输送到第 $i-1$ 层的一个门。最终 prover 想要证明某个输入 $\vec{x}$ 得到的输出为 $\vec{y}$。

这个问题也是没有 witness 的，verifier 自身就可以检验输出是不是对的，只需要自行带入运算即可。这里我们想要实现的是 prover 可以比较高效的运行同时 verifier 可以超级高效的运行（输入规模的对数级别）。这个听起来非常不可思议，因为一个人居然连问题本身都没看全就能从别人那里验证结果的正确性。

首先我们介绍一个引理：

!!! note "Schwarz Zippel Lemma"
	$p \in \mathbb{F}[X_1, \cdots X_l],\;\; \mathcal{S} \subset \mathbb{F}$，那么随机选一个 $\vec{x}$ 使得多项式取值为 0 的概率 $\text{Pr} \le \frac{\deg p}{|\mathcal{S}|}$。










