# # 🚀 End-to-End MLOps Project: Medical Insurance Cost Prediction

## 📌 **Project Overview**
This project demonstrates a complete **MLOps pipeline** using **ZenML, MLflow, Docker, GitHub, and AWS** to develop, deploy, and monitor a regression model for predicting **medical insurance costs** based on patient attributes.

## 🏗 **Tech Stack**
- **Machine Learning**: Scikit-learn, XGBoost
- **MLOps Tools**: ZenML, MLflow
- **Cloud & Deployment**: AWS (S3, EC2, Lambda)
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Logging & Exception Handling**: Custom Scripts

## 📊 **Dataset**
- **Source**: [Kaggle - Medical Insurance Cost](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Features**:
  - `age`: Age of the patient
  - `sex`: Gender (Male/Female)
  - `bmi`: Body Mass Index
  - `children`: Number of dependents
  - `smoker`: Whether the patient is a smoker (Yes/No)
  - `region`: Geographical region
  - `charges`: **(Target variable)** Insurance cost

## 🛠 **Project Structure**
```
📂 mlops-project
│── 📂 data              # Data storage (raw, processed, train/test splits)
│── 📂 src               # Source code
│   ├── 📂 components   # ML pipeline components
│   ├── 📂 pipelines    # ZenML pipelines (training, inference)
│   ├── 📂 utils        # Logger, exception handling
│── 📂 models           # Trained model storage
│── 📂 docker           # Docker files
│── 📂 config           # Configuration files
│── 📂 tests            # Unit and integration tests
│── 📂 docs             # Project documentation
│── .gitignore
│── README.md
│── requirements.txt
│── zenml_config.yaml
│── mlflow_config.yaml
│── docker-compose.yaml
```

## 🏁 **Step-by-Step Workflow**
1️⃣ **Project Setup** (GitHub, Virtual Environment, ZenML Init)  
2️⃣ **Data Ingestion & Preprocessing**  
3️⃣ **Model Training & Experiment Tracking (MLflow)**  
4️⃣ **Logging & Exception Handling**  
5️⃣ **Model Registry & Versioning**  
6️⃣ **Containerization with Docker**  
7️⃣ **CI/CD Pipeline (GitHub Actions)**  
8️⃣ **Deployment on AWS (S3, Lambda, or EC2)**  
9️⃣ **Monitoring & Retraining**  

## 🎯 **Goals of the Project**
✅ Automate the entire ML pipeline using **ZenML**  
✅ Track experiments and model versions using **MLflow**  
✅ Deploy a scalable model on **AWS**  
✅ Implement **best practices** for logging, exception handling, and CI/CD  

## 📜 **Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone <repo-url>
cd mlops-project
```
### **2️⃣ Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # (Windows)
```
### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
### **4️⃣ Initialize ZenML & MLflow**
```bash
zenml init
mlflow ui  # To start MLflow tracking
```

## 🚀 **Running the Pipelines**
### **1️⃣ Run Data Ingestion Pipeline**
```bash
python src/pipelines/data_ingestion_pipeline.py
```
### **2️⃣ Train the Model**
```bash
python src/pipelines/training_pipeline.py
```
### **3️⃣ Deploy the Model**
```bash
python src/pipelines/deployment_pipeline.py
```

## 📬 **Contributing**
Feel free to **fork** this repo, create a new branch, and submit a PR if you want to contribute! 🚀

## 📜 **License**
This project is licensed under the **MIT License**.

