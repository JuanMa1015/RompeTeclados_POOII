#.
from Insertion import insertion_sort

def bucket_sort(arr, key, ascending=True):
    # Filtrar y convertir los valores a números
    filtered_data = []
    for item in arr:
        if key in item:
            try:
                float(item[key])  # Verificar que sea convertible a float
                filtered_data.append(item)  # Mantener el objeto original
            except (ValueError, TypeError):
                continue  # Ignorar elementos con valores no convertibles a float
    
    if not filtered_data:
        return arr  # Devolver los datos originales si no hay valores válidos
    
    # Obtener el valor máximo y mínimo
    max_val = max(float(item[key]) for item in filtered_data)
    min_val = min(float(item[key]) for item in filtered_data)
    
    # Evitar división por cero si todos los valores son iguales
    if max_val == min_val:
        return filtered_data
    
    # Crear los buckets
    num_buckets = min(len(filtered_data), 10)  # Usar un número razonable de buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribuir los elementos en los buckets
    range_val = max_val - min_val
    for item in filtered_data:
        item_val = float(item[key])
        # Calcular el índice del bucket, asegurando que esté en el rango correcto
        bucket_index = min(int(((item_val - min_val) / range_val) * (num_buckets - 1)), num_buckets - 1)
        buckets[bucket_index].append(item)
    
    # Ordenar todos los buckets individualmente
    for i in range(num_buckets):
        if buckets[i]:  # Solo ordenar si el bucket no está vacío
            buckets[i] = insertion_sort(buckets[i], key, True)  # Siempre ordenar ascendente dentro del bucket
    
    # Combinar buckets según el orden deseado
    result = []
    if ascending:
        # Orden ascendente: recorrer buckets de 0 a n-1
        for bucket in buckets:
            result.extend(bucket)
    else:
        # Orden descendente: recorrer buckets de n-1 a 0
        for bucket in reversed(buckets):
            # También invertir cada bucket individualmente
            bucket.reverse()
            result.extend(bucket)
    
    return result