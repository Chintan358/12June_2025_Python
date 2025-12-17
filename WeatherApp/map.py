from geopy.geocoders import Nominatim
import folium

# Input: location name
location_name = input("Enter location to search: ")

# Initialize geocoder
geolocator = Nominatim(user_agent="location_search_app")
location = geolocator.geocode(location_name)

if location:
    print("Location found:")
    print("Name:", location.address)
    print("Latitude:", location.latitude)
    print("Longitude:", location.longitude)

    # Create a map centered at the location
    m = folium.Map(location=[location.latitude, location.longitude], zoom_start=14)

    # Add marker
    folium.Marker(
        [location.latitude, location.longitude],
        popup=location.address,
        tooltip="Click for details"
    ).add_to(m)

    # Save map
    m.save("location_map.html")
    print("Map saved as location_map.html")
else:
    print("Location not found!")
