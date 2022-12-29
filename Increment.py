from nfa import NFA

def increment(n,m,i,X):
    return NFA({i}, Q := set(range(n, m + 1)), {
        # (p, k if k < 0 else f"+{k}", p + k )
        (p, k , p + k )
        for p in Q
        for k in X
        if n <= p + k  <= m
    }).named(f"Time")
