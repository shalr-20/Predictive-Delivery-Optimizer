def calculate_risk_score(row, weights):
    score = 0
    score += weights['priority'] * (row['priority'] == 'Express')
    score += weights['traffic'] * (row['traffic_delay_hours'] > 2)
    score += weights['weather'] * (row['weather_impact'] != 'None')
    score += weights['distance'] * (row['distance_km'] > 500)
    score += weights['carrier_history'] * (row['carrier_avg_delay'] > 0.5) # New factor
    score += weights['time_of_day'] * (row['hour_of_day'] in [8, 9, 10, 17, 18]) # New factor
    return min(score, 1.0) # Cap at 1.0

# Placeholder structure for external data
def get_live_traffic(origin, destination):
    return np.random.uniform(0, 3)

def get_weather_forecast(location):
    return np.random.choice(['Clear', 'Rain', 'Storm'])