from __future__ import annotations
from functools import lru_cache, wraps
import time
import matplotlib.pyplot as plt
from typing import Callable, Dict

timings: Dict[int, float] = {}

def timer(func: Callable[[int], int]) -> Callable[[int], int]:
    @wraps(func)
    def wrapper(n: int) -> int:
        start = time.perf_counter()
        result = func(n)
        end = time.perf_counter()
        duration = end - start
        if n not in timings:
            timings[n] = duration
        print(f"Finished in {duration:.8f}s: f({n}) -> {result}")
        return result

    return wrapper


@lru_cache(maxsize=None)
@timer
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    N = 100
    fib.cache_clear()
    timings.clear()
    fib(N)
    xs = sorted(timings.keys())
    ys = [timings[i] for i in xs]
    plt.figure()
    plt.plot(xs, ys)
    plt.xlabel("n (Fibonacci index)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Fibonacci Execution Time")
    plt.grid(True)
    plt.savefig("fib.png", dpi=200, bbox_inches="tight")
    plt.show()
