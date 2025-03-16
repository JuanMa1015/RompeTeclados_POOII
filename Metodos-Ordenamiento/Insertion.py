def insertion_sort(arr, key, ascending=True):
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

    # Ordenar los datos filtrados
    for i in range(1, len(filtered_data)):
        current = filtered_data[i]
        j = i - 1
        while j >= 0 and ((filtered_data[j][key] > current[key]) if ascending else (filtered_data[j][key] < current[key])):
            filtered_data[j + 1] = filtered_data[j]
            j -= 1
        filtered_data[j + 1] = current

    return filtered_data