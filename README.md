# Crop-Recomondation-System


A Crop Recommendation System is an application of machine learning and data science that aims to assist farmers in making informed decisions about the optimal crops to cultivate based on various factors. The system analyzes agricultural data, environmental conditions, and soil properties to provide recommendations on suitable crops for a specific region or plot of land.

This project implements a Crop Recommendation System using Machine Learning. The system takes input parameters such as Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall to predict the suitable crop for cultivation.

## Project Structure

- **app.py:** Flask application for serving the model and handling predictions.
- **templates/index.html:** HTML template for the user interface.
- **crop_recommendation_model.pkl:** Pre-trained machine learning model using scikit-learn.

## Getting Started

1. **Clone the Repository:**
     ```bash
    git clone https://github.com/your-username/crop-recommendation-system.git
    cd crop-recommendation-system
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    ```bash
    python app.py
    ```
    Open your web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to interact with the Crop Recommendation System.

## Usage

1. Enter the required parameters (N, P, K, Temperature, Humidity, pH, Rainfall) in the provided form.
2. Click the "Predict" button.
3. The predicted crop will be displayed on the webpage.

## Model Information

The machine learning model used for crop prediction is a RandomForestClassifier trained on the Crop Recommendation dataset.

## Acknowledgments

- The dataset used for training the model: [Crop Recommendation Dataset]
- Flask: [Flask Documentation](https://flask.palletsprojects.com/)
- scikit-learn: [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)

