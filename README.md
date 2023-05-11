## END to END Machine Learning Project

1. Set up the GitHub repository & local machine
   a) Creating New environment
   b) Setup.py
   c) requirements.txt

2. src (source) folder and build the package
3. Project Structure - Logging and Exception
4. EDA and Model Training.
5. Data Ingestion
6. Data Transformation
7. Model Trainer
8. prediction Pipeline(for front end web app)
9. Flask app and Html Web app
10. Build Docker Image
11. Model Deployment
        - Azure Deployment:
        1. create container Registry
        2. docker login testdockermadhan.azurecr.io
        3. Azure web app with container
        4. Configured with github Deployment center

#### STEPS INVOLVED

step 1: create a repository
step 2: create a folder in local machine to work on.
step 3: open anaconda prompt and locate to the folder created and type "code ." to create a vs code instance.
step 4: once vs instance opened, open terminal and creat a new environment and activate the new environment using conda activate envname/

SYNCING THE GITHUB:
step 5: initiate the empty git repository using "git init" command.
step 6: create a README.md file
step 7: then follow the commands 
           git commit -m "first commit"
	     git branch -M main
	     git remote add origin https://github.com/Madhan-sukumar/mlproject.git
	     git remote -v
	     git push -u origin main
step 8: create ".gitignore" in github and command "git pull" in terminal to see changes happened on local machine 

SETUP:
step 9: create setup.py (building our ml application as a package) and requirements.txt files
step 10: create src folder and __init__.py file under src for the setup.py file to build ML application as package
STEP 11: pip install -r requirements.txt

step 12: create components folder under src and create __init__.py file in components folder
step 13: create data_ingestion.py, data_transformation.py,model_trainer.py files under components
step 14: create pipeline folder under src and create __init__.py file in pipeline folder.
step 15: create train_pipeline.py and predict_pipeline.py under pipeline folder
step 16: create logger.py,exception.py and utils.py files under src
step 17: fill exception.py, logger.py  and utils.py with code
step 18: create notebook folder and data folder under notebook and move csv to the data folder.
step 18: create ipynb file under notebook folder and start EDA, model training

READ THE DATASET\DATA INGESTION:
step 19: fill the code in data ingestion file(data ingestion is process of importing large, assorted data files from multiple sources into a single, cloud-based storage medium)

DATA TRANSFORMATION
step 20: fill the code for data transformation in data transformation file

MODEL TRAINING:
step 21: fill the code for model training in model training file

CREATING PREDICTION PIPELINE FOR FRONT END(WEB APP):
step 22: create app.py for flask app, html front end
input data flow from front end html --> back end flask app --> predict pipeline

PIPELINE:
step 23: create a pipeline in predict pipeline file to predict values given from the web application

DEPLOYMENT:
Web app created into ---> Docker private Image --> docker privte image deployed to --> azure container registry --> Azure container registry pulled by --> Azure Web app(server) --> Deployed as web app.   

step 24: create azure container registry and azure web app.
step 25: create docker image and push it to container registry.
step 26: Finally Deployed


#### Docker Run from terminal 

docker build -t testdockermadhan.azurecr.io/studentperformance:latest .

docker login testdockermadhan.azurecr.io

docker push testdockermadhan.azurecr.io/studentperformance:latest