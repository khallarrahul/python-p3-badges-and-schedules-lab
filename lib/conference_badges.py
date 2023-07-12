def badge_maker(name):
    sentence = f"Hello, my name is {name}."
    return sentence


badge_maker("Rahul")


def assign_rooms(names):
    index = 1
    newlist = []
    for name in names:
        newlist.append(f"Hello, {name}! You'll be assigned to room {index}!")
        index += 1
    return newlist


assign_rooms(["Arel", "Carol"])


def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = f"Hello, my name is {name}."
        badges.append(badge)
    return badges


batch_badge_creator(["Arel", "Carol"])


def printer(names):
    for item in batch_badge_creator(names):
        print(item)
    for item in assign_rooms(names):
        print(item)


printer(["Arel", "Carol"])
