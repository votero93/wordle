from tkinter import *
import random


file = open("word-list.txt", "r")
wordList = file.read().split("\n")

secretWord = random.choice(wordList).upper()
print(secretWord)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rowNum = 0
colNum = 0
guess = ""
canGuess = True


def inputLetters(event):
    global colNum, guess
    entry = (event.keysym).upper()
    if colNum < 5 and entry in alphabet and canGuess:
        allEntries[rowNum][colNum].config(state="normal")
        allEntries[rowNum][colNum].insert(0, entry)
        allEntries[rowNum][colNum].config(state = 'disabled')
        colNum += 1
        guess += entry


def backSpace(event):
    global colNum, guess

    if colNum > 0:
        colNum -= 1
        allEntries[rowNum][colNum].config(state="normal")
        allEntries[rowNum][colNum].delete(0)
        allEntries[rowNum][colNum].config(state="disabled")
        guess = guess[0 : len(guess) - 1]
    messageDisplay.pack_forget()


def enter(event):
    global rowNum, colNum, guess, canGuess
    if not canGuess:
        return
    if len(guess) == 5:
        messageDisplay.pack_forget()
        checkGuess()
    else:
        messageDisplay.config(text="Word must be 5 characters")
        messageDisplay.pack()
    if rowNum == 6 and canGuess:
        canGuess = False
        endGame(secretWord)


def checkGuess():
    global rowNum, colNum, guess, canGuess
    if guess == secretWord:
        canGuess = False
        endGame("You Win")
    if guess.upper() in wordList:

        for i in range(5):
            allEntries[rowNum][i].config(state="normal")
            if guess[i] == secretWord[i]:
                allEntries[rowNum][i].config(bg="#56AF1F")
            elif guess[i] in secretWord:
                allEntries[rowNum][i].config(bg="#D8C848")
            else:
                allEntries[rowNum][i].config(bg="#8D8C80")
        colNum = 0
        rowNum += 1
        guess = ""
    else:
        print(guess)
        messageDisplay.config(text="Not in word list")
        messageDisplay.pack()


def restart():
    global rowNum, colNum, canGuess, secretWord
    for i in range(6):
        for j in range(5):
            allEntries[i][j].config(bg="#EEDCD8")
            allEntries[i][j].delete(0)
    rowNum = 0
    colNum = 0
    canGuess = True
    secretWord = random.choice(wordList).upper()
    messageDisplay.pack_forget()
    playAgain.pack_forget()


def endGame(message):
    messageDisplay.config(text=message)
    messageDisplay.pack()
    playAgain.pack()


window = Tk()
bgColor = "#b94e48"
window.geometry("350x400")
window.title("Wordle")
window.config(bg=bgColor)
window.resizable(False, False)


title = Label(window, text="WORDLE", font=("Eras Bold ITC", 30, "bold"), bg=bgColor)

title.pack()

frame = Frame(window, bg=bgColor)
frame.pack()

allEntries = []

for i in range(6):
    arr = []
    for j in range(5):
        entry = Entry(
            frame,
            bg="#EEDCD8",
            width=3,
            font=("Arial", 20),
            justify="center",
            state="disabled",
        )
        entry.grid(row=i, column=j, padx=3, pady=3)
        arr.append(entry)
    allEntries.append(arr)

messageDisplay = Label(window, font=("Bell MT", 20), bg=bgColor)

playAgain = Button(window, text="Play Again", font=("Bell MT", 20), command=restart)

window.bind("<Key>", inputLetters)
window.bind("<BackSpace>", backSpace)
window.bind("<Return>", enter)

window.mainloop()
