__author__ = 'user'

from kwutils import *

def main():


    table = HighScoreTable("Zelda", 4)
    table.add("KAW", 1000)
    table.add("JHW", 5655)
    table.add("REW", 115655)
    print(str(table.is_high_score(1000)))
    table.add("KAWz", 1000)
    table.add("KAWzz", 1000)
    table.add("zzz", 2)

    table.print()


    print(str(table.is_high_score(2)))
    print(str(table.is_high_score(20000)))
    print(str(table.is_high_score(1000)))
    print(str(table.is_high_score(1001)))

    table.save()


    table2 = HighScoreTable("Zelda", 4)
    table2.load()
    table2.add("FFFW", 1015655)
    table2.print()

    table.print()


if __name__ == "__main__":
    main()
