class Search:
    def sequencial_search(self, array: list, value: int) -> list | None:

        print("\nRealizando Pesquisa Sequencial...")

        c = 0
        for i in range(len(array)):
            c += 1
            print(f"Posição {i}: {array[i]}")

            if array[i] == value: return [i, c]
        return [c]
    

    def binary_search(self, array: list, value: int) -> list | None:

        print("\nRealizando Pesquisa Binária...")

        left = 0
        right = len(array) - 1
        steps = 0

        while left <= right:
            steps += 1
            middle = (left + right) // 2
            print(f"Posição {middle}: {array[middle]}")

            if array[middle] == value: return [middle, steps]
            elif array[middle] < value: left = middle + 1
            else: right = middle - 1
        return [steps]