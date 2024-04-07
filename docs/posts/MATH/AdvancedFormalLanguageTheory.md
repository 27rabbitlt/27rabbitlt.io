# Advanced Formal Language Theory

## 2 WFSA

Important definitions on section 3.2.3

+ $\Pi^n(i, j)$: paths from $i$ to $j$ with exactly $n$ edges
+ $\Pi^{(n)}(i, j)$: paths from $i$ to $j$ with no more than $n$ edges

### 2.1 Intersection

#### 2.1.1 Non-epsilon transition

It's natural to think about intersections between WFSAs since we can construct more complicated ones by intersecting basic ones. If we have two WFSA $A_1, A_2$ accepting languages $L_1, L_2$, then the intersection language should be $L_1 \bigcap L_2$ and the weight of a string $y$ is $(A_1 \bigcap A_2)(y) = A_1(y) \otimes A_2(y)$ (we assume string weight semiring is commutative, otherwise it's hard to achieve this intersection weight). 

Naively, we can correspond new WFSA's state to every pair of states in original WFSAs and there is a new transition from $(q_1, q_2) \rightarrow (q_3, q_4)$ iff there are two transitions $q_1 \rightarrow q_3$ and $q_2 \rightarrow q_4$ originally. Naturally the transition weight should be the multiplication (that's why we assume commutativity).

The correctness of such construction is obvious and left as excercise.

#### 2.1.2 epsilon transition

We still have a tough problem to deal with: epsilon-transition. It's easy to see that if $q_1$ in $A_1$ can accept $\epsilon$ and transit to $q_3$ then there should be a valid transition in new WFSA like: $(q_1, q_2) \rightarrow (q_3, q_2)$ even if there is no $\epsilon$ transition from $q_2$ to itself.

So we augment the original WFSA by adding new transitions called $\epsilon_1, \epsilon_2$ transitions, which explicitly indicates which automaton is transiting over $\epsilon$. We replace $\epsilon$ in $A_1$ with $\epsilon_2$ and replace $\epsilon$ in $A_2$ with $\epsilon_1$. Then we further add self-loops in $A_1$ with $\epsilon_1$ and in $A_2$ iwth $\epsilon_2$. Given the modification we can thus safely use the non-epsilon version algorithm( really? ). We call the augmented automaton $\tilde{A_1}, \tilde{A_2}$.

However another problem arises. Using such augmentation the new intersection would have redundant paths (think about why). To remove redundant paths, we need to filter out these unqualified transitions. For example, $(\epsilon_1, \epsilon_2)$ transition should be forbidden; also, $(\epsilon_2, \epsilon_2)$ followed by $(\epsilon_1, \epsilon_1)$ should be forbidden becuase it's equivalent to a simpler form: $(\epsilon_2, \epsilon_1)$. Such filter can be implemented by a FSA with very few states, leave this as an excercise.

### 2.2 Path Sum

As the name itself suggests, **path sum** means the summation of path weights. Using different definition of $\oplus$, path sum corresponds to different tasks:

+ Shortest path in the graph (tropical semiring)
+ Sum of all paths (real semiring)
+ Transforming WFSA into a weighted regular language (Kleene semiring)

#### 2.2.1 Acyclic automaton path sum

Obviously we can use topological sort to calculate the path sum with time complexity $O(n + m)$.

#### 2.2.2 Closed Semiring

There might be cycles in non-acyclic graph, which means there would be infinitely many paths in automaton. Then here is the problem: how do we calculate path sum, it might not even converge?

To make sure such *sum* exists, we further require closed semiring to have a new operation **Kleene star** defined as:

!!! note "Kleene star"
    Kleene star operation must satisfy following two axioms:
    1. $x^* = 1 \oplus x \otimes x^*$
    2. $x^* = 1 \oplus x^* \otimes x$

Another definition that impies **closed** is **k- closed**.

!!! note "k-closed semiring"
    A semiring is **k-closed** if for any $x$, we have $\bigoplus_{i=1}^{k + 1} x^{\otimes_i} = \bigoplus_{i=1}^{k} x^{\otimes_i}$, where $x^{\otimes_i} = x \otimes x \otimes \cdots x$

So we can now safely compute path sum on closed semiring or k-closed semiring.

#### 2.2.3 Semiring Lifted to Matrix

It's easy to check that we can naturally define corresponding matrix addition and multiplication over a semiring, and the matrix addition multiplication again form a new semiring.

The Kleene star and matrix exponent on matrix semiring can be interpreted as complete path sum and path sum of a specific length.

However, note that closeness of original semiring **doesn't** guarantee closeness of induced matrix semiring. So we further define a **commutative** semiring $W$ is **k-closed for graph $G$** if for any cycle $\pi$ in $G$ it holds that:

$$
\bigoplus_{i=0}^{k+1} w(\pi) = \bigoplus_{i=1}^{k} w(\pi)
$$

We requires the semiring to be commutative because we want weight of a cycle not to depend on the node we enter in.
A}



