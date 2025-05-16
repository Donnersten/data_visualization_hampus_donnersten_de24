from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px
import random
import pandas as pd

number_dices = 5
number_throws = 1
kast= 0
dices=0
df = pd.DataFrame(columns=["Kast", "Resultat"])

def number_dice(state):
    state.kast += 1
    resultat = state.number_dice

    df.iloc[len(df)] = [kast, resultat]

def throw_dices(num):
    return [random.randint(1, 6) for i in range(num)]



with tgb.Page() as page:
    with tgb.part(class_name="container stack card"):
        with tgb.part(class_name="card"):
            tgb.text("# Dice simulations", mode="md")

        with tgb.layout(columns="1 1"):
            with tgb.part(class_name="card"):
                tgb.table("{df}")
                tgb.text("Number of dices chosen: {number_dices}", mode="md")
                tgb.slider("{number_dices}", min=1, max=20, )
                tgb.text("Number of throws: {number_throws}", mode="md")
                tgb.slider("{number_throws}", min=1, max=100,)
                tgb.button(label="Simulate", class_name="plain", on_action=number_dice)

Gui(page, css_file="assets/main.css").run(dark_mode=False, use_reloader=True, port=8080)

