from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px

df = px.data.gapminder()
fig = px.line(df.query("country == 'Sweden'"), x="year", y="pop")

slider_value = 20
selected_fruit= "Avocado"
number1 = 2
number2 = 8
sum_ = number1+number2

speed = 60
variation = 15
layout = {
                "paper_bgcolor": "white",
                "font": {
                    "size": 10,
                    "color": "blue",
                    "family": "Arial",
                },
            }     

def preform_calculation(state):
    state.sum_ = int(state.number1) + int(state.numebr2)

def clear_results(state):
    state.sum_ = ""

with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        tgb.text("# Hello there taipy", mode="md")
        tgb.text("Welcome to the world of reactive programing") 
        with tgb.layout(columns="1 1 1"):
            with tgb.part(class_name="container card"):
                tgb.text("# Hello there taipy", mode="md")
                tgb.text("Welcome to the world of reactive programing") 

                # Bindes to slider value varible and makes it dynamic
                tgb.slider(value="{slider_value}" ,min=0,max=100, step=5, continuous=False)
                tgb.text("Slider value is at {slider_value}")

                tgb.text("Select your favorite fruit")
                tgb.selector(value="{selected_fruit}", lov=["tomato", "apple", "avocado", "banana"], dropdown=True)
                tgb.text("Yummy {selected_fruit}")
                tgb.image("assets/{selected_fruit}.jpg")
            with tgb.part(class_name="container card"):
                tgb.text("## Coolu calculator", mode='md')
                tgb.text("Type in a number:")
                tgb.input("{number1}", on_change=clear_results)

                tgb.text("Type in a anuther number:")
                tgb.input("{number2}", on_change=clear_results)

                tgb.text("You have typed in {number1} and {number2}")
                # on action buttun will activete when the buttun is pressed
                tgb.button(label="CALCULATU", class_name="plain", on_action=preform_calculation)
                tgb.text("{number1} + {number2} = {sum_}")
                tgb.text("  ")
            with tgb.part(class_name="container card"):
                tgb.text("## Speed", mode="md")
                tgb.metric("{speed}", format="%d km/h", delta="{variation}", delta_format="%d %%", layout="{layout}", width=300, height=300)
        with tgb.layout(columns="1 1", class_name="container card"):
            with tgb.part():
                tgb.table("{df}", page_size=10)
            with tgb.part():
                tgb.chart(figure="{fig}")

if __name__ == '__main__':
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)
