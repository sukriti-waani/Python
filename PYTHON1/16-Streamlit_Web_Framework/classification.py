import streamlit as st                      # Import Streamlit for building web app
import pandas as pd                        # Import pandas for data handling
from sklearn.datasets import load_iris     # Import Iris dataset
from sklearn.ensemble import RandomForestClassifier  # Import Random Forest model


@st.cache_data   # Cache data to avoid reloading every time
def load_data():
    iris = load_iris()   # Load Iris dataset
    df = pd.DataFrame(iris.data, columns=iris.feature_names)  # Create DataFrame with features
    df['species'] = iris.target   # Add target (species) column
    return df, iris.target_names   # Return DataFrame and species names


df, target_names = load_data()   # Load and unpack dataset and labels


model = RandomForestClassifier()  # Create Random Forest classifier
model.fit(df.iloc[:, :-1], df['species'])  # Train model using features and target


st.sidebar.title("Input Features")  # Sidebar title for user inputs

sepal_length = st.slider(   # Slider for sepal length input
    "Sepal length",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max())
)

sepal_width = st.slider(   # Slider for sepal width input
    "Sepal width",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max())
)

petal_length = st.slider(   # Slider for petal length input
    "Petal length",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max())
)

petal_width = st.slider(  # Slider for petal width input
    "Petal width",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max())
)


input_data = [[   # Combine inputs into model-compatible format
    sepal_length, sepal_width,
    petal_length, petal_width
]]


prediction = model.predict(input_data)   # Predict species using trained model
predicted_species = target_names[prediction[0]]  # Map prediction to species name


st.write("Prediction")   # Display prediction heading
st.write(f"The predicted species is: {predicted_species}")  # Show predicted species
