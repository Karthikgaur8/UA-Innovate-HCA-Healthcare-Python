
# HCA Healthcare Facilities Interactive Map

## Project Overview
This interactive map visualizes over 250 HCA Healthcare facilities across the continental United States, including Alaska and Hawaii as insets. Designed for HCA employees, it serves as a powerful tool for geographically searching and filtering facilities based on various demographic criteria. By integrating different technologies, this project provides an intuitive user interface to explore facility locations with detailed information.

## Features & Functionality

### Interactive Map Visualization
- **Geographical Coverage**: Displays all HCA facilities in the continental US with Alaska and Hawaii included as insets to provide comprehensive coverage.
- **Facility Type Differentiation**: Utilizes unique icons (circle, square, star, triangle, etc.) to represent different facility types, enhancing visual distinction and user experience.

### Detailed Facility Information
- **Hover-Over Tooltips**: Hovering over facility icons reveals essential information like the facility name, division, and state, offering quick insights without additional clicks.
- **Information Panel**: Clicking on a facility icon populates a side panel with extensive demographic details including the facility's name, COID, address, division, time zone, and EMR (Electronic Medical Record system), facilitating detailed analysis at a glance.

### Advanced Interaction & Filtering
- **Zoom & Detail Viewing**: Supports zooming into specific geographic areas, enabling users to explore facilities in densely populated regions with high precision.
- **Dynamic Facility Filtering**: Features the ability to apply filters based on facility demographics such as address, state or zip code, division, time zone, and EMR system, allowing for customized viewing and analysis tailored to user needs.

### Clustering & Icon Separation (Stretch Goal)
- **Icon Clustering**: Addresses the challenge of visualizing closely located facilities by implementing an icon clustering solution. This ensures that each facility, regardless of its proximity to others, is individually selectable without the need for excessive zooming.
- **Separation for Clarity**: In regions with high facility density, such as Florida, the map innovatively separates facility icons that would otherwise overlap, placing some in adjacent water bodies for clarity while maintaining interactive functionality.

## Technology Stack
- **Python**: Backbone of the project for data processing and map generation.
- **Folium**: Leverages this library to create the interactive map, providing a user-friendly interface and seamless integration with Python.
- **Pandas**: Empowers data manipulation and cleaning, ensuring accurate and efficient handling of facility demographics.
- **MarkerCluster (Folium Plugin)**: Enhances the map with clustering capabilities, crucial for managing the visualization of closely spaced facilities.

## Contributing
Your contributions can help make the HCA Healthcare Facilities Interactive Map even better! Whether it's adding new features, improving existing ones, or suggesting enhancements, we'd love to see your ideas. Please feel free to fork the repository, submit pull requests, or open issues with your feedback.


---
