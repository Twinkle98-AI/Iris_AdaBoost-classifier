🌸 Iris Flower Classification using AdaBoost
📌 Project Overview

This project demonstrates the implementation of the AdaBoost (Adaptive Boosting) algorithm to classify Iris flower species based on their physical characteristics. AdaBoost is a powerful ensemble learning technique that combines multiple weak learners to form a strong classifier and improve prediction accuracy.

The project also includes a Streamlit-based interactive frontend, allowing users to input flower measurements and get real-time predictions.

🧠 Problem Statement

Given the measurements of an Iris flower:

Sepal Length

Sepal Width

Petal Length

Petal Width

Predict the species of the flower:

Setosa

Versicolor

Virginica

🗂 Dataset

Source: Iris Dataset (UCI / Kaggle)

Samples: 150

Features: 4 numerical features

Target: Species (3 classes)

⚙️ Tech Stack

Python

Scikit-learn

AdaBoost Classifier

Decision Tree (Weak Learner)

NumPy & Pandas

Streamlit

Pickle (Model Serialization)

🏗 Model Architecture

Ensemble Method: Boosting (Sequential)

Base Estimator: Decision Tree (max_depth = 1)

Number of Estimators: 50

Learning Rate: 1.0

🚀 Features

End-to-end ML pipeline

Label encoding for categorical target

Train–test split for evaluation

Streamlit-based user interface

Real-time prediction

Production-ready serialized model (.pkl)

📊 Model Performance

Accuracy: ~86–91% (depending on base estimator)

Demonstrates improved performance through ensemble learning

🖥 Frontend Preview

The Streamlit app allows users to:

Enter flower measurements

Click Predict

Instantly view predicted Iris species

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/iris-adaboost-classifier.git
cd iris-adaboost-classifier

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run iris.py

📈 Key Learnings

Understanding ensemble learning techniques

Difference between Bagging and Boosting

Practical implementation of AdaBoost

Importance of weak learners

Model deployment using Streamlit

📌 Future Enhancements

Probability visualization

Model comparison (AdaBoost vs GBM vs XGBoost)

Hyperparameter tuning

Cloud deployment

🤝 Acknowledgements

Thanks to the open-source community and mentors for guidance and continuous learning support.

📬 Contact

Haimabati HaripriyaSahu
Aspiring Data Scientist | Machine Learning Enthusiast
