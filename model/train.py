import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import os
from sklearn.model_selection import train_test_split
import cv2


def create_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model


def load_data(data_dir):
    images = []
    labels = []

    # Load real faces
    real_dir = os.path.join(data_dir, 'real')
    for img_name in os.listdir(real_dir):
        img_path = os.path.join(real_dir, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (128, 128))
        images.append(img)
        labels.append(1)  # 1 for real

    # Load fake faces
    fake_dir = os.path.join(data_dir, 'fake')
    for img_name in os.listdir(fake_dir):
        img_path = os.path.join(fake_dir, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (128, 128))
        images.append(img)
        labels.append(0)  # 0 for fake

    return np.array(images), np.array(labels)


def train_model():
    # Load and preprocess data
    images, labels = load_data('dataset')

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        images, labels, test_size=0.2, random_state=42
    )

    # Normalize pixel values
    X_train = X_train.astype('float32') / 255
    X_test = X_test.astype('float32') / 255

    # Create and train model
    model = create_model()

    history = model.fit(
        X_train, y_train,
        epochs=20,
        batch_size=32,
        validation_data=(X_test, y_test)
    )

    # Save the model
    model.save('model/veriface_model.h5')

    return history


if __name__ == '__main__':
    train_model()