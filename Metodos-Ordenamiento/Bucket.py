from Insertion import insertion_sort

def bucket_sort(arr, key, ascending=True):
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

    # Obtener el valor máximo y mínimo
    max_val = max(filtered_data, key=lambda x: x[key])[key]
    min_val = min(filtered_data, key=lambda x: x[key])[key]

    # Evitar división por cero si todos los valores son iguales
    if max_val == min_val:
        return filtered_data

    # Crear los buckets
    num_buckets = len(filtered_data)
    buckets = [[] for _ in range(num_buckets + 1)]

    # Distribuir los elementos en los buckets
    for item in filtered_data:
        # Calcular el índice del bucket
        index = int(((item[key] - min_val) / (max_val - min_val)) * num_buckets)
        if index >= len(buckets):
            index = len(buckets) - 1
        buckets[index].append(item)

    # Ordenar cada bucket
    for bucket in buckets:
        insertion_sort(bucket, key, ascending)

    # Combinar los buckets en un solo arreglo ordenado
    sorted_arr = []
    if ascending:
        for bucket in buckets:
            sorted_arr.extend(bucket)
    else:
        for bucket in reversed(buckets):
            sorted_arr.extend(bucket)

    return sorted_arr