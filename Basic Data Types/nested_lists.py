if __name__ == '__main__':
    students = [[input(), float(input())] for _ in range(int(input()))]
    second_highest = sorted(list(set([score for _, score in students])))[1]
    print("\n".join(
        sorted([name for name, score in students if score == second_highest])))
