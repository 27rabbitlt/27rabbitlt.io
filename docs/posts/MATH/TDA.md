# Topological Data Analysis

好好学一学代数拓扑基础

## 2 Homology 同调

开始数洞

!!! note "Simplicial Map"
    A *map* $f: K_1 \rightarrow K_2$ is called simplicial if it can be described by a vertex map $g: V(K_1) \rightarrow V_(K_2)$ s.t. $f(\{v_0, \cdots, v_k\}) = \{g(v_0), \cdots, g(v_k)\}$ and every simplex in $K_1$ is mapped to another simplex in $K_2$.

Note that it doesn't require a k-dim simplex is mapped to also a **k-dim** simplex.

Now we introduce a very famous theorem which has lots of interesting applications.

!!! note "Brouwer Fixed Point Theorem"
    Let $f: \mathbb{B}^d \rightarrow \mathbb{B}^d$ be continuous, then f has a fixed point, that is, $\exists x \in \mathbb{B}^d \implies f(x) = x$.

To prove this, we need some lemmas. The first one is:


