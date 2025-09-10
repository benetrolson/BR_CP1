# BHR 2nd Crew Shares

earnings = int(input("How many dollars did Bob(the ship's captain) and his crew earn? "))
crew = int(input("How many people are in the crew? "))
bass_share = earnings/(crew + 10)
share_for_mate = bass_share * 3
share_for_bob = bass_share * 7
share_per_crew = bass_share - 500
print(f"Bob(the captain) earned ${share_for_bob}. \nGeorge(the first mate) earned ${share_for_mate}. \nAnd the crew members each earned an additional ${share_per_crew}. \nThe bass share is ${bass_share}. ")
