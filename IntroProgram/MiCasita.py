import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi casita con jardin")
ventana.geometry("800x600")

# espacio para dibujar
canvas = tk.Canvas(ventana, width=700, height=700, bg="skyblue")
canvas.pack()

# Dibujar el sol amarillo
canvas.create_oval (50, 50, 150, 150, fill="yellow", outline="orange")

# Cuerpo de la casa, color rosa
canvas.create_rectangle(300, 300, 500, 500, fill="pink", outline="black")   

#Techo
canvas.create_polygon(280, 300, 400, 200, 520, 300, fill="brown", outline="black")

# Chimenea café
canvas.create_rectangle(430, 180, 460, 250, fill="saddlebrown", outline="black")

# Puerta
canvas.create_rectangle(370, 400, 430, 500, fill="saddlebrown", outline="black")

# Ventanas 
canvas.create_rectangle(320, 340, 360, 380, fill="white")
canvas.create_rectangle(440, 340, 480, 380, fill="white")

# Jardin afuera de la casa
# Pasto verde
canvas.create_rectangle(0, 500, 800, 600, fill="lightgreen", outline="")

# Rosas rojas
rosas_pos = [(200, 520), (250, 540), (600, 530), (650, 520), (550, 550)]
for (x, y) in rosas_pos:
    canvas.create_oval(x, y, x+20, y+20, fill="red", outline="darkred")
    canvas.create_line(x+10, y+20, x+10, y+40, fill="green", width=3)

#Saludo
canvas.create_text(400, 100, text="¡Buenos días Nelly, excelente día!", font=("Comic Sans MS", 25, "bold"), fill="purple")

# Iniciar la ventana
ventana.mainloop()
