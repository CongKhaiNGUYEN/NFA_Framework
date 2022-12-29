from itertools import chain, combinations
from nfa import *


NFA.clear()

NFA.NOVISU = False
NFA.VISULANG = 2
NFA.VISU_INITIAL_ARROW = False
NFA.VISUDOUBLEARROWS = True

actorsv = I,G,W,C,Lamp,Time = "Indy","Girl","Wounded","Child","Lamp",15

actors = fset(actorsv)

NFA.visutext("Naïve method")


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def tau(a,b):
    time = {"Indy":1, "Girl":2, "Wounded":4, "Child":8,"Lamp":0}
    return max(time.get(a),time.get(b))

Qv = { x + (y, ) for x in powerset(["Indy","Girl","Wounded","Child","Lamp"]) for y in range(16) }
# Qv_ =  set(powerset(["Indy","Girl","Wounded","Child","Lamp"]))
# F = {x for x in range(16)}  # {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}

# NFA_Indy = NFA(
#     {("Indy","Girl","Wounded","Child","Lamp",15)},
#     F,
#     {
#         (p + (t,),(a,b,L),tuple(set(p) - set((L,a,b))) + (t - tau(a,b),))
#         for p in Qv_
#         for a in ("Indy","Girl","Wounded","Child")
#         for b in ("Indy","Girl","Wounded","Child")
#         for t in range(16)
#     } | {
#         (p + (t,),(a,b,L),p + (L,a,b) + (t - tau(a,b),))
#         for p in Qv_
#         for a in ("Indy","Girl","Wounded","Child")
#         for b in ("Indy","Girl","Wounded","Child")
#         for t in range(16)
#     },
#     name="Indiana Jones",
#     Q = Qv,
#     trimmed = True,
#     worder=tuple
# ).visu()

def growLamp(A):
    has=False
    def extend(q):
        nonlocal has
        if Lamp in q:
            for a in q:
                if type(a) == int:
                    continue

                for b in q:
                    if type(b) == int:
                        continue
                    x = 15
                    for c in q:
                        if type(c) == int:
                            x=c                    
                    Q = q - {a,b, Lamp} - {x} 
                    Q =Q | {x -tau(a,b)}
                    has = A.try_rule(q, a, Q) or has

        # if Lamp not in q:
        #     for a in actors - q:
        #         Q = q | {a,Lamp}
        #         has = A.try_rule(q, a, Q) or has

    for q in A.Q.copy(): extend(q)
    return has

FWGC_Problem = NFA(
    {actors},
    name="Indiana Jones",
    worder=tuple
).visu()

FWGC_Problem.growtofixpoint(growLamp, record_steps=True)
FWGC_Problem.F = {x for x in range(16)}