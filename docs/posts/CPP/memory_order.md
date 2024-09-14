# Memory Order

Let's talk about memory order.

I've learnt about this for the fourth time and each time I thought I fully understood everything and wouldn't forget anything. While it turns out that this is not the case.

Firstly, in case in the future I still forgot everything and this blog doesn't help, here is the blogs that I read, I should be able to recover from these articles:

+ https://preshing.com/20120930/weak-vs-strong-memory-models/

Actually this is a series of articles all about memory models.

+ https://www.cl.cam.ac.uk/~pes20/weakmemory/

Some tools, papers.

+ https://github.com/27rabbitlt/memory_order_test_demo

Simple test demos.

Alright then, let's officially start.

## 1 What is memory order?

Memory order, by its name, is the order of access to memory by CPU. 

Let's firstly talk about the case where there is only one CPU.

To increase throughput and reduce latency, it's understandable to re-order instructions. It can be done by compilers and the CPU.

For the compiler side, a piece of code written in high-level language serves the functionality to help human-beings understand and maintain the code, so the order of statements are meant to be human-readable instead of maximize performance. Thus compiler will try to swap some statements and improve performace.

For the CPU side, compiler would never have full access of every details of CPU so it's still up to CPU to re-re-order the instructions. Note that memory re-order is not just caused by instruction re-order, it can involve read-write re-order done by memory.

No matter what ordering compiler and CPU are taking, the basic rule is that: **The result should be the same**. While, at least the CPU that performs re-ordering believes that the result should be the same if no memory address is shared with other CPUs.

The truth is, in practice we tend to have multiple threads which share some specific meomory with each other. Now the problem arises: what if the re-ordering done by CPU A affects the result of CPU B?

Here is a very simple demo:

| P1             | P2                 |
|----------------|--------------------|
| X = 1          | if ready_X: read X |
| ready_X = true |                    |

Assume before P1 sets X to be 1, the value of X is just garbage that we don't know.

Then for P1, if there is only one CPU, then the result won't change if we swap the instructions `X = 1` an `ready_X = true`. It's impossible for P1 to know that somewhere on another CPU there is a piece of code `if ready_X: read X`.

So it's possible that P1 swaped `X = 1` an `ready_X = true` and P2 sees `ready_X` is true but get garbage value from `X`.

## Memory Barrier

Now memory re-ordering seems to be a bad thing, it might cause the wrong result!

However, if we stick to sequential-order, i.e. we don't allow any kind of reordering and the whole program runs as if each thread is executed sequentially, we also cannot accept the performance.

Here is where memory barrier comes in.

Memory barrier prevent compiler and CPU to do certain types of re-ordering so as to make sure the result is still correct and meanwhile we can have as less restrictions for CPU as possible to get best performance.

Typically, there are four kinds of re-ordering: LoadLoad, LoadStore, StoreLoad, StoreStore. So in the same way, we can have four types of barriers. Notice that these four types are just conceptual, they do not really exist. In practice, barriers are often some combinations of these four types.

We always see something like acquire-release in C++ atomics. Acquire can be roughly described as the combination of LoadLoad and LoadStore barrier; and Release can be described as the combination of LoadStore and StoreStore barrier.

## Memory Model of CPU

Granted, there are 4 types of re-ordering, but not all CPUs allow all 4 re-ordering. The restrictions of re-ordering is called the memory model of CPU.

We discuss models from the weakest to the strongest.

A classical example of weak memory model is: https://www.cs.umd.edu/~pugh/java/memoryModel/AlphaReordering.html. 

Weakest memory model allows all kinds of re-ordering.

ARM has stronger model, but still classified as weak-order model.

It guarantees order with data dependencies. For example, the expression `A->b`, it's guaranteed that `b` is at least as new as `A`.

x86 is a strong-order model. None of LoadLoad, LoadStore, or StoreStore are allowed, which means basically instructions on x86 themselves are using acquire-release semantic naturally.

But, StoreLoad re-ordering is still possible: https://github.com/27rabbitlt/memory_order_test_demo/blob/main/test_arm_store_load_reorder.cpp

Another interesting demo that shows some re-ordering won't happen on x86 but will on ARM is: https://github.com/27rabbitlt/memory_order_test_demo/blob/main/test_arm_store_load_reorder.cpp

TBD: explain why it will happen on arm but won't do on x86.