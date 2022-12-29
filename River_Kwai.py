from nfa import *
from Increment import *

NFA.clear()

NFA.NOVISU = False
NFA.VISULANG = 2
NFA.VISU_INITIAL_ARROW = False
NFA.VISUDOUBLEARROWS = True

NFA.visutext("The Bridge on the River Kwaï")

Char = NFA.spec("""
0
1
0 1 1
1 0 0""","Char").visu()

actorsv = A, B, C, S, E = "Alice", "Bob", "Capitaine", "Soldat", "Esquif"
actors = fset(actorsv)

sysv = [Char.copy().named(x) for x in actorsv]



# sds = [{L:x,a:x,b:x,"Time":-tau(a,b)} for x in {0,1} for a in actors_at for b in actors_at]

sds = [{E:x, c:x, d:x} for x in {0,1} for c in {A,B} for d in {A,B} ] + [{E:x,c:x} for x in {0,1} for c in {C,S}]


def _licit(s):
    return len(s - {E}) > 2 if {A,C} in s else True

def prodfilter(A, P, v, Q):
    return Q not in A.Q and _licit(invd(Q)[0]) and _licit(invd(Q)[1])

P = NFA.nsprod(*sysv,
               sds=sds
               ).visu()


NFA.visutext("River Kwaï et le capitalisme")

# def increment(n,m,i,X):
#     return NFA({i}, Q := set(range(n, m + 1)), {
#         (p, k , p + k )
#         for p in Q
#         for k in X
#         if n <= p + k  <= m
#     }).named(f"Simflouz")

N = 18
Simflouz = increment(0,N,0,{1,2,4}).named("Simflouz")
# Simflouz = increment(0,N,N,{-1,-2,-4}).named("Simflouz")

def pay(a):
    a = list(a)
    price = {"Alice":1, "Bob":1, "Capitaine":4, "Soldat":4}
    return price.get((a[0])) if len(a) == 1 else price.get((a[0])) + price.get((a[1]))

sds_2 = [{E:x, c:x, d:x, "Simflouz":pay({c,d})} for x in {0,1} for c in {A,B} for d in {A,B} ] + [{E:x,c:x,"Simflouz":pay({c})} for x in {0,1} for c in {C,S}]


P = NFA.nsprod(*sysv, Simflouz,
               sds=sds_2
               ).trim().visu()