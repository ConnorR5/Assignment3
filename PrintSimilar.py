import pandas as pd

# Load the updated CSV file
file_path = 'processed_and_updated_sales.csv'  # Update with your file path
real_estate_data = pd.read_csv(file_path)

# Function to print top 10 similar properties for a given property
def print_top_similar_properties(property_similarity_column):
    # Sort by the similarity column
    top_similar = real_estate_data.sort_values(by=property_similarity_column, ascending=True).head(10)
    # Print Address, Town, and Year
    for index, row in top_similar.iterrows():
        print(f"{row['Address']} - {row['Town']} - {row['List Year']}")

# Print top 10 similar properties for Property 1
print("Top 10 Similar Properties for Property 1:")
print_top_similar_properties('Property 1 Similarity')

# Print top 10 similar properties for Property 2
print("\nTop 10 Similar Properties for Property 2:")
print_top_similar_properties('Property 2 Similarity')

# Print top 10 similar properties for Property 3
print("\nTop 10 Similar Properties for Property 3:")
print_top_similar_properties('Property 3 Similarity')
