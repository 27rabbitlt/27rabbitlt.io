# Tips for LaTex

## enumerate
### enumerate using alphabet

```latex
\begin{enumerate}[label=(\alph*)]
```

## equations
### case

![](assets/equation_case.jpg)

```latex
\begin{equation}
  D_{it} =
    \begin{cases}
      1 & \text{if bank $i$ issues ABs at time $t$}\\
      2 & \text{if bank $i$ issues CBs at time $t$}\\
      0 & \text{otherwise}
    \end{cases}       
\end{equation}
```

### font

Normal font:
$$RQSZ$$

Calligraphy font:
$$\mathcal{RQSZ}$$

Fraktur font:
$$\mathfrak{RQSZ}$$

Bold font:
$$\mathbb{RQSZ}$$