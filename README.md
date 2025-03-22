# VeriFace AI - Fake Face Detection

A deep learning-based web application for detecting AI-generated fake faces.

## Features

- Real-time face image analysis
- Deep learning-based classification
- User-friendly web interface
- Drag-and-drop image upload
- Confidence score visualization

## Project Structure

```
veriface-ai/
├── app.py                 # Flask application
├── model/
│   ├── train.py          # Model training script
│   ├── predict.py        # Prediction functions
│   └── veriface_model.h5 # Trained model (generated after training)
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── images/
│   │   └── upload-icon.svg
│   └── uploads/          # Temporary storage for uploaded images
├── templates/
│   └── index.html
├── dataset/              # Training dataset (not included)
│   ├── real/
│   └── fake/
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Prepare the dataset:
   - Create a `dataset` directory
   - Add real face images to `dataset/real/`
   - Add fake face images to `dataset/fake/`

4. Train the model:
   ```bash
   python model/train.py
   ```

5. Run the application:
   ```bash
   python app.py
   ```

## Dataset Structure

Organize your dataset as follows:
- `dataset/real/`: Contains real face images
- `dataset/fake/`: Contains AI-generated fake face images

Recommended dataset size:
- Training: 1400 images (700 per class)
- Testing: 600 images (300 per class)

## Model Architecture

The CNN model architecture:
- Input layer (128x128x3)
- Convolutional layers with ReLU activation
- MaxPooling layers
- Dense layers with dropout
- Binary classification output

## Performance

- Accuracy: 83.2%
- Additional metrics available after training

## License

MIT License