# Aplicación GUI de listas de tarreas
import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Configuración del fondo y bordes
        self.root.configure(bg="orange")  # Fondo anaranjado

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task, bg="green", fg="white")  # Botón verde
        self.add_task_button.pack(pady=5)

        # Botón para marcar tarea como completada
        self.complete_task_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task, bg="green", fg="white")  # Botón verde
        self.complete_task_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task, bg="red", fg="white")  # Botón rojo
        self.delete_task_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Scrollbar para la lista de tareas
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Vincular la tecla Enter para añadir tareas
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Bordes negros para los widgets
        self.task_entry.config(highlightbackground="black", highlightthickness=2)
        self.task_listbox.config(highlightbackground="black", highlightthickness=2)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(END, task)
            self.task_entry.delete(0, END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            completed_task = f"{task} (Completada)"
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, completed_task)  # Reemplazar con el texto completado
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
