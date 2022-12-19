# FIFA22 Players App

This web app is the capstone project for my data science fellowship at ReadyForWork (SFAN).
The aim is to build an app that uses machine learning to make prediction(s) and visualise data in an interactive way. 
I used a publicly available dataset on Kaggle that contains information of 18,145 players and 702 teams.

## Features and Capabilities

The app contains the following features:

* A dropdown to see a preview of the dataset.
* Input bars that take values from users and make a prediction about a prospective
player’s weekly wage.
* Information panel that allows users to view a player’s biodata, technical, mental and
physical attributes.
* A correlation graph of attributes.
* A country plot of young players with high potential.

##  Running the Visualisation

To run the visualisation, you will need to have Python 3 and the following dependencies installed:

* streamlit
* numpy
* pandas
* plotly_express
* seaborn
* matplotlib
* joblib

You can install these dependencies using pip:

`pip install requirements`

Once the dependencies are installed, you can run the visualisation by navigating to the
directory containing the app.py file and running the following command:

`streamlit run app.py`

## Credits and References
1. The dataset for this project was prepared by Stefano Leone on [Kaggle](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset)
