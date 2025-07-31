from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
import joblib 

def train_and_eval(X_full,y):
    results={}

    highest_score={
       'model': None,
       'score': 0
}

    models = {
    'RandomForest': RandomForestClassifier(random_state=42),
    'LogisticRegression': LogisticRegression(random_state=42, max_iter=100000),
    'SVM': SVC(random_state=42),
    'KNN': KNeighborsClassifier()
}
    #splitting dataset into train and test before scaling
    X_train, X_test, y_train, y_test = train_test_split(
       X_full,
       y,
       test_size=0.2,
       random_state=42,
       stratify=y
)
     #Impute nan/missing values
    imputer = SimpleImputer(strategy='mean')
    X_train_imputed = imputer.fit_transform(X_train)
    X_test_imputed = imputer.transform(X_test)

#Train and evaluate all models (no scaling or PCA)
    for name, model in models.items():
        model.fit(X_train_imputed, y_train)
        y_pred = model.predict(X_test_imputed)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        print(f"RAW MODEL EVAL: {name}: {accuracy:.3f}")
    best_model = max(results, key=results.get)
    if results[best_model] > highest_score["score"]:
        highest_score["score"] = results[best_model]
        highest_score["model"] = best_model
    print("")
    print(f"Best RAW Model: {best_model} with accuracy: {results[best_model]:.3f}")
    print("---------------------------------------------")
    #Scale trainig and test data
    scaler = StandardScaler(with_mean=False)  
    X_train_scaled = scaler.fit_transform(X_train_imputed) 
    X_test_scaled= scaler.transform(X_test_imputed)
    
    #convert sparse matrices to dense
    X_train_scaled_dense = X_train_scaled.toarray()  
    X_test_scaled_dense = X_test_scaled.toarray()
    
    #Train and evaluate all models with scaled data
    for name, model in models.items():
        model.fit(X_train_scaled_dense, y_train)
        y_pred = model.predict(X_test_scaled_dense)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        print(f"SCALED MODEL EVAL (DENSE): {name}: {accuracy:.3f}")
    best_model = max(results, key=results.get)
    if results[best_model] > highest_score["score"]:
        highest_score["score"] = results[best_model]
        highest_score["model"] = best_model
    print("")
    print(f"Best SCALED Model: {best_model} with accuracy: {results[best_model]:.3f}")
        
    print("---------------------------------------------")
    
    
#Apply PCA to capture 95% variance
    pca=PCA(n_components=0.95)
    X_train_pca = pca.fit_transform(X_train_scaled_dense)
    X_test_pca = pca.transform(X_test_scaled_dense)
    
    #Train and evaluate all models with scaled + PCA data
    for name, model in models.items():
        model.fit(X_train_pca, y_train)
        y_pred = model.predict(X_test_pca)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        print(f"PCA APPLIED MODEL EVAL {name}: {accuracy:.3f}")
    if results[best_model] > highest_score["score"]:
        highest_score["score"] = results[best_model]
        highest_score["model"] = best_model
    best_model = max(results, key=results.get)
    print("")
    print(f"Best PCA Model: {best_model} with accuracy: {results[best_model]:.3f}")
    print("")
    print("----------------------------------OVERALL RESULTS-----------------------------------")
    print("")
    print(f"BEST SCORING MODEL: {highest_score['model']} with accuracy: {highest_score['score']:.3f}")
    print("-----------------------------------")
    # Final Model
    best_svm = SVC(C=1, gamma='scale', kernel='rbf')
    best_svm.fit(X_train_pca, y_train)
    y_pred_final = best_svm.predict(X_test_pca)

    print("Final Model Performance:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_final):.3f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred_final))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred_final))
    
    
    model_path = 'models/svm_pca_model.joblib'
    joblib.dump(best_svm, model_path)
    print(f"\nFinal model saved to {model_path}")
    
