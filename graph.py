import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
})

# Create a line plot of the data
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Sample Line Plot')

# Display the plot in Streamlit
st.pyplot(fig)

