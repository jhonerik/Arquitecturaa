import tkinter as tk
from tkinter import ttk, messagebox
import math
import random
from datetime import datetime

class CalculadoraInteractiva:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🧮 Calculadora Súper Interactiva 🧮")
        self.root.geometry("500x600")
        self.root.configure(bg='#2C3E50')
        self.root.resizable(False, False)

        # Centrar ventana
        self.centrar_ventana()
        
        # Variables
        self.historial = []
        self.tema_actual = 0
        self.temas = [
            {'bg': '#2C3E50', 'fg': '#ECF0F1', 'btn': '#3498DB'},
            {'bg': '#8E44AD', 'fg': '#F8F9FA', 'btn': '#E74C3C'},
            {'bg': '#27AE60', 'fg': '#FFFFFF', 'btn': '#F39C12'},
            {'bg': '#34495E', 'fg': '#BDC3C7', 'btn': '#E67E22'}
        ]
        
        self.crear_interfaz()
        self.mensaje_bienvenida()
    
    def centrar_ventana(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        ancho = self.root.winfo_width()
        alto = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")
    
    def crear_interfaz(self):
        """Crea toda la interfaz de usuario"""
        # Título principal con animación
        self.titulo = tk.Label(
            self.root, 
            text="🧮 CALCULADORA MÁGICA 🧮",
            font=("Arial", 16, "bold"),
            bg=self.temas[self.tema_actual]['bg'],
            fg=self.temas[self.tema_actual]['fg']
        )
        self.titulo.pack(pady=10)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.temas[self.tema_actual]['bg'])
        main_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Entradas de números con efectos
        self.crear_entradas(main_frame)
        
        # Botones de operaciones con colores
        self.crear_botones_operaciones(main_frame)
        
        # Botones especiales
        self.crear_botones_especiales(main_frame)
        
        # Área de resultado
        self.crear_area_resultado(main_frame)
        
        # Historial
        self.crear_historial(main_frame)
        
        # Barra de estado
        self.crear_barra_estado()
    
    def crear_entradas(self, parent):
        """Crea las entradas para los números"""
        frame_entradas = tk.Frame(parent, bg=self.temas[self.tema_actual]['bg'])
        frame_entradas.pack(pady=10)
        
        tk.Label(frame_entradas, text="Primer número:", 
                font=("Arial", 12, "bold"),
                bg=self.temas[self.tema_actual]['bg'],
                fg=self.temas[self.tema_actual]['fg']).grid(row=0, column=0, padx=5, pady=5)
        
        self.entry1 = tk.Entry(frame_entradas, font=("Arial", 12), width=15, justify="center")
        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        self.entry1.bind('<KeyRelease>', self.animar_entrada)
        
        tk.Label(frame_entradas, text="Segundo número:", 
                font=("Arial", 12, "bold"),
                bg=self.temas[self.tema_actual]['bg'],
                fg=self.temas[self.tema_actual]['fg']).grid(row=1, column=0, padx=5, pady=5)
        
        self.entry2 = tk.Entry(frame_entradas, font=("Arial", 12), width=15, justify="center")
        self.entry2.grid(row=1, column=1, padx=5, pady=5)
        self.entry2.bind('<KeyRelease>', self.animar_entrada)
    
    def crear_botones_operaciones(self, parent):
        """Crea los botones de operaciones básicas"""
        frame_ops = tk.Frame(parent, bg=self.temas[self.tema_actual]['bg'])
        frame_ops.pack(pady=15)
        
        operaciones = [
            ("➕ SUMAR", self.sumar, "#27AE60"),
            ("➖ RESTAR", self.restar, "#E74C3C"),
            ("✖️ MULTIPLICAR", self.multiplicar, "#8E44AD"),
            ("➗ DIVIDIR", self.dividir, "#F39C12")
        ]
        
        for i, (texto, comando, color) in enumerate(operaciones):
            btn = tk.Button(
                frame_ops, text=texto, command=comando,
                font=("Arial", 11, "bold"), width=15, height=2,
                bg=color, fg="white", relief="raised",
                cursor="hand2"
            )
            btn.grid(row=i//2, column=i%2, padx=8, pady=5)
            btn.bind("<Enter>", lambda e, b=btn: self.efecto_hover(b, True))
            btn.bind("<Leave>", lambda e, b=btn, c=color: self.efecto_hover(b, False, c))
    
    def crear_botones_especiales(self, parent):
        """Crea botones para operaciones especiales"""
        frame_especial = tk.Frame(parent, bg=self.temas[self.tema_actual]['bg'])
        frame_especial.pack(pady=10)
        
        especiales = [
            ("🔢 POTENCIA", self.potencia),
            ("√ RAÍZ CUADRADA", self.raiz_cuadrada),
            ("🎲 NÚMERO RANDOM", self.numero_random),
            ("🎨 CAMBIAR TEMA", self.cambiar_tema)
        ]
        
        for i, (texto, comando) in enumerate(especiales):
            btn = tk.Button(
                frame_especial, text=texto, command=comando,
                font=("Arial", 9, "bold"), width=18,
                bg=self.temas[self.tema_actual]['btn'], fg="white",
                cursor="hand2"
            )
            btn.grid(row=i//2, column=i%2, padx=5, pady=3)
    
    def crear_area_resultado(self, parent):
        """Crea el área para mostrar resultados"""
        frame_resultado = tk.Frame(parent, bg=self.temas[self.tema_actual]['bg'])
        frame_resultado.pack(pady=15)
        
        tk.Label(frame_resultado, text="🎯 RESULTADO:", 
                font=("Arial", 14, "bold"),
                bg=self.temas[self.tema_actual]['bg'],
                fg=self.temas[self.tema_actual]['fg']).pack()
        
        self.resultado_label = tk.Label(
            frame_resultado, text="Esperando operación...",
            font=("Arial", 16, "bold"), 
            bg="#ECF0F1", fg="#2C3E50",
            relief="sunken", padx=20, pady=10, width=30
        )
        self.resultado_label.pack(pady=5)
    
    def crear_historial(self, parent):
        """Crea el área de historial"""
        frame_historial = tk.Frame(parent, bg=self.temas[self.tema_actual]['bg'])
        frame_historial.pack(pady=10, fill="both", expand=True)
        
        tk.Label(frame_historial, text="📜 HISTORIAL DE OPERACIONES:", 
                font=("Arial", 12, "bold"),
                bg=self.temas[self.tema_actual]['bg'],
                fg=self.temas[self.tema_actual]['fg']).pack()
        
        # Scrollbar para el historial
        frame_scroll = tk.Frame(frame_historial)
        frame_scroll.pack(fill="both", expand=True, padx=10, pady=5)
        
        scrollbar = tk.Scrollbar(frame_scroll)
        scrollbar.pack(side="right", fill="y")
        
        self.historial_text = tk.Listbox(
            frame_scroll, font=("Consolas", 10),
            height=6, yscrollcommand=scrollbar.set
        )
        self.historial_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.historial_text.yview)
        
        # Botón limpiar historial
        btn_limpiar = tk.Button(
            frame_historial, text="🗑️ Limpiar Historial",
            command=self.limpiar_historial,
            bg="#E74C3C", fg="white", font=("Arial", 10, "bold")
        )
        btn_limpiar.pack(pady=5)
    
    def crear_barra_estado(self):
        """Crea la barra de estado"""
        self.status_bar = tk.Label(
            self.root, text=f"Calculadora lista • {datetime.now().strftime('%H:%M:%S')}",
            relief="sunken", anchor="w",
            bg="#34495E", fg="#ECF0F1", font=("Arial", 9)
        )
        self.status_bar.pack(side="bottom", fill="x")
        self.actualizar_hora()
    
    def obtener_numeros(self):
        """Obtiene y valida los números de las entradas"""
        try:
            num1 = float(self.entry1.get()) if self.entry1.get() else 0
            num2 = float(self.entry2.get()) if self.entry2.get() else 0
            return num1, num2, True
        except ValueError:
            messagebox.showerror("❌ Error", "Por favor, ingrese números válidos")
            return 0, 0, False
    
    def agregar_historial(self, operacion, resultado):
        """Agrega una operación al historial"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        entrada = f"[{timestamp}] {operacion} = {resultado}"
        self.historial.append(entrada)
        self.historial_text.insert(tk.END, entrada)
        self.historial_text.see(tk.END)
    
    def mostrar_resultado(self, resultado, operacion):
        """Muestra el resultado con efectos especiales"""
        self.resultado_label.config(
            text=f"{resultado}",
            bg="#27AE60", fg="white"
        )
        self.agregar_historial(operacion, resultado)
        self.animar_resultado()
        self.mostrar_mensaje_exito(resultado)
    
    def animar_resultado(self):
        """Anima el resultado con cambio de colores"""
        colores = ["#27AE60", "#2ECC71", "#27AE60", "#58D68D"]
        for i, color in enumerate(colores):
            self.root.after(i * 200, lambda c=color: self.resultado_label.config(bg=c))
    
    def animar_entrada(self, event):
        """Anima las entradas cuando se escriben"""
        widget = event.widget
        if widget.get():
            widget.config(bg="#D5DBDB", fg="#2C3E50")
        else:
            widget.config(bg="white", fg="black")
    
    def efecto_hover(self, boton, entrar, color_original=None):
        """Efecto hover para botones"""
        if entrar:
            boton.config(relief="sunken", bg="#F8C471")
        else:
            boton.config(relief="raised", bg=color_original or self.temas[self.tema_actual]['btn'])
    
    # Operaciones matemáticas
    def sumar(self):
        num1, num2, valido = self.obtener_numeros()
        if valido:
            resultado = num1 + num2
            self.mostrar_resultado(resultado, f"{num1} + {num2}")
    
    def restar(self):
        num1, num2, valido = self.obtener_numeros()
        if valido:
            resultado = num1 - num2
            self.mostrar_resultado(resultado, f"{num1} - {num2}")
    
    def multiplicar(self):
        num1, num2, valido = self.obtener_numeros()
        if valido:
            resultado = num1 * num2
            self.mostrar_resultado(resultado, f"{num1} × {num2}")
    
    def dividir(self):
        num1, num2, valido = self.obtener_numeros()
        if valido:
            if num2 == 0:
                messagebox.showerror("❌ Error", "¡No se puede dividir por cero!")
                self.explosion_error()
            else:
                resultado = num1 / num2
                self.mostrar_resultado(resultado, f"{num1} ÷ {num2}")
    
    def potencia(self):
        num1, num2, valido = self.obtener_numeros()
        if valido:
            try:
                resultado = num1 ** num2
                self.mostrar_resultado(resultado, f"{num1} ^ {num2}")
            except OverflowError:
                messagebox.showwarning("⚠️ Advertencia", "Resultado demasiado grande")
    
    def raiz_cuadrada(self):
        num1, _, valido = self.obtener_numeros()
        if valido:
            if num1 < 0:
                messagebox.showerror("❌ Error", "No se puede calcular raíz de número negativo")
            else:
                resultado = math.sqrt(num1)
                self.mostrar_resultado(resultado, f"√{num1}")
    
    def numero_random(self):
        numero = random.randint(1, 1000)
        self.entry1.delete(0, tk.END)
        self.entry1.insert(0, str(numero))
        messagebox.showinfo("🎲 Número Random", f"¡Número generado: {numero}!")
    
    def cambiar_tema(self):
        """Cambia el tema de colores"""
        self.tema_actual = (self.tema_actual + 1) % len(self.temas)
        tema = self.temas[self.tema_actual]
        
        self.root.configure(bg=tema['bg'])
        # Aquí actualizarías todos los widgets con los nuevos colores
        messagebox.showinfo("🎨 Tema Cambiado", "¡Nuevo tema aplicado!")
    
    def limpiar_historial(self):
        """Limpia el historial de operaciones"""
        respuesta = messagebox.askyesno("🗑️ Limpiar", "¿Está seguro de limpiar el historial?")
        if respuesta:
            self.historial.clear()
            self.historial_text.delete(0, tk.END)
            messagebox.showinfo("✅ Limpio", "Historial limpiado exitosamente")
    
    def explosion_error(self):
        """Efecto visual para errores"""
        for i in range(5):
            self.root.after(i * 100, lambda: self.titulo.config(fg="red"))
            self.root.after(i * 100 + 50, lambda: self.titulo.config(fg=self.temas[self.tema_actual]['fg']))
    
    def mostrar_mensaje_exito(self, resultado):
        """Muestra mensajes motivacionales"""
        mensajes = [
            f"¡Excelente! El resultado es {resultado} 🎉",
            f"¡Perfecto! Has calculado {resultado} ⭐",
            f"¡Increíble! La respuesta es {resultado} 🚀",
            f"¡Fantástico! Obtuviste {resultado} 💫"
        ]
        mensaje = random.choice(mensajes)
        # Mostrar brevemente en la barra de estado
        self.status_bar.config(text=mensaje)
        self.root.after(3000, lambda: self.status_bar.config(
            text=f"Calculadora lista • {datetime.now().strftime('%H:%M:%S')}"
        ))
    
    def mensaje_bienvenida(self):
        """Muestra mensaje de bienvenida"""
        messagebox.showinfo(
            "🎉 ¡Bienvenido!", 
            "¡Bienvenido a la Calculadora Súper Interactiva!\n\n"
            "✨ Características:\n"
            "• Operaciones básicas y avanzadas\n"
            "• Historial de operaciones\n"
            "• Múltiples temas de colores\n"
            "• Efectos visuales y animaciones\n"
            "• ¡Y mucho más!\n\n"
            "¡Disfruta calculando! 🧮"
        )
    
    def actualizar_hora(self):
        """Actualiza la hora en la barra de estado"""
        if "Calculadora lista" in self.status_bar.cget("text"):
            hora = datetime.now().strftime('%H:%M:%S')
            self.status_bar.config(text=f"Calculadora lista • {hora}")
        self.root.after(1000, self.actualizar_hora)
    
    def ejecutar(self):
        """Inicia la aplicación"""
        self.root.mainloop()

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    calculadora = CalculadoraInteractiva()
    calculadora.ejecutar()

    # Se aplicaron nuevas mejoras a la calculadora

    # Se agrego la ejecucion de los programas 
    