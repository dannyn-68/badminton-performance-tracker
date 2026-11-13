from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

@dataclass
class Match:
    opponent: str
    points_won: int
from drafter import *
from dataclasses import dataclass


# =========================
# DATACLASSES
# =========================

@dataclass
class Match:
    opponent: str
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


# =========================
# HOME PAGE
# =========================

@route
def index(state: State) -> Page:
    return Page(state, [
        Header("Badminton Performance Tracker"),

        "Welcome, " + state.player_name + "!",

        "Track your badminton matches, analyze your "
        "performance, and improve your skills.",

        Header("Your Progress"),

        "Matches recorded: " + str(len(state.matches)),
        "Your goal: " + state.goal,

        Button("Record Match", record_match),
        Button("Match History", match_history),
        Button("Performance Statistics", statistics),
        Button("My Profile", profile)
    ])


# =========================
# RECORD MATCH PAGE
# =========================

@route
def record_match(state: State) -> Page:
    return Page(state, [
        Header("Record a Match"),

        "Opponent:",
        TextBox("opponent", ""),

        "Points Won:",
        TextBox("points_won", "0"),

        "Total Points:",
        TextBox("total_points", "0"),

        "Errors:",
        TextBox("errors", "0"),

        "Total Smashes:",
        TextBox("total_smashes", "0"),

        "Successful Smashes:",
        TextBox("successful_smashes", "0"),

        "Total Serves:",
        TextBox("total_serves", "0"),

        "Successful Serves:",
        TextBox("successful_serves", "0"),

        Button("Save Match", save_match),
        Button("Back to Home", index)
    ])


# =========================
# SAVE MATCH ROUTE
# =========================

@route
def save_match(state: State,
               opponent: str,
               points_won: str,
               total_points: str,
               errors: str,
               total_smashes: str,
               successful_smashes: str,
               total_serves: str,
               successful_serves: str) -> Page:

    # Advanced technique: Exception handling.
    # TextBox inputs are strings. The try block attempts
    # to convert each string into an integer.
    # If the user enters invalid text, Python raises
    # a ValueError. The except block catches the error
    # and displays an error page instead of crashing.
    # New variables are used to keep string and integer
    # types separate for the type checker.

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

            Button("Try Again", record_match)
        ])

    # Validate user inputs

    if opponent == "":
        return Page(state, [
            Header("Error"),

            "Please enter your opponent's name.",

            Button("Try Again", record_match)
        ])

    if total <= 0 or won < 0:
        return Page(state, [
            Header("Error"),

            "Please enter valid points.",

            Button("Try Again", record_match)
        ])

    if won > total:
        return Page(state, [
            Header("Error"),

            "Points won cannot exceed total points.",

            Button("Try Again", record_match)
        ])

    if error_count < 0 or smashes < 0 or serves < 0:
        return Page(state, [
            Header("Error"),

            "Statistics cannot be negative.",

            Button("Try Again", record_match)
        ])

    if good_smashes < 0 or good_smashes > smashes:
        return Page(state, [
            Header("Error"),

            "Please enter valid smash statistics.",

            Button("Try Again", record_match)
        ])

    if good_serves < 0 or good_serves > serves:
        return Page(state, [
            Header("Error"),

            "Please enter valid serve statistics.",

            Button("Try Again", record_match)
        ])

    # Create a new Match using integer values

    new_match = Match(
        opponent,
        won,
        total,
        error_count,
        smashes,
        good_smashes,
        serves,
        good_serves
    )

    # Meaningfully modify the matches field in State

    state.matches.append(new_match)

    return Page(state, [
        Header("Match Saved!"),

        "Your match has been successfully recorded.",

        Button("Record Another Match", record_match),
        Button("View Match History", match_history),
        Button("Back to Home", index)
    ])


# =========================
# MATCH HISTORY PAGE
# =========================

