def expected_party_rank(voteA, voteB, swingA, swingB):
    voteA += swingA
    voteB += swingB
    voteC = 100 - (voteA + voteB)
    if voteA + voteB + voteC == 100:
        parties = {
            'A' : voteA,
            'B' : voteB,
            'C' : voteC
        }
        print(parties)
        guesses = []
        for value, key in sorted(parties.items(), key=lambda x:x[1], reverse=True):
            guesses.append(value)
        return guesses