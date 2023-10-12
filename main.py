# Normalisieren
def normalize(value, min_val1, max_val1):
    normalized_value = (value - min_val1) / (max_val1 - min_val1)
    return normalized_value


# Skalieren
def scale(normalized_value, min_val2, max_val2):
    scaled_value = normalized_value * (max_val2 - min_val2) + min_val2
    return scaled_value


# Analogwert
analog_value = -14500
min_analog = -27648
max_analog = 27648

# Normalisieren
normalized_value = normalize(analog_value, min_analog, max_analog)

# Ausgabebereich (m/s)
min_val2 = -8
max_val2 = 8

# Skalieren auf Bereich
scaled_value = scale(normalized_value, min_val2, max_val2)

# Ausgabe
print("Analogwert:", analog_value)
print("Skalierter Wert:", scaled_value, "m/s")
