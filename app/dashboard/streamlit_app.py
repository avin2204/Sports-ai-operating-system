import streamlit as st

st.set_page_config(
    page_title="Sports Enterprise AI OS",
    layout="wide"
)

st.title(
    "🏆 Sports Enterprise AI Operating System"
)

tab1, tab2, tab3, tab4 = st.tabs([
    "Player Rankings",
    "Team Rankings",
    "Predictions",
    "Knowledge Graph"
])

with tab1:

    st.subheader(
        "Player Rankings"
    )

    st.dataframe([
        {
            "player": "Virat Kohli",
            "score": 95
        },
        {
            "player": "Messi",
            "score": 92
        }
    ])

with tab2:

    st.subheader(
        "Team Rankings"
    )

    st.dataframe([
        {
            "team": "India",
            "score": 98
        },
        {
            "team": "Liverpool",
            "score": 91
        }
    ])

with tab3:

    st.subheader(
        "Predictions"
    )

    st.metric(
        "Prediction Confidence",
        "82%"
    )

with tab4:

    st.subheader(
        "Knowledge Graph"
    )

    st.write(
        "Virat Kohli → RCB → IPL"
    )

    st.write(
        "Messi → Inter Miami → MLS"
    )