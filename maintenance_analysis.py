import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


df = pd.read_csv("dataset/ai4i2020.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
df.drop(
["UDI","Product ID"],
axis=1,
inplace=True
)
print(df.head())
print(df["Machine failure"].value_counts())


sns.countplot(
x="Machine failure",
data=df
)

plt.show()
corr = df.corr(numeric_only=True)

print(corr)
# Failure Distribution
plt.figure(figsize=(6,4))
sns.countplot(x="Machine failure", data=df)
plt.title("Failure Distribution")
plt.savefig("output/failure_distribution.png")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.savefig("output/correlation_heatmap.png")
plt.show()
X = df[
[
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]
]

y = df["Machine failure"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
import joblib
joblib.dump(
    model,
    "model/random_forest_model.pkl"
)

print("Model Saved Successfully")

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("Accuracy:", accuracy)

print(classification_report(
    y_test,
    predictions
))

cm = confusion_matrix(
    y_test,
    predictions
)

print(cm)

plt.figure(figsize=(6,4))

sns.heatmap(
    cm,
    annot=True,
    fmt='d'
)

plt.title("Confusion Matrix")

plt.savefig(
    "output/confusion_matrix.png"
)

plt.show()
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)
failure_probability = probabilities[:,1]

health_score = 100 - (failure_probability * 100)
def get_priority(score):

    if score >= 80:
        return "Low"

    elif score >= 60:
        return "Medium"

    elif score >= 40:
        return "High"

    else:
        return "Critical"
priority_levels = []

for score in health_score:
    priority_levels.append(
        get_priority(score)
    ) 
def maintenance_due(priority):

    if priority == "Critical":
        return 7

    elif priority == "High":
        return 15

    elif priority == "Medium":
        return 30

    else:
        return 60    
maintenance_days = []

for p in priority_levels:
    maintenance_days.append(
        maintenance_due(p)
    )  
def recommendation(priority):

    if priority == "Critical":
        return "Inspect bearings and lubrication"

    elif priority == "High":
        return "Perform detailed inspection"

    elif priority == "Medium":
        return "Schedule preventive maintenance"

    else:
        return "Routine monitoring"      
recommendations = []

for p in priority_levels:
    recommendations.append(
        recommendation(p)
    )    
results = X_test.copy()

results["Failure Probability"] = (
    failure_probability * 100
)

results["Health Score"] = health_score

results["Priority"] = priority_levels

results["Maintenance Due (Days)"] = maintenance_days

results["Recommendation"] = recommendations    
print(results.head())
results.to_csv(
    "output/maintenance_results.csv",
    index=False
)