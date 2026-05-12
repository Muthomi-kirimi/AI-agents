# MNIST DIGIT CLASSIFICATION USING TENSORFLOW

# Import libraries
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

# LOAD MNIST DATASET
# Dataset contains handwritten digits 0 - 9

(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

print("Training images shape:", x_train.shape)
print("Testing images shape:", x_test.shape)

# NORMALIZE DATA
# Convert pixel values from 0-255 to 0-1

x_train = x_train / 255.0
x_test = x_test / 255.0

# DISPLAY SAMPLE IMAGE

plt.imshow(x_train[0], cmap='gray')
plt.title(f"Label: {y_train[0]}")
plt.show()

# BUILD NEURAL NETWORK MODEL

model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# COMPILE MODEL

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# TRAIN MODEL

model.fit(x_train, y_train, epochs=5)

# EVALUATE MODEL

loss, accuracy = model.evaluate(x_test, y_test)

print("\nTest Accuracy:", accuracy)

# MAKE PREDICTIONS


predictions = model.predict(x_test)

predicted_digit = np.argmax(predictions[0])

print("Predicted Digit:", predicted_digit)
print("Actual Digit:", y_test[0])

# DISPLAY TEST IMAGE

plt.imshow(x_test[0], cmap='gray')
plt.title(f"Predicted: {predicted_digit}")
plt.show()

