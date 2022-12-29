from nfa import *

NFA.clear()

Char_ = NFA.spec("""
    0
    2
    0 1 1 2 2
    1 2 2 0 0
    2 0 0 1 1
    """).map(g=int).named("Char")#.visu()

Char = NFA(
    {0},
    {2},
    {
        (p,(p,q),q)
        for q in range(3)
        for p in range(3)
        if p != q
    },
    name = "Three Islands",
    worder=tuple
).visu()


actorsv = W1, W2, G, C, F = "Wolf1", "Wolf2", "Goat", "Cabb", "Farmer"
actors = fset(actorsv)


# ensemble de automate de chaque acteur
sysv = [Char.copy().named(x) for x in actorsv]

sds = [{F:(x, y), a:(x, y)} for a in actors for x in (0, 1, 2) for y in (0, 1, 2) if x != y]


def _licit(s):
    return F in s if {W1, G} <= s or {W2, G} <= s or {G, C} <= s else True

def prodfilter(A, P, v, Q):
    print(f'{invd(Q)[0]} {_licit(invd(Q)[0])} {invd(Q)[1]} {_licit(invd(Q)[1])} {invd(Q)[2]} {_licit(invd(Q)[2])}')
    return Q not in A.Q and _licit(invd(Q)[0]) and _licit(invd(Q)[1]) and _licit(invd(Q)[2])


P = NFA.nsprod(*sysv, sds=sds, filter=prodfilter).trim().visu()

