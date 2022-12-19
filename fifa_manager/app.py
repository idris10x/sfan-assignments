import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

st.set_page_config(
    layout="wide", page_title="FIFA 2022 Players Viz", page_icon="⚽")

df = pd.read_csv("players_22.csv")

# Introduction
st.title('FIFA 2022 Players Viz')
st.subheader(
    'Streamlit App by [Idris Abdulkareem](https://www.linkedin.com/in/idrisinkedin/)')

# See Data
row1_spacer1, row1_1, row1_spacer2 = st.columns((.2, 7.1, .2))
with row1_1:
    st.subheader("Data:")

row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3, row2_3, row2_spacer4, row2_4, row2_spacer5 = st.columns(
    (.2, 1.6, .2, 1.6, .2, 1.6, .2, 1.6, .2))
with row2_1:
    unique_players_in_df = df.short_name.nunique()
    str_players = "⚽ " + str(unique_players_in_df) + " Players"
    st.markdown(
        f'<h1 style="color:#FFFFFF;font-size:20px;">{str_players}</h1>', unsafe_allow_html=True)
with row2_2:
    unique_teams_in_df = len(pd.unique(df.club_name).tolist())
    t = " Teams"
    if (unique_teams_in_df == 1):
        t = " Team"
    str_teams = "🏟️" + str(unique_teams_in_df) + t
    st.markdown(
        f'<h1 style="color:#FFFFFF;font-size:20px;">{str_teams}</h1>', unsafe_allow_html=True)
with row2_3:
    total_league_in_df = len(pd.unique(df.league_name).tolist())
    str_league = "👟⚽" + str(total_league_in_df) + " League"
    st.markdown(
        f'<h1 style="color:#FFFFFF;font-size:20px;">{str_league}</h1>', unsafe_allow_html=True)

row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.markdown("")
    see_data = st.expander('You can click here to see the raw data first 👉')
    with see_data:
        st.dataframe(data=df.iloc[:, :37].reset_index(drop=True))
st.text('')

# Make Prediction
row10_spacer1, row10_1, row10_spacer2 = st.columns((.2, 7.1, .2))
with row10_1:
    st.subheader('Predict Player Wage')

row11_spacer1, row11_1, row11_spacer2 = st.columns((.2, 7.1, .2))
with row11_1:
    overall = st.number_input('Input Overall Points',
                              min_value=1, max_value=95, value=25)
    potential = st.number_input(
        'Input Potential Points', min_value=1, max_value=95, value=25)
    passing = st.number_input('Input Passing Points',
                              min_value=1, max_value=95, value=25)
    dribbling = st.number_input(
        'Input Dribbling Points', min_value=1, max_value=95, value=25)

# If button is pressed
row12_spacer1, row12_1, row12_spacer2 = st.columns((.2, 7.1, .2))
with row11_1:
    if st.button("Submit"):

        # Unpickle classifier
        model = joblib.load("pred151222.pkl")

        # Store inputs into dataframe
        X = pd.DataFrame([[overall, potential, passing, dribbling]],
                         columns=["overall", "potential", "passing", "dribbling"])

        # Get prediction
        prediction = model.predict(X)[0]

        # Output prediction
        st.text(f"This player will earn {round(prediction,2)} Euros per week")

# Player Data Explorer
row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
with row4_1:
    st.subheader('Player Information')

row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3, row5_3, row5_spacer4, row5_4, row5_spacer4 = st.columns(
    (.2, 2.3, .2, 2.3, .2, 2.3, .2, 2.3, .2))
with row5_1:
    show_me_Nation = st.selectbox("League Nation",
                                  df.league_nation.value_counts().index.tolist(),
                                  key="playernation")

with row5_2:
    show_me_league = st.selectbox("Player's League",
                                  df[df.league_nation == show_me_Nation]["league_name"].value_counts(
                                  ).index.tolist(),
                                  key="playerleague")

with row5_3:
    show_me_team = st.selectbox("Player's Team",
                                df[df.league_name == show_me_league]["club_name"].value_counts(
                                ).index.tolist(),
                                key="playerteam")

with row5_4:
    show_me_player = st.selectbox("Player's Name",
                                  df[df.club_name == show_me_team]["short_name"].value_counts(
                                  ).index.tolist(),
                                  key="playername")


row6_spacer1, row6_1, row6_spacer2, row6_2, row6_spacer3, row6_3, row6_spacer4, row6_4, row6_spacer4 = st.columns(
    (.2, 2.3, .2, 2.3, .2, 2.3, .2, 2.3, .2))
with row6_1:
    st.subheader("Player")
with row6_2:
    st.subheader("Technical")
with row6_3:
    st.subheader("Mental")
with row6_4:
    st.subheader("Physical")

