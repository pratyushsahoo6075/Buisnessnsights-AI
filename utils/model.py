"""
utils/model.py

Machine Learning utilities for DecisionPilot AI
"""

from pathlib import Path
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split

from sklearn.linear_model import (
    LinearRegression,
    LogisticRegression
)

from sklearn.tree import (
    DecisionTreeClassifier,
    DecisionTreeRegressor
)

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

from config import (
    MODEL_DIR,
    RANDOM_STATE,
    TEST_SIZE
)

MODEL_DIR.mkdir(exist_ok=True)

# =====================================================
# Model Factory
# =====================================================

def get_model(task_type, algorithm):

    if task_type == "Classification":

        models = {

            "Logistic Regression":
                LogisticRegression(max_iter=1000),

            "Decision Tree":
                DecisionTreeClassifier(random_state=RANDOM_STATE),

            "Random Forest":
                RandomForestClassifier(random_state=RANDOM_STATE)

        }

    else:

        models = {

            "Linear Regression":
                LinearRegression(),

            "Decision Tree":
                DecisionTreeRegressor(random_state=RANDOM_STATE),

            "Random Forest":
                RandomForestRegressor(random_state=RANDOM_STATE)

        }

    return models[algorithm]

# =====================================================
# Build Pipeline
# =====================================================

def create_pipeline(df, target, algorithm, task_type):

    X = df.drop(columns=[target])

    y = df[target]

    numeric = X.select_dtypes(include="number").columns

    categorical = X.select_dtypes(exclude="number").columns

    numeric_pipeline = Pipeline(

        [

            ("imputer", SimpleImputer(strategy="median"))

        ]

    )

    categorical_pipeline = Pipeline(

        [

            ("imputer", SimpleImputer(strategy="most_frequent")),

            ("encoder", OneHotEncoder(handle_unknown="ignore"))

        ]

    )

    preprocessor = ColumnTransformer(

        [

            ("num", numeric_pipeline, numeric),

            ("cat", categorical_pipeline, categorical)

        ]

    )

    model = get_model(task_type, algorithm)

    pipeline = Pipeline(

        [

            ("preprocessor", preprocessor),

            ("model", model)

        ]

    )

    return pipeline

# =====================================================
# Train
# =====================================================

def train_model(df, target, algorithm, task_type):

    X = df.drop(columns=[target])

    y = df[target]

    pipeline = create_pipeline(
        df,
        target,
        algorithm,
        task_type
    )

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=TEST_SIZE,

        random_state=RANDOM_STATE

    )

    pipeline.fit(
        X_train,
        y_train
    )

    predictions = pipeline.predict(X_test)

    if task_type == "Classification":

        metrics = {

            "Accuracy":
                accuracy_score(y_test, predictions),

            "Precision":
                precision_score(
                    y_test,
                    predictions,
                    average="weighted",
                    zero_division=0
                ),

            "Recall":
                recall_score(
                    y_test,
                    predictions,
                    average="weighted",
                    zero_division=0
                ),

            "F1 Score":
                f1_score(
                    y_test,
                    predictions,
                    average="weighted",
                    zero_division=0
                )

        }

    else:

        metrics = {

            "R²":
                r2_score(
                    y_test,
                    predictions
                ),

            "MAE":
                mean_absolute_error(
                    y_test,
                    predictions
                ),

            "RMSE":
                mean_squared_error(
                    y_test,
                    predictions
                ) ** 0.5

        }

    joblib.dump(
        pipeline,
        MODEL_DIR / "trained_model.pkl"
    )

    return pipeline, metrics

# =====================================================
# Prediction
# =====================================================

def predict(model, dataframe):

    return model.predict(dataframe)

# =====================================================
# Load Model
# =====================================================

def load_saved_model():

    path = MODEL_DIR / "trained_model.pkl"

    if path.exists():

        return joblib.load(path)

    return None