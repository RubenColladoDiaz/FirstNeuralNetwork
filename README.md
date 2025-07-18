# First Neural Network: Celsius to Fahrenheit Converter

This project demonstrates a simple neural network built with TensorFlow and Keras to convert temperatures from Celsius to Fahrenheit. It is designed as an introductory exercise in artificial intelligence and machine learning.

## Description

The script trains a neural network to learn the mathematical relationship between Celsius and Fahrenheit using a small dataset. After training, the model can predict the Fahrenheit value for any given Celsius input.

## Technologies Used

- Python 3
- TensorFlow
- NumPy
- Matplotlib

## How It Works

1. **Data Preparation:**
   - Example Celsius and Fahrenheit values are provided as training data.
2. **Model Definition:**
   - A simple neural network with one dense layer is created.
3. **Training:**
   - The model is trained using mean squared error as the loss function and Adam as the optimizer.
4. **Visualization:**
   - The loss over epochs is plotted to visualize the training process.
5. **Prediction:**
   - The trained model predicts the Fahrenheit value for a given Celsius input (e.g., 100°C).

## Usage

1. Install the required libraries:
   ```bash
   pip install tensorflow numpy matplotlib
   ```
2. Run the script:
   ```bash
   python NeuralNetwork.py
   ```

## Output

- A plot showing the loss reduction during training.
- The predicted Fahrenheit value for 100°C.
- The internal weights of the trained model.

## Aprendido de tutorial

Ringa Tech - https://www.youtube.com/watch?v=iX_on3VxZzk

## License

This project is licensed under the MIT License.
