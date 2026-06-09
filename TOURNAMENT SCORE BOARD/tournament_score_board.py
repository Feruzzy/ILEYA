def get_scores(num_teams, num_matches_played):
  
    all_scores = []
    
    for count in range(num_teams):
        print(f"Entering score for team {count + 1}")
        team_scores = [] 
        
        for matches_number_played in range(1, num_matches_played + 1):
            while True:
                score = float(input(f"  Enter score for matches {matches_number_played}: "))
                if score >= 0:
                    team_scores.append(score)
                    break
                else:
                    print("  Constraint: Score must be 0 or more than 0. Try again.")
                    
        all_scores.append(team_scores)

    return all_scores


def print_table_header(num_matches_played):
    
    print("=========================================================")
    print("TEAMS\t\t", end="")
    for counter in range(num_matches_played):
        print(f"M{counter+1}\t", end="")
    print("TOTAL\tHIGH\tLOW\tPOS")
    print("=========================================================")





def calculate_totals(all_scores, num_teams, num_matches_played):

    totals = []
    for count in range(num_teams):
        total_score = sum(all_scores[count])
        totals.append(total_score)
     
    return totals




def teams_results(all_scores, totals, num_teams, num_matches_played):
    
    for count in range(num_teams):
        print(f"Teams {count+1}\t", end="")
        
        for counter in range(num_matches_played):
            print(f"{all_scores[count][counter]}\t", end="")
            
        
        position = 1
        for other_total in totals:
            if other_total > totals[count]:
                position += 1
                
        print(f"{totals[count]:.0f}\t{position}")
    print("=========================================================\n")