row7_spacer1, row7_1, row7_spacer2, row7_2, row7_spacer3, row7_3, row7_spacer4, row7_4, row7_spacer5 = st.columns(
    (.2, 2.3, .2, 2.3, .2, 2.3, .2, 2.3, .2))

with row7_1:
    col_player_info = df.columns[2:13]
    k = 0
    for i in df[col_player_info]:
        if k == 0:
            st.image(df[df["short_name"] == str(show_me_player)
                        ].loc[:, "player_face_url"].tolist()[0], width=125)

        st.markdown('**' + i + '**: ' + '' + str(
            df[col_player_info][df["short_name"] == str(show_me_player)].loc[:, i].tolist()[0]) + '')
        k = k+1

with row7_2:
    col_player_tech = df.columns[39:53]
    for i in df[col_player_tech]:
        st.markdown('**' + i + '**: ' + '' + str(
            df[col_player_tech][df["short_name"] == str(show_me_player)].loc[:, i].tolist()[0]) + '')

with row7_3:
    col_player_mental = df.columns[63:69]
    for i in df[col_player_mental]:
        st.markdown('**' + i + '**: ' + '' + str(
            df[col_player_mental][df["short_name"] == str(show_me_player)].loc[:, i].tolist()[0]) + '')

with row7_4:
    col_player_physical = df.columns[54:62]
    for i in df[col_player_physical]:
        st.markdown('**' + i + '**: ' + '' + str(df[col_player_physical]
                    [df["short_name"] == str(show_me_player)].loc[:, i].tolist()[0]) + '')


# Plotting

label_attr_dict_correlation = {"Pace": "pace", "Shooting": "shooting", "Passing": "passing",
                               "Dribbling": "dribbling", "Defending": "defending", "Physique": "physic"}


def plt_attribute_correlation(aspect1, aspect2):
    rc = {'figure.figsize': (5, 5),
          'axes.facecolor': '#0e1117',
          'axes.edgecolor': '#0e1117',
          'axes.labelcolor': 'white',
          'figure.facecolor': '#0e1117',
          'patch.edgecolor': '#0e1117',
          'text.color': 'white',
          'xtick.color': 'white',
          'ytick.color': 'white',
          'grid.color': 'grey',
          'font.size': 8,
          'axes.labelsize': 8,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8}
    plt.rcParams.update(rc)
    fig, ax = plt.subplots()
    asp1 = label_attr_dict_correlation[aspect1]
    asp2 = label_attr_dict_correlation[aspect2]
    ax = sns.regplot(x=asp1, y=asp2, x_jitter=.1, data=df, color='#f21111', scatter_kws={
                     "color": "#f21111"}, line_kws={"color": "#c2dbfc"})
    ax.set(xlabel=aspect1, ylabel=aspect2)
    st.pyplot(fig, ax)


row8_spacer1, row8_1, row8_spacer2 = st.columns((.2, 7.1, .2))
with row8_1:
    st.subheader('Correlation of Attributes')
row9_spacer1, row9_1, row9_spacer2, row9_2, row9_spacer3 = st.columns(
    (.2, 2.3, .2, 2.3, .2))
with row9_1:
    st.markdown('Investigate the correlation of players technical attributes, but keep in mind correlation does not imply causation. Do players that pass more also dribble more?')
    y_axis_aspect2 = st.selectbox(
        "Which attribute do you want on the y-axis?", list(label_attr_dict_correlation.keys()))
    x_axis_aspect1 = st.selectbox(
        "Which attribute do you want on the x-axis?", list(label_attr_dict_correlation.keys()))
with row9_2:
    plt_attribute_correlation(x_axis_aspect1, y_axis_aspect2)

potentialBiggerThan80 = df[(df.potential >= 80) & (df.age <= 23)]

highPotentialCountries = potentialBiggerThan80.groupby(
    ['nationality_name', 'overall']).size().reset_index(name='count')
highPotentialCountries = pd.DataFrame(highPotentialCountries.groupby(
    'nationality_name')['count'].sum().reset_index())

row13_spacer1, row13_1, row13_spacer2 = st.columns((.2, 7.1, .2))
with row13_1:
    st.subheader("Country plot of young players with high potential")

    fig = go.Figure(data=go.Choropleth(
        colorscale='Agsunset',
        locationmode='country names',
        locations=highPotentialCountries['nationality_name'],
        text=highPotentialCountries['nationality_name'],
        z=highPotentialCountries['count'],
        marker_line_color='black',
        autocolorscale=False,
    ))

    fig.update_layout(
        title_text='Countries with players of age (<=23) and potential (>=80)',
        paper_bgcolor='rgb(0,0,0)',
        plot_bgcolor='rgb(0,0,0)',
        font_family="Arial",
        font_color="white",
        title_font_family="Arial",
        title_font_color="white",
        legend_title_font_color="white",
    )

    st.plotly_chart(fig, use_container_width=True)
