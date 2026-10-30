# Sports Tournament Ranking System

def create_teams(team_names):
    teams = {}

    for name in team_names:
        teams[name] = {
            "played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "goals_for": 0,
            "goals_against": 0,
            "goal_difference": 0,
            "points": 0
        }

    return teams


def record_match(teams, home_team, away_team, home_goals, away_goals):
    # Validate team names
    if home_team not in teams or away_team not in teams:
        return "ERROR: One or both teams do not exist."

    if home_team == away_team:
        return "ERROR: A team cannot play against itself."

    if home_goals < 0 or away_goals < 0:
        return "ERROR: Goals cannot be negative."

    # Update matches played and goals
    teams[home_team]["played"] += 1
    teams[away_team]["played"] += 1

    teams[home_team]["goals_for"] += home_goals
    teams[home_team]["goals_against"] += away_goals

    teams[away_team]["goals_for"] += away_goals
    teams[away_team]["goals_against"] += home_goals

    # Determine the match result
    if home_goals > away_goals:
        teams[home_team]["wins"] += 1
        teams[home_team]["points"] += 3

        teams[away_team]["losses"] += 1

        result = f"{home_team} won"

    elif home_goals < away_goals:
        teams[away_team]["wins"] += 1
        teams[away_team]["points"] += 3

        teams[home_team]["losses"] += 1

        result = f"{away_team} won"

    else:
        teams[home_team]["draws"] += 1
        teams[away_team]["draws"] += 1

        teams[home_team]["points"] += 1
        teams[away_team]["points"] += 1

        result = "Match drawn"

    # Calculate goal difference
    teams[home_team]["goal_difference"] = (
        teams[home_team]["goals_for"]
        - teams[home_team]["goals_against"]
    )

    teams[away_team]["goal_difference"] = (
        teams[away_team]["goals_for"]
        - teams[away_team]["goals_against"]
    )

    return (
        f"Match recorded: {home_team} {home_goals} - "
        f"{away_goals} {away_team}. {result}."
    )


def calculate_rankings(teams):
    # Ranking policy:
    # 1. Total points (highest first)
    # 2. Goal difference (highest first)
    # 3. Goals scored (highest first)
    # 4. Team name (alphabetical order)

    rankings = sorted(
        teams.items(),
        key=lambda item: (
            -item[1]["points"],
            -item[1]["goal_difference"],
            -item[1]["goals_for"],
            item[0].lower()
        )
    )

    return rankings


def display_rankings(teams):
    rankings = calculate_rankings(teams)

    print("\n" + "=" * 100)
    print("                    TOURNAMENT LEADERBOARD")
    print("=" * 100)

    print(
        f"{'Rank':<6}"
        f"{'Team':<20}"
        f"{'P':>5}"
        f"{'W':>5}"
        f"{'D':>5}"
        f"{'L':>5}"
        f"{'GF':>7}"
        f"{'GA':>7}"
        f"{'GD':>7}"
        f"{'Points':>9}"
    )

    print("-" * 100)

    for rank, (team_name, stats) in enumerate(rankings, start=1):
        print(
            f"{rank:<6}"
            f"{team_name:<20}"
            f"{stats['played']:>5}"
            f"{stats['wins']:>5}"
            f"{stats['draws']:>5}"
            f"{stats['losses']:>5}"
            f"{stats['goals_for']:>7}"
            f"{stats['goals_against']:>7}"
            f"{stats['goal_difference']:>7}"
            f"{stats['points']:>9}"
        )

    print("=" * 100)
    print("P = Played | W = Wins | D = Draws | L = Losses")
    print("GF = Goals For | GA = Goals Against | GD = Goal Difference")


def main():
    print("=" * 55)
    print("          SPORTS TOURNAMENT RANKING SYSTEM")
    print("=" * 55)

    try:
        number_of_teams = int(input("Enter the number of teams: "))

        if number_of_teams < 2:
            print("A tournament requires at least two teams.")
            return

        team_names = []

        for i in range(number_of_teams):
            name = input(f"Enter name of Team {i + 1}: ").strip()

            if not name:
                print("Team name cannot be empty.")
                return

            if any(name.lower() == existing.lower() for existing in team_names):
                print("Duplicate team names are not allowed.")
                return

            team_names.append(name)

        teams = create_teams(team_names)
        match_count = int(input("\nEnter the number of matches: "))

        if match_count < 0:
            print("Number of matches cannot be negative.")
            return

        print("\nAvailable teams:")
        for name in team_names:
            print("-", name)

        for i in range(match_count):
            print(f"\nMatch {i + 1}")

            home_team = input("Enter first team: ").strip()
            away_team = input("Enter second team: ").strip()

            try:
                home_goals = int(input(f"Goals scored by {home_team}: "))
                away_goals = int(input(f"Goals scored by {away_team}: "))
            except ValueError:
                print("Invalid score. Enter whole numbers.")
                return

            result = record_match(
                teams,
                home_team,
                away_team,
                home_goals,
                away_goals
            )

            print(result)

            if result.startswith("ERROR:"):
                print("Please restart and enter the match details correctly.")
                return

        display_rankings(teams)

    except ValueError:
        print("Invalid input. Please enter whole numbers where required.")


if __name__ == "__main__":
    main()