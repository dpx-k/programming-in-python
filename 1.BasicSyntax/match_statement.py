# the match statement is used similar to a switch statement in other programming languages 
# it was introduced in python 3.10 

# the following code demonstrates handling http error requests using the match statement 

http_status = 501

match http_status:
    case 200: 
        print('Sucess')
    case 400: 
        print('Bad Request')
    case 404: 
        print('Not Found')
    case 500 | 501:
        print('Server Error')
    case _:
        print("Unknown error")