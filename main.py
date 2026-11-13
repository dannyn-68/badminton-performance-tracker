
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
        "https://drafter-edu.github.io/drafter/",
        "https://drafter-edu.github.io/drafter/reference/components/layout/div/"
    ]
)


# ==========================================
# ADVANCED TECHNIQUE: CUSTOM CSS
# ==========================================

# CSS stands for Cascading Style Sheets.
# It is used to customize the appearance of a website.
#
# add_website_css() allows me to add custom CSS
# to my Drafter website.
#
# I use CSS to change background colors, fonts,
# buttons, borders, spacing, and page layouts.
#
# CSS classes begin with a period, such as .hero.
# A Drafter component can use that CSS class
# by setting classes="hero".
#
# Source:
# https://drafter-edu.github.io/drafter/

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
        color: #15803d;
        font-size: 20px;
        font-weight: bold;
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
# ADVANCED TECHNIQUE: DIV
# ==========================================

# Div is a Drafter component that groups multiple
# website components into a single container.
#
# A Div can contain text, headers, buttons,
# input fields, or other Div components.
#
# I use Div to organize my website into sections,
# such as the welcome banner, performance cards,
# navigation buttons, and training goals.
#
# The classes parameter connects a Div to a CSS
# class defined in add_website_css().
#
# For example:
#
# Div(
#     Header("Welcome"),
#     "Track your badminton performance.",
#     classes="hero"
# )
#
# The hero CSS class gives the entire container
# a gradient background, padding, rounded corners,
# and other decorations.
#
# A Div can also contain other Div components.
# This is called nesting.
#
# Using nested Div components allows me to create
# organized sections and responsive card layouts.
#
# Source:
# https://drafter-edu.github.io/drafter/reference/components/layout/div/


