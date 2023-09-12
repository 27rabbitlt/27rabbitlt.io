# MST Naive Survey

### 0 Abstract
This is a very simple and naive survey on M(Minimum) S(Spanning) T(Tree) problem. This problem is a widely researched and extremely important combinatorial problem, which has significant influences on all kinds of fields such as computer architecture allocation, transportation, express logistics, to name but a few. 

Also, a MST can also provide bounds (lower bound and 2-approximation upper bound if given triangle inequality) for Travelling Salesman Problem. Here I will introduce some classical algorithms and several modern and asymptotically better algorithms as well as parallel algorithms.
### 1 Introduction
In a network composed of nodes and arcs with costs, a **spanning tree** is a acyclic subgraph connecting all the nodes together. A **minimum spanning tree** is the spanning tree with minimum cost on the network. That is it is the spanning tree with the least sum of the costs of all the edges. 

Finding the minimum spanning tree is useful in several different applications. Perhaps the most direct application is designing physical systems like road system. For example, consider isolated villages that need to be connected with roads. We need to ensure that each village has at least one way to go to any other villages. Obviously, we also want the total construction cost to be minimum, and this forms a MST problem. 

We can easily come up with other ideas and situations needing the aid of MST.
Another application of the minimum spanning tree problem is cluster analysis. Suppose that we have a network and want to split the network into $k$ different clusters such that the total cost of all the clusters is minimized. We can take the minimum spanning tree and delete the $k-1$ arcs with the highest cost. The result is a forest of $k$ trees with minimal cost. 

We can see that the above two examples respectively correspond to adding edges and deleting edges. We will then show that both adding and deleting edges are important with respect to MST problem. They are important in finding a MST and using MST to solve a practical problem.
### 2 Basic Principle
> [!Definition]
> **Fundamental Cutset**
> For a graph  $G$  two distinct vertices say  $i$  and  $j$ , let  $X$ be any subset of vertices that contains $i$ but not  $j$ and let  $\bar{X}$ be its complement, then set  $X$ is a  $cut$ and the set of edges  $(i,j), i\in X,j\in \bar{X}, (i,j)\in E$ is called a   $cutset$ . 
> The removal of the arcs in a   $cutset$ leaves a disconnected subgraph of  $G$ . Corresponding to each edge  $e$ of a spanning tree  $T$ of a connected graph  $G$ , there is a unique cutset called the `fundamental cutset` of the tree  $T$ with respect to edge  $e$ .

We will then show that this definition has much to do with adding edges.

> [!Definition]
> **Fundamental Circle**
> Given a graph  $G$ , a spanning tree  $T$ and a co-tree edge   $e=(i, j)\in E - T$ , the unique cycle in  $G$  consisting of the edge  $e$ and the edges of the unique chain in  $T$ between  $i$ and  $j$ is called	a `fundamental cycle` of  $G$ relative to  $T$ with respect to  $e$ .

We will then show that this definition has much to do with deleting edges.

> [!Theorem]
> **Fundamental Cut Optimality**
> A spanning tree  $T$ in a weighted graph is a MST if and only if every edge in the tree is a minimum weight edge in the`fundamental cutset`defined by that edge.  

**Proof**:

the weight of edge  $(i,j)$ is noted as  $c_{ij}$ .

**1' MST==>Cut Opt**: This can be proved by contradiction. Suppose  $T^*$ is a minimum spanning tree violating **Cut Opt**, then there are two edges   $c_{ij}\in T$ and  $c_{kl}\in cut_{ij}$  such that  $c_{ij}>c_{kl}$ . Then replacing   $c_{ik}$ with  $c_{kl}$ would yield a lower cost spanning tree.

