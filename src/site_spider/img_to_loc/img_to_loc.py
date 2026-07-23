from PIL import Image
from PIL.ExifTags import GPSTAGS

def convert_to_degrees(value):
    """Converts the GPS coordinates from DMS tuple format to decimal degrees."""
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def get_google_maps_link(image_path):
    img = Image.open(image_path)
    exif_data = img.getexif()

    if not exif_data:
        return "No metadata found."

    # Look specifically for the GPS info block (Tag ID: 34853)
    gps_info = exif_data.get_ifd(34853)

    if not gps_info:
        return "No GPS metadata found in this image."

    # Translate numeric GPS keys to readable labels (e.g., 'GPSLatitude')
    gps_data = {}
    for key, val in gps_info.items():
        label = GPSTAGS.get(key, key)
        gps_data[label] = val

    # Verify all necessary tags exist
    required_tags = ['GPSLatitude', 'GPSLatitudeRef', 'GPSLongitude', 'GPSLongitudeRef']
    if not all(tag in gps_data for tag in required_tags):
        return "Incomplete GPS data."

    # Convert values to Decimal Degrees
    lat = convert_to_degrees(gps_data['GPSLatitude'])
    if gps_data['GPSLatitudeRef'] != 'N':
        lat = -lat  # Make negative for South

    lon = convert_to_degrees(gps_data['GPSLongitude'])
    if gps_data['GPSLongitudeRef'] != 'E':
        lon = -lon  # Make negative for West

        # Format the Google Maps URL
    maps_url = f"https://google.com {lat},{lon}/"
    return maps_url

print(get_google_maps_link("test1.jpg"))