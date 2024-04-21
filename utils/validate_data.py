EXPECTED_FIELDS = [
    "525nm", "680nm", "740nm", "980nm", "1450nm",
    "525nm_amb", "680nm_amb", "740nm_amb", "980nm_amb", "1450nm_amb",
    "longitude", "latitude", "tree_pos"
]

def validate_data(data):
    if not all(field in data for field in EXPECTED_FIELDS):
        return False
    
    if (
        not (0 <= data["365nm"] <= 10000) or
        not (0 <= data["405nm"] <= 10000) or
        not (0 <= data["680nm"] <= 10000) or
        not (0 <= data["740nm"] <= 10000) or
        not (0 <= data["980nm"] <= 10000) or
        not (0 <= data["1450nm"] <= 10000) or
        not (0 <= data["0nm"] <= 10000) or
        not (0 <= data["365nm_amb"] <= 10000) or
        not (0 <= data["405nm_amb"] <= 10000) or
        not (0 <= data["525nm_amb"] <= 10000) or
        not (0 <= data["680nm_amb"] <= 10000) or
        not (0 <= data["740nm_amb"] <= 10000) or
        not (0 <= data["980nm_amb"] <= 10000) or
        not (0 <= data["1450nm_amb"] <= 10000) or
        not (0 <= data["0nm_amb"] <= 10000) or
        not (-180 <= data["longitude"] <= 180) or
        not (-90 <= data["latitude"] <= 90) or
        data["tree_pos"] not in ["top", "middle", "bottom"]
    ):
        return False
    
    return True