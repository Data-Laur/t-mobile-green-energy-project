# ---------------------------------------------------------
# FILE: src/data_generator.py
# ---------------------------------------------------------

# 1. IMPORT THE "LANGUAGES" (LIBRARIES)
# The script needs these to understand the code below.
import pandas as pd
import numpy as np

# 2. DEFINE THE FUNCTION
def generate_5g_digital_twin(n_days=7, n_towers=5):
    """
    Generates a physics-based 5G dataset.
    Simulates: Daily traffic tides, Weekend dips, and AAU Power Consumption.
    """
    # Use 'h' for hours (pandas 2.2+ compliant)
    timestamps = pd.date_range(start='2024-01-01', periods=n_days * 24, freq='h')
    
    dfs = []
    
    for tower_id in range(1, n_towers + 1):
        # Simulate Traffic (The "Tide")
        hours = timestamps.hour
        daily_pattern = np.sin((hours - 6) * np.pi / 12) + 1  # Sine wave
        traffic_noise = np.random.normal(0, 0.2, len(timestamps))
        
        # Add Weekend Drop (Sat/Sun traffic is 80% of normal)
        is_weekend = timestamps.dayofweek >= 5
        weekend_factor = np.where(is_weekend, 0.8, 1.0)
        
        load = (daily_pattern + traffic_noise) * weekend_factor
        load = np.clip(load, 0.05, 1.0) 
        
        # Simulate Energy Physics (The "Money")
        base_static_power = 300  # Watts (Idle)
        max_dynamic_power = 1200 # Watts (Full Load)
        
        energy = base_static_power + (max_dynamic_power * load)
        
        # Add some sensor noise
        energy += np.random.normal(0, 15, len(timestamps))
        
        # Create DataFrame
        tower_df = pd.DataFrame({
            'Time': timestamps,
            'BS': f'BS_{tower_id:02d}',
            'Load': load,
            'Energy': energy,
            'Capacity': 1000, 
            'Antennas': 64
        })
        dfs.append(tower_df)
    
    return pd.concat(dfs, ignore_index=True)