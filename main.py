
from drafter import *
from dataclasses import dataclass


# ==========================================
# WEBSITE INFORMATION
# ==========================================

set_website_title("Badminton Performance Tracker")

set_site_information(
    author="Danny Nguyen",
    description=(
        "A website that helps badminton players track matches, "
        "analyze statistics, and improve their performance."
    ),
    sources=(
        "Drafter Documentation, CISC 106 course materials, "
        "and ChatGPT for coding assistance."
    ),
    planning=(
        "Badminton Performance Tracker Final Project "
        "Mockup and Implementing Requirements."
    ),
    links=[
        "https://github.com/dannyn-68/badminton-performance-tracker",
        "https://drafter-edu.github.io/drafter/"
    ]
)


# ==========================================
# ADVANCED TECHNIQUE: CUSTOM CSS
# ==========================================

# CSS stands for Cascading Style Sheets.
# It allows me to customize the appearance of my website.
#
# add_website_css() adds custom CSS to a Drafter website.
#
# CSS classes begin with a period, such as .hero.
# Drafter components use these classes through the
# classes parameter, such as classes="hero".
#
# CSS Grid organizes cards into columns.
# repeat(auto-fit, minmax(...)) adjusts the number
# of columns depending on the available screen width.
#
# A media query changes the layout on smaller screens,
# making the website easier to use on mobile devices.
#
# Sources:
# https://drafter-edu.github.io/drafter/
# https://developer.mozilla.org/en-US/docs/Web/CSS

set_website_style("none")

add_website_css("""

    body {
        background-color: #f1f5f9;
        font-family: Arial, Helvetica, sans-serif;
        color: #102a43;
        margin: 0;
        padding: 20px;
        line-height: 1.6;
    }

    h1 {
        color: #102a43;
        font-size: 34px;
        font-weight: bold;
        margin: 10px 0 16px;
    }

    h2 {
        color: #102a43;
        font-size: 23px;
    }

    h3 {
        color: #15803d;
        font-size: 18px;
    }

    button {
        background-color: #16a34a;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 13px 22px;
        font-size: 15px;
        font-weight: bold;
        margin: 6px 4px;
        cursor: pointer;
        transition: 0.2s;
    }

    button:hover {
        background-color: #15803d;
        transform: translateY(-2px);
        box-shadow: 0 5px 12px #b6d8c0;
    }

    input, select, textarea {
        background-color: white;
        color: #102a43;
        border: 2px solid #cbd5e1;
        border-radius: 10px;
        padding: 12px;
        margin: 6px 0 16px;
        font-size: 16px;
        width: 100%;
        box-sizing: border-box;
    }

    input:focus, select:focus, textarea:focus {
        border-color: #16a34a;
        outline: none;
        box-shadow: 0 0 0 3px #dcfce7;
    }

    hr {
        border: none;
        height: 1px;
        background-color: #cbd5e1;
        margin: 24px 0;
    }

    .dashboard {
        max-width: 1050px;
        margin: 0 auto;
    }

    .topbar {
        background-color: #102a43;
        color: white;
        border-radius: 14px;
        padding: 16px 24px;
        margin-bottom: 18px;
        font-weight: bold;
        letter-spacing: 2px;
        font-size: 14px;
    }

    .hero {
        background: linear-gradient(
            135deg, #102a43, #14532d
        );
        color: white;
        border-radius: 22px;
        padding: 38px;
        margin-bottom: 24px;
        box-shadow: 0 8px 20px #cbd5e1;
        border-bottom: 5px solid #86efac;
    }

    .hero h1 {
        color: white;
        font-size: 38px;
    }

    .hero h2 {
        color: #dcfce7;
    }

    .hero button {
        background-color: #86efac;
        color: #14532d;
        margin-top: 20px;
    }

    .hero button:hover {
        background-color: #bbf7d0;
    }

    .eyebrow {
        color: #86efac;
        font-size: 13px;
        font-weight: bold;
        letter-spacing: 3px;
        margin-bottom: 12px;
    }

    .hero-description {
        color: #dcfce7;
        font-size: 17px;
        margin: 12px 0;
    }

    .section-title {
        font-size: 24px;
        font-weight: bold;
        color: #102a43;
        margin: 26px 0 14px;
    }

    .section-card {
        background-color: white;
        border-radius: 16px;
        padding: 24px;
        margin: 18px 0;
        box-shadow: 0 4px 14px #dbe4ed;
        border-left: 5px solid #22c55e;
    }

    .stat-grid {
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(170px, 1fr));
        gap: 16px;
        margin: 20px 0;
    }

    .navigation-grid {
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(250px, 1fr));
        gap: 16px;
        margin: 20px 0;
    }

    .stat-card {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 4px 12px #dbe4ed;
    }

    .stat-icon {
        font-size: 28px;
        margin-bottom: 8px;
    }

    .stat-value {
        font-size: 30px;
        font-weight: bold;
        color: #15803d;
        margin: 6px 0;
    }

    .stat-label {
        font-size: 14px;
        color: #64748b;
        font-weight: bold;
    }

    .match-card {
        background-color: white;
        border-radius: 18px;
        padding: 24px;
        margin: 18px 0;
        border-left: 6px solid #16a34a;
        box-shadow: 0 4px 12px #dbe4ed;
    }

    .goal-card {
        background-color: white;
        border-left: 5px solid #22c55e;
        border-radius: 16px;
        padding: 20px;
        margin: 18px 0;
        color: #102a43;
        box-shadow: 0 4px 14px #dbe4ed;
    }

    .success-card {
        background-color: #f0fdf4;
        border: 2px solid #86efac;
        border-radius: 18px;
        padding: 28px;
        margin: 20px 0;
        text-align: center;
        color: #14532d;
    }

    .error-card {
        background-color: #fef2f2;
        border: 2px solid #fca5a5;
        border-radius: 18px;
        padding: 28px;
        margin: 20px 0;
        color: #b91c1c;
    }

    .win-label {
        background-color: #dcfce7;
        color: #15803d;
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
    }

    .loss-label {
        background-color: #fee2e2;
        color: #b91c1c;
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
    }

    .tip-card {
        background-color: #ecfdf5;
        border: 1px solid #bbf7d0;
        border-radius: 14px;
        padding: 20px;
        margin: 20px 0;
        color: #14532d;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 13px;
        padding: 24px;
        margin-top: 30px;
        border-top: 1px solid #cbd5e1;
    }

    @media (max-width: 600px) {

        body {
            padding: 10px;
        }

        .hero {
            padding: 24px;
        }

        .hero h1 {
            font-size: 28px;
        }

        .stat-grid {
            grid-template-columns:
                repeat(2, minmax(0, 1fr));
        }

        .stat-value {
            font-size: 22px;
        }

        .section-card {
            padding: 18px;
        }

        .navigation-grid {
            grid-template-columns: 1fr;
        }
    }

""")


