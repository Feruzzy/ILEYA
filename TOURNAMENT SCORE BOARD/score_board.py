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
    # Put RANK at the very front, followed by TEAMS
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
    # 1. Bundle all team details together so we don't lose track of original team names when sorting
    team_data_list = []
    for count in range(num_teams):
        team_info = {
            "name": f"Team {count+1}",
            "scores": all_scores[count],
            "total": totals[count],
            "high": max(all_scores[count]),
            "low": min(all_scores[count])
        }
        team_data_list.append(team_info)

    # 2. Sort the teams based on their total score in descending order (highest score first)
    team_data_list.sort(key=lambda team: team["total"], reverse=True)

    # 3. Print the results table
    for index, team in enumerate(team_data_list):
        # Calculate rank dynamically based on position in sorted list
        # We check if they tied with the previous team's score to handle joint ranking
        if index > 0 and team["total"] == team_data_list[index - 1]["total"]:
            rank = previous_rank
        else:
            rank = index + 1
            
        previous_rank = rank # Save for next loop iteration check

        # Print columns matching the new header order: RANK -> TEAMS -> MATCHES -> TOTAL -> HIGH -> LOW
        print(f"{rank}\t{team['name']}\t", end="")
        
        for score in team["scores"]:
            print(f"{score:.0f}\t", end="")
            
        print(f"{team['total']:.0f}\t{team['high']:.0f}\t{team['low']:.0f}")
        
    print("=====================================================================\n")


 
