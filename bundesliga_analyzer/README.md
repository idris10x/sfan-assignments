# Streamlit Visualization of Bundesliga Data (2013/14 - 2019/20)

This Streamlit visualisation allows users to explore and analyse Bundesliga data from 2013/14 to 2019/20 season in an interactive way. 
It includes a matchfinder, analysis per team, analysis per season, analysis per matchday and correlation of game stats.

## Running the Visualization

To run the visualisation, you will need to have Python 3 and the following dependencies installed:

* streamlit
* pandas
* numpy
* matplotlib
* seaborn

You can install these dependencies using pip:

`pip install requirements`

Once the dependencies are installed, you can run the visualisation by navigating to the directory containing the app.py file and running the following command:

`streamlit run app.py`

## Features and Capabilities

The visualisation includes the following features:

* Matchfinder that shows details of matches with minimum/maximum stats by team(s).
* Interactive chart that shows analysis per team and changes as users adjust input
parameters.
* Interactive chart that shows analysis per season and changes as users adjust input
parameters.
* Interactive chart that shows analysis per matchday and changes as users adjust
input parameters.
* Filtering and sorting options that allows users to focus on specific teams or seasons.

## Credits and References

1. This app is based on Tim Denzler [app](https://tdenzl-bulian-bulian-ifeiih.streamlit.app/)
2. The data and scripts of the original app can be found [here](https://github.com/tdenzl/BuLiAn)
