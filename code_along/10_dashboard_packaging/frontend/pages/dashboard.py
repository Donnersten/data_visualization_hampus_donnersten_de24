import taipy.gui.builder as tgb
from backend.data_processing import filter_df, df
from frontend.charts import create_municipality_bar
from backend.update import filter_data

df_municipality = filter_df(df)

number_municipalites = 5
municipalites_title = number_municipalites

selected_educational_area = "Data/IT"
educational_area_title = selected_educational_area

municipality_chart = create_municipality_bar(
    df_municipality.head(10), ylable= "KOMMUN", xlable="# ANSÖKTA UTBILDNINGAR")


with tgb.Page() as dashboard_page:
    with tgb.part(class_name="container stack card"):
        with tgb.part(class_name="card"):
            tgb.text("# MYH dashboard 2024", mode="md")
            tgb.text(
                "En dashboard för att visa statistik och information om ansökningsomgång 2024",
                mode="md",
                )
        
        with tgb.layout(columns="2 1"):
            with tgb.part(class_name="card") as column_chart:
                tgb.text("## Antalet ansökta YH utbildningar per kummun (topp {municipalites_title}) för {educational_area_title}",
                          mode="md")
                tgb.chart(figure="{municipality_chart}")
            
            with tgb.part(class_name="card") as column_chart:
                tgb.text("## Filtrerad data", mode="md")
                tgb.text("Filtrera antalet kommuner", mode="md")

                tgb.slider(value="{number_municipalites}", min=5, max=len(df_municipality), continuous=False)

                tgb.text("Välj utbildningsområde", mode="md")
                tgb.selector(value="{selected_educational_area}",
                             lov=df["Utbildningsområde"].unique(),
                             dropdown=True)
                
                tgb.button("FILTRERA DATA", on_action=filter_data, class_name="plain")
       

