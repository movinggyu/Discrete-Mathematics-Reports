import os

def main():
    os.system('cls')
    N = int(input("관계행렬의 크기 N을 입력하세요: "))
    A = set(range(1,N+1))
    relMat = inputMat(N)
    printMat(relMat, "입력된 관계")
    printRelationSet(relMat)

    # 반사, 대칭, 추이관계 판별
    reflexive = isReflexivity(relMat)
    symmetric = isSymmetry(relMat)
    transitive = isTransitivity(relMat)

    print("관계 판별:")
    print("반사성:", "O" if reflexive else "X")
    print("대칭성:", "O" if symmetric else "X")
    print("추이성:", "O" if transitive else "X")

    # 동치관계 판별
    if isEquivalence(relMat):
        print("동치 관계입니다. 동치류 출력:")
        for a in sorted(A):
            print(f"[{a}] =", getEquivalenceClass(a, relMat))
        return

    # 폐포 단계별 적용
    print("동치 관계가 아닙니다. 폐포를 단계적으로 적용합니다.")
    current = [row[:] for row in relMat]

    if not reflexive:
        print("반사 폐포 적용:")
        current = getReflexiveClosure(current)
        printMat(current, "반사 폐포 적용 후")
        printRelationSet(current)
        print("반사성:", "O" if isReflexivity(current) else "X")

    if not symmetric:
        print("대칭 폐포 적용:")
        current = getSymmetricClosure(current)
        printMat(current, "대칭 폐포 적용 후")
        printRelationSet(current)
        print("대칭성:", "O" if isSymmetry(current) else "X")

    if not transitive:
        print("추이 폐포 적용:")
        current = getTransitiveClosure(current)
        printMat(current, "추이 폐포 적용 후")
        printRelationSet(current)
        print("추이성:", "O" if isTransitivity(current) else "X")

    # 최종 판별
    print("폐포 적용 후 최종 판별:")
    if isEquivalence(current):
        print("동치 관계가 되었습니다. 동치류 출력:")
        for a in sorted(A):
            print(f"[{a}] =", getEquivalenceClass(a, current))
    else:
        print("폐포 적용 후에도 동치 관계가 아닙니다.")


def inputMat(size: int) -> list:
    mat = []
    i = 0
    while i < size:
        try:
            print(f"{size}x{size} 행렬의 {i+1}번째 행 입력 : ", end="")
            row = list(map(int, input().strip().split()))
            if len(row) != size:
                print(f"행의 길이가 {size}이 아닙니다. 다시 입력하세요.")
                continue
            mat.append(row)
            i += 1
        except ValueError:
            print("숫자만 입력해야 합니다. 다시 입력하세요.")
    return mat


def isReflexivity(mat: list) -> bool:
    size = len(mat)
    for i in range(size):
        if mat[i][i] != 1: return False
    return True


def isSymmetry(mat: list) -> bool:
    size = len(mat)
    for i in range(0, size):
        for j in range(i+1, size):
            if mat[i][j] != mat[j][i]: return False
    return True


def isTransitivity(mat: list) -> bool:
    size = len(mat)
    for i in range(size):
        for j in range(size):
            if mat[i][j] == 1:
                for k in range(size):
                    if mat[j][k] == 1 and mat[i][k] == 0:
                        return False
    return True


def isEquivalence(mat: list) -> bool:
    return isReflexivity(mat) and isSymmetry(mat) and isTransitivity(mat)


def getEquivalenceClass(elem: int, mat: list) -> set:
    size = len(mat)
    result = set()
    for i in range(size):
        if mat[elem-1][i] == 1: result.add(i+1)
    return result


def getReflexiveClosure(mat: list) -> list:
    size = len(mat)
    closure = [row[:] for row in mat]
    for i in range(size):
        closure[i][i] = 1
    return closure


def getSymmetricClosure(mat: list) -> list:
    size = len(mat)
    closure = [row[:] for row in mat]
    for i in range(size):
        for j in range(size):
            if closure[i][j] == 1: closure[j][i] = 1
    return closure


def getTransitiveClosure(mat: list) -> list:
    size = len(mat)
    closure = [row[:] for row in mat]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if closure[i][k] and closure[k][j]:
                    closure[i][j] = 1
    return closure


def printMat(mat: list, name: str) -> None:
    print(f"{name}행렬은 다음과 같습니다:")
    print("┌", " "*(7*len(mat[0])+len(mat[0])), "┐", sep="")
    for i in range(len(mat)):
        print("│", end="")
        for j in range(len(mat[i])):
            print(f"{mat[i][j]:7.2f} ", end="")
        print("│")
    print("└", " "*(7*len(mat[0])+len(mat[0])), "┘", sep="")


def printRelationSet(mat: list) -> None:
    size = len(mat)
    relation = []
    for i in range(size):
        for j in range(size):
            if mat[i][j] == 1:
                relation.append((i+1, j+1))
    print("관계 R =", relation)


if __name__ == "__main__":
    main()
