import json


with open("bank.json", "r") as read_file:
    info = json.load(read_file)


def balance(primary_user):
    if primary_user in info:
        print(f'You have ${info[primary_user]}')
    else:
        if primary_user not in info:
            info[primary_user] = 0
            with open('bank.json', 'w+') as f:
                json.dump(info, f, indent=4)


def add(primary_user, amount):
    if primary_user not in info:
        info[primary_user] = int(amount)
    else:
        info[primary_user] += amount
    with open('bank.json', 'w+') as f:
        json.dump(info, indent=4)


def give(primary_id, other_id, amount):
    if primary_id not in info:
        if other_id not in info:
            info[other_id] = 0
            with open('bank.json', 'w+') as f:
                json.dump(info, f, indent=4)
    elif other_id not in info:
        print('The other user does not have an account. Making one now...')
        info[other_id] = 0
        with open('bank.json', 'w+') as f:
            json.dump(info, f, indent=4)

        if info[primary_id] < amount:
            print(f"You don't have ${amount}.")
        elif amount < 0:
            print('Invalid amount.')
        else:
            info[primary_id] -= amount
            info[other_id] += amount
            print(f'{primary_id} gave ${amount} to {other_id}')

    elif info[primary_id] < amount:
        print(f"You don't have ${amount}.")

    elif amount < 0:
        print('Invalid amount.')

    else:
        info[primary_id] -= amount
        info[other_id] += amount
        print(f'{primary_id} gave ${amount} to {other_id}')

    with open('bank.json', 'w+') as f:
        json.dump(info, f, indent=4)


def make_user_profile(primary_user):
    info[str(primary_user)] = {"rpinfo": {"characters": [{"name": "name here", "age": 0,
                                                          "gender": "gender here", "species": "species here"}, {"same stuff as before": "yeah"}]}}
    with open('bank.json', 'w+') as f:
        json.dump(info, f, indent=4)


make_user_profile("user3")


def see_user_profile(primary_user):
    if primary_user in info:
        print(info[primary_user]["rpinfo"]
              ["characters"])
    else:
        print("doesnt have profile")


see_user_profile("user3")
