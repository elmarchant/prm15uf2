import pandas as pd;

dades = pd.read_csv("./src/data/main.csv")
dades.columns=["Date", "Team", "Opponent", "Goal Scored", "Ball Possession %", "Attempts", "On-Target", "Off-Target", "Blocked", "Corners", "Offsides", "Free Kicks", "Saves", "Pass Accuracy %", "Passes", "Distance Covered (Kms)", "Fouls Committed", "Yellow Card", "Yellow & Red", "Red", "Man of the Match", "1st Goal", "Round", "PSO", "Goals in PSO", "Own goals", "Own goal Time"]
print(type(dades))
