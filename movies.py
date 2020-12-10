import json
from Deque import Deque
from HashSet import HashSet


#welcome message
def welcomeing():
    print("           Welcome to our MovieHub")
    print("       Please write the movie you want")

#providing message of choices
def askingToChoose(desireMovie):
    print("   We have found something for you")
    print("  What do you want to know about " + desireMovie + "?")
    print("1. Director")
    print("2. Year of premiere")
    print("3. Short discription of movie")
    print("4. Genres")
    print("0. To skip")

# Determining the choice of the user
def determinTheChoice(desireMovie,movieList):
    choice = input()
    while choice != "0":

        if (choice == "1"):
            print(movieList[desireMovie]["director"])
        if (choice == "2"):
            print(movieList[desireMovie]["year"])
        if (choice == "3"):
            print(movieList[desireMovie]["description"])
        if (choice == "4"):
            print(movieList[desireMovie]["genre"])

        choice = input()

# Determining whether to add movie in favourite list or not
def addingToFavTen(desireMovie,favouriteTen):
    print('   Do you wanna add this movie to your top 10 movies list?')

    answer = input()

    if (answer == 'Yes'):
        favouriteTen.addLast(desireMovie)

# Printing user's favourite movies
def printingFavMovies(favouriteTen):
    print('   Here are your favourite movies!!!')
    favouriteTen.printDeq()


def menu(movieSet,movieList,favouriteTen):
    welcomeing()
    desireMovie=input()
    while desireMovie!='thank you':
        if movieSet.contains(desireMovie):

            askingToChoose(desireMovie)

            determinTheChoice(desireMovie,movieList)

            addingToFavTen(desireMovie,favouriteTen)

        else:
            print ("Sorry, we could not find it")

        desireMovie=input()

    printingFavMovies()

def main():
    # Creating HashSet
    movieSet=HashSet(100)

    # Creating the list that will have all movies
    with open('movieList.json')as data_file:
        movieList = json.load(data_file)

    # Adding movies to HashSet
    for movie in movieList:
        movieSet.add(movie)

    favouriteTen=Deque(10)
    menu(movieSet,movieList,favouriteTen)

main()




