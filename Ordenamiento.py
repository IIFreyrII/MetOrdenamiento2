def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    steps = []
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        steps.append(arr.copy())  # Guardar cada paso
        gap //= 2
    print("Pasos de ShellSort:", steps)
    return arr

def quick_sort(arr, steps=None):
    if steps is None:
        steps = []
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    result = quick_sort(left, steps) + middle + quick_sort(right, steps)
    steps.append(result.copy())  # Guardar cada paso
    print("Pasos de Quicksort:", steps)
    return result

def heapify(arr, n, i, steps):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, steps)
    steps.append(arr.copy())  # Guardar cada paso

def heap_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, steps)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, steps)
    print("Pasos de Heapsort:", steps)
    return arr

def counting_sort(arr, exp, steps):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(len(arr)):
        arr[i] = output[i]
    steps.append(arr.copy())  # Guardar cada paso

def radix_sort(arr):
    steps = []
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp, steps)
        exp *= 10
    print("Pasos de Radix Sort:", steps)
    return arr

# Diccionario para almacenar listas ordenadas
sorted_lists = {}

def menu():
    while True:
        print("\nSeleccione el método de ordenamiento:")
        print("1. ShellSort")
        print("2. Quicksort")
        print("3. Heapsort")
        print("4. Radix Sort")
        print("5. Ver listas guardadas")
        print("6. Salir")
        choice = int(input("Opción: "))

        if choice == 6:
            print("Saliendo...")
            break

        if choice == 5:
            print("Listas guardadas:")
            for key, value in sorted_lists.items():
                print(f"{key}: {value}")
            continue

        n = int(input("Ingrese la cantidad de números: "))
        arr = [int(input("Número: ")) for _ in range(n)]
        original_arr = arr.copy()

        if choice == 1:
            sorted_arr = shell_sort(arr)
            sorted_lists['ShellSort'] = sorted_arr.copy()
        elif choice == 2:
            sorted_arr = quick_sort(arr)
            sorted_lists['Quicksort'] = sorted_arr.copy()
        elif choice == 3:
            sorted_arr = heap_sort(arr)
            sorted_lists['Heapsort'] = sorted_arr.copy()
        elif choice == 4:
            sorted_arr = radix_sort(arr)
            sorted_lists['RadixSort'] = sorted_arr.copy()
        else:
            print("Opción no válida")
            continue

        print("Lista original:", original_arr)
        print("Lista ordenada:", sorted_arr)

menu()
