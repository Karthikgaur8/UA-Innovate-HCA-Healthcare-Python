import pandas as pd
import folium
from folium import IFrame
import os
# Import the plugin
from folium.plugins import MarkerCluster
 
# Load facility data from Excel file
df = pd.read_csv('C:/PyProject/UA Innovate-HCA Healthcare/output.csv')
 
# Create a map centered on the continental US
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4, min_zoom=4, max_zoom=8, zoom_control=False)
 
# Create a function to generate HTML content for popup
def generate_popup(row):
    popup_html = "<h4>Facility Demographics</h4>"
    for col, val in row.items():
        popup_html += f"<b>{col}:</b> {val}<br>"
    return popup_html
 
# Create a MarkerCluster object
marker_cluster = MarkerCluster().add_to(m)
 
# Iterate over rows in DataFrame and add CircleMarkers to the marker cluster
for index, row in df.iterrows():
    # Create HTML content for popup
    popup_content = generate_popup(row)
   
    # Create iframe for popup
    popup = folium.Popup(IFrame(html=popup_content, width=300, height=200), max_width=300)
   
    # Add CircleMarker with popup to the marker cluster
    folium.CircleMarker(location=[row['latitude'], row['longitude']],
                        radius=5,  # Adjust radius as needed
                        popup=popup,
                        tooltip=row['facility_name'],
                        color='blue',  # Change circle color if needed
                        fill=True,
                        fill_color='blue'  # Change fill color if needed
                       ).add_to(marker_cluster)
 
# Save the map as an HTML file
directory = 'C:/PyProject/UA Innovate-HCA Healthcare'
m.save(os.path.join(directory, 'mapa.html'))
 
# Display the map
m
 