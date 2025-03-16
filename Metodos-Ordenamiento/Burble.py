def bubble_sort(arr, key, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Verificar si la clave existe en ambos elementos
            if key not in arr[j] or key not in arr[j + 1]:
                continue  # Ignorar elementos sin la clave

            # Obtener los valores, manejando casos donde no sean numéricos
            try:
                val_j = float(arr[j][key]) if arr[j][key] is not None else (float('-inf') if ascending else float('inf'))
                val_j_plus_1 = float(arr[j + 1][key]) if arr[j + 1][key] is not None else (float('-inf') if ascending else float('inf'))
            except (ValueError, TypeError):
                continue  # Ignorar elementos con valores no convertibles a float

            # Comparar y intercambiar si es necesario
            if (val_j > val_j_plus_1) if ascending else (val_j < val_j_plus_1):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr