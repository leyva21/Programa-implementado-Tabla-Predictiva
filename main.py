import tkinter as tk
from tkinter import scrolledtext
from auto_pila import AutoPila

class MiVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Gramática")
        
        self.text_edit = scrolledtext.ScrolledText(root, width=45, height=10)
        self.text_edit.pack(padx=10, pady=10)
        
        self.btn_verificar = tk.Button(root, text="Verificar", command=self.verificar)
        self.btn_verificar.pack(pady=5)
        
        self.text_resultado = scrolledtext.ScrolledText(root, width=60, height=20)
        self.text_resultado.pack(padx=10, pady=10)
    
    def has_numbers(self, input_string):
        return any(char.isdigit() for char in input_string)
    
    def verificar(self):
        texto = self.text_edit.get("1.0", tk.END)
        analisis = AutoPila(texto)
        exito = analisis.analis()
        self.mostrar_recorrido(analisis.recorrido, exito)

        if self.has_numbers(texto):
            self.mostrar_error("La cadena contiene números. No es válida.")
            return
    def mostrar_error(self, mensaje):
        self.text_resultado.delete("1.0", tk.END)
        self.text_resultado.insert(tk.END, mensaje + "\n")
        
    def mostrar_recorrido(self, recorrido, exito):
        self.text_resultado.delete("1.0", tk.END)
        if exito:
            self.text_resultado.insert(tk.END, "Resultado de la pila:\n")
            for i, paso in enumerate(recorrido):
                self.text_resultado.insert(tk.END, f"Paso {i + 1}: {' '.join(paso)}\n")
            self.text_resultado.insert(tk.END, "Pila vacía: $\n")
            self.text_resultado.insert(tk.END, "La cadena es válida según la gramática\n")
            print("Pila vacía: $\n")
            print("La cadena es válida según la gramática\n")
        else:
            for i, paso in enumerate(recorrido):
                self.text_resultado.insert(tk.END, f"Paso {i + 1}: {' '.join(paso)}\n")
            if not recorrido[-1]:
                self.text_resultado.insert(tk.END, "\nLa cadena no es válida debido a la pila vacía\n")
            else:
                self.text_resultado.insert(tk.END, "\nLa cadena no es válida según la gramática\n")


root = tk.Tk()
app = MiVentana(root)
root.mainloop()

#function a (var s :boolean; a:string)
#function a (var s :boolean)
#function asdasd (var asdadsdas :string; asdsdasd:string)
#function asdasd (var asdadsdas :boolean; asdsdasd:boolean)
#function asdasd (var asdadsdas :string; asdsdasd:boolean)