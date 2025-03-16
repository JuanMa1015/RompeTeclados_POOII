def radix_sort(arr, key, ascending=True):
    # Filtrar y convertir los valores a números
    filtered_data = []
    for item in arr:
        if key in item:
            try:
                value = int(float(item[key]))  # Convertir a entero
                filtered_data.append({**item, key: value})  # Actualizar el valor en el diccionario
            except (ValueError, TypeError):
                continue  # Ignorar elementos con valores no convertibles

    if not filtered_data:
        return arr  # Devolver los datos originales si no hay valores válidos

    # Obtener el valor máximo
    max_val = max(filtered_data, key=lambda x: x[key])[key]

    # Ordenar por cada dígito
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(filtered_data, key, exp, ascending)
        exp *= 10

    return filtered_data

def counting_sort_by_digit(arr, key, exp, ascending):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Contar la frecuencia de cada dígito
    for i in range(n):
        index = (arr[i][key] // exp) % 10
        count[index] += 1

    # Acumular los conteos
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el arreglo de salida
    i = n - 1
    while i >= 0:
        index = (arr[i][key] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiar el arreglo de salida al arreglo original
    for i in range(n):
        arr[i] = output[i]

    # Invertir el orden si es descendente
    if not ascending:
        arr.reverse()