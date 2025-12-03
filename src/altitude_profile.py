"""
Functions for generating altitude profiles for ski touring trails
"""
import numpy as np
from scipy.ndimage import gaussian_filter1d


def generate_altitude_profile(trail_name, length_km, elevation_gain):
    """
    Generate a realistic altitude profile for a ski touring trail with ascent and descent

    Args:
        trail_name (str): Name of the trail
        length_km (float): Total length of the trail in kilometers (round trip)
        elevation_gain (int): Total elevation gain in meters

    Returns:
        tuple: (distance, altitude, start_altitude, peak_altitude)
            - distance: Array of distance points in km
            - altitude: Array of altitude values in meters
            - start_altitude: Starting altitude in meters
            - peak_altitude: Peak altitude in meters
    """
    # Number of points based on length
    num_points = int(length_km * 10)
    distance = np.linspace(0, length_km, num_points)

    # Starting altitude (typical valley start in Tatras)
    start_altitude = np.random.randint(1000, 1400)
    peak_altitude = start_altitude + elevation_gain

    # Peak position (slightly past middle to account for different ascent/descent paths)
    peak_position = 0.52  # 52% of the way through

    # Create normalized distance
    normalized_distance = distance / length_km

    # Create altitude profile with ascent and descent
    altitude = np.zeros(num_points)

    for i, norm_dist in enumerate(normalized_distance):
        if norm_dist <= peak_position:
            # Ascending phase - gradual start, steeper middle
            progress = norm_dist / peak_position
            # Use polynomial curve for realistic climbing
            climb_curve = (
                progress ** 1.6 * 0.75 +  # Main climbing curve
                progress ** 3 * 0.25  # Steeper sections
            )
            altitude[i] = start_altitude + climb_curve * elevation_gain
        else:
            # Descending phase - reverse the curve
            progress = (norm_dist - peak_position) / (1 - peak_position)
            descent_curve = 1 - (progress ** 1.4)  # Slightly different descent profile
            altitude[i] = start_altitude + descent_curve * elevation_gain

    # Add small undulations for realism
    undulations = np.sin(normalized_distance * np.pi * 8) * (elevation_gain * 0.02)
    altitude = altitude + undulations

    # Add some realistic noise/variation
    noise = np.random.normal(0, elevation_gain * 0.012, num_points)
    altitude = altitude + noise

    # Smooth the profile
    altitude = gaussian_filter1d(altitude, sigma=2.5)

    # Ensure we end close to start altitude
    altitude[-1] = start_altitude + np.random.randint(-20, 20)

    return distance, altitude, start_altitude, peak_altitude
