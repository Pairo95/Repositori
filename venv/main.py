import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time

class DungeonGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🏰 Masmorres de Python 🐍")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(False, False)
        
        # Estat del joc
        self.lives = 3
        self.score = 0
        self.current_room = 0
        self.player_pos = [100, 100]
        self.in_battle = False
        self.rooms_completed = [False] * 5
        
        # Posicions de les sales
        self.room_positions = [
            (150, 150), (350, 150), (550, 150),
            (250, 300), (450, 300)
        ]
        
        # Reptes de programació
        self.challenges = [
            {
                "title": "Salutació Bàsica",
                "description": "Escriu codi que imprimeixi: Hola enemic!",
                "solution": 'print("Hola enemic!")',
                "hint": "Usa print() amb el text entre cometes",
                "enemy": "👹 Goblin"
            },
            {
                "title": "Càlcul Simple",
                "description": "Calcula 25 + 15 i imprimeix el resultat",
                "solution": "print(25 + 15)",
                "hint": "Pots fer operacions dins de print()",
                "enemy": "🧌 Troll"
            },
            {
                "title": "Condició IF",
                "description": "Si x = 50 i x > 30, imprimeix 'Gran', sinó 'Petit'",
                "solution": "x = 50\nif x > 30:\n    print('Gran')\nelse:\n    print('Petit')",
                "hint": "Usa if/else amb la variable x",
                "enemy": "👻 Fantasma"
            },
            {
                "title": "Bucle WHILE",
                "description": "Conta del 1 al 3 amb while i imprimeix cada número",
                "solution": "i = 1\nwhile i <= 3:\n    print(i)\n    i += 1",
                "hint": "Comença amb i=1, usa while i <= 3",
                "enemy": "🐉 Drac"
            },
            {
                "title": "Bucle FOR",
                "description": "Imprimeix cada lletra de la paraula 'HERO'",
                "solution": "for lletra in 'HERO':\n    print(lletra)",
                "hint": "Usa for lletra in 'HERO':",
                "enemy": "💀 Rei Esquelet"
            }
        ]
        
        self.setup_ui()
        self.show_summary()
        
    def setup_ui(self):
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg='#1a1a2e')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Canvas per al mapa
        self.canvas = tk.Canvas(self.main_frame, width=700, height=400, bg='#2c3e50', highlightthickness=2, highlightbackground='#34495e')
        self.canvas.pack(side=tk.LEFT, padx=(0, 20))
        
        # Frame lateral dret
        self.side_frame = tk.Frame(self.main_frame, bg='#1a1a2e', width=250)
        self.side_frame.pack(side=tk.RIGHT, fill=tk.Y)
        self.side_frame.pack_propagate(False)
        
        # Estadístiques
        stats_frame = tk.Frame(self.side_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(stats_frame, text="📊 ESTADÍSTIQUES", font=('Arial', 12, 'bold'), 
                bg='#34495e', fg='white').pack(pady=5)
        
        self.lives_label = tk.Label(stats_frame, text="❤️ Vides: 3", font=('Arial', 10), 
                                   bg='#34495e', fg='#e74c3c')
        self.lives_label.pack()
        
        self.score_label = tk.Label(stats_frame, text="⭐ Puntuació: 0", font=('Arial', 10), 
                                   bg='#34495e', fg='#f39c12')
        self.score_label.pack()
        
        self.room_label = tk.Label(stats_frame, text="🏰 Sala: 0/5", font=('Arial', 10), 
                                  bg='#34495e', fg='#3498db')
        self.room_label.pack(pady=(0, 5))
        
        # Àrea d'informació
        self.info_frame = tk.Frame(self.side_frame, bg='#8e44ad', relief=tk.RAISED, bd=2)
        self.info_frame.pack(fill=tk.BOTH, expand=True)
        
        # Controls
        controls_frame = tk.Frame(self.side_frame, bg='#1a1a2e')
        controls_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(controls_frame, text="🎮 CONTROLS", font=('Arial', 10, 'bold'), 
                bg='#1a1a2e', fg='white').pack()
        tk.Label(controls_frame, text="WASD o Fletxes per moure", font=('Arial', 8), 
                bg='#1a1a2e', fg='#bdc3c7').pack()
        tk.Label(controls_frame, text="Espai per entrar a sales", font=('Arial', 8), 
                bg='#1a1a2e', fg='#bdc3c7').pack()
        
        # Bind controls
        self.root.bind('<Key>', self.handle_keypress)
        self.root.focus_set()
        
    def show_summary(self):
        summary_window = tk.Toplevel(self.root)
        summary_window.title("📚 Recordatori de Python")
        summary_window.geometry("600x500")
        summary_window.configure(bg='#2c3e50')
        summary_window.resizable(False, False)
        
        # Centrar la finestra
        summary_window.transient(self.root)
        summary_window.grab_set()
        
        tk.Label(summary_window, text="📚 Recordatori ràpid de Python", 
                font=('Arial', 16, 'bold'), bg='#2c3e50', fg='#3498db').pack(pady=10)
        
        concepts = [
            ("🔹 print()", "Mostra text a la pantalla\nExemple: print('Hola')"),
            ("🔹 Variables", "Emmagatzemen dades\nExemple: x = 10"),
            ("🔹 if/else", "Decisions condicionals\nif x > 5:\n    print('Gran')\nelse:\n    print('Petit')"),
            ("🔹 while", "Repeteix mentre sigui cert\ni = 1\nwhile i <= 3:\n    print(i)\n    i += 1"),
            ("🔹 for", "Repeteix per cada element\nfor lletra in 'HOLA':\n    print(lletra)")
        ]
        
        for title, desc in concepts:
            frame = tk.Frame(summary_window, bg='#34495e', relief=tk.RAISED, bd=1)
            frame.pack(fill=tk.X, padx=20, pady=5)
            
            tk.Label(frame, text=title, font=('Arial', 12, 'bold'), 
                    bg='#34495e', fg='#e67e22', anchor='w').pack(fill=tk.X, padx=10, pady=2)
            tk.Label(frame, text=desc, font=('Courier', 9), 
                    bg='#34495e', fg='white', anchor='w', justify=tk.LEFT).pack(fill=tk.X, padx=10, pady=2)
        
        start_btn = tk.Button(summary_window, text="🚀 Començar Aventura!", 
                             font=('Arial', 14, 'bold'), bg='#e74c3c', fg='white',
                             command=lambda: [summary_window.destroy(), self.start_game()])
        start_btn.pack(pady=20)
        
    def start_game(self):
        self.draw_map()
        self.update_display()
        
    def draw_map(self):
        self.canvas.delete("all")
        
        # Dibuixar passadissos
        corridors = [
            (200, 175, 300, 175),  # Horitzontal superior esquerra
            (400, 175, 500, 175),  # Horitzontal superior dreta
            (275, 200, 275, 250),  # Vertical esquerra
            (425, 200, 425, 250),  # Vertical dreta
            (300, 325, 400, 325)   # Horitzontal inferior
        ]
        
        for x1, y1, x2, y2 in corridors:
            self.canvas.create_line(x1, y1, x2, y2, fill='#95a5a6', width=4)
        
        # Dibuixar sales
        for i, (x, y) in enumerate(self.room_positions):
            color = '#27ae60' if self.rooms_completed[i] else '#3498db'
            if i == 4:  # Sala final
                color = '#8e44ad'
            
            self.canvas.create_rectangle(x-30, y-20, x+30, y+20, 
                                       fill=color, outline='#2c3e50', width=2)
            
            text = f"S{i+1}"
            if i == 4:
                text = "👑"
            
            self.canvas.create_text(x, y, text=text, fill='white', 
                                  font=('Arial', 10, 'bold'))
        
        # Dibuixar jugador
        self.canvas.create_oval(self.player_pos[0]-15, self.player_pos[1]-15,
                               self.player_pos[0]+15, self.player_pos[1]+15,
                               fill='#f39c12', outline='#e67e22', width=3)
        self.canvas.create_text(self.player_pos[0], self.player_pos[1], 
                               text='🧙', font=('Arial', 12))
        
    def handle_keypress(self, event):
        if self.in_battle:
            return
            
        key = event.keysym.lower()
        dx, dy = 0, 0
        
        if key in ['w', 'up']:
            dy = -10
        elif key in ['s', 'down']:
            dy = 10
        elif key in ['a', 'left']:
            dx = -10
        elif key in ['d', 'right']:
            dx = 10
        elif key == 'space':
            self.check_room_entry()
            return
        
        # Moure jugador
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        
        if 50 <= new_x <= 650 and 50 <= new_y <= 350:
            self.player_pos[0] = new_x
            self.player_pos[1] = new_y
            self.draw_map()
            
    def check_room_entry(self):
        for i, (room_x, room_y) in enumerate(self.room_positions):
            distance = ((self.player_pos[0] - room_x) ** 2 + (self.player_pos[1] - room_y) ** 2) ** 0.5
            if distance < 50:
                if not self.rooms_completed[i]:
                    self.enter_room(i)
                else:
                    messagebox.showinfo("Sala completada", "Ja has completat aquesta sala!")
                return
        
        messagebox.showinfo("Cap sala", "No hi ha cap sala aquí. Acosta't més a una sala i prem Espai.")
    
    def enter_room(self, room_id):
        self.in_battle = True
        self.current_room = room_id
        challenge = self.challenges[room_id]
        
        # Crear finestra de batalla
        self.battle_window = tk.Toplevel(self.root)
        self.battle_window.title(f"⚔️ Batalla - {challenge['enemy']}")
        self.battle_window.geometry("700x600")
        self.battle_window.configure(bg='#2c3e50')
        self.battle_window.resizable(False, False)
        self.battle_window.transient(self.root)
        self.battle_window.grab_set()
        
        # Enemic
        enemy_frame = tk.Frame(self.battle_window, bg='#e74c3c', relief=tk.RAISED, bd=3)
        enemy_frame.pack(fill=tk.X, pady=10, padx=20)
        
        tk.Label(enemy_frame, text=challenge['enemy'], font=('Arial', 24), 
                bg='#e74c3c', fg='white').pack(pady=10)
        
        # Repte
        challenge_frame = tk.Frame(self.battle_window, bg='#8e44ad', relief=tk.RAISED, bd=2)
        challenge_frame.pack(fill=tk.X, pady=10, padx=20)
        
        tk.Label(challenge_frame, text=challenge['title'], font=('Arial', 16, 'bold'), 
                bg='#8e44ad', fg='white').pack(pady=5)
        tk.Label(challenge_frame, text=challenge['description'], font=('Arial', 12), 
                bg='#8e44ad', fg='white', wraplength=600).pack(pady=5)
        
        # Àrea de codi
        code_frame = tk.Frame(self.battle_window, bg='#34495e', relief=tk.RAISED, bd=2)
        code_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)
        
        tk.Label(code_frame, text="💻 Escriu el teu codi Python:", font=('Arial', 12, 'bold'), 
                bg='#34495e', fg='white').pack(pady=5)
        
        self.code_text = tk.Text(code_frame, height=8, font=('Courier', 11), 
                                bg='#2c3e50', fg='white', insertbackground='white')
        self.code_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Botons
        btn_frame = tk.Frame(self.battle_window, bg='#2c3e50')
        btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(btn_frame, text="⚔️ Atacar!", font=('Arial', 12, 'bold'), 
                 bg='#e74c3c', fg='white', command=self.check_solution).pack(side=tk.LEFT, padx=20)
        
        tk.Button(btn_frame, text="💡 Pista", font=('Arial', 12), 
                 bg='#f39c12', fg='white', command=self.show_hint).pack(side=tk.LEFT, padx=10)
        
        tk.Button(btn_frame, text="🚪 Sortir", font=('Arial', 12), 
                 bg='#7f8c8d', fg='white', command=self.exit_battle).pack(side=tk.RIGHT, padx=20)
    
    def show_hint(self):
        challenge = self.challenges[self.current_room]
        messagebox.showinfo("💡 Pista", challenge['hint'])
    
    def check_solution(self):
        user_code = self.code_text.get("1.0", tk.END).strip()
        challenge = self.challenges[self.current_room]
        
        # Normalitzar codi per comparació
        user_normalized = user_code.replace(' ', '').replace('\n', '').lower()
        solution_normalized = challenge['solution'].replace(' ', '').replace('\n', '').lower()
        
        if user_normalized == solution_normalized or self.check_code_logic(user_code, challenge):
            # Victòria!
            self.score += 100
            self.rooms_completed[self.current_room] = True
            messagebox.showinfo("🎉 Victòria!", "Has derrotat l'enemic!\n+100 punts")
            self.exit_battle()
            
            if all(self.rooms_completed):
                self.game_won()
        else:
            # Error!
            self.lives -= 1
            if self.lives <= 0:
                self.game_over()
            else:
                messagebox.showerror("❌ Error!", f"Codi incorrecte! L'enemic t'ataca!\nVides restants: {self.lives}")
    
    def check_code_logic(self, code, challenge):
        # Verificació més flexible
        if challenge['title'] == "Salutació Bàsica":
            return 'print' in code and 'hola enemic' in code.lower()
        elif challenge['title'] == "Càlcul Simple":
            return 'print' in code and ('40' in code or '25+15' in code.replace(' ', ''))
        return False
    
    def exit_battle(self):
        self.in_battle = False
        self.battle_window.destroy()
        self.update_display()
        self.draw_map()
    
    def update_display(self):
        self.lives_label.config(text=f"❤️ Vides: {self.lives}")
        self.score_label.config(text=f"⭐ Puntuació: {self.score}")
        completed = sum(self.rooms_completed)
        self.room_label.config(text=f"🏰 Sales: {completed}/5")
    
    def game_won(self):
        messagebox.showinfo("🎉 HAS GUANYAT!", f"Has conquerit totes les masmorres!\nPuntuació final: {self.score}")
        self.restart_game()
    
    def game_over(self):
        messagebox.showinfo("💀 GAME OVER", f"T'has quedat sense vides!\nPuntuació final: {self.score}")
        self.restart_game()
    
    def restart_game(self):
        self.lives = 3
        self.score = 0
        self.current_room = 0
        self.player_pos = [100, 100]
        self.in_battle = False
        self.rooms_completed = [False] * 5
        self.update_display()
        self.draw_map()
    
    def run(self):
        self.root.mainloop()

# Executar el joc
if __name__ == "__main__":
    game = DungeonGame()
    game.run()