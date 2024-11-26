# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster = ["Claude", "Brown", "Cadeau", "Davis", "Tyson", "Davis", "Trimble", "Powell", "Jackson", "Washington" ]
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)
