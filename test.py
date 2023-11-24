import tkinter as tk

def copy_text_to_clipboard(event=None):
    # Get the selected text from the Text widget
    selected_text = text_widget.get("1.0", "end-1c")

    # Copy the selected text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(selected_text)
    root.update()

# Create the main window
root = tk.Tk()
root.title("Copy Text to Clipboard Example")

# Create a Text widget
text_widget = tk.Text(root, wrap="word", height=10, width=40)
text_widget.pack(padx=10, pady=10)

# Insert some text into the Text widget
text_widget.insert("1.0", "This is some sample text.\nYou can select and copy this text.")

# Bind the Ctrl+C shortcut to the copy_text_to_clipboard function
text_widget.bind("<Control-c>", copy_text_to_clipboard)

# Run the Tkinter event loop
root.mainloop()

