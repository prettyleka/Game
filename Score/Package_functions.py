def add_score(difficalty):
    f = open("Scores.txt", "r+")
    lastScore = f.read()
    if lastScore=="":
        POINTS_OF_WINNING = (int(difficalty) * 3) + 5
        f.write(str(POINTS_OF_WINNING))
        f.close()
        return POINTS_OF_WINNING
    else:
        POINTS_OF_WINNING = (int(difficalty) * 3) + 5
        newScore = int(lastScore)+POINTS_OF_WINNING
        f.seek(0)
        f.write(str(newScore))
        f.close()
        return newScore
