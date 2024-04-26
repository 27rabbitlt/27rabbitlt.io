# Topological Data Analysis

## 0 Topology basics

### 0.1 Open Sets

Topology is basically about shapes and distances. We care about how different two shapes are and how far two points/elements are. Instead of using distance directly, we use *open set* as our basic building block.

The topology can be seen as how we define open sets. A topological space is a set $X$ together with a subset family $O$ of which each subset is called an open set. $O$ needs to satisfy three properties:

+ $\emptyset \in O, X \in O$
+ $\bigcap_{i}^n O_i \in O$, where $O_i \in O$.
+ For every $S \subset O$, $\bigcup S \in O$.

We can conclude that open sets have closure under finite intersection and arbitrary union. This definition is consistent with the intuition we already got in middle school: infinite intersection of open intervals $\bigcap_n^\infty I_n$, where $I_n = (0-\frac{1}{n}, 1+\frac{1}{n})$ is a close interval $[0,1]$.

### 0.2 Base

Base $\mathcal{B}$ is a set of open sets such that for any open set $U$ we can find a subset $\mathcal{B}'$ of $\mathcal{B}$ satisfying $U = \bigcup_{B \in \mathcal{B}'}B$, where $\mathcal{B}' \subset \mathcal{B}$.

So the base is a subset of $O$ but can construct every open set by appropriate union.

For our old friend Euclidean space $R$, we can give a base using rational number and open balls: $\mathcal{B} = \{B(x, 1/p) | x \in \mathbb{Q}, p \in \mathbb{N}_+\}$

### 0.3 Closure, Boundary, Interior, and Limit Point

*Closure* of a set $A$ is the smallest (or the intersection of all) close sets that contains $A$.

*Interior* of a set $A$ is the biggest (or the union of all) open sets that is contained in $A$.

*Boundary* is closure mod interiror.

A point $p$ is *limit point* of a set $A$ if every open set that contains $p$ intersects with $A$. 

Note that this definition of boundary is different from what we will see of the simplex chain. However the definition of boundary of manifold is consistent with that of simplex chain. The boundary of a $d$-dim manifold is all the points whose neighbourhood is homeomorphic to half-ball $H^d$, while interiror is these whose neighbourhood is homeomorphic to an open ball $B^d$.

## 1 Homotopy 同伦 

Homotopy is actually between two maps. A *homotopy* connecting between maps $g, h: X \rightarrow Y$ is a map $H: X \times [0,1] \rightarrow Y$ such that $H(\cdot, 0) = g, H(\cdot, 1) = h$. In this case $g$ and $h$ are called homotopic.

However, usually we care about the equivalence relation induced by this notion of homotopy. Two sapces $X, Y$ are homotopy equivalent if there exist maps $g: X \rightarrow Y, h: Y \rightarrow X$ such that:

+ $h \circ g$ is homotopic to $\text{id}_X$, and
+ $g \circ h$ is homotopic to $\text{id}_Y$.

Where $\text{id}_X$ is the identity map from $X$ to $X$.

This definition is a bit abstract thus difficult to intuitively think about. Another usefull definition is deformation retract.

Let $A \subset X$, a *deformation retract* of X onto $A$ is a map $R: X \times [0,1] \rightarrow X$ such that:

+ $R(\cdot, 0) = \text{id}_X$
+ $R(x,1) \in A, \forall x \in X$
+ $R(a,t) = a, \forall a \in A, \forall t \in [0,1]$

If such deformation retractt of $X$ onto $A$ exists, we also say that $A$ is a deformation retract of $X$ and we can prove that $X$ and $A$ are homotopy equivalent.

Another importance fact is that $X, Y$ are homotopy equivalent iff there exists a space $Z$ such that $X, Y$ are deformation retracts of $Z$.

!!! note "Deformation Retract and Homotopy Equivalent"
    $X, Y$ are homotopy equivalent iff there exists a space $Z$ such that $X, Y$ are deformation retracts of $Z$.


## 2 Homology 同调

代数拓扑课本啥也看不懂

开始数洞

!!! note "Simplicial Map"
    A *map* $f: K_1 \rightarrow K_2$ is called simplicial if it can be described by a vertex map $g: V(K_1) \rightarrow V_(K_2)$ s.t. $f(\{v_0, \cdots, v_k\}) = \{g(v_0), \cdots, g(v_k)\}$ and every simplex in $K_1$ is mapped to another simplex in $K_2$.

Note that it doesn't require a k-dim simplex is mapped to also a **k-dim** simplex.

Now we introduce a very famous theorem which has lots of interesting applications.

!!! note "Brouwer Fixed Point Theorem"
    Let $f: \mathbb{B}^d \rightarrow \mathbb{B}^d$ be continuous, then f has a fixed point, that is, $\exists x \in \mathbb{B}^d \implies f(x) = x$.

To prove this, we need some lemmas. The first one is:


