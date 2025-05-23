from utils.constans import DATA_DIRECTORY
import pandas as pd

df = pd.read_excel(DATA_DIRECTORY / "resultat-ansokningsomgang-2024.xlsx", sheet_name="Tabell 3", skiprows=5)


def filter_df(df,educational_area="Data/IT"):
    return df.query("Utbildningsområde == @educational_area")["Kommun"].value_counts().reset_index().rename({"count": "Ansökta utbildningar"}, axis=1)
