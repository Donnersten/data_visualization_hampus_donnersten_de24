from taipy.gui import Gui
import taipy.gui.builder as tgb

slider_value = 20
selected_fruit= "Avocado"

with tgb.Page() as page:
    tgb.text("# Hello there taipy", mode="md")
    tgb.text("Welcome to the world of reactive programing")
    speed = 60
    variation = 15
    layout = {
    "paper_bgcolor": "#f1f5f7",
    "font": {
        "size": 30,
        "color": "blue",
        "family": "Arial",
    },
}      
    tgb.metric("{speed}", format="%d km/h", delta="{variation}", delta_format="%d %%", layout="{layout}")

    # Bindes to slider value varible and makes it dynamic
    tgb.slider(value="{slider_value}" ,min=0,max=100, step=5)
    tgb.text("Slider value is at {slider_value}")

    tgb.text("Select your favorite fruit")
    tgb.selector(value="{selected_fruit}", lov=["tomato", "apple", "avocado", "banana"], dropdown=True)
    tgb.text("Yummy {selected_fruit}")
    tgb.image("assets/{selected_fruit}.jpg")

if __name__ == '__main__':
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)