@route
def match_history(state: State) -> Page:

    content = [
        Header("Match History"),

        "Review your previous badminton matches."
    ]

    if len(state.matches) == 0:
        content.append(
            "You have not recorded any matches yet."
        )

    match_number = 1

    # Iterate over the list of Match instances in State.
    # This loop displays the statistics of every match.

    for match in state.matches:

        content.append(
            Header("Match " + str(match_number))
        )

        content.append(
            "Opponent: " + match.opponent
        )

        content.append(
            "Points Won: " + str(match.points_won)
            + "/" + str(match.total_points)
        )

        content.append(
            "Errors: " + str(match.errors)
        )

        content.append(
            "Smashes: " + str(match.successful_smashes)
            + "/" + str(match.total_smashes)
        )

        content.append(
            "Serves: " + str(match.successful_serves)
            + "/" + str(match.total_serves)
        )

        match_number += 1

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


# =========================
# PERFORMANCE STATISTICS
# =========================

@route
def statistics(state: State) -> Page:

    if len(state.matches) == 0:
        return Page(state, [
            Header("Performance Statistics"),

            "Record a match to view your statistics.",

            Button("Record Match", record_match),
            Button("Back to Home", index)
        ])

    points_won = 0
    total_points = 0
    errors = 0
    total_smashes = 0
    successful_smashes = 0
    total_serves = 0
    successful_serves = 0

    # Calculate the totals from all saved matches.

    for match in state.matches:

        points_won += match.points_won
        total_points += match.total_points
        errors += match.errors
        total_smashes += match.total_smashes
        successful_smashes += match.successful_smashes
        total_serves += match.total_serves
        successful_serves += match.successful_serves

    # Calculate point win rate.

    point_rate = points_won / total_points * 100

    # Initialize rates as floats because division
    # produces a floating-point result.

    smash_rate = 0.0

    if total_smashes > 0:
        smash_rate = successful_smashes / total_smashes * 100

    serve_rate = 0.0

    if total_serves > 0:
        serve_rate = successful_serves / total_serves * 100

    # Calculate average errors per match.

    average_errors = errors / len(state.matches)

    return Page(state, [
        Header("Performance Statistics"),

        "Total Matches: " + str(len(state.matches)),

        Header("Point Statistics"),

        "Total Points Won: " + str(points_won),

        "Total Points Played: " + str(total_points),

        "Point Win Rate: "
        + str(round(point_rate, 2)) + "%",

        Header("Smash Statistics"),

        "Total Smashes: " + str(total_smashes),

        "Successful Smashes: " + str(successful_smashes),

        "Smash Success Rate: "
        + str(round(smash_rate, 2)) + "%",

        Header("Serve Statistics"),

        "Total Serves: " + str(total_serves),

        "Successful Serves: " + str(successful_serves),

        "Serve Success Rate: "
        + str(round(serve_rate, 2)) + "%",

        Header("Error Statistics"),

        "Total Errors: " + str(errors),

        "Average Errors per Match: "
        + str(round(average_errors, 2)),

        Button("Match History", match_history),
        Button("Record Match", record_match),
        Button("Back to Home", index)
    ])


# =========================
# PROFILE PAGE
# =========================

@route
def profile(state: State) -> Page:

    return Page(state, [
        Header("My Profile"),

        "Player Name:",
        TextBox("player_name", state.player_name),

        "Your Training Goal:",
        TextBox("goal", state.goal),

        "Favorite Shot:",
        SelectBox("favorite_shot", [
            "Smash",
            "Drop Shot",
            "Clear",
            "Drive",
            "Net Shot"
        ], state.favorite_shot),

        Button("Save Profile", save_profile),
        Button("Back to Home", index)
    ])


# =========================
# SAVE PROFILE ROUTE
# =========================

@route
def save_profile(state: State,
                 player_name: str,
                 goal: str,
                 favorite_shot: str) -> Page:

    if player_name == "":
        return Page(state, [
            Header("Error"),

            "Please enter your name.",

            Button("Back to Profile", profile)
        ])

    # Meaningfully modify three fields in State.

    state.player_name = player_name
    state.goal = goal
    state.favorite_shot = favorite_shot

    return Page(state, [
        Header("Profile Updated!"),

        "Player Name: " + state.player_name,

        "Training Goal: " + state.goal,

        "Favorite Shot: " + state.favorite_shot,

        Button("Back to Home", index),
        Button("Edit Profile", profile)
    ])


