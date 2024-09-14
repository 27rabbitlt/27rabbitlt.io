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

## 3 Persistence

For a simplicial filtration, each time when we add a new $p$-dim simplex, it has to be either a creator or a destructor. A creator means it creates a new $p$-dim cycle (hole) and a destructor means it destroys a $p-1$-dim cycle (hole) since that cycle is the boundary of added simplex.

But we need to notice that, here either a creator or a destructor creates or destroys not only a cycle, but instead a base cycle. So the rank increases or decreases by 1, which means the number different cycles actually doubles or shrinks to a half.

This definition agrees with the definition of betti number and persistence diagram.

It's easy to prove that a new simplex is either a creator or a destructor. So we can pair them in this way: each time we pair a destructor with the youngest still unpaired creator within the cycle it destroys. This algorithm avoids the ambiguity of exactly which cycle is destroyed, when there are two cycles in fact merged into one cycle after adding a destructor.

What if all the creators within the destroyed cycle  have been paired? Then for each creator $\rho$, we consider its paired destructor $\tau$, we replace $\rho$ by  $\rho + \partial \tau$. Then we get a new set of candidates. Repeat the previous precedure until we find an unpaired creator or if there is no more creator then the added cycle could not be a destructor (WHY?).

Then for each pair of paired simplexes, we draw a point on the persistence diagram, with the coordinate $(f(\rho), f(\tau))$, where $\rho$ is the creator, $\tau$ is the destructor, $f(\cdot)$ is timestamp function. For technical reason, we add infinitely many points on diagonal.

Given persistence diagrams, it's natural to think about how similar two diagrams are or can we define a distance metric for diagrams.

Here we use bottleneck distance, which is defined as:

$$
d_b(Dgm_p(F), Dgm_p(G)) = \inf_{\pi \in \Pi} \sup_{x \in Dgm_p(F)}  || x - \pi(x) ||_\infty
$$

We can prove if the diagrams have finite off-diagonal points then bottleneck distance is a metric.

We want to prove the stability of simplicial filtrations.

!!! note "Stability for Simplicial Filtration Theorem"
    Let $f, g: K \rightarrow \mathbb{R}$  be simplex-wise monotone functions. Then $d_b(Dgm_p(F_f), Dgm_p(F_g)) \le |f-g|_\infty$.

This theorem states that if we only change a little on the filtration level function $f$, the diagram also changes a little, which implies stability.

The idea behind the proof is that we construct a new function $v(x, t) = t f(x) + (1 - t) g(x)$, then we draw diagrams for each timestamp $t$, which forms a vineyard. The slope of each vine is at most $|| f - g ||_\infty$.

We can also generalize this to any triangulable topological space, which will be proved later using stability with respect to interleaving distance.

### Wasserstein Distance

Bottleneck distance cannot capture the number of "mismatching". Say if there is a relatively deviated point, then no matter how many other points, which are closer to diagonal, are added, the bottleneck distance won't change. We always only look at the longest edge in matching.

To avoid this problem we can use Wasserstein distance.

$$ 
d_{W, q}(Dgm_p(F), Dgm_p(G)) = \big[ \inf_{\pi \in \Pi} (\sum_{x \in Dgm_p(F)} (||x - \pi(x)||_\infty)^q) \big]^{1/q}
$$

Note that when $q = \infty$, $d_{W, \infty} = d_b$.

We cannot guarantee stability of Wasserstein distance. Counterexamples can be found for simplicial complex and topological spaces. But if we restrict the function to be Lipschitz, we do have stability for Wasserstein distance.

### Interleaving Distance

Interleaving distance of two function levelset induced filtration is at most $||f - g||_infty$.

And using the theorem of stability with respect to interleaving distance, we have $d_b(Dgm(U), Dgm(V)) = d_I (U, V)$. Note that here $U, V$ are homology group based persistence module, but not filtration. 

It's also obvious that the interleaving distance of homology goup is no greater than the interleaving distance of corresponding interleaving distance, because we can always construct a map for homology group based on the map for its corresponding simplexes.

So:

$d_b(Dgm(H_p U), Dgm(H_p V)) = d_I (H_p U, H_p V) \le d_I (U, V) \le || f - g ||_\infty$.

A reason why we consider interleaving distance is that previously we only pay attention to stability of one space or simplicial complex with different filtrations induced by levelset of some function. However in real application, we only have point cloud, which may vary in size. Interleaving distance still gives some promise about stability even with different sizes.

Based on this intuition, we consider Hausdoff distance.

## 5 Reeb Graph and Mapper

### Reeb Graph

The idea of Reeb graph is that we extract the 1-dimensional information out of the space $X$ using a function $f: X \rightarrow \mathbb{R}$.


!!! note "Reeb Graph"
    $X$ is a topological space, and $f$ is a function from $X$ to $\mathbb{R}$. Two points $x, y \in X$ are called equivalent ($x \sim y$) iff $f(x) = f(y) = \alpha$ and $x, y$ are in the same path-connected component of $f^{-1}(\alpha)$. The Reeb graph $R_f$ is the quotient space $X / \sim$.

To exclude the weird and meaningless cases, we only consider the situations where there are always connected components and homology groups of levelsets only change at finitely many critical values.

Reeb graph by definition is a topological space (it's a quotient space), we call it a graph because it's 1-dimensional. To get a real graph we need a discretization.

It's very natural to consider the number of "neighbours" that a point has. Let $u$ be the number of neighbours in the direction of $f$-value increases; $l$ be the number of neighbours in the direction of decreasing. Then if $u = l = 1$, this point is a regular one; while in the other cases it's a critical point which should be displaced as a distinct vertex in the graph.

### From Topospace to $\mathbb{R}$

Mapper is an approximation of Reeb graph. Instead of preimage of single point, we now consider preimage of intervals.

Again we need a function $f: X \rightarrow \mathbb{R}$, and for an open cover $\{U_\alpha\}$ of $\mathbb{R}$, we consider the path-connected components of preimages of each interval $U_\alpha$ and further compute the nerve of this family, i.e. $f^{-1}(U_\alpha) = \bigcup_{\beta} V_\beta$, let $f^*(U) = \{V_\beta\}$, and finally $N(f^*(U))$.

If we take sufficiently appropriate function $f$ and sufficiently appropriate cover $\{U\}$ then $N(f^*(U))$ is isomorphic to $R_f$.

### Topological Mapper

Previous definition only considers maps to $\mathbb{R}$, now we generalize to arbitary space.

!!! note "Def: well-behaved"
    TBD

!!! note "Def: Mapper"
    Let $f: X \rightarrow Z$ be well-behaved, and $U$ be a finite open cover of $Z$. Then the Mapper is defined as $M(U,f) = N(f^*(U))$.

    