from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px


guess = ""
result_text = ""
result_image = ""
game_over_text = ""
end_text = ""
score = 0
start_score = 5
game_over = False

def clear_results(state):
    state.result_text = ""
    state.result_image = ""

def reset_game(state):
    state.guess = ""
    state.result_text = ""
    state.result_image = ""
    state.game_over_text = ""
    state.end_text = ""
    state.score = 0
    state.start_score = 5
    state.game_over = False



def play(state):    
        guess = state.guess.replace(" ","").lower()
        if guess == guess[::-1] and guess != "":
            state.start_score -= 1
            state.result_text = "Det är en palindrome"
            state.result_image = "assets/fake_cat.png"
            if score < 5:
                 state.score += 1
        else:
            state.score -= 1
            state.result_text =  "Det är inte en palindrome"
            state.result_image = "assets/fake_sad_rabbit.png"
            if start_score <= 5:
                state.start_score += 1
                 

        if state.score == 5:
            state.end_text = ("🎉 GRATTIS DU VANN! 🎉")
            state.game_over_text = "Spelet är över. Klicka på 'Starta om' för att spela igen."
            state.result_image = "assets/fake_cat.png"
            state.game_over = True
        elif state.score <= 0:
            state.end_text = ("❌ DU DOG! 0 LIV KVAR ❌")
            state.game_over_text = "Spelet är över. Klicka på 'Starta om' för att spela igen."
            state.result_image = "assets/fake_sad_rabbit.png"
            state.game_over = True
              

with tgb.Page() as page:
    with tgb.part(class_name="container card"):
                    tgb.text("# Palindrome game", mode='md')
                    with tgb.layout(columns="1 1"):
                        with tgb.part(class_name="container card"):
                            tgb.text("Skriv ett ord: ")
                            tgb.input("{guess}", on_change=clear_results)
                            tgb.text("Du har gussat {guess}")
                            tgb.button(label="Gissa", class_name="plain", on_action=play)
                            tgb.button(label="Starta om", on_action=reset_game)
                        with tgb.part():
                            tgb.text("{result_text}")
                            tgb.image("{result_image}")
                            tgb.text("{end_text}")
                            tgb.text("{game_over_text}")
                            tgb.text("Poäng: {'⭐️' * score}{'💀' * start_score}")


if __name__ == '__main__':
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)
