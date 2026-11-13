
from drafter import *
from dataclasses import dataclass


# ==========================================
# WEBSITE INFORMATION
# ==========================================

set_website_title("Badminton Performance Tracker")

set_site_information(
    author="Danny Nguyen",
    description="A website that helps badminton players track matches, analyze statistics, and improve their performance.",
    sources="Drafter Documentation, CISC 106 course materials, and ChatGPT for coding assistance.",
    planning="Badminton Performance Tracker Final Project Mockup and Implementing Requirements.",
    links=[
        "https://github.com/dannyn-68/badminton-performance-tracker",
        "https://drafter-edu.github.io/drafter/"
    ]
)


# ==========================================
# DATACLASSES
# ==========================================

@dataclass
class Match:
    opponent: str
    date: str
    result: str
    points_won: int
    total_points: int
    errors: int
    total_smashes: int
    successful_smashes: int
    total_serves: int
    successful_serves: int


@dataclass
class State:
    matches: list[Match]
    player_name: str
    goal: str
    favorite_shot: str


# ==========================================
# ROUTE 1: HOME PAGE
# ==========================================

@route
def index(state: State) -> Page:

    # Calculate wins and losses.
    wins = 0
    losses = 0

    for match in state.matches:
        if match.result == "Win":
            wins += 1
        else:
            losses += 1

    # Calculate win percentage.
    win_rate = 0.0

    if len(state.matches) > 0:
        win_rate = wins / len(state.matches) * 100

    return Page(state, [
        Header("🏸 Badminton Performance Tracker"),

        "Welcome, " + state.player_name + "!",

        "Track your badminton matches, analyze your "
        "performance, and improve your skills.",

        HorizontalRule(),

        Header("Your Progress"),

        "Matches Recorded: " + str(len(state.matches)),

        "Wins: " + str(wins),

        "Losses: " + str(losses),

        "Win Rate: " + str(round(win_rate, 2)) + "%",

        "Training Goal: " + state.goal,

        "Favorite Shot: " + state.favorite_shot,

        HorizontalRule(),

        Button("Record Match", record_match),

        Button("Match History", match_history),

        Button("Performance Statistics", statistics),

        Button("My Profile", profile)
    ])


# ==========================================
# ROUTE 2: RECORD MATCH PAGE
# ==========================================

@route
def record_match(state: State) -> Page:

    return Page(state, [
        Header("Record a Match"),

        "Enter your match statistics below.",

        Header("Match Information"),

        "Opponent:",
        TextBox("opponent", ""),

        "Match Date (MM/DD/YYYY):",
        TextBox("date", ""),

        "Match Result:",
        SelectBox("result", ["Win", "Loss"], "Win"),

        HorizontalRule(),

        Header("Point Statistics"),

        "Points Won:",
        TextBox("points_won", "0"),

        "Total Points:",
        TextBox("total_points", "0"),

        "Errors:",
        TextBox("errors", "0"),

        HorizontalRule(),

        Header("Smash Statistics"),

        "Total Smashes:",
        TextBox("total_smashes", "0"),

        "Successful Smashes:",
        TextBox("successful_smashes", "0"),

        HorizontalRule(),

        Header("Serve Statistics"),

        "Total Serves:",
        TextBox("total_serves", "0"),

        "Successful Serves:",
        TextBox("successful_serves", "0"),

        HorizontalRule(),

        Button("Save Match", save_match),

        Button("Back to Home", index)
    ])


# ==========================================
# ROUTE 3: SAVE MATCH
# ==========================================

