# medals.py

def award_medal(points):
    if points >= 9.0:
        print("You got a Gold medal!!!")
        return "Gold"
    if points >= 7.0:
        print("You got a Silver medal!")
        return "Silver"
    print("You got a Bronze medal.")
    return "Bronze"


def verb(count):
    if count == 1:
        return "is"
    return 'are'

def pluralize(count):
    if count == 1:
        return None
    return 's'


# Award medals
medals = []
scores = [ 9.8, 6.9, 8.0, 10.0, 7.6, 8.5, 9.9 ]
for score in scores:
    medals.append(award_medal(score))

medals_lst = []
class medal:
    def __init__(self, name):
        self.name = name
        self.count = medals.count(name)
        medals_lst.append(self)

medal("Gold")
medal("Silver")
medal("Bronze")

for medal in medals_lst:
    print(f"There {verb(medal.count)} {medal.count} {medal.name} medal{pluralize(medal.count)} in total.")
