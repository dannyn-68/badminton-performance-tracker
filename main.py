
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
# WEBSITE DECORATION
# ==========================================

set_website_style("default")

add_website_css("""

    body {
        background-color: #f0fdf4;
        font-family: Arial, sans-serif;
    }

    #drafter-body-- {
        background-color: #f0fdf4;
        color: #14532d;
        padding: 24px;
    }

    h1 {
        color: #14532d;
        font-size: 34px;
        text-align: center;
        margin-bottom: 20px;
    }

    h2 {
        color: #166534;
        font-size: 24px;
    }

    button {
        background-color: #15803d;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 22px;
        margin: 6px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: 0.2s;
    }

    button:hover {
        background-color: #166534;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    input, select {
        background-color: white;
        border: 1px solid #86efac;
        border-radius: 8px;
        padding: 10px;
        margin: 5px 0 12px 0;
        font-size: 16px;
        color: #14532d;
    }

    input:focus, select:focus {
        border-color: #16a34a;
        outline: none;
        box-shadow: 0 0 5px #86efac;
    }

    hr {
        border: none;
        height: 2px;
        background-color: #bbf7d0;
        margin: 24px 0;
    }

    .hero {
        background: linear-gradient(
            135deg, #14532d, #16a34a
        );
        color: white;
        padding: 35px 20px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.12);
    }

    .tagline {
        text-align: center;
        color: #16a34a;
        font-size: 15px;
        font-weight: bold;
        letter-spacing: 3px;
        margin-bottom: 20px;
    }

    .intro {
        text-align: center;
        color: #166534;
        font-size: 17px;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    .stat-card {
        background-color: white;
        border: 1px solid #bbf7d0;
        border-left: 6px solid #22c55e;
        border-radius: 12px;
        padding: 18px;
        margin: 10px 0;
        font-size: 20px;
        font-weight: bold;
        color: #14532d;
        box-shadow: 0 3px 8px rgba(0,0,0,0.06);
    }

    .goal-card {
        background-color: #dcfce7;
        border-radius: 12px;
        padding: 18px;
        margin: 12px 0;
        color: #166534;
        line-height: 1.6;
    }

    .success-card {
        background-color: #dcfce7;
        border: 1px solid #86efac;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        color: #166534;
        font-weight: bold;
        text-align: center;
    }

    .error-card {
        background-color: #fef2f2;
        border: 1px solid #fca5a5;
        border-radius: 12px;
        padding: 18px;
        margin: 15px 0;
        color: #991b1b;
    }

    .match-card {
        background-color: white;
        border: 1px solid #bbf7d0;
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
        color: #14532d;
        box-shadow: 0 3px 8px rgba(0,0,0,0.06);
    }

    .win-label {
        background-color: #dcfce7;
        color: #166534;
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
    }

    .loss-label {
        background-color: #fee2e2;
        color: #991b1b;
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 13px;
        padding: 20px;
        margin-top: 25px;
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

        Text(
            "TRACK. ANALYZE. IMPROVE.",
            classes="tagline"
        ),

        # Welcome banner

        Text(
            "Welcome, " + state.player_name + "!",
            classes="hero",
            style_font_size="30px",
            style_font_weight="bold"
        ),

        Text(
            "Every match is a chance to improve. "
            "Track your performance and take your "
            "badminton skills to the next level.",
            classes="intro"
        ),

        HorizontalRule(),

        # Performance overview

        Header("📊 Performance Overview"),

        Text(
            "🏸 Matches Played: "
            + str(len(state.matches)),
            classes="stat-card"
        ),

        Text(
            "🏆 Total Wins: " + str(wins),
            classes="stat-card"
        ),

        Text(
            "🎯 Total Losses: " + str(losses),
            classes="stat-card"
        ),

        Text(
            "📈 Win Rate: "
            + str(round(win_rate, 2)) + "%",
            classes="stat-card"
        ),

        HorizontalRule(),

        # Navigation

        Header("⚡ Quick Navigation"),

        Button("📝 Record Match", record_match),

        Button("📋 Match History", match_history),

        Button("📊 Performance Statistics", statistics),

        Button("💡 Strategy Tips", strategy_tips),

        Button("👤 My Profile", profile),

        HorizontalRule(),

        # Player information

        Header("🎯 Your Training Journey"),

        Text(
            "Training Goal: " + state.goal,
            classes="goal-card"
        ),

        Text(
            "Favorite Shot: " + state.favorite_shot,
            classes="goal-card"
        ),

        # Footer

        Text(
            "🏸 Badminton Performance Tracker | "
            "Created by Danny Nguyen | "
            "Built with Python & Drafter",
            classes="footer"
        )
    ])


# ==========================================
# ROUTE 2: RECORD MATCH PAGE
# ==========================================

@route
def record_match(state: State) -> Page:

    return Page(state, [

        Header("📝 Record a Match"),

        Text(
            "Enter your latest match results and track "
            "your progress on the court.",
            classes="goal-card"
        ),

        Header("🏸 Match Information"),

        "Opponent:",
        TextBox("opponent", ""),

        "Match Date (MM/DD/YYYY):",
        TextBox("date", ""),

        "Match Result:",
        SelectBox("result", ["Win", "Loss"], "Win"),

        HorizontalRule(),

        Header("🎯 Point Statistics"),

        "Points Won:",
        TextBox("points_won", "0"),

        "Total Points:",
        TextBox("total_points", "0"),

        "Errors:",
        TextBox("errors", "0"),

        HorizontalRule(),

        Header("💥 Smash Statistics"),

        "Total Smashes:",
        TextBox("total_smashes", "0"),

        "Successful Smashes:",
        TextBox("successful_smashes", "0"),

        HorizontalRule(),

        Header("🏸 Serve Statistics"),

        "Total Serves:",
        TextBox("total_serves", "0"),

        "Successful Serves:",
        TextBox("successful_serves", "0"),

        HorizontalRule(),

        Button("💾 Save Match", save_match),

        Button("🏠 Back to Home", index),

        Text(
            "Record your statistics after every match "
            "to see how much you improve over time.",
            classes="footer"
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
    # Convert TextBox strings into integers.
    # Catch invalid inputs instead of crashing.

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

            Text(
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

            Text(
                "Please enter your opponent's name.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check the match date.

    if date.strip() == "":
        return Page(state, [

            Header("⚠️ Invalid Input"),

            Text(
                "Please enter the match date.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check the match result.

    if result != "Win" and result != "Loss":
        return Page(state, [

            Header("⚠️ Invalid Input"),

            Text(
                "Please select Win or Loss.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check point statistics.

    if total <= 0 or won < 0 or won > total:
        return Page(state, [

            Header("⚠️ Invalid Input"),

            Text(
                "Points won must be between 0 "
                "and total points. Total points "
                "must be greater than zero.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check the number of errors.

    if error_count < 0:
        return Page(state, [

            Header("⚠️ Invalid Input"),

            Text(
                "The number of errors cannot be negative.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check smash statistics.

    if smashes < 0 or good_smashes < 0 or good_smashes > smashes:
        return Page(state, [

            Header("⚠️ Invalid Input"),

            Text(
                "Successful smashes must be between "
                "0 and total smashes.",
                classes="error-card"
            ),

            Button("Try Again", record_match)
        ])

    # Check serve statistics.

    if serves < 0 or good_serves < 0 or good_serves > serves:
        return Page(state, [

            Header("⚠️ Invalid Input"),

            Text(
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
    # Display a message based on the result.

    if result == "Win":
        message = "🏆 Congratulations on your win!"
    else:
        message = "💪 Keep practicing and improving!"

    return Page(state, [

        Header("🎉 Match Saved Successfully!"),

        Text(
            "Your match against " + opponent
            + " has been successfully recorded.",
            classes="success-card"
        ),

        HorizontalRule(),

        Text(
            "📅 Match Date: " + date,
            classes="match-card"
        ),

        Text(
            "🏸 Match Result: " + result,
            classes="match-card"
        ),

        Text(
            message,
            classes="goal-card"
        ),

        Text(
            "Total Matches Recorded: "
            + str(len(state.matches)),
            classes="stat-card"
        ),

        HorizontalRule(),

        Button("📝 Record Another Match", record_match),

        Button("📋 View Match History", match_history),

        Button("📊 View Statistics", statistics),

        Button("🏠 Back to Home", index)
    ])


# ==========================================
# ROUTE 4: MATCH HISTORY PAGE
# ==========================================

@route
def match_history(state: State) -> Page:

    content = [

        Header("📋 Match History"),

        Text(
            "Review your previously recorded matches "
            "and celebrate your progress.",
            classes="goal-card"
        )
    ]

    # Check whether there are any matches.

    if len(state.matches) == 0:

        content.append(
            Text(
                "You have not recorded any matches yet. "
                "Record your first match to get started!",
                classes="match-card"
            )
        )

    match_number = 1

    # Meaningful loop:
    # Iterate over Match instances in State.
    # Display the statistics of every match.

    for match in state.matches:

        content.append(HorizontalRule())

        content.append(
            Header("🏸 Match " + str(match_number))
        )

        content.append(
            Text(
                "Opponent: " + match.opponent,
                classes="match-card"
            )
        )

        content.append(
            Text(
                "📅 Date: " + match.date,
                classes="match-card"
            )
        )

        # Display wins in green and losses in red.

        if match.result == "Win":
            content.append(
                Text(
                    "🏆 Result: WIN",
                    classes="win-label"
                )
            )

        else:
            content.append(
                Text(
                    "Result: LOSS",
                    classes="loss-label"
                )
            )

        content.append(
            Text(
                "🎯 Points Won: "
                + str(match.points_won)
                + "/" + str(match.total_points),
                classes="match-card"
            )
        )

        content.append(
            Text(
                "Errors: " + str(match.errors),
                classes="match-card"
            )
        )

        content.append(
            Text(
                "💥 Successful Smashes: "
                + str(match.successful_smashes)
                + "/" + str(match.total_smashes),
                classes="match-card"
            )
        )

        content.append(
            Text(
                "🏸 Successful Serves: "
                + str(match.successful_serves)
                + "/" + str(match.total_serves),
                classes="match-card"
            )
        )

        match_number += 1

    content.append(HorizontalRule())

    content.append(
        Button("📝 Record Match", record_match)
    )

    content.append(
        Button("📊 Performance Statistics", statistics)
    )

    content.append(
        Button("🏠 Back to Home", index)
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

            Text(
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
        smash_rate = successful_smashes / total_smashes * 100

    # Calculate serve success rate.

    serve_rate = 0.0

    if total_serves > 0:
        serve_rate = successful_serves / total_serves * 100

    # Calculate average errors per match.

    average_errors = errors / len(state.matches)

    # Calculate errors per 100 points.

    error_rate = errors / total_points * 100

    return Page(state, [

        Header("📊 Performance Statistics"),

        Text(
            "Understand your strengths and discover "
            "opportunities to improve your game.",
            classes="goal-card"
        ),

        Header("🏆 Match Overview"),

        Text(
            "Total Matches: "
            + str(len(state.matches)),
            classes="stat-card"
        ),

        Text(
            "Wins: " + str(wins),
            classes="stat-card"
        ),

        Text(
            "Losses: " + str(losses),
            classes="stat-card"
        ),

        Text(
            "Win Rate: "
            + str(round(win_rate, 2)) + "%",
            classes="stat-card"
        ),

        HorizontalRule(),

        Header("🎯 Point Statistics"),

        Text(
            "Total Points Won: " + str(points_won),
            classes="match-card"
        ),

        Text(
            "Total Points Played: " + str(total_points),
            classes="match-card"
        ),

        Text(
            "Point Win Rate: "
            + str(round(point_rate, 2)) + "%",
            classes="stat-card"
        ),

        HorizontalRule(),

        Header("💥 Smash Statistics"),

        Text(
            "Total Smashes: " + str(total_smashes),
            classes="match-card"
        ),

        Text(
            "Successful Smashes: "
            + str(successful_smashes),
            classes="match-card"
        ),

        Text(
            "Smash Success Rate: "
            + str(round(smash_rate, 2)) + "%",
            classes="stat-card"
        ),

        HorizontalRule(),

        Header("🏸 Serve Statistics"),

        Text(
            "Total Serves: " + str(total_serves),
            classes="match-card"
        ),

        Text(
            "Successful Serves: "
            + str(successful_serves),
            classes="match-card"
        ),

        Text(
            "Serve Success Rate: "
            + str(round(serve_rate, 2)) + "%",
            classes="stat-card"
        ),

        HorizontalRule(),

        Header("⚠️ Error Statistics"),

        Text(
            "Total Errors: " + str(errors),
            classes="match-card"
        ),

        Text(
            "Average Errors per Match: "
            + str(round(average_errors, 2)),
            classes="stat-card"
        ),

        Text(
            "Errors per 100 Points: "
            + str(round(error_rate, 2)),
            classes="stat-card"
        ),

        HorizontalRule(),

        Button("💡 View Strategy Tips", strategy_tips),

        Button("📋 Match History", match_history),

        Button("📝 Record Match", record_match),

        Button("🏠 Back to Home", index)
    ])


# ==========================================
# ROUTE 6: STRATEGY TIPS PAGE
# ==========================================

@route
def strategy_tips(state: State) -> Page:

    # Check whether there are recorded matches.

    if len(state.matches) == 0:

        return Page(state, [

            Header("💡 Strategy Tips"),

            Text(
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

    # Calculate totals from all matches.

    for match in state.matches:

        total_smashes += match.total_smashes

        successful_smashes += match.successful_smashes

        total_serves += match.total_serves

        successful_serves += match.successful_serves

        total_errors += match.errors

    # Calculate smash success rate.

    smash_rate = 0.0

    if total_smashes > 0:
        smash_rate = successful_smashes / total_smashes * 100

    # Calculate serve success rate.

    serve_rate = 0.0

    if total_serves > 0:
        serve_rate = successful_serves / total_serves * 100

    # Calculate average errors.

    average_errors = total_errors / len(state.matches)

    content = [

        Header("💡 Personalized Strategy Tips"),

        Text(
            "These recommendations are based on "
            "your recorded match statistics.",
            classes="goal-card"
        ),

        Header("💥 Improve Your Smash")
    ]

    # Meaningful conditional:
    # Recommend smash practice if accuracy is below 60%.

    if total_smashes == 0:

        content.append(
            Text(
                "Record some smashes to receive "
                "smash-specific recommendations.",
                classes="goal-card"
            )
        )

    elif smash_rate < 60:

        content.append(
            Text(
                "Your smash success rate is "
                + str(round(smash_rate, 2))
                + "%. Focus on timing, placement, "
                "and accuracy before increasing power.",
                classes="goal-card"
            )
        )

    else:

        content.append(
            Text(
                "Great job! Your smash success rate is "
                + str(round(smash_rate, 2))
                + "%. Keep improving your placement "
                "and shot selection.",
                classes="success-card"
            )
        )

    content.append(HorizontalRule())

    content.append(
        Header("🏸 Improve Your Serve")
    )

    # Meaningful conditional:
    # Recommend serve practice if success is below 80%.

    if total_serves == 0:

        content.append(
            Text(
                "Record some serves to receive "
                "serve-specific recommendations.",
                classes="goal-card"
            )
        )

    elif serve_rate < 80:

        content.append(
            Text(
                "Your serve success rate is "
                + str(round(serve_rate, 2))
                + "%. Practice consistent low serves "
                "and focus on accuracy.",
                classes="goal-card"
            )
        )

    else:

        content.append(
            Text(
                "Excellent serving! Your success rate is "
                + str(round(serve_rate, 2))
                + "%. Keep practicing different "
                "serve placements.",
                classes="success-card"
            )
        )

    content.append(HorizontalRule())

    content.append(
        Header("🎯 Reduce Your Errors")
    )

    # Meaningful conditional:
    # Recommend reducing errors if average exceeds 10.

    if average_errors > 10:

        content.append(
            Text(
                "You average "
                + str(round(average_errors, 2))
                + " errors per match. Focus on "
                "consistent footwork, safer shots, "
                "and reducing unforced errors.",
                classes="goal-card"
            )
        )

    else:

        content.append(
            Text(
                "Good consistency! You average "
                + str(round(average_errors, 2))
                + " errors per match. Keep focusing "
                "on controlled and accurate shots.",
                classes="success-card"
            )
        )

    content.append(HorizontalRule())

    content.append(
        Header("🔥 Your Training Goal")
    )

    content.append(
        Text(
            state.goal,
            classes="stat-card"
        )
    )

    content.append(
        Button("📊 View Statistics", statistics)
    )

    content.append(
        Button("👤 Update Training Goal", profile)
    )

    content.append(
        Button("🏠 Back to Home", index)
    )

    return Page(state, content)


# ==========================================
# ROUTE 7: PROFILE PAGE
# ==========================================

@route
def profile(state: State) -> Page:

    return Page(state, [

        Header("👤 My Player Profile"),

        Text(
            "Customize your player information "
            "and set your personal badminton goals.",
            classes="goal-card"
        ),

        HorizontalRule(),

        Header("🏸 Player Information"),

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

        Button("💾 Save Profile", save_profile),

        Button("🏠 Back to Home", index)
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

            Text(
                "Please enter your name.",
                classes="error-card"
            ),

            Button("Back to Profile", profile)
        ])

    # Meaningfully modify three State fields.

    state.player_name = player_name

    state.goal = goal

    state.favorite_shot = favorite_shot

    return Page(state, [

        Header("🎉 Profile Updated!"),

        Text(
            "Your profile has been successfully saved.",
            classes="success-card"
        ),

        HorizontalRule(),

        Text(
            "👤 Player Name: " + state.player_name,
            classes="stat-card"
        ),

        Text(
            "🎯 Training Goal: " + state.goal,
            classes="goal-card"
        ),

        Text(
            "🏸 Favorite Shot: " + state.favorite_shot,
            classes="goal-card"
        ),

        HorizontalRule(),

        Button("🏠 Back to Home", index),

        Button("✏️ Edit Profile", profile)
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
