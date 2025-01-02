# Values-in-a-Matrix Sort Function
# Funcióm para Acomodo de Valores en una Matriz
def read_intensity_file(filename):
    data = []
    with open(filename, 'r') as file:
        for _ in range(64):
            layer = []
            for _ in range(64):
                line = file.readline()
                pixel_values = [float(value) / 2 for value in line.split()]
                layer.append(pixel_values)
            data.append(layer)
    return data

# Read .txt file that contains the values (each one in a line)
# Leer archivo .txt que contiene los valores (un valor por línea)
filename = "Path to file / Ruta del archivo"
intensity_data = read_intensity_file(filename)

# Validate the matriz structure
# Validar la estructura de la matriz
print("Dimensiones de la matriz: ", len(intensity_data), "x", len(intensity_data[0]), "x", len(intensity_data[0][0]))