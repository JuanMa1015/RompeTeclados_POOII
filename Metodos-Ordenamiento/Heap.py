# def heap_sort(arr, key, ascending=True):
#     # Filtrar y convertir los valores a números
#     filtered_data = []
#     for item in arr:
#         if key in item:
#             try:
#                 value = float(item[key])  # Convertir a float
#                 filtered_data.append({**item, key: value})  # Actualizar el valor en el diccionario
#             except (ValueError, TypeError):
#                 continue  # Ignorar elementos con valores no convertibles a float

#     if not filtered_data:
#         return arr  # Devolver los datos originales si no hay valores válidos

#     def heapify(arr, n, i):
#         largest = i
#         left = 2 * i + 1
#         right = 2 * i + 2

#         if left < n and ((arr[left][key] > arr[largest][key]) if ascending else (arr[left][key] < arr[largest][key])):
#             largest = left

#         if right < n and ((arr[right][key] > arr[largest][key]) if ascending else (arr[right][key] < arr[largest][key])):
#             largest = right

#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             heapify(arr, n, largest)

#     n = len(filtered_data)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(filtered_data, n, i)

#     for i in range(n - 1, 0, -1):
#         filtered_data[i], filtered_data[0] = filtered_data[0], filtered_data[i]
#         heapify(filtered_data, i, 0)

#     return filtered_data
from SortingAlgorithm import SortingAlgorithm

class HeapSort(SortingAlgorithm):
    def sort(self, arr, key, ascending=True):
        filtered_data = []
        for item in arr:
            if key in item:
                try:
                    value = float(item[key])
                    filtered_data.append({**item, key: value})
                except (ValueError, TypeError):
                    continue

        if not filtered_data:
            return arr

        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and ((arr[left][key] > arr[largest][key]) if ascending else (arr[left][key] < arr[largest][key])):
                largest = left

            if right < n and ((arr[right][key] > arr[largest][key]) if ascending else (arr[right][key] < arr[largest][key])):
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(filtered_data)
        for i in range(n // 2 - 1, -1, -1):
            heapify(filtered_data, n, i)

        for i in range(n - 1, 0, -1):
            filtered_data[i], filtered_data[0] = filtered_data[0], filtered_data[i]
            heapify(filtered_data, i, 0)

        return filtered_data