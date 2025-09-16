# BHR 2nd Crew Shares
earnings = float(input("How many dollars did Bob(the ship's captain) and his crew earn? "))
while True:
    crew = float(input("How many people are in the crew? "))
    if crew < 0.1:
        print("Please try again. The crew cannot be that small. ")
    else:
        break
bass_share = earnings/(crew + 10)
share_for_mate = bass_share * 3
share_for_bob = bass_share * 7
share_per_crew = bass_share - 500
if share_per_crew < 0:
  share_per_crew = share_per_crew * (-1)
  print(f"Bob(the captain) earned ${share_for_bob:.2f}. \nGeorge(the first mate) earned ${share_for_mate:.2f}. \nAnd the crew members each have to pay their captain ${share_per_crew:.2f}. \nThe bass share is ${bass_share:.2f}. ")
else:
    print(f"Bob(the captain) earned ${share_for_bob:.2f}. \nGeorge(the first mate) earned ${share_for_mate:.2f}. \nAnd the crew members each earned an additional ${share_per_crew:.2f}. \nThe bass share is ${bass_share:.2f}. ")
