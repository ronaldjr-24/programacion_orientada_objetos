# Aplicación GUI para Gestión de Tareas con Atajos de Teclado
import tkinter as tk

def add_task(event=None):
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def complete_task(event=None):
    try:
        selected_task_index = task_listbox.curselection()[0]
        selected_task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"[Completada] {selected_task}")
    except IndexError:
        pass

def delete_task(event=None):
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        pass

def close_app(event=None):
    root.quit()

root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")
root.config(bg='peachpuff')  # Fondo de color durazno

# Campo de entrada de tareas
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Botón para añadir tarea
add_button = tk.Button(root, text="Añadir Tarea", command=add_task, bg='green', fg='white')
add_button.pack(pady=5)

# Botón para marcar como completada
complete_button = tk.Button(root, text="Marcar como Completada", command=complete_task, bg='blue', fg='white')
complete_button.pack(pady=5)

# Botón para eliminar tarea
delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task, bg='red', fg='white')
delete_button.pack(pady=5)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=20)

# Atajos de teclado
root.bind('<Return>', add_task)  # Tecla Enter para añadir tarea
root.bind('<Control-c>', complete_task)  # Control + C para marcar como completada
root.bind('<c>', complete_task)  # Tecla C para marcar como completada
root.bind('<Delete>', delete_task)  # Tecla Delete para eliminar tarea
root.bind('d', delete_task)  # Tecla D para eliminar tarea
root.bind('<Escape>', close_app)  # Tecla Escape para salir
root.bind('<Control-q>', close_app)  # Control + Q para salir

root.mainloop()
