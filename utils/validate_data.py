EXPECTED_FIELDS = [
    "365nm", "365nm_amb", "405nm", "405nm_amb", "525nm", "525nm_amb", "680nm", "680nm_amb",
    "740nm", "740nm_amb", "980nm", "980nm_amb", "1450nm", "1450nm_amb", "0nm", "0nm_amb",
    "longitude", "latitude", "tree_pos"
]

def validate_data(data):
    if not all(field in data for field in EXPECTED_FIELDS):
        return False

    if (isinstance(data["365nm"], str)):
        data["365nm"] = int(data["365nm"])
        data["365nm_amb"] = int(data["365nm_amb"])
        data["405nm"] = int(data["405nm"])
        data["405nm_amb"] = int(data["405nm_amb"])
        data["525nm"] = int(data["525nm"])
        data["525nm_amb"] = int(data["525nm_amb"])
        data["680nm"] = int(data["680nm"])
        data["680nm_amb"] = int(data["680nm_amb"])
        data["740nm"] = int(data["740nm"])
        data["740nm_amb"] = int(data["740nm_amb"])
        data["980nm"] = int(data["980nm"])
        data["980nm_amb"] = int(data["980nm_amb"])
        data["1450nm"] = int(data["1450nm"])
        data["1450nm_amb"] = int(data["1450nm_amb"])
        data["0nm"] = int(data["0nm"])
        data["0nm_amb"] = int(data["0nm_amb"])
        data["longitude"] = float(data["longitude"])
        data["latitude"] = float(data["latitude"])

    if (
        not (0 <= data["365nm"] <= 10000) or
        not (0 <= data["405nm"] <= 10000) or
        not (0 <= data["525nm"] <= 10000) or
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