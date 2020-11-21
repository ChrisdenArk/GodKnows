# Nome: Gabriel Ramires TIA:42060681
def divisores(k):
    i = 1
    lista = []
    while i <= k:
        if k % i == 0:
            lista.append(i)
        i = i + 1
    return lista


def pertence(A, k):
    if k in A:
        return True
    else:
        return False


def inter(A, B):
    AinterB = [value for value in A if value in B]
    return AinterB


def main():
    m = int(input("Digite o primeiro inteiro positivo "))
    n = int(input("Digite o segundo inteiro positivo "))

    print("Divisores de", m, ":", divisores(m))
    print("Divisores de", n, ":", divisores(n))

    print("Divisores comuns:", inter(divisores(m), divisores(n)))


main()
