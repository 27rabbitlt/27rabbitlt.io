## 1 INTRO
Consider there is a list $a[0] ... a[n]$ containing $n$ elements which needs to be sorted. Assume we can swap arbitraty two elements in one operations. What is the minimum number of operations we need to take to get this list sorted?
## 2 THINKING
We can start from some simple cases. 
+ If we only have two elements in total, then we can easily sort them in at most one operation. 
+ If we have three elements in total, then there are multiple cases:
	+ If the list is 3, 2, 1, then we only need one operation.
	+ If the list is 2, 3, 1, then we need two operations.
+ If we have four elements in total, the situation is slightly more complicated:
	+ If the list is 2, 1, 4, 3, then we only need two operations.
	+ If the list is 2, 3, 4, 1, then we need three operations.
Seems that there is an obscure rule coming out. Let's compare the two cases where $n=4$. In the first case, though each element is not in the correct plcae, we can solve two *incorrectness* by one operation because $a$ is in the place where $b$ should be, while $b$ is in the place where $a$ should be. However, in the second case, the four elements are in a ring, which means that each element is in the place where the next element should be, just like a circle. In such a *circle* with 4 elements, we need to take 3 operations; with 5 elements, we need 4 operations, which can be easily validated.
So we can come up with a guess:
> For a *circle* with n elements, we need n - 1 operations to sort it.
## 3 PROOF
Actually, it's easier to prove a even stronger theorem:
> For a $n$ elements list with $k$ circles, we need $n-k$ operations to sort it.

Let's consider an extreme situation first. If a $n$ elements list has $n$ circles, then it is already sorted (we take a self-loop as a circle). So our target is actually to create as many circles as possible. Then how many circles can we create using one operation? At most one. 
If we think of it as a directed graph where vertex represents for element, and directed edge $(u, v)$ represents for element $u$ should be in the position which is currently occupied by element $v$. In this graph, each vertex $u$ has exactly one out-edge, of which the other endpoint is denoted by $out(u)$. An operation in the list  swapping $u$ and $v$ could be seen as a swap of $out(u)$ and $out(v)$ in the graph, which means:
$$
\begin{aligned}
out'(u) = out(v)\\
out'(v) = out(u)
\end{aligned}
$$
If $u$ and $v$ belongs to the same circle in the graph, then we will create a new circle. If $u$ and $v$ belongs to different circles, then we will eliminate one circle. 
So, we could at most create one circle using one operation.
Now that we have $k$ circles initially, we still need $n-k$ operations to get $n-k$ more circles, and $n$ circles in total. And eventually $n$ circles in the graph means the list is sorted.