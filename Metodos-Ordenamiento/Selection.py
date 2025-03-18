# def selection_sort(arr, key, ascending=True):
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

#     # Ordenar los datos filtrados
#     for i in range(len(filtered_data)):
#         min_idx = i
#         for j in range(i + 1, len(filtered_data)):
#             if (filtered_data[j][key] < filtered_data[min_idx][key]) if ascending else (filtered_data[j][key] > filtered_data[min_idx][key]):
#                 min_idx = j
#         filtered_data[i], filtered_data[min_idx] = filtered_data[min_idx], filtered_data[i]

#     return filtered_data
from SortingAlgorithm import SortingAlgorithm

class SelectionSort(SortingAlgorithm):
    def sort(self, arr, key, ascending=True):
        # Filtrar y convertir los valores a números
        filtered_data = []
        for item in arr:
            if key in item:
                try:
                    value = float(item[key])  # Convertir a float
                    filtered_data.append({**item, key: value})  # Actualizar el valor en el diccionario
                except (ValueError, TypeError):
                    continue  # Ignorar elementos con valores no convertibles

        if not filtered_data:
            return arr  # Devolver los datos originales si no hay valores válidos

        # Ordenar los datos filtrados
        n = len(filtered_data)
        for i in range(n):
            # Encontrar el índice del elemento mínimo (o máximo) en el resto del arreglo
            idx = i
            for j in range(i + 1, n):
                if (filtered_data[j][key] < filtered_data[idx][key]) if ascending else (filtered_data[j][key] > filtered_data[idx][key]):
                    idx = j

            # Intercambiar el elemento encontrado con el elemento en la posición actual
            filtered_data[i], filtered_data[idx] = filtered_data[idx], filtered_data[i]

        return filtered_data