# ==========================================
# HELPER FUNCTION: PERFORMANCE CARD
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

    This function uses nested Div components
    to style each part of the performance card.

    The outer Div uses the stat-card CSS class.
    Each inner Div uses a different CSS class
    to customize its appearance.
    """

    return Div(
        Div(icon, classes="stat-icon"),

        Div(value, classes="stat-value"),

        Div(label, classes="stat-label"),

        classes="stat-card"
    )


# ==========================================
# ROUTE 1: HOME PAGE
# ==========================================

@route
def index(state: State) -> Page:

    # Calculate total wins and losses.

    wins = 0
    losses = 0

    for match in state.matches:

        if match.result == "Win":
            wins += 1

        else:
            losses += 1

    # Calculate win percentage.
    # Avoid division by zero if there are no matches.

    win_rate = 0.0

    if len(state.matches) > 0:
        win_rate = wins / len(state.matches) * 100

    return Page(state, [

        # The outer Div groups the entire homepage.
        # The dashboard CSS class controls its width
        # and centers it on the screen.

        Div(

            # ==================================
            # TOP NAVIGATION BAR
            # ==================================

            Div(
                "🏸 BADMINTON PERFORMANCE TRACKER",
                classes="topbar"
            ),

            # ==================================
            # WELCOME BANNER
            # ==================================

            # This Div groups the welcome heading,
            # description, and Record Match button.
            # The hero class gives the entire group
            # a navy-to-green gradient background.

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

            # ==================================
            # PERFORMANCE OVERVIEW
            # ==================================

            Div(
                "Your Performance Overview",
                classes="section-title"
            ),

            # This Div contains four performance cards.
            # The stat-grid CSS class uses a grid layout
            # to display the cards next to each other.

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

            # ==================================
            # TRAINING GOAL
            # ==================================

            Div(

                Header("🎯 Your Training Goal", 2),

                Div(state.goal),

                Div(
                    "Favorite Shot: "
                    + state.favorite_shot
                ),

                Button(
                    "Update Goal",
                    profile
                ),

                classes="section-card"
            ),

            # ==================================
            # DASHBOARD NAVIGATION
            # ==================================

            Div(
                "Explore Your Dashboard",
                classes="section-title"
            ),

            # Each navigation card is a separate Div.
            # The outer Div arranges the cards
            # into a responsive grid layout.

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

            # ==================================
            # TRAINING TIP
            # ==================================

            Div(

                Header("💡 Training Tip", 2),

                Div(
                    "Focus on consistency before power. "
                    "Reducing unforced errors can make "
                    "a big difference in your matches."
                ),

                classes="tip-card"
            ),

            # ==================================
            # FOOTER
            # ==================================

            Div(

                "Badminton Performance Tracker",

                Div("Train. Track. Improve."),

                Div(
                    "Designed by Danny Nguyen | 2026"
                ),

                classes="footer"
            ),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 2: RECORD MATCH PAGE
# ==========================================

@route
def record_match(state: State) -> Page:

    return Page(state, [

        Div(

            Div(
                "🏸 BADMINTON PERFORMANCE TRACKER",
                classes="topbar"
            ),

            Header("📝 Record a Match"),

            Div(
                "Enter your latest match results "
                "and track your progress.",
                classes="goal-card"
            ),

            # Match information section

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

            # Point statistics section

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

            # Smash statistics section

            Div(

                Header("💥 Smash Statistics", 2),

                "Total Smashes:",
                TextBox("total_smashes", "0"),

                "Successful Smashes:",
                TextBox("successful_smashes", "0"),

                classes="section-card"
            ),

            # Serve statistics section

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

    # Advanced technique: Exception handling.
    #
    # TextBox inputs are strings.
    # The try block converts them into integers.
    # If a user enters invalid text, int() raises
    # a ValueError.
    # The except block catches the error and
    # displays a message instead of crashing.

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

            Header("⚠️ Invalid Input"),

            Div(
                "Please enter whole numbers "
                "for all statistics.",
                classes="error-card"
            ),

            Button("Try Again", record_match),

            Button("Back to Home", index)
        ])

    # Check the opponent's name.

    if opponent.strip() == "":

        return Page(state, [

            Header("⚠️ Invalid Input"),

            Div(
                "Please enter your opponent's name.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check the match date.

    if date.strip() == "":

        return Page(state, [

            Header("⚠️ Invalid Input"),

            Div(
                "Please enter the match date.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check the match result.

    if result != "Win" and result != "Loss":

        return Page(state, [

            Header("⚠️ Invalid Input"),

            Div(
                "Please select Win or Loss.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check the point statistics.

    if total <= 0 or won < 0 or won > total:

        return Page(state, [

            Header("⚠️ Invalid Input"),

            Div(
                "Points won must be between 0 "
                "and total points. Total points "
                "must be greater than zero.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check the error count.

    if error_count < 0:

        return Page(state, [

            Header("⚠️ Invalid Input"),

            Div(
                "The number of errors cannot be negative.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check the smash statistics.

    if smashes < 0 or good_smashes < 0 or good_smashes > smashes:

        return Page(state, [

            Header("⚠️ Invalid Input"),

            Div(
                "Successful smashes must be between "
                "0 and total smashes.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check the serve statistics.

    if serves < 0 or good_serves < 0 or good_serves > serves:

        return Page(state, [

            Header("⚠️ Invalid Input"),

            Div(
                "Successful serves must be between "
                "0 and total serves.",
                classes="error-card"
            ),

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

    # Meaningful conditional:
    # Display a message based on the match result.

    if result == "Win":
        message = "🏆 Congratulations on your win!"

    else:
        message = "💪 Keep practicing and improving!"

    return Page(state, [

        Div(

            Div(
                "🏸 BADMINTON PERFORMANCE TRACKER",
                classes="topbar"
            ),

            Header("🎉 Match Saved Successfully!"),

            Div(

                Header("Match Recorded!", 2),

                "Your match against " + opponent
                + " has been successfully recorded.",

                Div(message),

                classes="success-card"
            ),

            Div(

                Header("Match Summary", 2),

                Div("Opponent: " + opponent),

                Div("📅 Date: " + date),

                Div("Result: " + result),

                Div(
                    "Points Won: "
                    + str(won)
                    + "/" + str(total)
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

            Button("🏠 Back to Home", index),

            classes="dashboard"
        )
    ])


# ==========================================
# ROUTE 4: MATCH HISTORY PAGE
# ==========================================

@route
def match_history(state: State) -> Page:

    content = [

        Div(
            "🏸 BADMINTON PERFORMANCE TRACKER",
            classes="topbar"
        ),

        Header("📋 Match History"),

        Div(
            "Review your previously recorded "
            "matches and celebrate your progress.",
            classes="goal-card"
        )
    ]

    # Check whether the player has recorded matches.

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
    # Iterate through the list of Match instances
    # in State and display each recorded match.
    #
    # Each match is grouped inside a Div so that
    # all its information appears in one card.

    for match in state.matches:

        # Choose the color of the result label.

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

        # Create a card for the current match.

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
                    + "/" + str(match.total_points)
                ),

                Div(
                    "Errors: " + str(match.errors)
                ),

                Div(
                    "💥 Successful Smashes: "
                    + str(match.successful_smashes)
                    + "/" + str(match.total_smashes)
                ),

                Div(
                    "🏸 Successful Serves: "
                    + str(match.successful_serves)
                    + "/" + str(match.total_serves)
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

    # Prevent calculations when there are no matches.

    if len(state.matches) == 0:

        return Page(state, [

            Header("📊 Performance Statistics"),

            Div(
                "Record a match to unlock your "
                "performance statistics!",
                classes="goal-card"
            ),

            Button("📝 Record Match", record_match),

            Button("🏠 Back to Home", index)
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
    # Calculate statistics from all recorded matches.

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

    smash_rate = 0.0

    if total_smashes > 0:

        smash_rate = (
            successful_smashes / total_smashes * 100
        )

    # Calculate serve success rate.

    serve_rate = 0.0

    if total_serves > 0:

        serve_rate = (
            successful_serves / total_serves * 100
        )

    # Calculate average errors per match.

    average_errors = errors / len(state.matches)

    # Calculate errors per 100 points.

    error_rate = errors / total_points * 100

    return Page(state, [

        Div(

            Div(
                "🏸 BADMINTON PERFORMANCE TRACKER",
                classes="topbar"
            ),

            Header("📊 Performance Statistics"),

            Div(
                "Understand your strengths and discover "
                "opportunities to improve your game.",
                classes="goal-card"
            ),

            # Match overview

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
                    + str(points_won)
                ),

                Div(
                    "Total Points Played: "
                    + str(total_points)
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
                    + str(total_smashes)
                ),

                Div(
                    "Successful Smashes: "
                    + str(successful_smashes)
                ),

                stat_card(
                    "💥",
                    str(round(smash_rate, 2)) + "%",
                    "Smash Success Rate"
                ),

                classes="section-card"
            ),

            # Serve statistics

            Div(

                Header("🏸 Serve Statistics", 2),

                Div(
                    "Total Serves: "
                    + str(total_serves)
                ),

                Div(
                    "Successful Serves: "
                    + str(successful_serves)
                ),

                stat_card(
                    "🏸",
                    str(round(serve_rate, 2)) + "%",
                    "Serve Success Rate"
                ),

                classes="section-card"
            ),

            # Error statistics

            Div(

                Header("⚠️ Error Statistics", 2),

                Div(
                    "Total Errors: " + str(errors)
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

    # Check whether the player has recorded matches.

    if len(state.matches) == 0:

        return Page(state, [

            Header("💡 Strategy Tips"),

            Div(
                "Record your first match to receive "
                "personalized training recommendations.",
                classes="goal-card"
            ),

            Button("📝 Record Match", record_match),

            Button("🏠 Back to Home", index)
        ])

    # Initialize totals.

    total_smashes = 0
    successful_smashes = 0
    total_serves = 0
    successful_serves = 0
    total_errors = 0

    # Calculate totals from all recorded matches.

    for match in state.matches:

        total_smashes += match.total_smashes

        successful_smashes += match.successful_smashes

        total_serves += match.total_serves

        successful_serves += match.successful_serves

        total_errors += match.errors

    # Calculate smash success rate.

    smash_rate = 0.0

    if total_smashes > 0:

        smash_rate = (
            successful_smashes / total_smashes * 100
        )

    # Calculate serve success rate.

    serve_rate = 0.0

    if total_serves > 0:

        serve_rate = (
            successful_serves / total_serves * 100
        )

    # Calculate average errors.

    average_errors = total_errors / len(state.matches)

    # ==========================================
    # SMASH RECOMMENDATION
    # ==========================================

    # Meaningful conditional:
    # Recommend smash practice when the player's
    # smash success rate is below 60%.

    if total_smashes == 0:

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

    # ==========================================
    # SERVE RECOMMENDATION
    # ==========================================

    # Meaningful conditional:
    # Recommend serve practice when the player's
    # serve success rate is below 80%.

    if total_serves == 0:

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

    # ==========================================
    # ERROR RECOMMENDATION
    # ==========================================

    # Meaningful conditional:
    # Recommend reducing errors if the player's
    # average errors per match is greater than 10.

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

    # Display all recommendations on the page.

    return Page(state, [

        Div(

            Div(
                "🏸 BADMINTON PERFORMANCE TRACKER",
                classes="topbar"
            ),

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

    return Page(state, [

        Div(

            Div(
                "🏸 BADMINTON PERFORMANCE TRACKER",
                classes="topbar"
            ),

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

    # Check whether the player entered a name.

    if player_name.strip() == "":

        return Page(state, [

            Header("⚠️ Invalid Input"),

            Div(
                "Please enter your name.",
                classes="error-card"
            ),

            Button("Back to Profile", profile)
        ])

    # Meaningfully modify three State attributes.

    state.player_name = player_name

    state.goal = goal

    state.favorite_shot = favorite_shot

    return Page(state, [

        Div(

            Div(
                "🏸 BADMINTON PERFORMANCE TRACKER",
                classes="topbar"
            ),

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
# START SERVER
# ==========================================

# Create the initial State of the website.
#
# The matches list starts empty.
# The default player name is Player.
# The default goal is to improve badminton skills.
# The default favorite shot is Smash.

start_server(State(
    [],
    "Player",
    "Improve my badminton skills",
    "Smash"
))
