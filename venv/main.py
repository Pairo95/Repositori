import random
import time

class CodeQuest:
    def __init__(self):
        self.vides = 3
        self.masmorra_actual = 1
        self.puntuacio = 0
        self.nom_jugador = ""
        
        # Definim les masmorres amb els seus desafiaments
        self.masmorres = {
            1: {
                "nom": "Masmorra de les Variables",
                "descripcio": "Aprèn a crear i utilitzar variables!",
                "desafiaments": [
                    {
                        "pregunta": "Com declares una variable 'nom' amb el valor 'Joan'?",
                        "opcions": ["nom = 'Joan'", "var nom = 'Joan'", "nom := 'Joan'", "declara nom = 'Joan'"],
                        "resposta_correcta": 0,
                        "explicacio": "En Python, declarem variables simplement amb el nom seguit de '=' i el valor."
                    },
                    {
                        "pregunta": "Què imprimirà: print(type(42))?",
                        "opcions": ["<class 'str'>", "<class 'int'>", "<class 'float'>", "42"],
                        "resposta_correcta": 1,
                        "explicacio": "42 és un nombre enter, per això type() retorna <class 'int'>."
                    }
                ]
            },
            2: {
                "nom": "Masmorra dels Bucles",
                "descripcio": "Domina els bucles for i while!",
                "desafiaments": [
                    {
                        "pregunta": "Com imprimeixes els números del 1 al 5?",
                        "opcions": [
                            "for i in range(1, 6): print(i)",
                            "for i in range(1, 5): print(i)",
                            "for i in range(5): print(i)",
                            "while i <= 5: print(i)"
                        ],
                        "resposta_correcta": 0,
                        "explicacio": "range(1, 6) genera números del 1 al 5 (el 6 no s'inclou)."
                    },
                    {
                        "pregunta": "Què fa 'break' dins un bucle?",
                        "opcions": [
                            "Pausa el bucle temporalment",
                            "Surt del bucle completament",
                            "Reinicia el bucle",
                            "No fa res"
                        ],
                        "resposta_correcta": 1,
                        "explicacio": "'break' surt del bucle immediatament, sense continuar les iteracions."
                    }
                ]
            },
            3: {
                "nom": "Masmorra de les Funcions",
                "descripcio": "Crea les teves pròpies funcions!",
                "desafiaments": [
                    {
                        "pregunta": "Com defineixes una funció que suma dos números?",
                        "opcions": [
                            "function suma(a, b): return a + b",
                            "def suma(a, b): return a + b",
                            "suma(a, b) = a + b",
                            "create suma(a, b): return a + b"
                        ],
                        "resposta_correcta": 1,
                        "explicacio": "En Python, utilitzem 'def' per definir funcions."
                    },
                    {
                        "pregunta": "Què retorna una funció sense 'return'?",
                        "opcions": ["0", "''", "None", "Error"],
                        "resposta_correcta": 2,
                        "explicacio": "Si una funció no té 'return', Python retorna automàticament 'None'."
                    }
                ]
            }
        }
    
    def mostrar_intro(self):
        print("=" * 50)
        print("🎮 BENVINGUT A CODE QUEST! 🎮")
        print("=" * 50)
        print("Un joc educatiu per aprendre Python!")
        print("Tens 3 vides per completar totes les masmorres.")
        print("Cada resposta correcta et dona 10 punts.")
        print("Cada resposta incorrecta et fa perdre una vida.")
        print("=" * 50)
        
        self.nom_jugador = input("Introdueix el teu nom: ").strip()
        if not self.nom_jugador:
            self.nom_jugador = "Aventurer"
        
        print(f"\nHola {self.nom_jugador}! Preparat per l'aventura? 🚀")
        input("Prem Enter per començar...")
    
    def mostrar_estat(self):
        print("\n" + "─" * 40)
        print(f"👤 Jugador: {self.nom_jugador}")
        print(f"❤️  Vides: {self.vides}")
        print(f"🏰 Masmorra: {self.masmorra_actual}")
        print(f"⭐ Puntuació: {self.puntuacio}")
        print("─" * 40)
    
    def mostrar_masmorra(self, num_masmorra):
        masmorra = self.masmorres[num_masmorra]
        print(f"\n🏰 {masmorra['nom']} 🏰")
        print(f"📝 {masmorra['descripcio']}")
        print("═" * 30)
    
    def fer_pregunta(self, desafiament):
        print(f"\n❓ {desafiament['pregunta']}")
        print()
        
        for i, opcio in enumerate(desafiament['opcions']):
            print(f"{i + 1}. {opcio}")
        
        while True:
            try:
                resposta = int(input("\nTrieu una opció (1-4): ")) - 1
                if 0 <= resposta < len(desafiament['opcions']):
                    break
                else:
                    print("❌ Opció no vàlida. Tria entre 1 i 4.")
            except ValueError:
                print("❌ Introdueix un número vàlid.")
        
        if resposta == desafiament['resposta_correcta']:
            print("✅ Correcte!")
            print(f"💡 {desafiament['explicacio']}")
            self.puntuacio += 10
            return True
        else:
            print("❌ Incorrecte!")
            print(f"📚 Resposta correcta: {desafiament['opcions'][desafiament['resposta_correcta']]}")
            print(f"💡 {desafiament['explicacio']}")
            self.vides -= 1
            return False
    
    def jugar_masmorra(self, num_masmorra):
        self.mostrar_masmorra(num_masmorra)
        masmorra = self.masmorres[num_masmorra]
        
        for i, desafiament in enumerate(masmorra['desafiaments']):
            print(f"\n🎯 Desafiament {i + 1}/{len(masmorra['desafiaments'])}")
            
            if not self.fer_pregunta(desafiament):
                if self.vides <= 0:
                    return False
                
                print(f"\n💔 Et queden {self.vides} vides.")
                input("Prem Enter per continuar...")
            else:
                time.sleep(1)
        
        print(f"\n🎉 Has completat la {masmorra['nom']}!")
        return True
    
    def mostrar_final(self, victoria=True):
        print("\n" + "=" * 50)
        if victoria:
            print("🏆 FELICITATS! HAS GUANYAT! 🏆")
            print("Has completat totes les masmorres!")
        else:
            print("💀 GAME OVER 💀")
            print("T'has quedat sense vides...")
        
        print(f"\n📊 PUNTUACIÓ FINAL:")
        print(f"👤 Jugador: {self.nom_jugador}")
        print(f"⭐ Puntuació: {self.puntuacio}")
        print(f"🏰 Masmorres completades: {self.masmorra_actual - 1}")
        print(f"❤️  Vides restants: {self.vides}")
        
        if victoria:
            if self.puntuacio >= 50:
                print("🌟 Ets un mestre de Python!")
            elif self.puntuacio >= 30:
                print("👍 Bon treball! Segueixes aprenent!")
            else:
                print("📚 Continua practicant!")
        
        print("=" * 50)
    
    def jugar(self):
        self.mostrar_intro()
        
        while self.vides > 0 and self.masmorra_actual <= len(self.masmorres):
            self.mostrar_estat()
            
            if not self.jugar_masmorra(self.masmorra_actual):
                break
            
            self.masmorra_actual += 1
            
            if self.masmorra_actual <= len(self.masmorres):
                print(f"\n🚪 Preparant-te per la següent masmorra...")
                time.sleep(2)
        
        # Determinar si ha guanyat
        victoria = self.masmorra_actual > len(self.masmorres) and self.vides > 0
        self.mostrar_final(victoria)

# Funció principal
def main():
    while True:
        joc = CodeQuest()
        joc.jugar()
        
        rejogar = input("\nVols tornar a jugar? (s/n): ").lower().strip()
        if rejogar not in ['s', 'sí', 'si', 'yes', 'y']:
            print("Gràcies per jugar a Code Quest! 👋")
            break

if __name__ == "__main__":
    main()