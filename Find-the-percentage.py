if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *num = input().split()
        scores = list(map(float, num))
        student_marks[name] = scores
    query_name = input()
    l1 = list(student_marks[query_name])
    addition = sum(l1)
    result = addition/len(l1)
    print("%.2f"% result)