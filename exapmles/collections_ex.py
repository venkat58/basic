from collections import Counter, OrderedDict,namedtuple

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

if __name__ == "__main__":
    #calculateCounter()
    student_avg()