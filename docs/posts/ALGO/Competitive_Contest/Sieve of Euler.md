The essence of sieve of euler is that we divide each composite number into two parts: the first one the least prime divisor and the quotient. 
Formally:
$$
C = p_1 \cdot \Pi_{i=2}^{k} \; p_i^{q_i}
$$
But how can we do this? Easy.
First, note that we use every number $x$ to *sieve* its multiples, mo matter it is a composite number or prime numer; we multiply it with different prime numbers to sieve other numbers.
Second, each time when $x$ is divisible by the prime number, we break the `for` loop.

This is the code:
```C++
void prime_sieve(int n) {
	for (int i = 2; i <= n; i++) {
		if (!noprime[i]) {
			prime[cnt++] = i;
		}
		for (int j = 0; j < cnt; j++) {
			noprime[i * prime[j]] = 1;
			if (i % prime[j] == 0) {
				break;
			}
		}
	}
}
```
