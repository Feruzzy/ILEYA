import scores_board

def main():

   
    num_teams = int(input("How many teams played? "))
    num_matches = int(input("How many matches was played? "))
    print()
    
    scores = scores_board.get_scores(num_teams, num_matches)
    totals = scores_board.calculate_totals(scores, num_teams)
    
    scores_board.print_table_header(num_matches)
    scores_board.teams_results(scores, totals, num_teams, num_matches)


main()

