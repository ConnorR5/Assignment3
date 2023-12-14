import pandas as pd
import numpy as np

# read from processed_sales
file_path = 'processed_sales.csv'
real_estate_data = pd.read_csv(file_path)

# used numpy array because processing the first time took 30 mins
property_1 = np.array([425000, 600000])
property_2 = np.array([800000, 1200000])
property_3 = np.array([2300000, 3000000])

property_1_type = 'Single Family'
property_2_type = 'Two Family'
property_3_type = 'Three Family'

# adjusted Euclidean distance calculation with type matching
# GPT helped me with adding the type matching in a previous version subtracting 1 was enough to influence results, but now not so much
real_estate_data['Property 1 Similarity'] = np.linalg.norm(
    real_estate_data[['Assessed Value', 'Sale Amount']].values - property_1, axis=1) - \
    real_estate_data['Residential Type'].eq(property_1_type).astype(int)

real_estate_data['Property 2 Similarity'] = np.linalg.norm(
    real_estate_data[['Assessed Value', 'Sale Amount']].values - property_2, axis=1) - \
    real_estate_data['Residential Type'].eq(property_2_type).astype(int)

real_estate_data['Property 3 Similarity'] = np.linalg.norm(
    real_estate_data[['Assessed Value', 'Sale Amount']].values - property_3, axis=1) - \
    real_estate_data['Residential Type'].eq(property_3_type).astype(int)

real_estate_data.to_csv('processed_and_updated_sales.csv', index=False)