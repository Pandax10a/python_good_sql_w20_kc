
import dbhelpers

def get_all_books():
    cursor = dbhelpers.just_connect()

    result = dbhelpers.cursor_result(cursor, 'CALL book_list')

    dbhelpers.the_closer(cursor)

    author_list = []
    for x in result:
        author_list.append(x[1])
        print(x[0], " ", x[1].decode("UTF-8"), " ", x[2].decode("UTF-8"), " ", x[3], " ", x[4])



    





def choose_author():
    get_all_books()
    while True:
        temp_answer = input("which author did u want to choose from the above?: ")
        if(temp_answer == 'Gabor Maté'):
            return temp_answer
        elif(temp_answer == "Kelly Ripa"):
            return temp_answer
        elif(temp_answer == "Colleen Hoover"):
            return temp_answer
        elif(temp_answer == "Roz Weston"):
            return temp_answer
        elif(temp_answer == "Jennette McCurdy"):
            return temp_answer
        elif(temp_answer == "Stephen King"):
            return temp_answer
        else:
            print('not on the list')

choose_author_input = choose_author()

print(choose_author_input)

def choose_author_search(author_name):
    
    cursor = dbhelpers.just_connect()

    result = dbhelpers.cursor_result(cursor, 'CALL search_by_author(?)', [author_name])
    print(result)

    dbhelpers.the_closer(cursor)


choose_author_search(choose_author_input)

