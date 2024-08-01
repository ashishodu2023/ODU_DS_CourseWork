import pandas as pd

# Original DataFrame
data = {
    "A": [31823, 27275, 32799, 58434, 68513, 85702, 137358, 41643, 68551, 137115, 27277, 41646, 85666, 58454, 58484, 41646, 27267],
    "P": [663, 605, 654, 981, 1015, 1107, 1365, 769, 1025, 1427, 605, 762, 1119, 965, 956, 768, 597],
    "L": [223, 220, 220, 396, 359, 428, 508, 295, 356, 519, 218, 286, 436, 392, 382, 288, 215],
    "I": [182, 158, 190, 190, 244, 257, 345, 181, 246, 337, 159, 186, 251, 196, 197, 186, 162],
    "K": [1.23, 1.39, 1.16, 2.09, 1.47, 1.66, 1.47, 1.63, 1.45, 1.54, 1.37, 1.53, 1.73, 2.0, 1.94, 1.55, 1.33],
    "Ec": [0.58, 0.69, 0.5, 0.88, 0.73, 0.8, 0.73, 0.79, 0.72, 0.76, 0.68, 0.76, 0.82, 0.87, 0.86, 0.76, 0.66],
    "C": [32274, 27604, 33087, 59309, 69406, 86542, 138093, 42233, 69684, 138970, 27611, 42074, 86305, 60280, 59456, 42225, 27575],
    "Ed": [201, 186, 204, 273, 295, 330, 418, 230, 295, 418, 186, 230, 330, 273, 273, 230, 186],
    "Class": ["SEKER", "DERMASON", "SEKER", "HOROZ", "BARBUNYA", "CALI", "BOMBAY", "SIRA", "BARBUNYA", "BOMBAY", "DERMASON", "SIRA", "CALI", "HOROZ", "HOROZ", "SIRA", "DERMASON"]
}

df = pd.DataFrame(data)

# Mapping for binary encoding
class_mapping = {
    "SEKER": "000",
    "DERMASON": "001",
    "HOROZ": "010",
    "BARBUNYA": "011",
    "CALI": "100",
    "BOMBAY": "101",
    "SIRA": "110"
}

# Encode "Class" column
df["Class"] = df["Class"].map(class_mapping)

print(df)