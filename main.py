from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

player_a_life = 20
player_b_life = 20

red = [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
violet = [0.5,0,0.5,1]
yellow = [0.5,0.5,0,1]
cyan = [0,0.5,0.5,1]

class GUI(App):

    def build(self):
        def decrease_life_a(self):
            global player_a_life
            player_a_life -= 1
            life_counter_a.text = "PLAYER A.: "+"\n       "+str(player_a_life)
            return player_a_life

        def increase_life_a(self):
            global player_a_life
            player_a_life += 1
            life_counter_a.text = "PLAYER A.: "+"\n       "+str(player_a_life)
            return player_a_life

        def decrease_life_b(self):
            global player_b_life
            player_b_life -= 1
            life_counter_b.text = "PLAYER B.: "+"\n       "+str(player_b_life)
            return player_b_life

        def increase_life_b(self):
            global player_b_life
            player_b_life += 1
            life_counter_b.text = "PLAYER B.: "+"\n       "+str(player_b_life)
            return player_b_life

        colors = [red,green,blue,violet,yellow,cyan]
        layout = FloatLayout(size=(100,100))

        btn = Button(text='+', size_hint=(0.5,0.4), pos_hint={'x':0.0,'y':0.6}, font_size=250
                    ,background_color=colors[1]
                    )
        btn_2 = Button(text='-', size_hint=(0.5, 0.4), pos_hint={'x': 0.5, 'y': 0.6}, font_size=350
                    ,background_color=colors[0]
                      )
        btn_3 = Button(text='+', size_hint=(0.5, 0.4), pos_hint={'x': 0.0, 'y': 0.0}, font_size=250
                    ,background_color=colors[1]
                      )
        btn_4 = Button(text='-', size_hint=(0.5, 0.4), pos_hint={'x': 0.5, 'y': 0.0}, font_size=350
                    ,background_color=colors[0]
                      )

        btn.bind(on_release = increase_life_a)
        btn_2.bind(on_release = decrease_life_a)
        btn_3.bind(on_release=increase_life_b)
        btn_4.bind(on_release=decrease_life_b)

        life_counter_a = Label(text="PLAYER A", pos_hint={'x': -0.25, 'y': 0.0}, font_size=85, color=colors[3])
        life_counter_b = Label(text="PLAYER B", pos_hint={'x': 0.25, 'y': 0.0}, font_size=85, color=colors[2])

        layout.add_widget(life_counter_a)
        layout.add_widget(life_counter_b)

        layout.add_widget(btn)
        layout.add_widget(btn_2)
        layout.add_widget(btn_3)
        layout.add_widget(btn_4)

        return layout

if __name__ == '__main__':

    app = GUI()
    app.run()