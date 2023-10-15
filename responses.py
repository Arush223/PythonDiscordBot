
def handle_response(message) -> str:
    p_message = message.lower()
    match p_message:
        case "test":
            return "Match case confirmed."

        case "challenge":
            return "Challenge sent. Awaiting response..."

        case "accept":
            return "Challenge accepted. The game is on!"

        case "reject":
            return "Challenge rejected."

        case "move":
            return "Your move has been registered."

        case "quit":
            return "You have quit the game."

        case "stats":
            return "Player statistics: Wins - 10, Losses - 5, Rank - Silver."

        case "help":
            return "Available commands: challenge, accept, reject, move, quit, stats, help."

        case "":
            return "Sorry, I didn't understand that command."




