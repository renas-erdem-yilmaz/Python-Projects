# AI Support Ticket Classifier

A simple machine learning project that classifies support messages into different categories using TF-IDF and Logistic Regression.

## Categories

The model can classify messages as:

- Billing
- Technical
- Feature Request
- General Question

## How It Works

The project follows a basic NLP machine learning pipeline:

1. Support messages are loaded from a CSV dataset.
2. The dataset is split into training and testing sets.
3. TF-IDF converts text into numerical features.
4. Logistic Regression learns patterns between words and ticket categories.
5. The model predicts the category of new support messages.
6. A confidence score is shown for each prediction.

If the model's confidence is below 45%, the prediction is marked as uncertain.

## Example

```text
Enter a support message: I paid for Pro but my account still says Free

Prediction: billing
Confidence: 63.42 %
```

## Project Structure

```text
ai-support-ticket-classifier/
├── main.py
├── tickets.csv
├── requirements.txt
└── README.md
```

## Installation

Clone the repository and install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

Run the project with:

```bash
python main.py
```

The program will first display the model's test accuracy and some learned features.

You can then enter your own support messages for classification.

Type:

```text
exit
```

to stop the program.

## Technologies

- Python
- pandas
- scikit-learn
- TF-IDF
- Logistic Regression

## What I Learned

Through this project, I practiced:

- Working with datasets using pandas
- Splitting data into training and testing sets
- Converting text into numerical features with TF-IDF
- Training a classification model with Logistic Regression
- Evaluating model accuracy
- Working with prediction probabilities and confidence scores
- Inspecting which features influence model predictions

## Limitations

The dataset used in this project is intentionally small, so the model is designed primarily as a learning project rather than a production-ready classifier.

Its performance could be improved by using a larger and more diverse dataset, better preprocessing, and more advanced NLP models.