# =========================
# START SERVER
# =========================

start_server(State(
    [],
    "Player",
    "Improve my badminton skills",
    "Smash"
))

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
    

@route
def index(state: State) -> Page:
    return Page(state, [
        Header("Badminton Performance Tracker"),

        "Welcome, " + state.player_name + "!",

        "Track your badminton matches, analyze your "
        "performance, and improve your skills.",

        Header("Your Progress"),

        "Matches recorded: " + str(len(state.matches)),
        "Your goal: " + state.goal,

        Button("Record Match", record_match),
        Button("Match History", match_history),
        Button("Performance Statistics", statistics),
        Button("My Profile", profile)
    ])

@route
def record_match(state: State) -> Page:
    return Page(state, [
        Header("Record a Match"),

        "Opponent:",
        TextBox("opponent", ""),

        "Points Won:",
        TextBox("points_won", "0"),

        "Total Points:",
        TextBox("total_points", "0"),

        "Errors:",
        TextBox("errors", "0"),

        "Total Smashes:",
        TextBox("total_smashes", "0"),

        "Successful Smashes:",
        TextBox("successful_smashes", "0"),

        "Total Serves:",
        TextBox("total_serves", "0"),

        "Successful Serves:",
        TextBox("successful_serves", "0"),

        Button("Save Match", save_match),
        Button("Back to Home", index)
    ])

@route
def save_match(state: State,
               opponent: str,
               points_won: str,
               total_points: str,
               errors: str,
               total_smashes: str,
               successful_smashes: str,
               total_serves: str,
               successful_serves: str) -> Page:

    # Convert text inputs into integers

    try:
        points_won = int(points_won)
        total_points = int(total_points)
        errors = int(errors)
        total_smashes = int(total_smashes)
        successful_smashes = int(successful_smashes)
        total_serves = int(total_serves)
        successful_serves = int(successful_serves)

    except ValueError:
        return Page(state, [
            Header("Invalid Input"),
            "Please enter whole numbers for all statistics.",
            Button("Try Again", record_match)
        ])

    # Validate user inputs

    if opponent == "":
        return Page(state, [
            Header("Error"),
            "Please enter your opponent's name.",
            Button("Try Again", record_match)
        ])

    if total_points <= 0 or points_won < 0:
        return Page(state, [
            Header("Error"),
            "Please enter valid points.",
            Button("Try Again", record_match)
        ])

    if points_won > total_points:
        return Page(state, [
            Header("Error"),
            "Points won cannot exceed total points.",
            Button("Try Again", record_match)
        ])

    if errors < 0 or total_smashes < 0 or total_serves < 0:
        return Page(state, [
            Header("Error"),
            "Statistics cannot be negative.",
            Button("Try Again", record_match)
        ])

    if successful_smashes < 0 or successful_smashes > total_smashes:
        return Page(state, [
            Header("Error"),
            "Please enter valid smash statistics.",
            Button("Try Again", record_match)
        ])

    if successful_serves < 0 or successful_serves > total_serves:
        return Page(state, [
            Header("Error"),
            "Please enter valid serve statistics.",
            Button("Try Again", record_match)
        ])

    new_match = Match(
        opponent,
        points_won,
        total_points,
        errors,
        total_smashes,
        successful_smashes,
        total_serves,
        successful_serves
    )

    # Save the match in State

    state.matches.append(new_match)

    return Page(state, [
        Header("Match Saved!"),

        "Your match has been successfully recorded.",

        Button("Record Another Match", record_match),
        Button("View Match History", match_history),
        Button("Back to Home", index)
    ])

