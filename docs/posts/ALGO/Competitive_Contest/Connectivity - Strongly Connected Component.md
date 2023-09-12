## 1 DFS Tree

First, we introduce `DFS tree` so as to help us understand the basic structure of strongly connected component.

![[Pasted image 20230911122608.png]]

As is shown in this graph, there are four different types of edges, naming:

1. Tree edge: the black one, indicating the edge in the DFS process.
2. back edge: the red one, indicating that the destination node is an ancester.
3. cross edge: the blue one, indicating that the destination node is not in the stack
4. forward edge: the green one, indicating that the destination node is in the stack but not an acester.

Here we used a stack, but that's not exactly the same as the DFS stack, which is quite similar though. We will explain this stack later on.

## 2 Intution

Since we want to find out the strongly connected component, which is a seemingly tough problem, we can try to find a representative in this component instead. Let's think about it: which vertex is the most *special* in a component so as to become a representative? The one with the lowest depth in the DFS tree (we can actually easily prove that there will only be one vertex with the lowest depth, left for readers).

WLOG, we call that vertex **father vertex** in the component. Our task transfered to finding the father vertex because once we find it, we can determine that all the vertices still in the stack belong to the corresponding component of that father vertex.

Then, let's think about the property of father vertex, i.e. how to determine whether a vertex is a father vertex or not. Since father vertex has the lowest depth by definition,  if we can matintain the lowest depth that a vertex could reach (just a rough definition for temporary usage), then a vertex with its own depth the same as the depth that it could reach would be a father vertex.

Now let's define all the stuff rigorously. 

## 3 Definition

> [!tip]
>

