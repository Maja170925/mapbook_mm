def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}! z miejscowości {user['location']} opublikował {user['posts']} postów")


def add_users(users_data: list) -> None:
    users_name = input("podaj imię nowego użytkownika: ")
    users_location = input("podaj lokalizacje nowego znajomego: ")
    users_posts = int(input("podaj liczbę postów: "))
    users_data.append({"name": users_name, "location": users_location, "posts": users_posts})
 
def remove_users(users_data: list, user_name=None) -> None:
    add_users.name=input("podaj imię użytkownika do usunięcia;")
    for user in users_data:
        if user["name"] == user_name:
                users_data.remove(user)


