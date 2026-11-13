import sys
import os
import re
import json
import urllib.request

def check_winner(b):
    for r in range(3):
        if b[r][0] != " " and b[r][0] == b[r][1] == b[r][2]:
            return b[r][0]
    for c in range(3):
        if b[0][c] != " " and b[0][c] == b[1][c] == b[2][c]:
            return b[0][c]
    if b[0][0] != " " and b[0][0] == b[1][1] == b[2][2]:
        return b[0][0]
    if b[0][2] != " " and b[0][2] == b[1][1] == b[2][0]:
        return b[0][2]
    if all(b[r][c] != " " for r in range(3) for c in range(3)):
        return "DRAW"
    return None

def bot_move(b):
    # Try winning move
    for r in range(3):
        for c in range(3):
            if b[r][c] == " ":
                b[r][c] = "O"
                if check_winner(b) == "O":
                    return
                b[r][c] = " "
    # Block visitor
    for r in range(3):
        for c in range(3):
            if b[r][c] == " ":
                b[r][c] = "X"
                if check_winner(b) == "X":
                    b[r][c] = "O"
                    return
                b[r][c] = " "
    # Take center
    if b[1][1] == " ":
        b[1][1] = "O"
        return
    # Take corners
    for (r, c) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if b[r][c] == " ":
            b[r][c] = "O"
            return
    # Take sides
    for (r, c) in [(0, 1), (1, 0), (1, 2), (2, 1)]:
        if b[r][c] == " ":
            b[r][c] = "O"
            return

def render_board(b, status):
    repo = "JustPirate/JustPirate"
    lines = []
    lines.append(f"**Status:** {status}\n")
    lines.append("| Col 1 | Col 2 | Col 3 |")
    lines.append("| :---: | :---: | :---: |")
    for r in range(3):
        cells = []
        for c in range(3):
            val = b[r][c]
            if val == "X":
                cells.append("❌")
            elif val == "O":
                cells.append("⭕")
            else:
                url = f"https://github.com/{repo}/issues/new?title=ttt%7Cplay%7C{r}%7C{c}&body=Click+%27Submit+new+issue%27+to+play+this+square!"
                cells.append(f"[ ⚔️ ]({url})")
        joined = " | ".join(cells)
        lines.append(f"| {joined} |")
    reset_url = f"https://github.com/{repo}/issues/new?title=ttt%7Creset&body=Click+%27Submit+new+issue%27+to+start+a+new+game!"
    lines.append("")
    lines.append(f"[🔄 **Start New Game**]({reset_url})")
    return "\n".join(lines)

def main():
    title = os.environ.get("ISSUE_TITLE", "").strip()
    sender = os.environ.get("ISSUE_USER", "A brave visitor")
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    start_tag = "<!-- TTT_START -->"
    end_tag = "<!-- TTT_END -->"
    state_tag = "<!-- TTT_STATE:"
    
    if start_tag not in content or end_tag not in content:
        print("TTT tags not found")
        return
    
    # Extract board state
    m = re.search(r"<!-- TTT_STATE:([0-9a-zA-Z_ ]{9}) -->", content)
    raw = m.group(1) if m else "_________"
    b = [[raw[r*3 + c] if raw[r*3 + c] in ["X", "O"] else " " for c in range(3)] for r in range(3)]
    
    if title == "ttt|reset":
        b = [[" "]*3 for _ in range(3)]
        status = f"Game reset by @{sender}! Your turn (❌): click any square below."
    elif title.startswith("ttt|play|"):
        parts = title.split("|")
        if len(parts) == 4:
            r, c = int(parts[2]), int(parts[3])
            if b[r][c] == " ":
                b[r][c] = "X"
                w = check_winner(b)
                if w == "X":
                    status = f"🎉 Victory! @{sender} (❌) defeated the Pirate bot!"
                elif w == "DRAW":
                    status = f"🤝 It is a draw between @{sender} and the Pirate bot!"
                else:
                    bot_move(b)
                    w2 = check_winner(b)
                    if w2 == "O":
                        status = f"💀 The Pirate bot (⭕) won against @{sender}! Start a new game below!"
                    elif w2 == "DRAW":
                        status = f"🤝 It is a draw between @{sender} and the Pirate bot!"
                    else:
                        status = f"@{sender} played ({r+1}, {c+1}). Pirate bot responded! Your turn (❌):"
            else:
                status = f"Square ({r+1}, {c+1}) is already taken! Pick an empty square."
    else:
        return
    
    new_state = "".join(b[r][c] if b[r][c] in ["X", "O"] else "_" for r in range(3) for c in range(3))
    new_board_md = f"<!-- TTT_STATE:{new_state} -->\n" + render_board(b, status)
    
    pattern = re.compile(rf"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
    new_content = pattern.sub(f"{start_tag}\n{new_board_md}\n{end_tag}", content)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README updated with new TTT state!")

if __name__ == "__main__":
    main()