2' **Cut Opt==>MST**: Contradiction again. Suppose  $T^∗$ satisfies the cut optimality conditions, but  $T^∗$ is not a minimum spanning tree. That is, there exists a tree  $T^′≠T^∗$ that is a minimum spanning tree. Then, since  $T^∗$ is not a minimum spanning tree, it must have an edge  $(i,j)$ not contained in  $T^′$ . Deleting edge  $(i,j)$ from  $T^∗$  creates a cut  $[S,\bar{S}]$ . Adding one edge to a tree will form and only form one circle. Assume we add  $(i,j)$ to   $T'$ then we will get a circle  $C$ . Since  $i\in S, j\in \bar{S}$ , there must be an edge  $(k,l)$ in circle  $C$ such that  $k\in S, l\in \bar{S}$ . According to **Cut Opt** we know that  $c_{ij}\leq c_{kl}$  , and also we have  $c_{kl}\leq c_{ij}$ because  $T'$ is a MST, which means that if  $c_{ij}<c_{kl}$ then we can replace  $(k,l)$ with  $(i,j)$ yielding a less cost tree. Having the both inequalities, we know that  $c_{ij}=c_{kl}$ . Then we just replace  $(k,l)$ freely with  $(i,j)$ making a new MST (the total cost doesn't change, so it's still a MST) . Following this process, we can gradually change  $T'$ into  $T^*$ , which means that  $T^*$ is already a MST. 
> **[Theorem 2]** **Fundamental Circle Optimality**
> A spanning tree  $T$ in a graph  $G$ is a MST if and only if every edge  $e\in E-T$ is a maximum weight edge in the unique`fundamental cycle`defined by that edge.

**Proof**:

**1' MST==>Circle Opt**: This can also be proved by contradiction. Assume that there exists a MST  $T^*$ violating Fundamental Circle Optimality, which means that there is an edge  $e\in E-T$ weighing less than one edge  $e'$ in the `fundamental cycle`defined by  $e$ . Then we could delete edge  $e'$ and add edge  $e$ , then we can get a new tree  $T'$ with less cost. This conflictst with the assumption that  $T^*$ is a MST.

**2' Circle Opt==>MST**: This can be proved with the help of **Theorem 1**. It's obvious that if a tree doesn't hold **Cut Opt**, then it will not hold **Circle Opt** either. So we know that: **Circle Opt==>Cut Opt**. Then we have: **Circle Opt==>Cut Opt==>MST** using **Theorem 1**.
This is my personal proof, and here is an another much more elegant proof in [^1].
> **Blue Rule**:
> Select a cutset that does not contain a blue edge. Among the uncoloured edges in the cutset, select one of minimum weight and colour it blue.

> **Red Rule**:
> Select a simple cycle containing no red edges. Among the uncoloured edges on the cycle, select one of maximum weight and colour it red.  

These two rules are proposed in Tarjan's book[^3], and elaborately illustrated by tutorial slides[^2]. Since we already proved these two optimality conditions, these two rules can be immediately derived.

Both red rules and blue rules can be used for the construction of MST, but in practice, we usually use blue rule. The most well known algorithms including Prim, Kruskal and Sollin's algorithm are all using blue rule.
### 3 Details of Classical Algorithm
#### 3.1 Sollin's (Boruvka's) Algorithm
More commonly known as Boruvka's algorithm, Sollin's algorithm was the first algorithm for the minimum spanning tree problem. Borukva first published his algorithm in 1926 which he designed as a way of constructing an efficient electricity network in Moravia, a region of the Czech Republic. He published two papers in the same year with this algorithm. One was 22 pages and has been viewed as unnecessarily complicated. The other was a one page paper that has been regarded as the key paper showing Boruvka's understanding and knowledge of the problem.

It was then independently rediscovered in 1938 by French mathematician Gustave Choquet, and finally rediscovered in 1962 by Georges Sollin. 

We have introduced this algorithm in our lectures, so here I will not elaborately illustrate it. Each time we choose an edge with lowest cost from all edges incident to a component. We then add these edges into the graph and form a new graph with less components. It's obvious that this algorithm is using blue rules to add edges.

The time complexity is  $O(e\log n)$ .
#### 3.2 Prim Algorithm
This algorithm is so classical that almost everyone will be taught with this algo when learning MST for the first time. It use an arbitrary starting vertex  $s$ and apply the color step  $n-1$ times. The color step is that: Let  $T$ be the blue tree containing the vertex  $s$ . 

Select a minimum weight edge incident to  $T$ and colour it blue.   