@route
def save_match(
    state: State,
    opponent: str,
    date: str,
    result: str,
    points_won: str,
    total_points: str,
    errors: str,
    total_smashes: str,
    successful_smashes: str,
    total_serves: str,
    successful_serves: str
) -> Page:

    # Advanced technique: Exception handling.
    # TextBox inputs are strings.
    # Convert the strings into integers.
    # If the user enters invalid text, catch the
    # ValueError and display an error page.

    try:
        won = int(points_won)
        total = int(total_points)
        error_count = int(errors)
        smashes = int(total_smashes)
        good_smashes = int(successful_smashes)
        serves = int(total_serves)
        good_serves = int(successful_serves)

    except ValueError:
        return Page(state, [
            Header("Invalid Input"),

            "Please enter whole numbers for all statistics.",

            Button("Try Again", record_match),

            Button("Back to Home", index)
        ])

    # Check the opponent's name.

    if opponent.strip() == "":
        return Page(state, [
            Header("Invalid Input"),

            "Please enter your opponent's name.",

            Button("Try Again", record_match)
        ])

    # Check the match date.

    if date.strip() == "":
        return Page(state, [
            Header("Invalid Input"),

            "Please enter the match date.",

            Button("Try Again", record_match)
        ])

    # Check the match result.

    if result != "Win" and result != "Loss":
        return Page(state, [
            Header("Invalid Input"),

            "Please select Win or Loss.",

            Button("Try Again", record_match)
        ])

    # Check the point statistics.

    if total <= 0 or won < 0 or won > total:
        return Page(state, [
            Header("Invalid Input"),

            "Points won must be between 0 and total points. "
            "Total points must be greater than zero.",

            Button("Try Again", record_match)
        ])

    # Check the error count.

    if error_count < 0:
        return Page(state, [
            Header("Invalid Input"),

            "The number of errors cannot be negative.",

            Button("Try Again", record_match)
        ])

    # Check the smash statistics.

    if smashes < 0 or good_smashes < 0 or good_smashes > smashes:
        return Page(state, [
            Header("Invalid Input"),

            "Successful smashes must be between "
            "0 and total smashes.",

            Button("Try Again", record_match)
        ])

    # Check the serve statistics.

    if serves < 0 or good_serves < 0 or good_serves > serves:
        return Page(state, [
            Header("Invalid Input"),

            "Successful serves must be between "
            "0 and total serves.",

            Button("Try Again", record_match)
        ])

    # Create a new Match dataclass instance.

    new_match = Match(
        opponent,
        date,
        result,
        won,
        total,
        error_count,
        smashes,
        good_smashes,
        serves,
        good_serves
    )

    # Modify the matches field in State.

    state.matches.append(new_match)

    # Display a message based on the match result.

    if result == "Win":
        message = "Congratulations on your win!"
    else:
        message = "Keep practicing and improving!"

    return Page(state, [
        Header("Match Saved!"),

        "Your match against " + opponent
        + " has been successfully recorded.",

        HorizontalRule(),

        "Match Date: " + date,

        "Match Result: " + result,

        message,

        "Total Matches Recorded: "
        + str(len(state.matches)),

        HorizontalRule(),

        Button("Record Another Match", record_match),

        Button("View Match History", match_history),

        Button("View Statistics", statistics),

        Button("Back to Home", index)
    ])


# ==========================================
# ROUTE 4: MATCH HISTORY PAGE
# ==========================================

@route
def match_history(state: State) -> Page:

    content = [
        Header("Match History"),

        "Review your previously recorded matches."
    ]

    # Check whether the user has saved any matches.

    if len(state.matches) == 0:
        content.append(
            "You have not recorded any matches yet."
        )

    match_number = 1

    # Meaningful loop:
    # Iterate over the list of Match instances in State.
    # Display the statistics of every recorded match.

    for match in state.matches:

        content.append(HorizontalRule())

        content.append(
            Header("Match " + str(match_number))
        )

        content.append(
            "Opponent: " + match.opponent
        )

        content.append(
            "Date: " + match.date
        )

        content.append(
            "Result: " + match.result
        )

        content.append(
            "Points Won: " + str(match.points_won)
            + "/" + str(match.total_points)
        )

        content.append(
            "Errors: " + str(match.errors)
        )

        content.append(
            "Total Smashes: "
            + str(match.total_smashes)
        )

        content.append(
            "Successful Smashes: "
            + str(match.successful_smashes)
        )

        content.append(
            "Total Serves: "
            + str(match.total_serves)
        )

        content.append(
            "Successful Serves: "
            + str(match.successful_serves)
        )

        match_number += 1

    content.append(HorizontalRule())

    content.append(
        Button("Record Match", record_match)
    )

    content.append(
        Button("Performance Statistics", statistics)
    )

    content.append(
        Button("Back to Home", index)
    )

    return Page(state, content)


# ==========================================
# ROUTE 5: PERFORMANCE STATISTICS PAGE
# ==========================================

