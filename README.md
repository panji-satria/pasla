# pasla

**A powerful and flexible framework for deep learning and machine learning projects.**
Pasla is a Python framework that provides various functionalities for processing data, building machine learning models, and tensor operations. This framework is designed to facilitate the development and implementation of data-driven solutions.

## Extended Description

pasla is a versatile and powerful framework designed to streamline the development of deep learning and machine learning projects. With a focus on simplicity and flexibility, pasla offers a range of features that cater to both novice and experienced users.

### Key Features

- **Tensor Operations:** Efficiently manipulate and preprocess data using fundamental tensor operations with the `tensor_operations.py` module.
- **Model Training:** Train machine learning models effortlessly, with support for random forest classifiers and neural networks using the `model_training.py` module.
- **Data Pre-processing:** Normalize and preprocess data for machine learning models using standard techniques.

#### Random Forest Classifier

```python
import pasla.model_training as mt

# Load data
data = mt.load_data("my_dataset.csv")
features, labels = mt.extract_features_labels(data)

# Train a random forest classifier
rf_model, accuracy = mt.train_random_forest_classifier(features, labels)

# Save the trained model
mt.save_model(rf_model, "random_forest_model.pkl")

## Installation
To install pasla, run the following command:

``` party w/me bash
pip install pasla

## Table of Contents

- [About the Project](#about-the-project)
- [Tensor Operations](#tensor-operations)
- [Model Training](#model-training)
- [Usage](#usage)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## About the Project

Pasla is an open-source framework designed to facilitate deep learning and machine learning tasks. It provides modules for tensor operations, model training, and other essential functionalities.

## Tensor Operations

The `tensor_operations.py` module includes functions for fundamental tensor operations required for data manipulation and preprocessing in machine learning.

## Model Training

The `model_training.py` module is dedicated to training machine learning models and includes functionalities for both random forest classifiers and neural networks. It also provides evaluation metrics and visualization tools.

### Random Forest Classifier

#### Training

```python
import pasla.model_training as mt

# Load data
data = mt.load_data("my_dataset.csv")
features, labels = mt.extract_features_labels(data)

# Train a random forest classifier
rf_model, accuracy = mt.train_random_forest_classifier(features, labels)

# Save the trained model
mt.save_model(rf_model, "random_forest_model.pkl")

# Load the trained model
loaded_rf_model = mt.load_model("random_forest_model.pkl")

# Evaluate the model on test data
test_data = mt.load_data("test_dataset.csv")
test_features, test_labels = mt.extract_features_labels(test_data)
test_accuracy = mt.evaluate_model(loaded_rf_model, test_features, test_labels)
print(f"Random Forest Model Accuracy: {test_accuracy}")

# Train a neural network
nn_model, history = mt.train_neural_network(features, labels, epochs=10)

# Save the trained model weights
mt.save_model_weights(nn_model, "neural_network_weights.h5")

# Save training history to a CSV file
mt.save_history(history, "neural_network_training_history.csv")

# Load the trained neural network model
loaded_nn_model = mt.load_neural_network_model("neural_network_weights.h5")

# Evaluate the model on test data
nn_test_accuracy, nn_auc_score = mt.evaluate_neural_network(loaded_nn_model, test_features, test_labels)
print(f"Neural Network Model Accuracy: {nn_test_accuracy}")
print(f"Neural Network Model AUC Score: {nn_auc_score}")

# Plot ROC curve for the neural network
mt.plot_roc_curve(loaded_nn_model, test_features, test_labels)

# Plot loss curve from training history
mt.plot_loss_curve(history)

# Plot confusion matrix for the neural network
mt.plot_confusion_matrix(loaded_nn_model, test_features, test_labels)
# Generate and plot feature importance for a random forest model
mt.plot_feature_importance(rf_model, features.columns)

# Generate feature importance table
feature_importance_df = mt.feature_importance_table(rf_model, features.columns)
print(feature_importance_df)


### Example Usage

```python
import pasla.tensor_operations as to

import pasla.model_training as mt

# Load data
data = mt.load_data("my_dataset.csv")
features, labels = mt.extract_features_labels(data)

# Train a random forest classifier
rf_model, accuracy = mt.train_random_forest_classifier(features, labels)

# Save the trained model
mt.save_model(rf_model, "random_forest_model.pkl")

# Load the trained model
loaded_rf_model = mt.load_model("random_forest_model.pkl")

# Evaluate the model on test data
test_data = mt.load_data("test_dataset.csv")
test_features, test_labels = mt.extract_features_labels(test_data)
test_accuracy = mt.evaluate_model(loaded_rf_model, test_features, test_labels)
print(f"Random Forest Model Accuracy: {test_accuracy}")

import pasla.tensor_operations as to

# Create a tensor
tensor_data = to.create_tensor([1, 2, 3, 4, 5])

# Perform tensor operations (contoh: mean)
tensor_mean = to.mean(tensor_data)
print(f"Mean of Tensor: {tensor_mean}")

# Example tensor operations
data = to.load_data("my_dataset.csv")
features, labels = to.extract_features_labels(data)t
normalized_data = to.normalize_data(features)

# core/tensor_operations.py

The `tensor_operations.py` module provides functionality for tensor operations and data pre-processing before machine learning models. Following is the functionality provided:

## Data Pre-processing

### `preprocess_data(data)`

This function pre-processes the data to model machine learning by normalizing it using `StandardScaler`.

Usage Example:

``` python
import pasla.tensor_operations as

# Loading data
data = to.load_data("my_dataset.csv")

# Preprocess data
scaled_data = to.preprocess_data(data)

import pasla.tensor_operations as to

# Create a tensor
tensor_data = to.create_tensor([1, 2, 3, 4, 5])


