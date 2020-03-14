import tkinter as tk
import random


class Pokemon:
    def __init__(self,name,dexnum,rate,speed):
        self.name = name
        self.dex = int(dexnum)
        self.catchrate = int(rate)
        self.speed = int(speed)
        #Path to image location made into a PhotoImage object
        self.photo = tk.PhotoImage(file = "sprites/" + str(self.dex) + ".gif")
        
    def __str__(self):
        return str(self.name)
    


class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        #Stores pokemon data in a 2D list
        pokedex = open('pokedex.csv')
        lines_list = pokedex.readlines()
        pokedex.close()
        pokelist = []
        for line in lines_list:
            line = line.strip('\n').split(',')
            pokelist.append(line)

        #Stored instance variables
        self.pokelist = pokelist
        self.balls_left = 30
        self.pokemon_caught = []
        self.pokemon_num = 0

        #Creates playing window
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.nextPokemon()
        self.createWidgets()
        


    def createWidgets(self):
        #GUI components
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack()
        

        self.throwButton = tk.Button(self)
        self.throwButton["text"] = "Throw Ball (" + str(self.balls_left)  + " left)"
        self.throwButton["command"] = self.throwBall
        self.throwButton.pack()


        self.messageLabel = tk.Label(bg="grey")
        self.messageLabel["text"] = "You encounter a wild " + self.pokemon.name
        self.messageLabel.pack(fill="x", padx=5, pady=5)


        self.pokemonImageLabel = tk.Label()
        self.pokemonImageLabel["image"] = self.pokemon.photo
        self.pokemonImageLabel.pack()

       
        
        self.catchProbLabel = tk.Label(bg="grey")
        self.catchProbLabel["text"] = "Your chance of catching it is " + str(int(min(self.pokemon.catchrate + 1, 151)/4.495)) + "%!"
        self.catchProbLabel.pack(fill="x", padx=5, pady=5)



    def nextPokemon(self):
        #Generates random number which represents index for pokemon in self.pokelist 
        num = random.randint(1,151)
        #Uses data to create Pokemon object
        self.pokelist[num][0] = Pokemon(self.pokelist[num][1],self.pokelist[num][0],self.pokelist[num][2],self.pokelist[num][3])
        #Assigns the Pokemon object to self.pokemon
        self.pokemon = self.pokelist[num][0]

        #Updates the text and images in the GUI labels
        self.pokemon_num += 1 #avoids labels being packed multiple times
        if self.pokemon_num > 1:
            self.messageLabel["text"] = "You encounter a wild " + self.pokemon.name
            self.pokemonImageLabel["image"] = self.pokemon.photo
            self.catchProbLabel["text"] = "Your chance of catching it is " + str(int(min(self.pokemon.catchrate + 1, 151)/4.495)) + "%!"
        

            
    def endAdventure(self):
        #clears screen
        self.runButton.pack_forget()
        self.throwButton.pack_forget()
        self.messageLabel.pack_forget()
        self.pokemonImageLabel.pack_forget()
        self.catchProbLabel.pack_forget()


        #Displays messages for end of game
        self.endMessage = tk.Label(bg="grey")
        self.endMessage["text"] = "You're all out of balls, hope you had fun!"
        self.endMessage.pack(fill="x",padx=5,pady=5)

        self.caughtPokemon = tk.Label(bg="grey")
        if len(self.pokemon_caught) > 0: #Determines whether or not player caught any Pokemon
            self.caughtPokemon["text"] = "You caught " + str(len(self.pokemon_caught)) + " Pokemon\n" + "\n".join(self.pokemon_caught)
        else:
            self.caughtPokemon["text"] = "Oops, you caught 0 Pokemon."
        self.caughtPokemon.pack(fill="x",padx=5,pady=0)

        

    def throwBall(self):
        self.balls_left -= 1

        #Updates the tect in self.throwButton
        self.throwButton["text"] = "Throw Ball (" + str(self.balls_left)  + " left)"
        
        if random.random() < (min(self.pokemon.catchrate + 1, 151))/449.5: #Checks if Pokemon should be caught
            self.pokemon_caught.append(self.pokemon.name) #Adds Pokemon name to list
            self.nextPokemon()
        else:
            self.messageLabel["text"] = "Aargh! It escaped"

        if self.balls_left == 0:
            self.endAdventure()
        
        

app = SafariSimulator(tk.Tk())
app.mainloop()
