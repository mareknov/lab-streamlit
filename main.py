import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

from src.footer import show_footer
from src.trail_data import TRAILS_DATA
from src.altitude_profile import generate_altitude_profile

# Page config
st.set_page_config(page_title="Slovakia Ski Touring Trails", layout="wide")

# Title - centered
st.markdown("<h1 style='text-align: center;'>🎿 Discover Slovakia's Ski Touring Trails</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Explore the majestic Tatras and beyond</h3>", unsafe_allow_html=True)

# Display topography image - centered
try:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("assets/sk-topography.png", use_container_width=True)
except:
    st.warning("Topography image not found. Please add 'sk-topography.jpg' to the assets folder.")

st.markdown("---")

# Load trail data
df = pd.DataFrame(TRAILS_DATA)

# Display table
st.markdown("<h2 style='text-align: center;'>📊 Ski Touring Trails Overview</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><em>Click on a row to see the terrain profile</em></p>", unsafe_allow_html=True)

# Create interactive table with selection
selected_indices = st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    on_select="rerun",
    selection_mode="single-row"
)

# Display terrain profile when a trail is selected
if selected_indices and len(selected_indices.selection.rows) > 0:
    selected_idx = selected_indices.selection.rows[0]
    selected_trail = df.iloc[selected_idx]

    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center;'>🏔️ Terrain Profile: {selected_trail['Name']}</h2>", unsafe_allow_html=True)

    # Display trail details
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Mountain Range", selected_trail['Mountains'])
    with col2:
        st.metric("Length", f"{selected_trail['Length (km)']} km")
    with col3:
        st.metric("Duration", f"{selected_trail['Time (hours)']} hrs")
    with col4:
        st.metric("Elevation Gain", f"{selected_trail['Elevation Gain (m)']} m")
    with col5:
        difficulty = "Intermediate" if selected_trail['Elevation Gain (m)'] < 1000 else "Advanced"
        st.metric("Difficulty", difficulty)

    # Generate and plot altitude profile
    try:
        distance, altitude, start_alt, peak_alt = generate_altitude_profile(
            selected_trail['Name'],
            selected_trail['Length (km)'],
            selected_trail['Elevation Gain (m)']
        )

        # Find peak position
        peak_idx = altitude.argmax()

        # Prepare data for echarts
        distance_data = [round(d, 2) for d in distance.tolist()]
        altitude_data = [round(a, 1) for a in altitude.tolist()]

        # Create marker data for start, peak, and end
        markers = [
            {
                'name': f'Start ({int(altitude[0])}m)',
                'coord': [distance_data[0], altitude_data[0]],
                'itemStyle': {'color': '#52c41a'}
            },
            {
                'name': f'Peak ({int(altitude[peak_idx])}m)',
                'coord': [distance_data[peak_idx], altitude_data[peak_idx]],
                'itemStyle': {'color': '#f5222d'}
            },
            {
                'name': f'End ({int(altitude[-1])}m)',
                'coord': [distance_data[-1], altitude_data[-1]],
                'itemStyle': {'color': '#52c41a'}
            }
        ]

        # ECharts option
        option = {
            'tooltip': {
                'trigger': 'axis',
                'axisPointer': {'type': 'cross'},
                'formatter': '{b} km<br/>Altitude: {c} m'
            },
            'grid': {
                'left': '3%',
                'right': '4%',
                'bottom': '3%',
                'containLabel': True
            },
            'xAxis': {
                'type': 'category',
                'boundaryGap': False,
                'data': distance_data,
                'name': 'Distance (km)',
                'nameLocation': 'middle',
                'nameGap': 30,
                'axisLabel': {'interval': 'auto'}
            },
            'yAxis': {
                'type': 'value',
                'name': 'Altitude (m)',
                'nameLocation': 'middle',
                'nameGap': 50,
                'min': int(start_alt - 100),
                'max': int(peak_alt + 100)
            },
            'series': [
                {
                    'name': 'Altitude',
                    'type': 'line',
                    'smooth': True,
                    'symbol': 'none',
                    'lineStyle': {'width': 3, 'color': '#1890ff'},
                    'areaStyle': {
                        'color': {
                            'type': 'linear',
                            'x': 0, 'y': 0, 'x2': 0, 'y2': 1,
                            'colorStops': [
                                {'offset': 0, 'color': 'rgba(24, 144, 255, 0.4)'},
                                {'offset': 1, 'color': 'rgba(24, 144, 255, 0.1)'}
                            ]
                        }
                    },
                    'data': altitude_data,
                    'markPoint': {
                        'data': markers,
                        'symbolSize': 50,
                        'label': {
                            'show': True,
                            'position': 'top',
                            'formatter': '{b}'
                        }
                    }
                }
            ]
        }

        st_echarts(options=option, height='500px')

    except ImportError:
        st.warning("Install scipy for altitude profiles: `uv add scipy`")
        st.info(f"**Trail starts at ~{1000 + selected_idx * 50}m and climbs {selected_trail['Elevation Gain (m)']}m over {selected_trail['Length (km)']}km**")

else:
    st.info("👆 Select a trail from the table above to view its terrain profile")

# Footer
show_footer()