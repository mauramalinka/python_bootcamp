# import sys
#
# try:
#     print(sys.argv)
# except IndexError:
#     print("Zapomniałeś podać nazwę pliku")
#
#
# file_name = sys.argv[1]
# print("ścieżka do plikuy to: ", file_name)

file_name = "dane/logs.txt"


def rozwiazanie_1():
    user_last_login = {}
    user_total_time = {}
    with open(file_name) as f:
        # i = 0
        for line in f:
            user, action, time_str = line.split(";")
            time = int(time_str)
            if action == 'LOGIN':
                user_last_login[user] = time
            elif action == "LOGOUT":
                #           logout - login
                time_temp = time - user_last_login[user]
                user_total_time[user] = user_total_time.get(user, 0) + time_temp

    return user_total_time


def rozwiazanie_2():
    user_total_time_login = {}
    user_total_time_logout = {}

    with open(file_name) as f:
        # i = 0
        for line in f:
            user, action, time_str = line.split(";")
            time = int(time_str)
            if action == 'LOGIN':
                user_total_time_login[user] = user_total_time_login.get(user, 0) + time
            elif action == "LOGOUT":
                user_total_time_logout[user] = user_total_time_logout.get(user, 0) + time

    final_result = {}
    for user in user_total_time_login:
        final_result[user] = user_total_time_logout[user] - user_total_time_login[user]

    return final_result


def rozwiazanie_3():
    out = {}
    with open(file_name) as f:
        for line in f:
            user, action, time_str = line.split(";")
            time = int(time_str)
            if action == "LOGIN":
                out[user] = out.get(user, 0) - time
            if action == "LOGOUT":
                out[user] = out.get(user, 0) + time
    return out


def nazwa(x):
    return x[1]


print("Czas przebywania w systemie: ")
for user, time in sorted(rozwiazanie_2().items(), key=nazwa, reverse=True):
    print(f' - {user}: {time} s')

print(rozwiazanie_1() == rozwiazanie_2())
print(rozwiazanie_1() == rozwiazanie_3())