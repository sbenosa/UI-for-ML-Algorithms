# UI-for-ML-Algorithms
This is an end to end sample algorithm exposed to users through UI

#### MultipleLinearRegression_Predict_Salary
This Multiple Linear Regression Model will predict employee salary based on Years of Experience, Industry and Position.

#### IRIS_Classifier
A sample classifier model

#### Deploying Machine Learning
This section will highlight what happens after a complete and tested model is ready for production run. Basically, we will create a pickle file out of the script of the trained machine learning model. This pickle file will be loaded up with a prediction script used to make predictions.

Then it will be wrapped up in a flask API framework to make predictions not only in a single data point
to data point but also in bulk processing via a files and databases. This will be wrap again on swagger so it can provide UI for user consumption. Finally create a docker file to containerized the application ready for deployment to any machines.

In essence, this process we will build a lego like blocks of codes put together in order to build a complete business use case. An application or machine learning application using a docker container ready to deploy in a production instance.

Please note though that the use of an industry grade web server to host our flask application like Apache, NginX is expected for enterprise implementations. These mature web technologies can scale to the numbers and volumes of transactions. It will continue to use the Web Server Gateway Interface; a middleware for a Python (Flask/Jango) API to connect to mature web like Apache

Users will be firing request which will land on the Apache split. Apache will the invoke the corresponding application in the Flask. Flask will send respond to Apache and apache will them pushed it to the users 

When deploying a web service in production, we need to make provisions (hardware, software) on how many concurrent users to ease up traffic into the system 

