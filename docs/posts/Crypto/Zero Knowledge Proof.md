感觉 ZKP 实在是很难用英文写笔记，太累了。。脑子跟不上，还是中文吧。
## Week 7 Sumcheck Protocol
### 1 Sumcheck Protocol Itself
这个 protocol 的 instance 是 $p(X_1, \cdots, X_l)$ over $\mathbb{F}$ 和 $u \in \mathbb{F}$，子集 $H \subset \mathbb{F}$。想要检验的是多项式 $p$ 在 $H^l$ 上求值然后全加起来是不是等于 $u$。在这里并没有 witness，那 verifier 到底想知道啥？他自己其实本来就可以验证，因为你自己把所有的值都加起来算算就知道了。但是他并不想花这么多时间，他只是想借助 prover 确认这件事是真的。

这个协议是这样工作的：
![sumcheck_protocol][assets/sumcheck1.png]
简单来说就是 prover 负责把后面的 $l-1$ 个变量都枚举了，相当于把多项式后面的变量都消除了，留给 verifier 自己枚举第一个变量所有可能的取值，然后检查和是不是 $u$。

这样 verifier 肯定不能轻信，否则 soundness 就炸了。verifier 继续出题，那我把多项式的第一个值固定（这就是我的第一个 challenge！），这样就是一个新的多项式了，现在压力回到 prover 这边，你继续递归地用这个多项式做一下 sumcheck。

这样做显然 verifier 的计算压力减小了，主要的计算由 prover 承担，同时 verifier 也能确定 prover 没有骗人。同时协议的 communication cost 也变小了，因为我们只传递单变量的多项式。

completeness 非常显然，如果 instance 本身就在 language 里，没有任何可能 verifier 会 reject。

soundness 建立在『域上多项式的根的数量不会超过 degree』这一事实上。即使prover 提供了一个假的多项式骗过了第一道检查（求和之后确实等于 $u$），verifier 想要验证你提供的多项式和真实的多项式确实是同一个多项式，它的方法是在随机一个点上取值，因为随机一个点两个多项式取值相等的概率其实就是随机点是两个多项式的差的根的概率，而这个不超过 $\frac{d}{|\mathbb{F}|}$。如果不巧随机取值两个多项式的值就是一样的，那么递归的子问题就在 language 中，所以 verifier 就没办法分辨了；但是如果取值不同，那么递归的子问题的 instance 也不在 language 里，这样就很容易使用归纳法了。最终可以说明 soundness error（也就是当 instance 不在 language 的时候 verifier 依然 accept 的概率）不超过 $(l-1)d/|\mathbb{F}|$。
### 2 CONP Is in IP
TO BE DONE
### 3 GKR Protocol


