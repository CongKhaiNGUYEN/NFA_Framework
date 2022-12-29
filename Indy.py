from nfa import *
from Increment import increment

NFA.clear()

NFA.NOVISU = False
NFA.VISULANG = 2
NFA.VISU_INITIAL_ARROW = False
NFA.VISUDOUBLEARROWS = True

# def increment(n,m,i,X):
#     return NFA({i}, Q := set(range(n, m + 1)), {
#         (p, k if k < 0 else f"+{k}", p + k )
#         for p in Q
#         for k in X
#         if n <= p + k  <= m
#     }).named(f"Time")

def tau(a,b):
    time = {"Indy":1, "Girl":2, "Wounded":4, "Child":8}
    return max(time.get(a),time.get(b))
Time = increment(0,15,15,{-1,-2,-4,-8})
actorsv = I, G, W, C, L = "Indy", "Girl", "Wounded", "Child", "Lamp"
actors = fset(actorsv)
actors_at = fset((I, G, W, C))

NFA.visutext("Indiana Jones")

Char = NFA.spec("""
0
1
0 1 1
1 0 0""","Char").visu()

sysv = [Char.copy().named(x) for x in actorsv]
# print(sysv)
sds = [{L:x,a:x,b:x,"Time":-tau(a,b)} for x in {0,1} for a in actors_at for b in actors_at]

P = NFA.nsprod(*sysv, Time,
               sds=sds
               ).trim().visu()

print(repr(P))
P.dnice().visu()
P.dnice(f="states").trim().visu()