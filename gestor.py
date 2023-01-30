from tkinter import *


# inicio de aplicacion
app = Tk()

#tamaño de la ventana

app.geometry("1020x636+0+0")

#evitar si maxim
app.resizable(0,0)

#titulo
app.title("restaurante")

#color ventana
app.config( bg="aquamarine")

#panel principal

panel_sup= Frame(app, bd=1, relief= FLAT )
panel_sup.pack(side=TOP)

#etiqueta titulo

etiqueta_titulo = Label(panel_sup, text= " sistema de facturacion", fg= "azure4", font= ("Times New Roman",58), bg= "burlywood", width= 27)
etiqueta_titulo.grid(row=0, column=0)

#panel izq
panel_izq=  Frame(app, bd=1, relief= FLAT )
panel_izq.pack(side=LEFT)
#panel costos
panel_costos =  Frame(app, bd=1, relief= FLAT )
panel_costos.pack(side= BOTTOM)
#panel comidas
panel_comidas =  LabelFrame(panel_izq, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)
#panel bebidas
panel_bebidas =  LabelFrame(panel_izq,text= 'Bebidass', font= ("Times New Roman", 19, "bold"), bd=1, relief= FLAT, fg= "azure4") 
panel_bebidas.pack(side=LEFT)

#panel postres'Postres'
panel_postres =  LabelFrame(panel_izq,text= 'Postres', font= ("Times New Roman", 19, "bold"), bd=1, relief= FLAT, fg= "azure4") 
panel_postres.pack(side=LEFT)

#panel derecha

panel_derecha = Frame(app, bd=1, relief= FLAT )
panel_derecha.pack(side=RIGHT)

#panel calculadora

panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg = 'burlywood' )
panel_calculadora.pack()

#panel recibo

panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg = 'burlywood' )
panel_recibo.pack()

#panel botones

panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg= 'burlywood' )
panel_botones.pack()


#lita de productos

# lista de productos
lista_comidas = ['pollo', 'coredero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

#generar items de comida
variables_comida=[]
cuadros_comida=[]
texto_comida = []
contador = 0
for comida in lista_comidas:
    #creacion de los checkbuttons
    variables_comida.append('')
    variables_comida[contador]= IntVar()
    comida= Checkbutton(panel_comidas,
                        text= comida.title(),
                        font =('Dosis', 19, "bold"),
                        onvalue= 1, offvalue= 0,
                        variable= variables_comida[contador] )
    comida.grid(row= contador,
                column=0,
                sticky=W) 
    #crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    cuadros_comida[contador] = Entry ( panel_comidas, 
                                    font =('Dosis', 19, "bold"),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable= texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)


    contador += 1

#generar items de bebida
variables_bebida=[]
cuadros_bebida=[]
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador]= IntVar()
    bebida= Checkbutton(panel_bebidas,
                        text= bebida.title(),  
                        font =('Dosis', 19, "bold"),
                        onvalue= 1,
                        offvalue= 0,
                        variable= variables_comida[contador] )
    bebida.grid(row= contador, column=0, sticky=W) 
    
    #crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    cuadros_bebida[contador] = Entry ( panel_bebidas, 
                                    font =('Dosis', 19, "bold"),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable= texto_comida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1
#generar items de postre
variables_postre=[]
cuadros_postre=[]
texto_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador]= IntVar()
    postre= Checkbutton(panel_postres,text= postre.title(),font =('Dosis', 19, "bold"), onvalue= 1, offvalue= 0, variable= variables_comida[contador] )
    postre.grid(row= contador, column=0, sticky=W) 
    #crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    cuadros_postre[contador] = Entry ( panel_postres, 
                                    font =('Dosis', 19, "bold"),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable= texto_comida[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    contador += 1

# evitar cierre

app.mainloop()

