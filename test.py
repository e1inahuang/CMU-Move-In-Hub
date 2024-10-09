import matplotlib.pyplot as plt
import numpy as np

# Generate some random data for the histogram
data = np.random.randn(1000)

# Create the histogram using a colormap
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(airbnb_df['Price'], bins=30, edgecolor='black')

# Apply the viridis colormap to the patches (bars)
plt.cm.viridis
for i, patch in enumerate(patches):
    plt.setp(patch, 'facecolor', plt.cm.viridis(i / len(patches)))

plt.title('Price Distribution of Airbnb Listings')
plt.xlabel('Price')
plt.ylabel('Frequency')

# Step 3: Save the plot as airbnb_price.png in the static folder
plt.savefig(os.path.join(static_folder, 'airbnb_price.png'))

# Step 4: Close the plot to free up memory
plt.close()
# Save the plot as an image file
plt.savefig('static/airbnb_price.png')