There are many ways to implement Prim algorithm, with different time complexity. The difference lies in the way we select the minimum-weight edge. If we simply go through all the edges, then the time complexity would be  $O(n^2)$ . If we use binary heap and adjacent list, the time complexity would be  $O(e\log n)$ . If we use Fibonacci heap, the time complexity would be  $O(e+n\log n)$ . If we use d-heap, which is a general case of binary heap and an implementation of priority queue, the time complexity would be  $O(nd\log_dn+m\log_dn)$ . If we properly choose  $d$ , we can always get a satisfying algorithm for both dense graph and sparse graph (if dense, use a large d; if sparse, use a small d).

#### 3.3 Kruskal Algorithm
This algorithm is easy to implement and very suitable for competitive programming contests, so many competitors are very familiar with this algorithm. And its algorithm process can be a proof to many properties. The time complexity is  $O(e\log e)=O(e\log n)$ . This algorithm is also using blue rule, each time picking up the minimum-weight edge. If the edges are already sorted for us, then the time complexity could be  $O(e\alpha (e,n))$ , where  $\alpha(a,b)$ is the inverse Ackermann's function. This is because we are using union-and-find. 

To be honest, I didn't understand the proof of the time complextiy of union-and-find, here I'm just using the result provided by Wikipedia.

### 4 Not That Well-Known Algorithm
We learned two not that well-known algorithms in this class: Yao algorithm and Cheriton-Tarjan algorithm. They are adapted from Sollin's algorithm, using smarter way to select the minimum-weight edge. 
#### 4.1 Yao Algorithm
This is an algorithm proposed by Qizhi Yao. It is on the basis of another algorithm finding the median with deterministic linear time[^8]. Assume that we already know how to find the median in linear time, then we can refine Sollin's algorithm by grouping edges. In Sollin's, we need to go through every edge to find the one with minimum weight. However, we know that some edges with large weight should not be considered in the early stages.

Consider dividing all the edges into  $k$ groups, then we each time only need to go through the edges within the group. Then the time complexity is  $O(dividing+\frac{n}{k}\log n)$ . Then what is the time complexity of dividing edges into  $k$ groups such that edges in  $i+1$th group have larger weight than these in  $i$th group? We each time find the median and divide the set into two parts, and then recurssively go down in these two smaller subset. It's obvious that the dividing time is  $O(n\log k)$ .  Then using simple calculus knowledge we can that when  $k=\log n$ the formula  $O(n\log k+\frac{n}{k}\log n)$ gets its minimum:  $O(n\log \log k)$ .

#### 4.2 Cheriton-Tarjan Algorithm
The full algorithm[^5] is very complex, here is the key point: A heap is kept for each blue tree. Each heap holds the edges with at least one endpoint in the tree and which are candidates for becoming blue. Similar to Kruskal's algorithm, it grows a spanning forest, beginning with a forest of   $n$ components each consisting of a single node. Since, every component    $T_u$ must eventually be connected to another component, this algorithm keeps a separate heap   $PQ_u$ for each component   $T_u$ , so, that initially   $n$ smaller heaps are used. Initially,   $PQ_u$ will contain only   $DEG(u)$ edges, since   $T_u$ consists only of vertex   $u$ . When   $T_u$ and   $T_v$  are merged,   $PQ_u$ and   $PQ_v$ must also be merged. This requires a modification of the data structures, since heaps cannot be merged efficiently. This is essentially because merging heaps reduces to building a new heap. It's difficult to work out the precise time complexity, I still need some time to understand the original paper. Here I just use the result provided by the paper, that the time complexity is   $O(e\log \log n)$ .

In Cheriton and Tarjan's paper, they also proposed an algorithm for planar graph with time complexity   $O(n)$ , and an algorithm for sparse graph with time complexity   $O(e)$ . 

### 5 Randomized Algorithm
#### 5.1 Tarjan's Expected Linear Time Algorithm
It was developed by David Karger, Philip Klein, and Robert Tarjan. So it is also known as Karger's algorithm. The algorithm relies on techniques from Boruvka's algorithm along with an algorithm for verifying a minimum spanning tree in linear time. It combines the design paradigms of divide and conquer algorithms, greedy algorithms, and randomized algorithms to achieve expected linear performance.
The key insight to the algorithm is a random sampling step which partitions a graph into two subgraphs by randomly selecting edges to include in each subgraph. The algorithm recursively finds the minimum spanning forest of the first subproblem and uses the solution in conjunction with a linear time verification algorithm to discard edges in the graph that cannot be in the minimum spanning tree. A procedure taken from Borůvka's algorithm is also used to reduce the size of the graph at each recursion. 

