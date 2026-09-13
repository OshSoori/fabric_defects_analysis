import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_defect_classifier():
    # Load cleaned Silver data
    df = pd.read_csv("data/silver_inspections.csv")

    # Diagnostic check for target classes
    print("Class distribution in dataset:")
    print(df["is_defective"].value_counts())

    # One-hot encode categorical features
    X = pd.get_dummies(
        df[["fabric_type", "line_id", "gsm", "tensile_strength"]],
        drop_first=True,
    )
    y = df["is_defective"].astype(int)

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"\nModel trained successfully! Accuracy: {accuracy * 100:.2f}%")

    # Save model artifact
    joblib.dump(model, "src/defect_classifier.pkl")


if __name__ == "__main__":
    train_defect_classifier()
