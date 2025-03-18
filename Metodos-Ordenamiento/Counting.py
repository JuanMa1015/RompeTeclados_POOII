# def counting_sort(arr, key, ascending=True):
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

#     # Obtener el valor máximo y mínimo
#     max_val = max(filtered_data, key=lambda x: x[key])[key]
#     min_val = min(filtered_data, key=lambda x: x[key])[key]
#     range_val = int(max_val - min_val + 1)

#     # Inicializar el arreglo de conteo
#     count = [0] * range_val
#     output = [0] * len(filtered_data)

#     # Contar la frecuencia de cada valor
#     for item in filtered_data:
#         count[int(item[key] - min_val)] += 1

#     # Acumular los conteos
#     for i in range(1, len(count)):
#         count[i] += count[i - 1]

#     # Construir el arreglo de salida
#     for item in reversed(filtered_data):
#         output[count[int(item[key] - min_val)] - 1] = item
#         count[int(item[key] - min_val)] -= 1

#     # Invertir el orden si es descendente
#     if not ascending:
#         output.reverse()

#     return output
from SortingAlgorithm import SortingAlgorithm

class CountingSort(SortingAlgorithm):
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

        max_val = max(filtered_data, key=lambda x: x[key])[key]
        min_val = min(filtered_data, key=lambda x: x[key])[key]
        range_val = int(max_val - min_val + 1)

        count = [0] * range_val
        output = [0] * len(filtered_data)

        for item in filtered_data:
            count[int(item[key] - min_val)] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for item in reversed(filtered_data):
            output[count[int(item[key] - min_val)] - 1] = item
            count[int(item[key] - min_val)] -= 1

        if not ascending:
            output.reverse()

        return output