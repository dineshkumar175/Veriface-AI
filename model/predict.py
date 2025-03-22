import tensorflow as tf
import numpy as np
import cv2


def load_and_prep_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))
    img = img.astype('float32') / 255
    return np.expand_dims(img, axis=0)


def predit_image(image_path):
    # Load the model
    model = tf.keras.models.load_model('model/veriface_model.h5')

    # Prepare image
    processed_image = load_and_prep_image(image_path)

    # Make prediction
    prediction = model.predict(processed_image)[0][0]

    # Convert prediction to label and probability
    label = 'Real' if prediction > 0.5 else 'Fake'
    probability = prediction if prediction > 0.5 else 1 - prediction

    return label, probability