# ==========================================
# DATACLASSES
# ==========================================

@dataclass
class Match:
    """Stores the information and statistics of one badminton match."""

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
    """Stores the player's recorded matches and profile information."""

    matches: list[Match]
    player_name: str
    goal: str
    favorite_shot: str


# ==========================================
# ADVANCED TECHNIQUE: DIV
# ==========================================

# Div is a Drafter component that groups multiple
# website components into one container.
#
# A Div can contain text, headers, buttons,
# input fields, or other Div components.
#
# The classes parameter connects a Div to a CSS
# class defined in add_website_css().
#
# Nesting means placing one Div inside another Div.
# I use nested Div components to create performance
# cards, navigation sections, and styled forms.
#
# Source:
# https://drafter-edu.github.io/drafter/


# ==========================================
# HELPER FUNCTION 1: PERFORMANCE CARD
# ==========================================

def stat_card(icon: str, value: str, label: str) -> Div:
    """
    Creates a styled performance card.

    Args:
        icon: An emoji representing the statistic.
        value: The numerical value as a string.
        label: The name of the statistic.

    Returns:
        A Div containing the icon, value, and label.
    """
    return Div(
        Div(icon, classes="stat-icon"),
        Div(value, classes="stat-value"),
        Div(label, classes="stat-label"),
        classes="stat-card"
    )


# ==========================================
# HELPER FUNCTION 2: CALCULATE PERCENTAGE
# ==========================================

def calculate_percentage(successful: int, total: int) -> float:
    """
    Calculates the percentage of successful attempts.

    Returns 0.0 when the total is zero to avoid
    division by zero.
    """
    if total == 0:
        return 0.0

    return successful / total * 100


# ==========================================
# HELPER FUNCTION 3: COUNT WINS
# ==========================================

def count_wins(matches: list[Match]) -> int:
    """Returns the number of matches won by the player."""

    wins = 0

    for match in matches:
        if match.result == "Win":
            wins += 1

    return wins


# ==========================================
# HELPER FUNCTION 4: TOTAL STATISTICS
# ==========================================

def total_statistics(matches: list[Match]) -> dict[str, int]:
    """
    Calculates the combined statistics of all recorded matches.

    Returns a dictionary containing the total points,
    errors, smashes, successful smashes, serves,
    and successful serves.
    """
    totals = {
        "points_won": 0,
        "total_points": 0,
        "errors": 0,
        "total_smashes": 0,
        "successful_smashes": 0,
        "total_serves": 0,
        "successful_serves": 0
    }

    # Meaningful loop through Match dataclass instances.

    for match in matches:
        totals["points_won"] += match.points_won
        totals["total_points"] += match.total_points
        totals["errors"] += match.errors
        totals["total_smashes"] += match.total_smashes
        totals["successful_smashes"] += match.successful_smashes
        totals["total_serves"] += match.total_serves
        totals["successful_serves"] += match.successful_serves

    return totals


# ==========================================
# HELPER FUNCTION 5: TOP NAVIGATION BAR
# ==========================================

def topbar() -> Div:
    """Creates a reusable banner containing the website title."""

    return Div(
        "🏸 BADMINTON PERFORMANCE TRACKER",
        classes="topbar"
    )


# ==========================================
# HELPER FUNCTION 6: MATCH ERROR PAGE
# ==========================================

