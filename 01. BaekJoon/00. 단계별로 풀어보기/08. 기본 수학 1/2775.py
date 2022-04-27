n = int(input())

for _ in range(n):
    floor = int(input())
    room = int(input())

    people = [v for v in range(1, room + 1)]

    for i in range(floor):
        # print("floor %d" % (i + 1))

        for j in range(1, room):
            people[j] += people[j - 1]

        # print(people)
    print(people[-1])