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
    print("=====================================================================")
    print("RANK\tTEAMS\t", end="")
    for counter in range(num_matches_played):
        print(f"M{counter+1}\t", end="")
    print("TOTAL\tHIGH\tLOW")
    print("=====================================================================")


def calculate_totals(all_scores, num_teams):
    totals = []
    for count in range(num_teams):
        total_score = sum(all_scores[count])
        totals.append(total_score)
    return totals


def teams_results(all_scores, totals, num_teams, num_matches_played):
    
    team_names = []
    highest_scores = []
    lowest_scores = []
    
    for count in range(num_teams):
        team_names.append(f"Team {count+1}")
        highest_scores.append(max(all_scores[count]))
        lowest_scores.append(min(all_scores[count]))

  
    for count in range(num_teams):
        for counter in range(count + 1, num_teams):
            if totals[counter] > totals[count]:
              
                totals[count], totals[counter] = totals[counter], totals[count]
               
                team_names[count], team_names[counter] = team_names[counter], team_names[count]
                
                all_scores[count], all_scores[counter] = all_scores[counter], all_scores[count]
               
                highest_scores[count], highest_scores[counter] = highest_scores[counter], highest_scores[count]
                
                lowest_scores[count], lowest_scores[counter] = lowest_scores[counter], lowest_scores[count]

   
    previous_rank = 1
    for count in range(num_teams):
        
        if count > 0 and totals[count] == totals[count - 1]:
            rank = previous_rank
        else:
            rank = count + 1
            
        previous_rank = rank

        
        print(f"{rank}\t{team_names[count]}\t", end="")
        
        for counter in range(num_matches_played):
            print(f"{all_scores[count][counter]:.0f}\t", end="")
            
        print(f"{totals[count]:.0f}\t{highest_scores[count]:.0f}\t{lowest_scores[count]:.0f}")
        
    print("=====================================================================\n")



