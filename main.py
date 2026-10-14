import customtkinter as ctk
import os
import sys
import random

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Lights Out")
        self.configure(fg_color="#0F1218")
        self.geometry("800x600")
        ctk.CTkLabel(self, text="Lights Out", font=("Arial", 32)).pack(pady=(28, 4))

        self.board = ctk.CTkFrame(
            self,
            fg_color="#1A1F2E",
            corner_radius=20,
            border_width=1,
            border_color="#2A3145",
        )
        self.board.pack(pady=16)

        self.grid_frame = ctk.CTkFrame(self.board, fg_color="transparent")
        self.grid_frame.pack(padx=6, pady=6)

        self.buttons = []
        self.lights = []

        for row in range (5):
            self.buttons.append([])
            self.lights.append([])
            for column in range (5):
                self.lights[row].append(True)
                button = ctk.CTkButton(self.grid_frame, text="", width=62, height=62, fg_color="transparent", corner_radius=10, border_width=2, border_color="#3a3a3c", command=lambda r=row, c=column: self.press(r, c))
                button.grid(row=row, column=column, padx=4, pady=4)
                self.buttons[row].append(button)
                self.paint(row, column)


        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 20), text_color="#3DDC97")
        self.result_label.pack(pady=8)

        modes = ctk.CTkFrame(self, fg_color="transparent")
        modes.pack(pady=8)

        for text, command in (("All on", self.all_on), ("Scrambled", self.scramble)):
            ctk.CTkButton(
                modes,
                text=text,
                width=140,
                height=40,
                corner_radius=12,
                fg_color="#1A1F2E",
                hover_color="#2A3145",
                border_width=1,
                border_color="#2A3145",
                command=command,
            ).pack(side="left", padx=6)

    def scramble(self):
        for row in range(5):
            for column in range(5):
                self.lights[row][column] = False
                self.paint(row, column)

        spots = []
        for row in range(5):
            for column in range(5):
                spots.append((row, column))
        random.shuffle(spots)

        for row, column in spots[:10]:
            self.press(row, column)

        self.result_label.configure(text="", fg_color="transparent")

    def all_on(self):
        for row in range(5):
            for column in range(5):
                self.lights[row][column] = True
                self.paint(row, column)
        self.result_label.configure(text="", fg_color="transparent")
        
    def press(self, row, column):
        self.toggle(row, column)
        self.toggle(row - 1, column)
        self.toggle(row + 1, column)
        self.toggle(row, column - 1)
        self.toggle(row, column + 1)
        if self.check_win():
            self.result_label.configure(text="You win!", text_color="green", fg_color="transparent")
            self.confetti()
        else:
            self.result_label.configure(text="", fg_color="transparent")

    def check_win(self):
        for row in range(5):
            for column in range(5):
                if self.lights[row][column]:
                    return False
        return True


    def toggle(self, row, column):
        if row < 0 or row > 4 or column < 0 or column > 4:
            return
        self.lights[row][column] = not self.lights[row][column]
        self.paint(row, column)

    def paint(self, row, column):
        if self.lights[row][column]:
            color = "#3DDC97"
            hover = "#34c486"
        else:
            color = "#12161F"
            hover = "#1a2030"
        self.buttons[row][column].configure(fg_color=color, hover_color=hover)

    def confetti(self):
        colors = ["#3DDC97", "#f6e58d", "#ff6b6b", "#7B61FF", "#ffffff"]
        pieces = []
        width = self.winfo_width()
        height = self.winfo_height()

        for _ in range(40):
            piece = ctk.CTkFrame(
                self,
                width=8,
                height=14,
                fg_color=random.choice(colors),
                corner_radius=2,
            )
            x = random.randint(20, max(21, width - 20))
            y = random.randint(-220, -20)
            speed = random.randint(6, 12)
            piece.place(x=x, y=y)
            pieces.append([piece, x, y, speed])

        def fall():
            still_falling = []
            for piece in pieces:
                piece[2] += piece[3]
                if piece[2] < height:
                    piece[0].place(x=piece[1], y=piece[2])
                    still_falling.append(piece)
                else:
                    piece[0].destroy()
            pieces[:] = still_falling
            if pieces:
                self.after(30, fall)

        fall()

app = App()
app.mainloop()




