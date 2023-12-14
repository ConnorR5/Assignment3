import pandas as pd

def preprocess_real_estate_data(file_path, output_file):
    data = pd.read_csv(file_path, low_memory=False)

    #preprocessing
    columns_to_keep = ['List Year', 'Town', 'Address', 'Assessed Value', 
                       'Sale Amount', 'Sales Ratio', 'Residential Type']
    
    data = data[columns_to_keep]
    data = data.drop_duplicates()
    data = data.dropna()

    residential_types = ['Single Family', 'Two Family', 'Three Family']
    data = data[data['Residential Type'].isin(residential_types)]

    # to processed_sales.csv
    data.to_csv(output_file, index=False)

# run VVV
# preprocess_real_estate_data('Real_Estate_Sales_2001-2020_GL.csv', 'processed_sales.csv')