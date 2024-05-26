# DSU on Tree (Heuristic Merge on Tree)

## 0 Usage

It could be used to solve some offline tree problem. Usually the time complexity would be $O(n\logn)$.

## 1 Idea

Although it's called heuristic in Chinese, this algorithm can be rigorously proved to be efficient.

The idea is quite simple: **go through light child twice**. 

Basically, tree-based algorithms always contain two parts: go through the child subtree; and merge the results of child subtrees.

If a node always go through ever child subtree exactly once, then time complexity would be $O(n)$; while merging results of child subtrees could be costy. DSU on Tree solves this kind of problem by seperate DFS child subtree and merging. If merging is a seperate task, then we can simply go through every node without maintaining anyting for child subtree.

However if we sepearte these two tasks then we need one more pass for some child subtree, how could we control the cost? 

We call a child heavy if it's the one with the largest child subtree, otherwise we call it light. For each node we only sepearate the tasks for light children, which means we will have one more pass for each light child. 

Compared with classical DFS algo, the only difference is that light child would be gone through one more time, so each node $v$ would be went through $l + 1$ times, where $l$ is the number of light child along the path from $v$ to root of tree.

There can't be more than $\logn$ light children in a path starting from root.