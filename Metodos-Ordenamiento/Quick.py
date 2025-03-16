def quick_sort(arr, key, ascending=True):
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

    # Elegir el pivote
    pivot = filtered_data[len(filtered_data) // 2][key]

    # Dividir los datos en left, middle y right
    left = [x for x in filtered_data if x[key] < pivot]
    middle = [x for x in filtered_data if x[key] == pivot]
    right = [x for x in filtered_data if x[key] > pivot]

    # Ordenar recursivamente y combinar los resultados
    if ascending:
        return quick_sort(left, key, ascending) + middle + quick_sort(right, key, ascending)
    else:
        return quick_sort(right, key, ascending) + middle + quick_sort(left, key, ascending)