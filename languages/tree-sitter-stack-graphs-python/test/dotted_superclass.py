class A:
    class B:
        pass
class Subclass(A.B): pass
#              ^ defined: 1
#                ^ defined: 2
    