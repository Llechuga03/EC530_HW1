#Function that converts dms format to decimal format for ease of use
def dms_to_decimal(dms):
    dms = dms.replace("°", " ").replace("'", " ").replace("\"", " ")
    parts = dms.split()

    if len(parts) < 2:
        return None #Invalid format
    
    degrees = float(parts[0])
    minutes = float(parts[1]) if len(parts) > 1 else 0
    seconds = float(parts[2]) if len(parts) > 2 else 0

    decimal = degrees + (minutes/60) + (seconds/3600)

    #Handle S/W directions
    if 'S' in dms or 'W' in dms:
        decimal *= -1

    return decimal
