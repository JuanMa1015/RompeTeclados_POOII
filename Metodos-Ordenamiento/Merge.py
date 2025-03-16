def merge_sort(arr, key, ascending=True):
    if len(arr) <= 1:
        return arr

    # Filtrar y convertir los valores a números
    filtered_data = []
    for item in arr:
        if key in item:
            try:
                value = float(item[key])  # Convertir a float
                filtered_data.append({**item, key: value})  # Actualizar el valor en el diccionario
            except (ValueError, TypeError):
                continue  # Ignorar elementos con valores no convertibles a float

    if not filtered_data:
        return arr  # Devolver los datos originales si no hay valores válidos

    # Dividir y ordenar recursivamente
    mid = len(filtered_data) // 2
    left = merge_sort(filtered_data[:mid], key, ascending)
    right = merge_sort(filtered_data[mid:], key, ascending)

    # Combinar los resultados
    return merge(left, right, key, ascending)

def merge(left, right, key, ascending):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if (left[i][key] < right[j][key]) if ascending else (left[i][key] > right[j][key]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result