@route
def statistics(state: State) -> Page:

    # Prevent calculations when there are no matches.

    if len(state.matches) == 0:
        return Page(state, [
            Header("Performance Statistics"),

            "Record a match to view your statistics.",

            Button("Record Match", record_match),

            Button("Back to Home", index)
        ])

    # Initialize integer totals.

    wins = 0
    losses = 0
    points_won = 0
    total_points = 0
    errors = 0
    total_smashes = 0
    successful_smashes = 0
    total_serves = 0
    successful_serves = 0

    # Meaningful loop:
    # Calculate the total statistics from all matches.

    for match in state.matches:

        if match.result == "Win":
            wins += 1
        else:
            losses += 1

        points_won += match.points_won

        total_points += match.total_points

        errors += match.errors

        total_smashes += match.total_smashes

        successful_smashes += match.successful_smashes

        total_serves += match.total_serves

        successful_serves += match.successful_serves

    # Calculate match win percentage.

    win_rate = wins / len(state.matches) * 100

    # Calculate point win percentage.

    point_rate = points_won / total_points * 100

    # Calculate smash success rate.
    # Check the denominator to avoid division by zero.

    smash_rate = 0.0

    if total_smashes > 0:
        smash_rate = successful_smashes / total_smashes * 100

    # Calculate serve success rate.

    serve_rate = 0.0

    if total_serves > 0:
        serve_rate = successful_serves / total_serves * 100

    # Calculate average errors per match.

    average_errors = errors / len(state.matches)

    # Calculate error percentage.

    error_rate = errors / total_points * 100

    return Page(state, [
        Header("Performance Statistics"),

        Header("Match Overview"),

        "Total Matches: " + str(len(state.matches)),

        "Wins: " + str(wins),

        "Losses: " + str(losses),

        "Win Rate: "
        + str(round(win_rate, 2)) + "%",

        HorizontalRule(),

        Header("Point Statistics"),

        "Total Points Won: " + str(points_won),

        "Total Points Played: " + str(total_points),

        "Point Win Rate: "
        + str(round(point_rate, 2)) + "%",

        HorizontalRule(),

        Header("Smash Statistics"),

        "Total Smashes: " + str(total_smashes),

        "Successful Smashes: " + str(successful_smashes),

        "Smash Success Rate: "
        + str(round(smash_rate, 2)) + "%",

        HorizontalRule(),

        Header("Serve Statistics"),

        "Total Serves: " + str(total_serves),

        "Successful Serves: " + str(successful_serves),

        "Serve Success Rate: "
        + str(round(serve_rate, 2)) + "%",

        HorizontalRule(),

        Header("Error Statistics"),

        "Total Errors: " + str(errors),

        "Average Errors per Match: "
        + str(round(average_errors, 2)),

        "Error Percentage: "
        + str(round(error_rate, 2)) + "%",

        HorizontalRule(),

        Button("Match History", match_history),

        Button("Record Match", record_match),

        Button("Back to Home", index)
    ])


# ==========================================
# ROUTE 6: PROFILE PAGE
# ==========================================

@route
def profile(state: State) -> Page:

    return Page(state, [
        Header("My Profile"),

        "Personalize your badminton profile.",

        HorizontalRule(),

        "Player Name:",
        TextBox("player_name", state.player_name),

        "Training Goal:",
        TextBox("goal", state.goal),

        "Favorite Shot:",
        SelectBox(
            "favorite_shot",
            [
                "Smash",
                "Drop Shot",
                "Clear",
                "Drive",
                "Net Shot"
            ],
            state.favorite_shot
        ),

        HorizontalRule(),

        Button("Save Profile", save_profile),

        Button("Back to Home", index)
    ])


# ==========================================
# ROUTE 7: SAVE PROFILE
# ==========================================

@route
def save_profile(
    state: State,
    player_name: str,
    goal: str,
    favorite_shot: str
) -> Page:

    # Check whether the player entered a name.

    if player_name.strip() == "":
        return Page(state, [
            Header("Invalid Input"),

            "Please enter your name.",

            Button("Back to Profile", profile)
        ])

    # Meaningfully modify three State fields.

    state.player_name = player_name

    state.goal = goal

    state.favorite_shot = favorite_shot

    return Page(state, [
        Header("Profile Updated!"),

        "Your profile has been successfully saved.",

        HorizontalRule(),

        "Player Name: " + state.player_name,

        "Training Goal: " + state.goal,

        "Favorite Shot: " + state.favorite_shot,

        HorizontalRule(),

        Button("Back to Home", index),

        Button("Edit Profile", profile)
    ])


# ==========================================
# START SERVER
# ==========================================

start_server(State(
    [],
    "Player",
    "Improve my badminton skills",
    "Smash"
))
