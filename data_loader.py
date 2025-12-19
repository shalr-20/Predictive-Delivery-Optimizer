def load_and_merge_all_data(data_path='data/'):
    data_frames = {}
    # Load each CSV
    data_frames['orders'] = pd.read_csv(f'{data_path}orders.csv')
    data_frames['delivery'] = pd.read_csv(f'{data_path}delivery_performance.csv')
    data_frames['routes'] = pd.read_csv(f'{data_path}routes_distance.csv')
    # ... load other files (vehicle_fleet.csv, warehouse_inventory.csv, etc.)

    # Merge dataframes step by step
    merged_data = pd.merge(data_frames['orders'], data_frames['delivery'], on='order_id', how='left')
    merged_data = pd.merge(merged_data, data_frames['routes'], on='order_id', how='left')
    # ... continue merging with other datasets
    return merged_data