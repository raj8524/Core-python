#pip install snakeviz,cProfilev
import cProfile
import time
start=time.time()
"""
def read_movies(src):
    with open(src)as fd:
        return fd.read().split()
def is_duplicate(needle,haystack):
    for movie in haystack:
        if needle.lower()==movie.lower():
            return movie
    return False
@cProfile
def duplicate_movies(src):
    movies1=read_movies(src)
    # print(len(movies))
    duplicate=[]
    while movies1:
        movie=movies1.pop()
        if is_duplicate(movie,movies1):
            duplicate.append(movie)
    # print(len(duplicate))
    return duplicate
end=time.time()
if __name__=="__main__":
    cProfile.run('duplicate_movies(src="movies.txt")')
    print(duplicate_movies())
# print(f"time taken to execute : {end-start}")

#--------------Cprofile---------------
import cProfile, pstats, io
def profile(fnc):
    #A decorator that uses cProfile to profile a function

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner

def read_movies(src):
    with open(src)as fd:
        return fd.read().split()
@profile
def duplicate_movies(src="movies.txt"):
    movies1=read_movies(src)
    movies1=[movie.lower() for movie in movies1]
    duplicate=[]
    while movies1:
        movie=movies1.pop()
        if movie in movies1:
            duplicate.append(movie)
    # print(len(duplicate))
    return duplicate
end=time.time()
print(duplicate_movies())
print(f"time taken to execute : {end-start}")


#---------------Cprofile-----
import cProfile, pstats, io
def profile(fnc):
    #A decorator that uses cProfile to profile a function

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner
def read_movies(src):
    with open(src) as fd:
        return fd.read().splitlines()

@profile
def find_duplicate_movies(src='movies.txt'):
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    movies.sort()
    duplicates = [movie1 for movie1, movie2 in zip(movies[:-1], movies[1:]) if movie1 == movie2]
    print(duplicates)

find_duplicate_movies()

"""

#-------------CROFILE---------###############################
"""
pr=cProfile.Profile()
pr.enable()
fucntion to be profiles()  duplicate_movies
pr.disable()
pr.print_stats()

pr.dump_stats('prof_data')
ps=pstats.Stats('prof_data')
ps.sort_stats(pstats.SortKey.CUMULATIVE)
ps.print_stats()
"""