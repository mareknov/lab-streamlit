"""
Functions for generating altitude profiles for ski touring trails
"""
import numpy as np
from scipy.ndimage import gaussian_filter1d


def generate_altitude_profile(trail_name, length_km, elevation_gain):
    """
    Generate a realistic altitude profile for a trail

    Args:
        trail_name (str): Name of the trail
        length_km (float): Length of the trail in kilometers
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

    # Create a realistic climbing profile
    # Most trails have gradual start, steeper middle, and final push to summit
    normalized_distance = distance / length_km

    # Use combination of polynomial and sine for realistic terrain
    base_profile = (
        normalized_distance ** 1.8 * 0.7 +  # Main climbing curve
        np.sin(normalized_distance * np.pi * 2) * 0.05 +  # Small undulations
        normalized_distance ** 3 * 0.3  # Steeper finish
    )

    # Normalize and scale to actual elevation
    base_profile = base_profile / base_profile.max()
    altitude = start_altitude + base_profile * elevation_gain

    # Add some realistic noise/variation
    noise = np.random.normal(0, elevation_gain * 0.015, num_points)
    altitude = altitude + noise

    # Smooth the profile
    altitude = gaussian_filter1d(altitude, sigma=2)

    return distance, altitude, start_altitude, peak_altitude