@route
def match_history(state: State) -> Page:

    content = [
        Header("Match History"),
        "Review your previous badminton matches."
    ]

    if len(state.matches) == 0:
        content.append(
            "You have not recorded any matches yet."
        )

    match_number = 1

    for match in state.matches:

        content.append(
            Header("Match " + str(match_number))
        )

        content.append(
            "Opponent: " + match.opponent
        )

        content.append(
            "Points Won: " + str(match.points_won)
            + "/" + str(match.total_points)
        )

        content.append(
            "Errors: " + str(match.errors)
        )

        content.append(
            "Smashes: " + str(match.successful_smashes)
            + "/" + str(match.total_smashes)
        )

        content.append(
            "Serves: " + str(match.successful_serves)
            + "/" + str(match.total_serves)
        )

        match_number += 1

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

@route
def statistics(state: State) -> Page:

    if len(state.matches) == 0:
        return Page(state, [
            Header("Performance Statistics"),

            "Record a match to view your statistics.",

            Button("Record Match", record_match),
            Button("Back to Home", index)
        ])

    points_won = 0
    total_points = 0
    errors = 0
    total_smashes = 0
    successful_smashes = 0
    total_serves = 0
    successful_serves = 0

    # Calculate totals from all matches

    for match in state.matches:

        points_won += match.points_won
        total_points += match.total_points
        errors += match.errors
        total_smashes += match.total_smashes
        successful_smashes += match.successful_smashes
        total_serves += match.total_serves
        successful_serves += match.successful_serves

    # Calculate point win rate

    point_rate = points_won / total_points * 100

    # Calculate smash success rate

    smash_rate = 0

    if total_smashes > 0:
        smash_rate = successful_smashes / total_smashes * 100

    # Calculate serve success rate

    serve_rate = 0

    if total_serves > 0:
        serve_rate = successful_serves / total_serves * 100

    # Calculate average errors

    average_errors = errors / len(state.matches)

    return Page(state, [
        Header("Performance Statistics"),

        "Total Matches: " + str(len(state.matches)),

        Header("Point Statistics"),

        "Total Points Won: " + str(points_won),

        "Total Points Played: " + str(total_points),

        "Point Win Rate: "
        + str(round(point_rate, 2)) + "%",

        Header("Smash Statistics"),

        "Total Smashes: " + str(total_smashes),

        "Successful Smashes: " + str(successful_smashes),

        "Smash Success Rate: "
        + str(round(smash_rate, 2)) + "%",

        Header("Serve Statistics"),

        "Total Serves: " + str(total_serves),

        "Successful Serves: " + str(successful_serves),

        "Serve Success Rate: "
        + str(round(serve_rate, 2)) + "%",

        Header("Error Statistics"),

        "Total Errors: " + str(errors),

        "Average Errors per Match: "
        + str(round(average_errors, 2)),

        Button("Match History", match_history),
        Button("Record Match", record_match),
        Button("Back to Home", index)
    ])


# =========================
# PROFILE PAGE
# =========================

@route
def profile(state: State) -> Page:

    return Page(state, [
        Header("My Profile"),

        "Player Name:",
        TextBox("player_name", state.player_name),

        "Your Training Goal:",
        TextBox("goal", state.goal),

        "Favorite Shot:",
        SelectBox("favorite_shot", [
            "Smash",
            "Drop Shot",
            "Clear",
            "Drive",
            "Net Shot"
        ], state.favorite_shot),

        Button("Save Profile", save_profile),
        Button("Back to Home", index)
    ])


# =========================
# SAVE PROFILE ROUTE
# =========================

@route
def save_profile(state: State,
                 player_name: str,
                 goal: str,
                 favorite_shot: str) -> Page:

    if player_name == "":
        return Page(state, [
            Header("Error"),

            "Please enter your name.",

            Button("Back to Profile", profile)
        ])

    state.player_name = player_name
    state.goal = goal
    state.favorite_shot = favorite_shot

    return Page(state, [
        Header("Profile Updated!"),

        "Player Name: " + state.player_name,

        "Training Goal: " + state.goal,

        "Favorite Shot: " + state.favorite_shot,

        Button("Back to Home", index),
        Button("Edit Profile", profile)
    ])


# =========================
# START SERVER
# =========================

start_server(State(
    [],
    "Player",
    "Improve my badminton skills",
    "Smash"
))

