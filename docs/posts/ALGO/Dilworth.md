# Dilworth Theorem

In high school many OIer must have heard of a classic problem [NOIP1999 提高组] 导弹拦截.

The problem asks us to calculate the least number of disjoint monotone decreasing subsequences that form a partition of the original sequence.

The answer is surprisingly easy: we only need to calculate the longeset monotone increasing subsequence and that's exactly the answer.

This could be proved by Greedy but it's more straightward if we use Dilworth Theorem.

!!! note "Dilworth Theorem"
    For a partial order set, the largest antichain has the same size as the smallest chain decomposition. Here antichain is a subset no two of which are comparable to each other, chain decomposition is a partition of the set by chain.

This theorem could be proved by induction.

It's easy to see that for any partial order set $S$, we can divide it into three parts: $S = A \cup D(A) \cup U(A)$, where $A$ is the largest antichain, $D(A) = \{x | \exists a \in A \;\; x \le a \}$, $U(A) = \{x | \exists a \in A \;\; a \le x \}$.

Then if there exists a largest antichain $A$ s.t. $D(A), U(A)$ are both not empty, we can apply induction hypothesis for $A \cup D(A)$ and $A \cup U(A)$ seperately ($A$ is the largest antichain of $S$ then it's also the largest antichain of $A \cup D(A)$) and combine the chains we get.

If any largest antichain $A$ has either empty $D(A)$ or empty $U(A)$ (which means every $A$ is either set of maximals or set of minimals) then we can firstly pick an arbitrary maximal element $y$ and then pick an minimal element $x$ such that $x \le y$ (this is always possible because we only need "walk" down along the chain). Obviously the path from $x$ to $y$: $(x, \cdots, y)$ forms a chian. Then any largest antichain would contain either $x$ or $y$ (if neither of them is contained, this largest antichain can include one of them and becomes larger). Thus we can remove $(x, \cdots, y)$, largest antichain's size must decrease by $1$ and we apply induction and finally and the chain $(x, \cdots, y)$ back.

This theorem can solve this interesting problem from lecture Graph Theory.

For a sequence of $kl + 1$ numbers, we can either get a (non-strictly) monotone increasing subsequence of length $k + 1$ or a montone decreasing subsequence of length $l + 1$.

This is because suppose any monotone increasing subsequence has length less than or equal to $k$, then to divide the whole sequence, we need at least $l + 1$ monotone increasing subseq. By Dilworth Theorem (monotone inc subseq is a chain), there has to be a antichain, i.e. a monotone dec. subseq., of size at least $l + 1$.