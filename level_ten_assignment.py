import pandas as pd
#ask user what season it wants to analyze, then looks at the season in the csv and returns the teams number of wins separated into categories


football_data = pd.read_csv("cfb.csv")

# Prompt the user to enter a valid season number until they do so

while True:
    try:
        season_number = int(input("Which season would you like to analyze? "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if season_number in football_data["Season"].values:
        break

    print("That season was not found. Please try again.")



season_table = football_data[
    (football_data["Season"] == season_number)
]


football_time = {
    "10 or more": season_table.query("Win >= 10"),
    "8 to 9": season_table.query("Win >= 8 and Win <= 9"),
    "6 to 7": season_table.query("Win >= 6 and Win <= 7"),
    "less than 6": season_table.query("Win < 6")
}


for category, teams in football_time.items():
    print(f"Teams with {category} wins:")
    print(teams[["Team", "Win"]])
    print()



