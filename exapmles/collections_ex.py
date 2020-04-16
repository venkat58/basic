from collections import Counter, OrderedDict,namedtuple
import datetime

class OrderedCounter(Counter, OrderedDict):
    pass
def calculateCounter():
    #input (4 abc abcd abcd ab) op(2 1 1)
    d = OrderedCounter(input() for _ in range(int(input())))
    print(len(d))
    print(*d.values())

def student_avg():
    #input(2 ID MARKS NAME CLASS \n 1 98 gv 7 2 76 vv 7)
    n,arrangement = int(input()),input()

    Student = namedtuple('Student',arrangement)

    print(sum( [int(Student._make(input().split()).MARKS) for _ in range(n)])/n)

def list_operations():
    '''input 12
     insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print'''
    N = int(input())
    l = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print(l)


if __name__ == "__main__":
    #calculateCounter()
    #student_avg()
    #list_operations()
    pass
    