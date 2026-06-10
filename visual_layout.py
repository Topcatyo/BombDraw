import random
import tkinter as tk
import time
import threading
import os

# Define the mauve color (darker shade)
MAUVE_BG = '#6e4b7c'  # Main background
MAUVE_BG_DARKER = '#4b3354'  # Lower background for cutout effect

class MainWindow(tk.Tk):
    def __init__(self, prompt_text=None, prompt_generator=None):
        super().__init__()
        self.title('BombDraw!')
        self.geometry('1000x500')
        self.configure(bg=MAUVE_BG)
        self.prompt_text = prompt_text or '[Drawing prompt will appear here]'
        self.prompt_generator = prompt_generator
        # Create a canvas for custom drawing
        self.canvas = tk.Canvas(self, width=1000, height=500, highlightthickness=0, bg=MAUVE_BG)
        self.canvas.pack(fill='both', expand=True)
        # Draw the cutout (rounded rectangle effect)
        self.cutout_y = 180
        self.cutout_height = 180  # Increased from 140 to 180 to fit 3 lines comfortably
        self.cutout_radius = 40
        self.draw_background()
        # Add 'Draw' label above the cutout
        self.draw_label = self.canvas.create_text(500, self.cutout_y - 40, text='Draw', font=('Arial', 38, 'bold'), fill='white', justify='center')
        # Add text item for prompt inside the cutout, top-aligned, without unsupported spacing options
        self.prompt_item = self.canvas.create_text(500, self.cutout_y + 20, text='', font=('Arial', 32, 'bold'), fill='white', justify='center', width=900, anchor='n')
        # Change button text to 'Roll'
        self.roll_button = tk.Button(self, text='Roll', font=('Arial', 16, 'bold'), command=self.roll_again)
        self.roll_button_window = self.canvas.create_window(500, 420, window=self.roll_button)
        # Do not start cycling effect automatically
        # Show placeholder text until roll is pressed
        self.canvas.itemconfig(self.prompt_item, text='[What will it be?]')
        self.has_rolled = False

    def draw_background(self):
        # Draw lower background
        self.canvas.create_rectangle(0, 0, 1000, 500, fill=MAUVE_BG, outline='')
        self.canvas.create_rectangle(0, self.cutout_y, 1000, self.cutout_y + self.cutout_height, fill=MAUVE_BG_DARKER, outline='')
        # Optionally, add rounded corners to the cutout (simulate with ovals)
        r = self.cutout_radius
        y = self.cutout_y
        h = self.cutout_height
        self.canvas.create_oval(0, y, 2*r, y+2*r, fill=MAUVE_BG_DARKER, outline=MAUVE_BG_DARKER)
        self.canvas.create_oval(1000-2*r, y, 1000, y+2*r, fill=MAUVE_BG_DARKER, outline=MAUVE_BG_DARKER)
        self.canvas.create_oval(0, y+h-2*r, 2*r, y+h, fill=MAUVE_BG_DARKER, outline=MAUVE_BG_DARKER)
        self.canvas.create_oval(1000-2*r, y+h-2*r, 1000, y+h, fill=MAUVE_BG_DARKER, outline=MAUVE_BG_DARKER)

    def roll_again(self):
        if self.prompt_generator:
            self.prompt_text = self.prompt_generator()
            self.has_rolled = True
            self.start_cycle()

    def set_prompt_text(self, text):
        # Set the prompt text, letting Tkinter wrap it (width=900)
        self.canvas.itemconfig(self.prompt_item, text=text)

    def cycle_next(self):
        if self.cycle_count < len(self.cycle_delays):
            prompt = self.prompt_generator()
            self.cycle_prompts.append(prompt)
            self.canvas.itemconfig(self.prompt_item, text=prompt)
            delay = self.cycle_delays[self.cycle_count]
            self.cycle_count += 1
            self.after(delay, self.cycle_next)
        else:
            self.set_prompt_text(self.final_prompt)

    def start_cycle(self):
        if not self.has_rolled or not self.prompt_generator:
            self.canvas.itemconfig(self.prompt_item, text='[Press Roll to generate a prompt]')
            return
        self.cycle_count = 0
        self.max_cycles = 30
        self.cycle_delays = [30]*10 + [60]*8 + [120]*6 + [200]*4 + [400, 600]  # ms delays
        self.cycle_prompts = []
        # Remove 'Draw' from the final prompt
        prompt = self.prompt_text
        self.final_prompt = prompt
        self.has_rolled = False  # Reset so you must click again for next roll
        self.cycle_next()

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()