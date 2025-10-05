def inputMat():
    while True:
        try:
            n = int(input("정방행렬 n x n에서 n의 크기 입력: "))
            if n <= 0:
                print("오류: n은 양수여야 합니다.\n다시 시도하세요.")
                continue

            mat = []
            for i in range(n):
                row = input(f"{i+1}번째 행 입력: ").split()
                if len(row) != n:
                    raise ValueError(f"{n}개의 숫자를 입력해야 합니다.")
                mat.append(list(map(float, row)))
            return mat  # 필요하다면 반환
        except ValueError as e:
            print(f"오류: {e}\n다시 시도하세요.")
        except Exception as e:
            print(f"예상치 못한 오류: {e}\n다시 시도하세요.")


def printMat(mat, name):
    print(f"{name}행렬은 다음과 같습니다:")
    print("┌", " "*(7*len(mat[0])+len(mat[0])), "┐", sep="")
    for i in range(len(mat)):
        print("│", end="")
        for j in range(len(mat[i])):
            print(f"{mat[i][j]:7.2f} ", end="")
        print("│")
    print("└", " "*(7*len(mat[0])+len(mat[0])), "┘", sep="")


def isEqualMat(mat1, mat2):
    n = len(mat1)
    m = len(mat1[0])
    eps = 1e-8
    for i in range(n):
        for j in range(m):
            if abs(mat1[i][j] - mat2[i][j]) > eps:
                return False
    return True


def isInverse(mat):
    det = getDeterminant(mat)
    eps = 1e-8
    if abs(det) < eps:
        print("오류: 해당 행렬은 행렬식 값이 0 이므로 역행렬 계산이 불가능합니다.")
        return False
    return True


def isOrthogonal(mat):
    n = len(mat)
    eps = 1e-8
    at = getTranspose(mat)
    ata = matMul(at, mat)
    for i in range(n):
        for j in range(n):
            target = 1.0 if i == j else 0.0
            if abs(ata[i][j] - target) > eps:
                return False
    return True


def getMinor(mat, i, j):
    n = len(mat[0])
    new = []
    for k in range(n):
        if k != i:
            row = []
            for l in range(n):
                if l != j:
                    row.append(mat[k][l])
            new.append(row)
    return new
        

def getDeterminant(mat):
    n = len(mat[0])
    if n == 1:
        return mat[0][0]
    elif n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    else:
        det = 0
        for i in range(n):
            det += mat[0][i] * ((-1)**i) * getDeterminant(getMinor(mat, 0, i))
        return det


def getTranspose(mat):
    n = len(mat[0])
    new = [[mat[i][j] for i in range(n)] for j in range(n)]
    return new


def getCofactor(mat):
    n = len(mat[0])
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[mat[1][1], -mat[1][0]], [-mat[0][1], mat[0][0]]]
    else:
        new = []
        for i in range(n):
            row = []
            for j in range(n):
                factor = ((-1)**(i+j)) * getDeterminant(getMinor(mat, i, j))
                row.append(factor)
            new.append(row)
        return new


def getInverseWithDet(mat):
    if not isInverse(mat):
        return
    det = getDeterminant(mat)
    print(f"행렬식 값: {det}")
    temp = (1/det)
    cof = getCofactor(mat)
    trans = getTranspose(cof)
    n = len(trans[0])
    inverse = [[temp * trans[i][j] for j in range(n)] for i in range(n)]
    return inverse


def getInverseWithGJE(mat):
    n = len(mat[0])
    augmented = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(mat[i][j])
        for j in range(n):
            row.append(1.0 if i == j else 0.0)
        augmented.append(row)

    for col in range(n):
        pivot_row = col
        eps = 1e-8
        # 1) 피벗 찾기
        if abs(augmented[pivot_row][col]) < eps:
            found = False
            for row in range(col + 1, n):
                if abs(augmented[row][col]) > eps:
                    pivot_row = row
                    found = True
                    break
            if not found:
                print("오류: 해당 행렬은 역행렬 계산이 불가능합니다.")
                return

        # 2) 필요 시 행 교환
        if pivot_row != col:
            augmented[col], augmented[pivot_row] = augmented[pivot_row], augmented[col]

        # 3) 피벗을 1로
        pivot = augmented[col][col]
        if abs(pivot) < eps:
            print("오류: 해당 행렬은 역행렬 계산이 불가능합니다.")
            return
        for j in range(2 * n):
            augmented[col][j] /= pivot

        # 4) 피벗 열의 다른 행들을 0으로
        for row in range(n):
            if row == col:
                continue
            factor = augmented[row][col]
            if abs(factor) < eps:
                continue
            for j in range(2 * n):
                augmented[row][j] -= factor * augmented[col][j]

    inverse = []
    for i in range(n):
        row = []
        for j in range(n, 2 * n):
            row.append(augmented[i][j])
        inverse.append(row)

    return inverse


def matMul(A, B):
    n, m, p = len(A), len(A[0]), len(B[0])
    new = []
    for i in range(n):
        row = []
        for j in range(p):
            s = 0.0
            for k in range(m):
                s += A[i][k] * B[k][j]
            row.append(s)
        new.append(row)
    return new


if __name__ == "__main__":
    while True:
        mat = inputMat()
        printMat(mat, "입력한 ")
        if isInverse(mat):
            inv1 = getInverseWithDet(mat)
            inv2 = getInverseWithGJE(mat)
            printMat(inv1, "행렬식을 이용한 역")
            printMat(inv2, "가우스-조던 소거법을 이용한 역")
            if isEqualMat(inv1, inv2):
                print("두 방법으로 계산한 두 역행렬의 결과는 같습니다.")
            else:
                print("두 방법으로 계산한 두 역행렬의 결과는 다릅니다.")
        print()
        printMat(getTranspose(mat), "전치")
        if isOrthogonal(mat):
            print("(A^T A ≈ I) 입력한 행렬은 직교행렬입니다.")
        else:
            print("(A^T A !≈ I) 입력한 행렬은 직교행렬이 아닙니다.")
        print()
