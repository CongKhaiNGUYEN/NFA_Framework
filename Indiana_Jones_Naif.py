def india_jones():
    # actors = ("jones", "girlfriend", "guy", "kid", "lamp")
    actors = ("Indy", "Girl", "Wounded", "Child", "Lamp")
    Lamp = NFA(
        {(actors, 15)},
        set(),
        set(),
        name="Lamp",
        worder=tuple
    ).visu()

    def growLamp(A):
        has=False
        def extend(q):
            nonlocal has
            if 'Lamp' in q[0]:
                for a in combinations_with_replacement(q[0], 2):
                    if set(a) != {"Lamp"}:
                        Q = set(q[0]) - set(a + ("Lamp", ))
                        re_t = q[1] - get_walked_minutes(set(a + ("Lamp", )))
                        if re_t >= 0:
                            if Q:
                                has = A.try_rule(q, tuple(set(a + ("Lamp", ))), (tuple(Q), re_t)) or has
                            else:
                                has = A.try_rule(q, tuple(set(a + ("Lamp", ))), (tuple(Q), re_t), final=True) or has

            if 'Lamp' not in q:
                for a in combinations_with_replacement(set(actors) - set(q[0]), 2):
                    if set(a) != {"Lamp"}:
                        Q = set(q[0]) | set(a + ("Lamp", ))
                        re_t = q[1] - get_walked_minutes(set(a + ("Lamp", )))
                        if re_t >= 0: 
                            if Q:
                                has = A.try_rule(q, tuple(set(a + ("Lamp", ))), (tuple(Q), re_t)) or has
                            else:
                                has = A.try_rule(q, tuple(set(a + ("Lamp", ))), (tuple(Q), re_t), final=True) or has

        for q in A.Q.copy(): extend(q)
        return has

    Lamp.growtofixpoint(growLamp, record_steps=True)
    Lamp.F = { (fset(()), x) for x in range(16)}
    Lamp.visusteps()
    Lamp.trim().visu()
    Lamp.map(f=lambda q: (
        ", ".join(q[0]) + ", " + str(q[1]) + " \\n~~~~~~~\\n " + ", ".join(set(actors)-set(q[0]))
    )).trim().visu(break_strings=False)
    Lamp.trim()



india_jones()