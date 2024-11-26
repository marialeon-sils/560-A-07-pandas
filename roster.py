# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster = ["Claude", "Brown", "Cadeau", "Davis", "Tyson", "Davis", "Trimble", "Powell", "Jackson", "Washington" ]
player = {"Last Name": roster,
          "First Name": ["Ty", "James", "Elliot", "RJ", "Cade", "Elijah", "Seth", "Drake", "Ian", "Jalen"],
          "height": [79, 82, 73, 72, 79, 75, 75, 78, 76, 82],
          "weight": [230, 215, 180, 180, 200, 215, 195, 195, 190, 235]}
data = pd.DataFrame(player)
print(data)