In more details, there are three steps in total: Boruvka step, random sampling step, and verification step.

- Boruvka Step: Given a graph  $G$ , apply the Boruvka algorithm to carry out one coloring step only. And then contract the graph  $G$ and get  $G'$ .
- Random sampling step: Given a contracted graph  $G$ , choose a subgraph  $H$ by selecting each edge

in  $G$ independently with a probability   $1/2$ .

- Verification step: Given any minimum spanning forest  $F$ of  $H$ , find the   $F_{heavy}$  edges and delete them from  $G$ to reduce the graph further. Here   $F_{heavy}$  means that the weight of an edge   $w(u,v)$  is larger than the weight of the path from   $u$  to   $v$  in a forest   $F$ . It's obvious that all the  $F_{heavy}$ edges will not appear in the final MST, so we can delete them.

The complete algorithm process is shown below:

1. Given   $G(V, E)$ , apply two successive Boruvka steps to the graph to contract  $G$ .
2. Apply the random sampling step to the contracted graph to select  $H$ .
3. Apply the algorithm recursively producing a minimum spanning forest  $F$ of the   $H$  formed in step 1
4. Given   $F$  of   $H$ , apply the verification step to the subgraph  $H$ , which was chosen, and obtain

a graph  $G$ which is reduced further.

5. Apply the algorithm recursively to  $G$ to compute the minimum spanning forest  $F$ of  $G$ .
6. Return those edges contracted in step 1 together with the edges of  $F$ .

The time complexity relies on two properties:
> **Property 1**
> Let  $H$ be a subgraph obtained from  $G$ by including each edge independently with probability  $p$ , and let  $F$ be the minimum spanning forest of  $H$ . The expected number of  $F$ edges in  $G$ is at mos  $n/p$ where  $n$ is the number of vertices.

> **Property 2**
> We can do the verification step in deterministic linear time with the algorithm[^9] proposed by V. King.

Both properties need further research and more time, I will get it through soon.
The expected running time is  $O(m)$ and it runs in   $O(m)$  time with probability   $1-exp(-\Omega (m))$ .
In the worst case, it will be equivalent to Boruvka's algorithm, so the worst time complexity is   $O(e\log n)$ .

### 6 Parallel Algorithms
The performance comparison of these sequencial algorithms is basically of no use, because in reality, we will never use one processer to handle a large-scale problem. And this is also the reason why parallel algorithms are getting more and more popular. All the classical algorithms illustrated above can be adapted into parallel version.

#### 6.1 Prim Parallel Version
Prim algorithm has the least parallelism possiblity. Because each time we need to update the distance vecter, which can't be paralleled, since each element can't be changed by two processes. What we can do is that: we can use paralleled priority queue with insert time complexity of  $O(1)$ .

#### 6.2 Kruskal Parallel Version
There are two ways to parallelize the Kruskal algorithm. The first is to parallelize the sorting stage. We know that in Kruskal algorithm, we need to sort all the edges by their weight, which could be parallelized. We can sort  $n$ elements in   $O(\log n)$  time with   $n$  processors. So the total time would be   $O(m\alpha(n))$ . The second way is to parallelize an adaptation of Kruskal algorithm, which is named Filter-Kruskal algorithm[10]. 

#### 6.3 Sollin Parallel Version
In Sollin's process, we have three stages. The first stage is finding the lightest edge, which can be parallelized; the second stage is to go through each subgraph, which can be parallelized; the third stage is to contract the graph, which can be parallelized. The respective time complexity is   $O(\frac{m}{p}+\log n+\log p), O(\frac{n}{p}+\log n), O(\frac{m}{p}+\log n)$ .

