from backend.data_processing import filter_df
from frontend.charts import create_municipality_bar


def filter_data(state):
    df_municipality = filter_df(
        state.df, educational_area=state.selected_educational_area
    )

    state.municipality_chart = create_municipality_bar(
        df_municipality.head(state.number_municipalites),
         ylable= "KOMMUN",
         xlable="# ANSÖKTA UTBILDNINGAR"
    )

    state.educational_area_title = state.selected_educational_area
    state.municipalites_title = state.number_municipalites