def match_error(state: State, message: str) -> Page:
    """
    Creates an error page for invalid match information.

    The page explains the error and allows the user
    to return to the match recording form.
    """
    return Page(state, [
        Div(
            topbar(),

            Header("⚠️ Invalid Input"),

            Div(
                message,
                classes="error-card"
            ),

            Button("Try Again", record_match),

            Button("Back to Home", index),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 1: HOME PAGE
# ==========================================

@route
def index(state: State) -> Page:
    """
    Displays the homepage with the player's match
    statistics, training goal, and navigation buttons.
    """
    wins = count_wins(state.matches)

    losses = len(state.matches) - wins

    win_rate = calculate_percentage(
        wins,
        len(state.matches)
    )

    return Page(state, [
        Div(
            topbar(),

            # Welcome banner

            Div(
                Div(
                    "TRAIN. TRACK. IMPROVE.",
                    classes="eyebrow"
                ),

                Header("🏸 Elevate Your Game."),

                Header(
                    "Welcome, " + state.player_name + "!",
                    2
                ),

                Div(
                    "Every match is a chance to get better. "
                    "Track your performance, discover your "
                    "strengths, and reach your goals.",
                    classes="hero-description"
                ),

                Button(
                    "+ Record a Match",
                    record_match
                ),

                classes="hero"
            ),

            # Performance overview

            Div(
                "Your Performance Overview",
                classes="section-title"
            ),

            Div(
                stat_card(
                    "🏸",
                    str(len(state.matches)),
                    "Matches Recorded"
                ),

                stat_card(
                    "🏆",
                    str(wins),
                    "Total Wins"
                ),

                stat_card(
                    "🎯",
                    str(losses),
                    "Total Losses"
                ),

                stat_card(
                    "📈",
                    str(round(win_rate, 2)) + "%",
                    "Win Rate"
                ),

                classes="stat-grid"
            ),

            # Training goal

            Div(
                Header("🎯 Your Training Goal", 2),

                Div(state.goal),

                Div(
                    "Favorite Shot: "
                    + state.favorite_shot
                ),

                Button("Update Goal", profile),

                classes="section-card"
            ),

            # Dashboard navigation

            Div(
                "Explore Your Dashboard",
                classes="section-title"
            ),

            Div(
                Div(
                    Header("🏸 Record Match", 2),

                    Div(
                        "Log your points, errors, "
                        "smashes, and serves."
                    ),

                    Button(
                        "Record Match",
                        record_match
                    ),

                    classes="section-card"
                ),

                Div(
                    Header("📋 Match History", 2),

                    Div(
                        "Review your previously "
                        "recorded matches."
                    ),

                    Button(
                        "Match History",
                        match_history
                    ),

                    classes="section-card"
                ),

                Div(
                    Header("📊 Statistics", 2),

                    Div(
                        "Analyze your success rates "
                        "and overall performance."
                    ),

                    Button(
                        "View Statistics",
                        statistics
                    ),

                    classes="section-card"
                ),

                Div(
                    Header("💡 Strategy Tips", 2),

                    Div(
                        "Get personalized training "
                        "recommendations."
                    ),

                    Button(
                        "Strategy Tips",
                        strategy_tips
                    ),

                    classes="section-card"
                ),

                Div(
                    Header("👤 My Profile", 2),

                    Div(
                        "Personalize your name, goals, "
                        "and favorite shot."
                    ),

                    Button(
                        "My Profile",
                        profile
                    ),

                    classes="section-card"
                ),

                classes="navigation-grid"
            ),

            # Training tip

            Div(
                Header("💡 Training Tip", 2),

                Div(
                    "Focus on consistency before power. "
                    "Reducing unforced errors can make "
                    "a big difference in your matches."
                ),

                classes="tip-card"
            ),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 2: RECORD MATCH PAGE
# ==========================================

@route
def record_match(state: State) -> Page:
    """
    Displays a form for recording badminton match
    information, points, errors, smashes, and serves.
    """
    return Page(state, [
        Div(
            topbar(),

            Header("📝 Record a Match"),

            Div(
                "Enter your latest match results "
                "and track your progress.",
                classes="goal-card"
            ),

            # Match information

            Div(
                Header("🏸 Match Information", 2),

                "Opponent:",
                TextBox("opponent", ""),

                "Match Date (MM/DD/YYYY):",
                TextBox("date", ""),

                "Match Result:",
                SelectBox(
                    "result",
                    ["Win", "Loss"],
                    "Win"
                ),

                classes="section-card"
            ),

            # Point statistics

            Div(
                Header("🎯 Point Statistics", 2),

                "Points Won:",
                TextBox("points_won", "0"),

                "Total Points:",
                TextBox("total_points", "0"),

                "Errors:",
                TextBox("errors", "0"),

                classes="section-card"
            ),

            # Smash statistics

            Div(
                Header("💥 Smash Statistics", 2),

                "Total Smashes:",
                TextBox("total_smashes", "0"),

                "Successful Smashes:",
                TextBox("successful_smashes", "0"),

                classes="section-card"
            ),

            # Serve statistics

            Div(
                Header("🏸 Serve Statistics", 2),

                "Total Serves:",
                TextBox("total_serves", "0"),

                "Successful Serves:",
                TextBox("successful_serves", "0"),

                classes="section-card"
            ),

            Button("💾 Save Match", save_match),

            Button("🏠 Back to Home", index),

            Div(
                "Record your statistics after every "
                "match to see your improvement.",
                classes="footer"
            ),

            classes="dashboard"
        )
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
    """
    Validates the user's match information and saves
    a new Match instance to the website state.

    Returns a confirmation page for valid information
    or an error page if the input is invalid.
    """

    # ADVANCED TECHNIQUE: EXCEPTION HANDLING
    #
    # TextBox inputs are strings.
    # int() converts a string into an integer.
    #
    # If a user enters invalid text, such as "abc",
    # int() raises a ValueError.
    #
    # The try block attempts the conversion.
    # The except block catches the ValueError and
    # returns an error page instead of crashing.
    #
    # Source:
    # https://docs.python.org/3/tutorial/errors.html

    try:
        won = int(points_won)
        total = int(total_points)
        error_count = int(errors)
        smashes = int(total_smashes)
        good_smashes = int(successful_smashes)
        serves = int(total_serves)
        good_serves = int(successful_serves)

    except ValueError:
        return match_error(
            state,
            "Please enter whole numbers for all statistics."
        )

    # strip() removes whitespace from the beginning
    # and end of a string.

    if opponent.strip() == "":
        return match_error(
            state,
            "Please enter your opponent's name."
        )

    if date.strip() == "":
        return match_error(
            state,
            "Please enter the match date."
        )

    if result != "Win" and result != "Loss":
        return match_error(
            state,
            "Please select Win or Loss."
        )

    if total <= 0 or won < 0 or won > total:
        return match_error(
            state,
            "Points won must be between 0 and total points. "
            "Total points must be greater than zero."
        )

    if error_count < 0:
        return match_error(
            state,
            "The number of errors cannot be negative."
        )

    if smashes < 0 or good_smashes < 0 or good_smashes > smashes:
        return match_error(
            state,
            "Successful smashes must be between "
            "0 and total smashes."
        )

    if serves < 0 or good_serves < 0 or good_serves > serves:
        return match_error(
            state,
            "Successful serves must be between "
            "0 and total serves."
        )

    # Create a new Match instance.

    new_match = Match(
        opponent.strip(),
        date.strip(),
        result,
        won,
        total,
        error_count,
        smashes,
        good_smashes,
        serves,
        good_serves
    )

    # Meaningfully modify the matches field in State.

    state.matches.append(new_match)

    # Meaningful conditional based on the match result.

    if result == "Win":
        message = "🏆 Congratulations on your win!"

    else:
        message = "💪 Keep practicing and improving!"

    return Page(state, [
        Div(
            topbar(),

            Header("🎉 Match Saved Successfully!"),

            Div(
                Header("Match Recorded!", 2),

                "Your match against "
                + new_match.opponent
                + " has been successfully recorded.",

                Div(message),

                classes="success-card"
            ),

            Div(
                Header("Match Summary", 2),

                Div(
                    "Opponent: " + new_match.opponent
                ),

                Div(
                    "📅 Date: " + new_match.date
                ),

                Div(
                    "Result: " + result
                ),

                Div(
                    "Points Won: "
                    + str(won)
                    + "/"
                    + str(total)
                ),

                classes="match-card"
            ),

            stat_card(
                "🏸",
                str(len(state.matches)),
                "Total Matches Recorded"
            ),

            Button(
                "📝 Record Another Match",
                record_match
            ),

            Button(
                "📋 View Match History",
                match_history
            ),

            Button(
                "📊 View Statistics",
                statistics
            ),

            Button(
                "🏠 Back to Home",
                index
            ),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 4: MATCH HISTORY PAGE
# ==========================================

@route
def match_history(state: State) -> Page:
    """
    Displays all previously recorded badminton matches,
    including the opponent, date, result, and statistics.
    """
    content = [
        topbar(),

        Header("📋 Match History"),

        Div(
            "Review your previously recorded "
            "matches and celebrate your progress.",
            classes="goal-card"
        )
    ]

    if len(state.matches) == 0:
        content.append(
            Div(
                "You have not recorded any matches yet. "
                "Record your first match to get started!",
                classes="match-card"
            )
        )

    match_number = 1

    # Meaningful loop:
    # Iterate through the Match instances in State
    # and display each recorded match.

    for match in state.matches:

        if match.result == "Win":
            result_label = Div(
                "🏆 Result: WIN",
                classes="win-label"
            )

        else:
            result_label = Div(
                "Result: LOSS",
                classes="loss-label"
            )

        content.append(
            Div(
                Header(
                    "🏸 Match " + str(match_number),
                    2
                ),

                Div(
                    "Opponent: " + match.opponent
                ),

                Div(
                    "📅 Date: " + match.date
                ),

                result_label,

                HorizontalRule(),

                Div(
                    "🎯 Points Won: "
                    + str(match.points_won)
                    + "/"
                    + str(match.total_points)
                ),

                Div(
                    "Errors: " + str(match.errors)
                ),

                Div(
                    "💥 Successful Smashes: "
                    + str(match.successful_smashes)
                    + "/"
                    + str(match.total_smashes)
                ),

                Div(
                    "🏸 Successful Serves: "
                    + str(match.successful_serves)
                    + "/"
                    + str(match.total_serves)
                ),

                classes="match-card"
            )
        )

        match_number += 1

    content.append(
        Button("📝 Record Match", record_match)
    )

    content.append(
        Button("📊 Performance Statistics", statistics)
    )

    content.append(
        Button("🏠 Back to Home", index)
    )

    content.append(
        Div(
            "Every match is an opportunity to improve.",
            classes="footer"
        )
    )

    return Page(state, content)


# ==========================================
# ROUTE 5: PERFORMANCE STATISTICS PAGE
# ==========================================

@route
def statistics(state: State) -> Page:
    """
    Calculates and displays the player's overall
    badminton performance statistics.

    Displays win rate, point win rate, smash success
    rate, serve success rate, and error statistics.
    """
    if len(state.matches) == 0:
        return Page(state, [
            Div(
                topbar(),

                Header("📊 Performance Statistics"),

                Div(
                    "Record a match to unlock your "
                    "performance statistics!",
                    classes="goal-card"
                ),

                Button(
                    "📝 Record Match",
                    record_match
                ),

                Button(
                    "🏠 Back to Home",
                    index
                ),

                classes="dashboard"
            )
        ])

    # Use helper functions to reduce repeated calculations.

    wins = count_wins(state.matches)

    losses = len(state.matches) - wins

    totals = total_statistics(state.matches)

    win_rate = calculate_percentage(
        wins,
        len(state.matches)
    )

    point_rate = calculate_percentage(
        totals["points_won"],
        totals["total_points"]
    )

    smash_rate = calculate_percentage(
        totals["successful_smashes"],
        totals["total_smashes"]
    )

    serve_rate = calculate_percentage(
        totals["successful_serves"],
        totals["total_serves"]
    )

    average_errors = (
        totals["errors"] / len(state.matches)
    )

    error_rate = calculate_percentage(
        totals["errors"],
        totals["total_points"]
    )

    # Display N/A when no attempts have been recorded.

    if totals["total_smashes"] == 0:
        smash_display = "N/A"

    else:
        smash_display = str(round(smash_rate, 2)) + "%"

    if totals["total_serves"] == 0:
        serve_display = "N/A"

    else:
        serve_display = str(round(serve_rate, 2)) + "%"

    return Page(state, [
        Div(
            topbar(),

            Header("📊 Performance Statistics"),

            Div(
                "Understand your strengths and discover "
                "opportunities to improve your game.",
                classes="goal-card"
            ),

            Header("🏆 Match Overview", 2),

            Div(
                stat_card(
                    "🏸",
                    str(len(state.matches)),
                    "Total Matches"
                ),

                stat_card(
                    "🏆",
                    str(wins),
                    "Wins"
                ),

                stat_card(
                    "🎯",
                    str(losses),
                    "Losses"
                ),

                stat_card(
                    "📈",
                    str(round(win_rate, 2)) + "%",
                    "Win Rate"
                ),

                classes="stat-grid"
            ),

            # Point statistics

            Div(
                Header("🎯 Point Statistics", 2),

                Div(
                    "Total Points Won: "
                    + str(totals["points_won"])
                ),

                Div(
                    "Total Points Played: "
                    + str(totals["total_points"])
                ),

                stat_card(
                    "🎯",
                    str(round(point_rate, 2)) + "%",
                    "Point Win Rate"
                ),

                classes="section-card"
            ),

            # Smash statistics

            Div(
                Header("💥 Smash Statistics", 2),

                Div(
                    "Total Smashes: "
                    + str(totals["total_smashes"])
                ),

                Div(
                    "Successful Smashes: "
                    + str(totals["successful_smashes"])
                ),

                stat_card(
                    "💥",
                    smash_display,
                    "Smash Success Rate"
                ),

                classes="section-card"
            ),

            # Serve statistics

            Div(
                Header("🏸 Serve Statistics", 2),

                Div(
                    "Total Serves: "
                    + str(totals["total_serves"])
                ),

                Div(
                    "Successful Serves: "
                    + str(totals["successful_serves"])
                ),

                stat_card(
                    "🏸",
                    serve_display,
                    "Serve Success Rate"
                ),

                classes="section-card"
            ),

            # Error statistics

            Div(
                Header("⚠️ Error Statistics", 2),

                Div(
                    "Total Errors: "
                    + str(totals["errors"])
                ),

                Div(
                    stat_card(
                        "🎯",
                        str(round(average_errors, 2)),
                        "Average Errors per Match"
                    ),

                    stat_card(
                        "📊",
                        str(round(error_rate, 2)),
                        "Errors per 100 Points"
                    ),

                    classes="stat-grid"
                ),

                classes="section-card"
            ),

            Button(
                "💡 View Strategy Tips",
                strategy_tips
            ),

            Button(
                "📋 Match History",
                match_history
            ),

            Button(
                "📝 Record Match",
                record_match
            ),

            Button(
                "🏠 Back to Home",
                index
            ),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 6: STRATEGY TIPS PAGE
# ==========================================

@route
def strategy_tips(state: State) -> Page:
    """
    Provides personalized training recommendations
    based on the player's recorded match statistics.

    Suggests ways to improve smashes, serves,
    and reduce errors.
    """
    if len(state.matches) == 0:
        return Page(state, [
            Div(
                topbar(),

                Header("💡 Strategy Tips"),

                Div(
                    "Record your first match to receive "
                    "personalized training recommendations.",
                    classes="goal-card"
                ),

                Button(
                    "📝 Record Match",
                    record_match
                ),

                Button(
                    "🏠 Back to Home",
                    index
                ),

                classes="dashboard"
            )
        ])

    totals = total_statistics(state.matches)

    smash_rate = calculate_percentage(
        totals["successful_smashes"],
        totals["total_smashes"]
    )

    serve_rate = calculate_percentage(
        totals["successful_serves"],
        totals["total_serves"]
    )

    average_errors = (
        totals["errors"] / len(state.matches)
    )

    # These thresholds are simple training targets
    # chosen for this project, not professional standards.

    # Smash recommendation

    if totals["total_smashes"] == 0:
        smash_message = (
            "Record some smashes to receive "
            "smash-specific recommendations."
        )

    elif smash_rate < 60:
        smash_message = (
            "Your smash success rate is "
            + str(round(smash_rate, 2))
            + "%. Focus on timing, placement, "
            "and accuracy before increasing power."
        )

    else:
        smash_message = (
            "Great job! Your smash success rate is "
            + str(round(smash_rate, 2))
            + "%. Keep improving your placement "
            "and shot selection."
        )

    # Serve recommendation

    if totals["total_serves"] == 0:
        serve_message = (
            "Record some serves to receive "
            "serve-specific recommendations."
        )

    elif serve_rate < 80:
        serve_message = (
            "Your serve success rate is "
            + str(round(serve_rate, 2))
            + "%. Practice consistent low serves "
            "and focus on accuracy."
        )

    else:
        serve_message = (
            "Excellent serving! Your success rate is "
            + str(round(serve_rate, 2))
            + "%. Keep practicing different "
            "serve placements."
        )

    # Error recommendation

    if average_errors > 10:
        error_message = (
            "You average "
            + str(round(average_errors, 2))
            + " errors per match. Focus on "
            "consistent footwork, safer shots, "
            "and reducing unforced errors."
        )

    else:
        error_message = (
            "Good consistency! You average "
            + str(round(average_errors, 2))
            + " errors per match. Keep focusing "
            "on controlled and accurate shots."
        )

    return Page(state, [
        Div(
            topbar(),

            Header("💡 Personalized Strategy Tips"),

            Div(
                "These recommendations are based on "
                "your recorded match statistics.",
                classes="goal-card"
            ),

            Div(
                Header("💥 Improve Your Smash", 2),

                Div(smash_message),

                classes="section-card"
            ),

            Div(
                Header("🏸 Improve Your Serve", 2),

                Div(serve_message),

                classes="section-card"
            ),

            Div(
                Header("🎯 Reduce Your Errors", 2),

                Div(error_message),

                classes="section-card"
            ),

            Div(
                Header("🔥 Your Training Goal", 2),

                Div(state.goal),

                Button(
                    "Update Training Goal",
                    profile
                ),

                classes="tip-card"
            ),

            Button(
                "📊 View Statistics",
                statistics
            ),

            Button(
                "🏠 Back to Home",
                index
            ),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 7: PROFILE PAGE
# ==========================================

@route
def profile(state: State) -> Page:
    """
    Displays a form for editing the player's name,
    training goal, and favorite badminton shot.
    """
    return Page(state, [
        Div(
            topbar(),

            Header("👤 My Player Profile"),

            Div(
                "Customize your player information "
                "and set your personal badminton goals.",
                classes="goal-card"
            ),

            Div(
                Header("🏸 Player Information", 2),

                "Player Name:",

                TextBox(
                    "player_name",
                    state.player_name
                ),

                "Training Goal:",

                TextBox(
                    "goal",
                    state.goal
                ),

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

                classes="section-card"
            ),

            Button(
                "💾 Save Profile",
                save_profile
            ),

            Button(
                "🏠 Back to Home",
                index
            ),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 8: SAVE PROFILE
# ==========================================

@route
def save_profile(
    state: State,
    player_name: str,
    goal: str,
    favorite_shot: str
) -> Page:
    """
    Validates and updates the player's profile information.

    Modifies the player's name, training goal, and
    favorite shot. Returns an error page if the
    player's name is empty.
    """
    if player_name.strip() == "":
        return Page(state, [
            Div(
                topbar(),

                Header("⚠️ Invalid Input"),

                Div(
                    "Please enter your name.",
                    classes="error-card"
                ),

                Button(
                    "Back to Profile",
                    profile
                ),

                classes="dashboard"
            )
        ])

    # Meaningfully modify three State attributes.

    state.player_name = player_name.strip()

    state.goal = goal

    state.favorite_shot = favorite_shot

    return Page(state, [
        Div(
            topbar(),

            Header("🎉 Profile Updated!"),

            Div(
                "Your profile has been successfully saved.",
                classes="success-card"
            ),

            Div(
                Header("👤 Player Information", 2),

                Div(
                    "Player Name: "
                    + state.player_name
                ),

                Div(
                    "Training Goal: "
                    + state.goal
                ),

                Div(
                    "Favorite Shot: "
                    + state.favorite_shot
                ),

                classes="section-card"
            ),

            Button(
                "🏠 Back to Home",
                index
            ),

            Button(
                "✏️ Edit Profile",
                profile
            ),

            classes="dashboard"
        )
    ])


# ==========================================
# UNIT TESTS
# ==========================================

# Drafter provides built-in testing functions.
#
# assert_equal compares actual and expected values.
#
# assert_has checks whether text or a component
# appears inside a returned Page.
#
# assert_state compares the State returned by a route
# with the expected State.
#
# Each test creates a separate State so testing
# does not modify the website's starting data.
#
# Source:
# https://drafter-edu.github.io/drafter/reference/testing-functions/


# ==========================================
# TEST HELPER: SAMPLE STATE
# ==========================================

def create_test_state() -> State:
    """
    Creates a new sample State containing two matches,
    one win and one loss, and player information.
    """
    return State(
        [
            Match(
                "Alex",
                "11/10/2026",
                "Win",
                21,
                35,
                5,
                10,
                8,
                10,
                9
            ),

            Match(
                "Chris",
                "11/11/2026",
                "Loss",
                15,
                36,
                7,
                8,
                4,
                10,
                7
            )
        ],
        "Danny",
        "Improve my smash",
        "Smash"
    )


# ==========================================
# TEST 1: HOME PAGE
# ==========================================

def test_index() -> None:
    """
    Tests that the homepage displays the correct
    player information and performance overview.
    """
    test_state = create_test_state()

    page = index(test_state)

    assert_equal(page.state, test_state)

    assert_has(page, "Welcome, Danny!")

    assert_has(page, "Matches Recorded")

    assert_has(page, "50.0%")

    assert_has(page, "Improve my smash")

    assert_has(page, "Favorite Shot: Smash")

    # Test the homepage with no matches.

    empty_state = State(
        [],
        "Player",
        "Improve my skills",
        "Smash"
    )

    empty_page = index(empty_state)

    assert_has(empty_page, "Welcome, Player!")

    assert_has(empty_page, "0.0%")


# ==========================================
# TEST 2: RECORD MATCH PAGE
# ==========================================

def test_record_match() -> None:
    """
    Tests that the recording page displays all
    required match input fields.
    """
    test_state = create_test_state()

    page = record_match(test_state)

    assert_equal(page.state, test_state)

    assert_has(page, "Record a Match")

    assert_has(page, TextBox("opponent", ""))

    assert_has(page, TextBox("date", ""))

    assert_has(
        page,
        SelectBox("result", ["Win", "Loss"], "Win")
    )

    assert_has(page, TextBox("points_won", "0"))

    assert_has(page, TextBox("total_points", "0"))

    assert_has(page, TextBox("errors", "0"))

    assert_has(page, TextBox("total_smashes", "0"))

    assert_has(page, TextBox("successful_smashes", "0"))

    assert_has(page, TextBox("total_serves", "0"))

    assert_has(page, TextBox("successful_serves", "0"))

    assert_has(page, "Save Match")


# ==========================================
# TEST 3: SAVE MATCH
# ==========================================

def test_save_match() -> None:
    """
    Tests that valid matches are saved and invalid
    match inputs do not modify the matches list.
    """
    test_state = State(
        [],
        "Danny",
        "Improve my smash",
        "Smash"
    )

    # Test a valid winning match.

    page = save_match(
        test_state,
        "Alex",
        "11/12/2026",
        "Win",
        "21",
        "35",
        "5",
        "10",
        "8",
        "10",
        "9"
    )

    expected_match = Match(
        "Alex",
        "11/12/2026",
        "Win",
        21,
        35,
        5,
        10,
        8,
        10,
        9
    )

    assert_equal(
        test_state.matches,
        [expected_match]
    )

    assert_equal(
        len(test_state.matches),
        1
    )

    assert_has(
        page,
        "Match Saved Successfully!"
    )

    assert_has(
        page,
        "Congratulations on your win!"
    )

    # Test a valid losing match.

    loss_page = save_match(
        test_state,
        "Chris",
        "11/13/2026",
        "Loss",
        "15",
        "36",
        "7",
        "8",
        "4",
        "10",
        "7"
    )

    assert_equal(
        len(test_state.matches),
        2
    )

    assert_equal(
        test_state.matches[1].result,
        "Loss"
    )

    assert_has(
        loss_page,
        "Keep practicing and improving!"
    )

    # Test invalid numeric input.

    invalid_page = save_match(
        test_state,
        "Alex",
        "11/14/2026",
        "Win",
        "abc",
        "35",
        "5",
        "10",
        "8",
        "10",
        "9"
    )

    assert_equal(
        len(test_state.matches),
        2
    )

    assert_has(
        invalid_page,
        "Please enter whole numbers for all statistics."
    )

    # Test points won greater than total points.

    invalid_points_page = save_match(
        test_state,
        "Alex",
        "11/14/2026",
        "Win",
        "40",
        "35",
        "5",
        "10",
        "8",
        "10",
        "9"
    )

    assert_equal(
        len(test_state.matches),
        2
    )

    assert_has(
        invalid_points_page,
        "Points won must be between 0 and total points."
    )

    # Test successful smashes greater than total smashes.

    invalid_smash_page = save_match(
        test_state,
        "Alex",
        "11/14/2026",
        "Win",
        "21",
        "35",
        "5",
        "10",
        "12",
        "10",
        "9"
    )

    assert_equal(
        len(test_state.matches),
        2
    )

    assert_has(
        invalid_smash_page,
        "Successful smashes must be between 0 and total smashes."
    )

    # Test an empty opponent name.

    empty_name_page = save_match(
        test_state,
        "",
        "11/14/2026",
        "Win",
        "21",
        "35",
        "5",
        "10",
        "8",
        "10",
        "9"
    )

    assert_equal(
        len(test_state.matches),
        2
    )

    assert_has(
        empty_name_page,
        "Please enter your opponent's name."
    )

    # Test an empty date.

    empty_date_page = save_match(
        test_state,
        "Alex",
        "",
        "Win",
        "21",
        "35",
        "5",
        "10",
        "8",
        "10",
        "9"
    )

    assert_equal(
        len(test_state.matches),
        2
    )

    assert_has(
        empty_date_page,
        "Please enter the match date."
    )

    # Test an invalid result.

    invalid_result_page = save_match(
        test_state,
        "Alex",
        "11/14/2026",
        "Draw",
        "21",
        "35",
        "5",
        "10",
        "8",
        "10",
        "9"
    )

    assert_equal(
        len(test_state.matches),
        2
    )

    assert_has(
        invalid_result_page,
        "Please select Win or Loss."
    )

    # Test negative errors.

    negative_errors_page = save_match(
        test_state,
        "Alex",
        "11/14/2026",
        "Win",
        "21",
        "35",
        "-5",
        "10",
        "8",
        "10",
        "9"
    )

    assert_equal(
        len(test_state.matches),
        2
    )

    assert_has(
        negative_errors_page,
        "The number of errors cannot be negative."
    )

    # Test zero total points.

    zero_points_page = save_match(
        test_state,
        "Alex",
        "11/14/2026",
        "Win",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0"
    )

    assert_equal(
        len(test_state.matches),
        2
    )

    assert_has(
        zero_points_page,
        "Total points must be greater than zero."
    )

    # Test successful serves greater than total serves.

    invalid_serve_page = save_match(
        test_state,
        "Alex",
        "11/14/2026",
        "Win",
        "21",
        "35",
        "5",
        "10",
        "8",
        "10",
        "11"
    )

    assert_equal(
        len(test_state.matches),
        2
    )

    assert_has(
        invalid_serve_page,
        "Successful serves must be between 0 and total serves."
    )


# ==========================================
# TEST 4: MATCH HISTORY
# ==========================================

def test_match_history() -> None:
    """
    Tests that recorded matches are displayed
    and an empty history shows an appropriate message.
    """
    test_state = create_test_state()

    page = match_history(test_state)

    assert_equal(page.state, test_state)

    assert_has(page, "Match History")

    assert_has(page, "Match 1")

    assert_has(page, "Match 2")

    assert_has(page, "Opponent: Alex")

    assert_has(page, "Opponent: Chris")

    assert_has(page, "Result: WIN")

    assert_has(page, "Result: LOSS")

    assert_has(page, "Points Won: 21/35")

    assert_has(page, "Points Won: 15/36")

    # Test an empty history.

    empty_state = State(
        [],
        "Danny",
        "Improve my skills",
        "Smash"
    )

    empty_page = match_history(empty_state)

    assert_has(
        empty_page,
        "You have not recorded any matches yet."
    )


# ==========================================
# TEST 5: PERFORMANCE STATISTICS
# ==========================================

def test_statistics() -> None:
    """
    Tests that performance statistics display correct
    percentages, totals, and empty-state messages.
    """
    test_state = create_test_state()

    page = statistics(test_state)

    assert_equal(page.state, test_state)

    assert_has(page, "Performance Statistics")

    # One win out of two matches = 50%.

    assert_has(page, "50.0%")

    # 36 points won out of 71 = 50.70%.

    assert_has(page, "Total Points Won: 36")

    assert_has(page, "Total Points Played: 71")

    assert_has(page, "50.7%")

    # 12 successful smashes out of 18 = 66.67%.

    assert_has(page, "Total Smashes: 18")

    assert_has(page, "Successful Smashes: 12")

    assert_has(page, "66.67%")

    # 16 successful serves out of 20 = 80%.

    assert_has(page, "Total Serves: 20")

    assert_has(page, "Successful Serves: 16")

    assert_has(page, "80.0%")

    # 12 errors across two matches = 6 per match.

    assert_has(page, "Total Errors: 12")

    assert_has(
        page,
        stat_card(
            "🎯",
            "6.0",
            "Average Errors per Match"
        )
    )

    # Test statistics with no recorded matches.

    empty_state = State(
        [],
        "Danny",
        "Improve my skills",
        "Smash"
    )

    empty_page = statistics(empty_state)

    assert_has(
        empty_page,
        "Record a match to unlock your performance statistics!"
    )

    # Test zero smash and serve attempts.

    zero_state = State(
        [
            Match(
                "Alex",
                "11/12/2026",
                "Win",
                21,
                35,
                0,
                0,
                0,
                0,
                0
            )
        ],
        "Danny",
        "Improve my skills",
        "Smash"
    )

    zero_page = statistics(zero_state)

    assert_has(
        zero_page,
        stat_card(
            "💥",
            "N/A",
            "Smash Success Rate"
        )
    )

    assert_has(
        zero_page,
        stat_card(
            "🏸",
            "N/A",
            "Serve Success Rate"
        )
    )


# ==========================================
# TEST 6: STRATEGY TIPS
# ==========================================

def test_strategy_tips() -> None:
    """
    Tests that training recommendations change
    based on the player's recorded statistics.
    """
    test_state = create_test_state()

    page = strategy_tips(test_state)

    assert_equal(page.state, test_state)

    assert_has(page, "Personalized Strategy Tips")

    assert_has(page, "Great job!")

    assert_has(page, "Excellent serving!")

    assert_has(page, "Good consistency!")

    # Test performance below the training targets.

    low_state = State(
        [
            Match(
                "Alex",
                "11/12/2026",
                "Loss",
                10,
                31,
                15,
                10,
                3,
                10,
                5
            )
        ],
        "Danny",
        "Improve my skills",
        "Smash"
    )

    low_page = strategy_tips(low_state)

    assert_has(
        low_page,
        "Focus on timing, placement, and accuracy"
    )

    assert_has(
        low_page,
        "Practice consistent low serves"
    )

    assert_has(
        low_page,
        "reducing unforced errors"
    )

    # Test no recorded matches.

    empty_state = State(
        [],
        "Danny",
        "Improve my skills",
        "Smash"
    )

    empty_page = strategy_tips(empty_state)

    assert_has(
        empty_page,
        "Record your first match"
    )

    # Test zero smash and serve attempts.

    zero_state = State(
        [
            Match(
                "Alex",
                "11/12/2026",
                "Win",
                21,
                35,
                5,
                0,
                0,
                0,
                0
            )
        ],
        "Danny",
        "Improve my skills",
        "Smash"
    )

    zero_page = strategy_tips(zero_state)

    assert_has(
        zero_page,
        "Record some smashes"
    )

    assert_has(
        zero_page,
        "Record some serves"
    )


# ==========================================
# TEST 7: PROFILE PAGE
# ==========================================

def test_profile() -> None:
    """
    Tests that the profile page displays the player's
    current information in the correct input fields.
    """
    test_state = create_test_state()

    page = profile(test_state)

    assert_equal(page.state, test_state)

    assert_has(page, "My Player Profile")

    assert_has(
        page,
        TextBox("player_name", "Danny")
    )

    assert_has(
        page,
        TextBox("goal", "Improve my smash")
    )

    assert_has(
        page,
        SelectBox(
            "favorite_shot",
            [
                "Smash",
                "Drop Shot",
                "Clear",
                "Drive",
                "Net Shot"
            ],
            "Smash"
        )
    )

    assert_has(page, "Save Profile")


# ==========================================
# TEST 8: SAVE PROFILE
# ==========================================

def test_save_profile() -> None:
    """
    Tests that saving a profile updates all three
    profile fields and rejects empty player names.
    """
    test_state = State(
        [],
        "Player",
        "Improve my skills",
        "Smash"
    )

    page = save_profile(
        test_state,
        "Danny",
        "Improve my serve",
        "Drop Shot"
    )

    assert_equal(
        test_state.player_name,
        "Danny"
    )

    assert_equal(
        test_state.goal,
        "Improve my serve"
    )

    assert_equal(
        test_state.favorite_shot,
        "Drop Shot"
    )

    assert_has(page, "Profile Updated!")

    # Test an empty player name.

    invalid_page = save_profile(
        test_state,
        "",
        "New goal",
        "Clear"
    )

    assert_equal(
        test_state.player_name,
        "Danny"
    )

    assert_equal(
        test_state.goal,
        "Improve my serve"
    )

    assert_equal(
        test_state.favorite_shot,
        "Drop Shot"
    )

    assert_has(
        invalid_page,
        "Please enter your name."
    )

    # Test a name containing only whitespace.

    whitespace_page = save_profile(
        test_state,
        "   ",
        "New goal",
        "Drive"
    )

    assert_equal(
        test_state.player_name,
        "Danny"
    )

    assert_has(
        whitespace_page,
        "Invalid Input"
    )


# ==========================================
# TEST HELPER FUNCTIONS
# ==========================================

def test_helper_functions() -> None:
    """
    Tests the helper functions for correct percentages,
    win counts, combined statistics, and components.
    """

    # Test calculate_percentage.

    assert_equal(
        calculate_percentage(5, 10),
        50.0
    )

    assert_equal(
        calculate_percentage(0, 10),
        0.0
    )

    assert_equal(
        calculate_percentage(10, 10),
        100.0
    )

    assert_equal(
        calculate_percentage(0, 0),
        0.0
    )

    assert_equal(
        calculate_percentage(3, 4),
        75.0
    )

    # Test count_wins.

    test_state = create_test_state()

    assert_equal(
        count_wins(test_state.matches),
        1
    )

    assert_equal(
        count_wins([]),
        0
    )

    # Test total_statistics.

    expected_totals = {
        "points_won": 36,
        "total_points": 71,
        "errors": 12,
        "total_smashes": 18,
        "successful_smashes": 12,
        "total_serves": 20,
        "successful_serves": 16
    }

    assert_equal(
        total_statistics(test_state.matches),
        expected_totals
    )

    empty_totals = {
        "points_won": 0,
        "total_points": 0,
        "errors": 0,
        "total_smashes": 0,
        "successful_smashes": 0,
        "total_serves": 0,
        "successful_serves": 0
    }

    assert_equal(
        total_statistics([]),
        empty_totals
    )

    # Test stat_card.

    card = stat_card(
        "🏆",
        "5",
        "Wins"
    )

    assert_has(card, "Wins")

    assert_has(card, "5")

    # Test topbar.

    assert_has(
        topbar(),
        "BADMINTON PERFORMANCE TRACKER"
    )

    # Test match_error.

    error_page = match_error(
        test_state,
        "Invalid match information."
    )

    assert_equal(
        error_page.state,
        test_state
    )

    assert_has(
        error_page,
        "Invalid match information."
    )


# ==========================================
# RUN ALL UNIT TESTS
# ==========================================

# Tests must run before start_server().
# Each test uses a separate sample State.

test_index()

test_record_match()

test_save_match()

test_match_history()

test_statistics()

test_strategy_tips()

test_profile()

test_save_profile()

test_helper_functions()


# ==========================================
# START SERVER
# ==========================================

start_server(State(
    [],
    "Player",
    "Improve my badminton skills",
    "Smash"
))
