// This function will be responsible for fetching the data from your API and then creating the heatmap
async function initMap() {
    const mapCenter = { lat: 0, lng: 0 }; // Center of the map for initial display
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 3, // Zoom level to show the entire globe
        center: mapCenter,
        mapTypeId: 'satellite'
    });

    try {
        // Replace 'YOUR_API_ENDPOINT_URL' with the endpoint from which you are fetching your data
        const response = await fetch('http://127.0.0.1:5000/');
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();

        const heatmapData = getHeatmapData(data);

        // Creating a heatmap layer and adding it to the map
        new google.maps.visualization.HeatmapLayer({
            data: heatmapData,
            map: map
        });
    } catch (error) {
        console.error('Could not load heatmap data:', error);
    }
}

// Converts your data to the format required by the heatmap
function getHeatmapData(data) {
    return data.map(item => {
        const averageIntensity = (item["nm_525"] + item["nm_680"] + item["nm_740"] + item["nm_980"] + item["nm_1450"]) / 5;
        return {
            location: new google.maps.LatLng(item.latitude, item.longitude),
            weight: averageIntensity
        };
    });
}

// Add this function to the global window object to be callable from the HTML script tag
window.initMap = initMap;
