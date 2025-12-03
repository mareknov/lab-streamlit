import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

        fig, ax = plt.subplots(figsize=(12, 5))
        ax.fill_between(distance, altitude, alpha=0.3, color='steelblue')
        ax.plot(distance, altitude, linewidth=2, color='darkblue', label='Elevation Profile')
        ax.set_xlabel('Distance (km)', fontsize=12)
        ax.set_ylabel('Altitude (m)', fontsize=12)
        ax.set_title(f'Altitude Profile - {selected_trail["Name"]}', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_ylim([start_alt - 100, peak_alt + 100])

        # Add start and end markers
        ax.plot(distance[0], altitude[0], 'go', markersize=10, label=f'Start ({int(altitude[0])}m)')
        ax.plot(distance[-1], altitude[-1], 'ro', markersize=10, label=f'Peak ({int(altitude[-1])}m)')
        ax.legend()

        st.pyplot(fig)

    except ImportError:
        st.warning("Install scipy for altitude profiles: `uv add scipy`")
        st.info(f"**Trail starts at ~{1000 + selected_idx * 50}m and climbs {selected_trail['Elevation Gain (m)']}m over {selected_trail['Length (km)']}km**")

else:
    st.info("👆 Select a trail from the table above to view its terrain profile")

# Footer
show_footer()