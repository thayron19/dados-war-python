import tkinter
import random
import keyboard


def sorteio():
    global peca_ataque
    global peca_defesa

    peca_atk = 0
    peca_def = 0

    dados_ataque = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    dados_defesa = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

    dados_ataque.sort(reverse=True)
    dados_defesa.sort(reverse=True)

    dado1atk_valor.set(str(f' {dados_ataque[0]} '))
    dado2atk_valor.set(str(f' {dados_ataque[1]} '))
    dado3atk_valor.set(str(f' {dados_ataque[2]} '))

    dado1def_valor.set(str(f' {dados_defesa[0]} '))
    dado2def_valor.set(str(f' {dados_defesa[1]} '))
    dado3def_valor.set(str(f' {dados_defesa[2]} '))

    if dados_ataque[0] <= dados_defesa[0]:
        var_resulta1.set('D')
        peca_ataque += 1
        peca_atk += 1
    else:
        var_resulta1.set('A')
        peca_defesa += 1
        peca_def += 1

    if dados_ataque[1] <= dados_defesa[1]:
        var_resulta2.set('D')
        peca_ataque += 1
        peca_atk += 1
    else:
        var_resulta2.set('A')
        peca_defesa += 1
        peca_def += 1

    if dados_ataque[2] <= dados_defesa[2]:
        var_resulta3.set('D')
        peca_ataque += 1
        peca_atk += 1
    else:
        var_resulta3.set('A')
        peca_defesa += 1
        peca_def += 1

    por_atk = peca_ataque / (peca_ataque + peca_defesa) * 100
    por_def = peca_defesa / (peca_ataque + peca_defesa) * 100

    var_atk.set(f'Ataque perdeu {peca_atk} peças')
    var_def.set(f'Defesa perdeu {peca_def} peças')

    var_acumulado_atk.set(f'Ataque perdeu {peca_ataque} peças {por_atk:.2f}%')
    var_acumulado_def.set(f'Defesa perdeu {peca_defesa} peças {por_def:.2f}%')

    var_total.set(f'Total de peças perdidas {peca_ataque + peca_defesa}')


# ---------------------------------------------------------------------------------------------------------------------
janela = tkinter.Tk()

janela.title('WAR')

largura_janela = 200
altura_janela = 310

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posl = float(largura_janela/2 - largura_tela/2)
posa = float(altura_janela/2 - altura_tela/2)

janela.geometry("%dx%d%d%d" % (largura_janela, altura_janela, posl, posa))
janela.resizable(width=False, height=False)
# ---------------------------------------------------------------------------------------------------------------------
peca_ataque = 0
peca_defesa = 0
# ---------------------------------------------------------------------------------------------------------------------
dado1atk_valor = tkinter.StringVar()
dado1atk = tkinter.Button(janela, textvariable=dado1atk_valor, bg='red', foreground='white')
dado1atk.place(x=10, y=10)

dado2atk_valor = tkinter.StringVar()
dado2atk = tkinter.Button(janela, textvariable=dado2atk_valor, bg='red', foreground='white')
dado2atk.place(x=40, y=10)

dado3atk_valor = tkinter.StringVar()
dado3atk = tkinter.Button(janela, textvariable=dado3atk_valor, bg='red', foreground='white')
dado3atk.place(x=70, y=10)

dado1def_valor = tkinter.StringVar()
dado1def = tkinter.Button(janela, textvariable=dado1def_valor, bg='blue', foreground='white')
dado1def.place(x=10, y=40)

dado2def_valor = tkinter.StringVar()
dado2def = tkinter.Button(janela, textvariable=dado2def_valor, bg='blue', foreground='white')
dado2def.place(x=40, y=40)

dado3def_valor = tkinter.StringVar()
dado3def = tkinter.Button(janela, textvariable=dado3def_valor, bg='blue', foreground='white')
dado3def.place(x=70, y=40)
# ---------------------------------------------------------------------------------------------------------------------
var_resulta1 = tkinter.StringVar()
texto_resulta1 = tkinter.Label(janela, textvariable=var_resulta1)
texto_resulta1.place(x=14, y=70)

var_resulta2 = tkinter.StringVar()
texto_resulta2 = tkinter.Label(janela, textvariable=var_resulta2)
texto_resulta2.place(x=44, y=70)

var_resulta3 = tkinter.StringVar()
texto_resulta3 = tkinter.Label(janela, textvariable=var_resulta3)
texto_resulta3.place(x=74, y=70)
# ---------------------------------------------------------------------------------------------------------------------
linha = tkinter.Label(janela, text='-'*39)
linha.place(x=0, y=90)

linha = tkinter.Label(janela, text='Jogada:')
linha.place(x=5, y=110)

var_atk = tkinter.StringVar()
atk = tkinter.Label(janela, textvariable=var_atk)
atk.place(x=14, y=130)

var_def = tkinter.StringVar()
defesa = tkinter.Label(janela, textvariable=var_def)
defesa.place(x=14, y=150)
# ---------------------------------------------------------------------------------------------------------------------
linha = tkinter.Label(janela, text='-'*39)
linha.place(x=0, y=170)

linha = tkinter.Label(janela, text='Acumulado:')
linha.place(x=5, y=190)

var_acumulado_atk = tkinter.StringVar()
acumulado_atk = tkinter.Label(janela, textvariable=var_acumulado_atk)
acumulado_atk.place(x=14, y=210)

var_acumulado_def = tkinter.StringVar()
acumulado_def = tkinter.Label(janela, textvariable=var_acumulado_def)
acumulado_def.place(x=14, y=230)
# ---------------------------------------------------------------------------------------------------------------------
linha = tkinter.Label(janela, text='-'*39)
linha.place(x=0, y=250)

var_total = tkinter.StringVar()
acumulado = tkinter.Label(janela, textvariable=var_total)
acumulado.place(x=14, y=270)
# ---------------------------------------------------------------------------------------------------------------------
jogar = tkinter.Button(janela, text='Jogar dados', command=lambda: sorteio())
jogar.place(x=110, y=25)
# ---------------------------------------------------------------------------------------------------------------------
dado1atk_valor.set(str(f'    '))
dado2atk_valor.set(str(f'    '))
dado3atk_valor.set(str(f'    '))
dado1def_valor.set(str(f'    '))
dado2def_valor.set(str(f'    '))
dado3def_valor.set(str(f'    '))
# ---------------------------------------------------------------------------------------------------------------------
var_resulta1.set('')
var_resulta2.set('')
var_resulta3.set('')
# ---------------------------------------------------------------------------------------------------------------------
keyboard.on_press_key('ENTER', lambda _: sorteio())
keyboard.on_press_key('ESC', lambda _: janela.destroy())
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()