### 7 Other Applicatioins and Properties
There are so many different variations about MST, coming up with different graceful properties. We can impose some edges, which means that these edges must be in MST, and then construct the MST; We can add a new vertex and the incident edges and find the new MST based on the previous MST, which is one of our homework problems; We can delete one vertex and find the new MST; We can change the weight of one edge and find the MST; We can get linear time approxiamations on MST, to name but a few.
Here I will introduce some simple properties:

1. Given a graph with its MST, and a new vertex with its incident edges, we can find the new MST in  $O(n)$ time. This is based the observation: the new MST will only contain the newly added edges and the edges in the original MST.
2. Given a graph with its MST, and a deleted vertex, we can also ensure that the new MST will consist all the edges in the previous MST except for these deleted ones.
3. Add a constant to the weight of every vertex will not change the MST.
4. Change the weight of an edge, there are four cases in total. If we decrease the edge in MST, remains the same; If we increase the edge not in MST, remains the same; If we increase the edge in MST, we just need   $O(m)$  time to find the new edge connecting the two components; If we decrease the edge not in MST, we just need to find the circle in  $MST\cup edge$ , if the decreased weight is smaller than any edge in that circle, we can do a substitution.
5. There might be many MSTs in a graph, but all the MSTs have the same edges-weight-set, which means that: if we only focus on the weight of the edges in MST, then the sorted array of the weights of the edges in any MST is the same.
### 8 Reference
[^1]: Slides about MST and cut optimality and path optimality conditions [https://copland.udel.edu/~amotong/teaching/algorithm%20design/lectures/(Lec%2012)%20Greedy%20Strategy%20-%20Minimum%20Spanning%20Tree%20-%20Optimality%20Condition.pdf](https://copland.udel.edu/~amotong/teaching/algorithm%20design/lectures/(Lec%2012)%20Greedy%20Strategy%20-%20Minimum%20Spanning%20Tree%20-%20Optimality%20Condition.pdf)

[^2]: Slides about MST and blue rule and red rule
[https://www.cs.princeton.edu/~wayne/cs423/lectures/mst.pdf](https://www.cs.princeton.edu/~wayne/cs423/lectures/mst.pdf)

[^3]: Tarjan RE. Data structures and network algorithms. In CBMS-NFS Regional Conference Series in Applied Mathematics. Philadelphia: Society for Industrial and Applied Mathematics, 1983. p. 44.  
[https://www.amazon.com/Structures-Algorithms-CBMS-NSF-Conference-Mathematics/dp/0898711878](https://www.amazon.com/Structures-Algorithms-CBMS-NSF-Conference-Mathematics/dp/0898711878)
(This is a book, so it's the link of the book on Amazon)

[^4]: Johnson DB. Priority queues with update and "finding minimum spanning trees. Information Processing Letters 1975;4:53}7.
[https://www.sciencedirect.com/science/article/abs/pii/0020019075900010](https://www.sciencedirect.com/science/article/abs/pii/0020019075900010) 
ZJU didn't subscribe to this journel, pity.

[^5]: FINDING MINIMUM SPANNING TREES, DAVID CHERITON AND ROBERT ENDRE TARJAN
[https://epubs.siam.org/doi/pdf/10.1137/0205051](https://epubs.siam.org/doi/pdf/10.1137/0205051)

[^6]: Improved Multiple Constant Multiplication Using a Minimum Spanning Tree  
[https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1399088](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1399088)

[^7]: Imposing edges in Minimum Spanning Tree
[https://arxiv.org/pdf/1912.09360.pdf](https://arxiv.org/pdf/1912.09360.pdf)

[^8]: Linear Time Median Finding: [https://rcoh.me/posts/linear-time-median-finding/](https://rcoh.me/posts/linear-time-median-finding/)

[^9]: A Simpler Minimum Spanning Tree Verification Algorithm 
[https://www.cs.princeton.edu/courses/archive/fall03/cs528/handouts/A%20Simpler%20Minimum%20Spanning.pdf](https://www.cs.princeton.edu/courses/archive/fall03/cs528/handouts/A%20Simpler%20Minimum%20Spanning.pdf)

[^10]: The Filter-Kruskal Minimum Spanning Tree Algorithm
[http://algo2.iti.kit.edu/documents/fkruskal.pdf](http://algo2.iti.kit.edu/documents/fkruskal.pdf)

