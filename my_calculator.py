import tkinter as tk

# -----------------------------------
#            INTERFACE
# -----------------------------------

# La classe suivante permet d'appeler les couleurs et polices d'écriture nécessaires
class colors_and_fonts:

    # Colors:
    background_color = '#92C5AF'
    digit_buttons_color = '#29464A'
    operator_buttons_color = '#7F7CB8'
    all_clear_button_color = '#CB6277'
    font_color = '#BBCFD4'
    screen_color = '#D8E3E4'
    screen_result_color = '#D7E3E4'

    # Fonts:
    digits_font_style = ('Century Gothic', 16)
    exe_font_style = ('Century Gothic', 11)
    result_font_style = ('Century Gothic', 26)

# On définit la fenêtre tkinter avec sa taille, son titre et sa couleur de fond
window = tk.Tk()
window.geometry('350x550')
window.title('Calculator')
window.configure(bg = colors_and_fonts.background_color)

# -----------------------------------
#                FRAMES
# -----------------------------------
# On crée deux frames, une pour l'écran, l'autre pour les touches
screen = tk.Frame(height = 220, width=300, bg=colors_and_fonts.screen_color)
screen.pack(pady=20)

commands = tk.Frame(height=400, width=320, bg=colors_and_fonts.background_color)
commands.pack()
    
# -----------------------------------
#          NUMBERS BUTTONS
# -----------------------------------

# On aurait pu faire une liste avec tous les boutons. Cependant, comme ils possèdent des propriétés différentes (tailles, couleurs, etc.), j'ai choisi ded les faire un à un
button_7 = tk.Button(bd= 0, width= 2, height=1, master=commands, text='7', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click(7))
button_7.grid(row=2, column=1)

button_8 = tk.Button(bd= 0, width= 2, height=1, master=commands, text='8', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click(8))
button_8.grid(row=2, column=2)

button_9 = tk.Button(bd= 0, width= 2, height=1, master=commands, text='9', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click(9))
button_9.grid(row=2, column=3)

button_4 = tk.Button(bd= 0, width= 2, height=1, master=commands, text='4', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click(4))
button_4.grid(row=3, column=1)

button_5 = tk.Button(bd= 0, width= 2, height=1, master=commands, text='5', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click(5))
button_5.grid(row=3, column=2)

button_6 = tk.Button(bd= 0, width= 2, height=1, master=commands, text='6', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click(6))
button_6.grid(row=3, column=3)

button_1 = tk.Button(bd= 0, width= 2, height=1, master=commands, text='1', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click(1))
button_1.grid(row=4, column=1)

button_2 = tk.Button(bd= 0, width= 2, height=1, master=commands, text='2', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click(2))
button_2.grid(row=4, column=2)

button_3 = tk.Button(bd= 0, width= 2, height=1, master=commands, text='3', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click(3))
button_3.grid(row=4, column=3)

button_0 = tk.Button(bd= 0, width= 2, height=1, master=commands, text='0', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click(0))
button_0.grid(row=5, column=1)

button_point = tk.Button(bd= 0, width= 2, height=1, master=commands, text='.', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, font=colors_and_fonts.digits_font_style, padx=10, pady=2, command=lambda: click('.'))
button_point.grid(row=5, column=2)


# -----------------------------------
#         OPERATOR and OTHERS
# -----------------------------------

sum = tk.Button(bd= 0, width= 2, height=1, master=commands, text='+', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.digits_font_style, command=lambda:click('+') )
sum.grid(row=4, column=4, pady=5, padx=4)

subtraction = tk.Button(bd= 0, width= 2, height=1, master=commands, text='-', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.digits_font_style, command=lambda:click('-'))
subtraction.grid(row=4, column=5, pady=5, padx=4)

multiplication = tk.Button(bd= 0, width= 2, height=1, master=commands, text='x', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.digits_font_style, command=lambda:click('*'))
multiplication.grid(row=3, column=4, pady=5, padx=4)

division = tk.Button(bd= 0, width= 2, height=1, master=commands, text='\u00F7', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.digits_font_style, command=lambda:click('/'))
division.grid(row=3, column=5, pady=5, padx=4)

exe = tk.Button(bd= 0, width= 3, height=2, master=commands, text='EXE', bg=colors_and_fonts.digit_buttons_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.exe_font_style, command=lambda:equals_to())
exe.grid(row=5, column=5, pady=5, padx=4)

all_clear = tk.Button(bd= 0, width= 2, height=1, master=commands, text='AC', bg=colors_and_fonts.all_clear_button_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.digits_font_style, command= lambda: clear())
all_clear.grid(row=2, column=5, pady=5, padx=4)

bracket_left = tk.Button(bd= 0, width= 2, height=1, master=commands, text='(', bg=colors_and_fonts.operator_buttons_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.digits_font_style, command=lambda:click('('))
bracket_left.grid(row=1, column=4, pady=10, padx=4)

bracket_right = tk.Button(bd= 0, width= 2, height=1, master=commands, text=')', bg=colors_and_fonts.operator_buttons_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.digits_font_style, command=lambda:click(')'))
bracket_right.grid(row=1, column=5, pady=10, padx=4)

modulo = tk.Button(bd= 0, width= 2, height=1, master=commands, text='%', bg=colors_and_fonts.operator_buttons_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.digits_font_style, command=lambda : click('%'))
modulo.grid(row=1, column=3, pady=10, padx=4)

pow = tk.Button(bd= 0, width= 2, height=1, master=commands, text='x²', bg=colors_and_fonts.operator_buttons_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.digits_font_style, command=lambda: click('**2'))
pow.grid(row=1, column=2, pady=10, padx=4)

square_root = tk.Button(bd= 0, width= 2, height=1, master=commands, text='\u221ax', bg=colors_and_fonts.operator_buttons_color, fg=colors_and_fonts.font_color, padx=10, pady=2, font=colors_and_fonts.digits_font_style, command=lambda:click('**0.5'))
square_root.grid(row=1, column=1, pady=10, padx=4)

# -----------------------------------
#                SCREEN
# -----------------------------------

operations = ""
results = ""
display_text = tk.StringVar()
display_result = tk.StringVar()

current_expression = tk.Label(textvariable= display_text, bd= 0, width=13, height=2, master=screen, fg=colors_and_fonts.screen_result_color, font=colors_and_fonts.result_font_style)
current_expression.grid(row=1, padx=3, pady=1)

total_expression = tk.Label(textvariable= display_result, bd=0, width=13, height=2, master=screen, fg=colors_and_fonts.screen_result_color, font=colors_and_fonts.result_font_style)
total_expression.grid(row=2, padx=3, pady=1)

        
# -----------------------------------
#             COMMANDES
# -----------------------------------

def click(item):
    global operations
    operations += str(item)
    display_text.set(operations)
    
#  Touche AC
def clear():
    global operations, results
    operations = ""
    results = ""
    display_text.set(operations)
    display_result.set(results)

# Touche EXE :
def equals_to():
    global results, operations
    try:
        results = str(eval(operations))
        display_result.set(results[:7])
        operations = ""
        display_text.set(operations)
    except:
        # Les opérations interdites :
        if "/0" in operations:
            results = "Error"
            display_result.set(results)
            operations = ""
            display_text.set(operations)


# Pour que la fenêtre reste ouverte en continu
window.mainloop()
