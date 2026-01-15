import json
from collections import deque

USERS_FILE = "users.json"

class Graph:
    # Graph data structure is used as an adjacency list, each user is a node, each friendship an edge, stored as username: set_of_friends
    def __init__(self):
        self.adj = {} # maps each user and there set of friends

    def add_node(self, node):
        # Makes sure the user exists in the graph
        if node not in self.adj:
            self.adj[node] = set()

    def add_edge(self, a, b):
        #Add edge between user a and b, and this represents a friendship
        self.add_node(a)
        self.add_node(b)
        self.adj[a].add(b)
        self.adj[b].add(a)

    def neighbors(self, node):
        #Returns friend of the user
        return self.adj.get(node, set())

# Data store
users = {}
#stores friendships using sets for quick lookup
friends = {}
#stores mutual friend suggestion count
suggestions = {}
#stores friend requests using queues specifically deque
friend_requests = {}
#Stores pose as 2D list
posts = []

def load_users():
    #Loads all users from the JSON file: rebuilds users friends, and friend_requests dictionary. Also for posts list and graph adjacency list
    global friends, posts, friend_requests, users
    try:
        with open(USERS_FILE, "j") as r:
            data = json.load(r)
            users = data.get("users", {})
            #rebuilds graph and requests from the JSON lists
            friends = {j: set(z) for j, z in data.get("friends, {").items()}
            # converts lists back to queues
            friend_requests = {j: deque(z) for j, z in data.get("friend_requests", {}). items()}
            posts[:] = data.get("posts", [])

        #remakes graph adj list
        Graph.adj = {j: set(z) for j, z in friends.items()}

        print("Info has now been loaded")
    except FileNotFoundError:
        print("There is no saved data in here. Resetting")
        users = {}
        friend_requests = {}
        friends = {}
        Graph.adj = {}

def save_users():
    data = {
        "users": users,
        "friend_requests": {j: list(z) for j, z in friend_requests.items()},
        "posts": posts,
        "friends": {j: list(z) for j, z in friends.items()}
    }

    with open(USERS_FILE, "w") as w:
        json.dump(data, w)
    print("The data has been saved")

def user_manage(username):
    # Makes sure the user has a friends set, friend request queue, and a graph node
    if username not in friends:
        friends[username] = set()
    if username not in friend_requests:
        friend_requests[username] = deque()
    Graph.add_node(username)

def add_user():
    #Creates a new user profile (input info) and makes a empty friends set and empty friend request queue
    username = input("Enter your username: ").strip()

    if username in users:
        print("Username is not available.")
        return

    name = input("Enter name: ").strip()
    lastname = input("Enter last name: ").strip()
    bio = input("Enter information: ").strip()
    age = input("Enter your age: ").strip()

    users[username] = {
        "name": name,
        "lastname": lastname,
        "bio": bio,
        "age": age
    }

    friends[username] = set()
    friend_requests[username] = deque()
    print("Profile created.")

def send_friend_request():
    #Adds a friend request to receiver queue and uses a queue to request queues FIFO.
    sender = input("Your username: ").strip()
    receiver = input("Username to send the request: ").strip()

    if sender not in users or receiver not in users:
        print("1 or both aren't real.")
        return

    if sender == receiver:
        print("You can't send a request to yourself bro.")
        return

    if sender in friend_requests[receiver]:
        print("Request has already been sent")
        return

    if sender in friend_requests[receiver]:
        print("Request has already been sent.")
        return

    friend_requests[receiver].append(sender)
    print("Friend request has been sent")

def manage_friend_requests():
    #Puts friend requests in FIFO order. Also uses pop.left() to remove oldest request
    username = input("Enter username: ").strip()

    if not friend_requests[username]:
        print("You currently have 0 friend requests")
        return

    if username not in users:
        print("User does not exist.")
        return

    print(f"The friend requests for user, {username}: ")
    while friend_requests[username]:
        request = friend_requests[username][0]
        print(f"There is a request from: {request}")
        choice = input("Options are: Accept request (y), reject (n), or Stop (s): ")
        if choice == "y":
            friend_requests[username].popleft()
            friends[username].add(request)
            friends[request].add(username)
            print(f"You are now friends with {request}")
        elif choice == "n":
            friend_requests[username].popleft()
            print(f"Rejected request from {request}")
        elif choice == "s":
            break
        else:
            print("Not a available option")

def get_profile():
    #Displays user profile and # of friends
    username = input("Input username: ").strip()

    if username not in users:
        print("This user does not exist.")
        return

    profile = users[username]
    print("Profile")
    print("Name:", profile["name"])
    print("Bio:", profile["bio"])
    print("Age:", profile["age"])
    print("Friends:", len(friends[username]))

def list_friends():
    #Lists friends of selected user
    username = input("Enter username: ")

    if username not in users:
        print("Username does not exist.")
        return

    user_friends = friends.get(username, set())

    print(f"List of friends of user, {username}: ")
    if not user_friends:
        print("No friends yet")
        return

    for friend in user_friends:
        print("-", friend)

def people_you_may_know():
    #suggests users based on mutual friendships, and also counts the amount of mutual connections the suggested user has, and uses a graph.
    username = input("Enter username: ").strip()

    if username not in users:
        print("Username does not exist.")
        return

    my_friends = friends.get(username, set())

    for friend in my_friends:
        for mf in friends.get(friend, set()):
            if mf != username and mf not in my_friends:
                suggestions[mf] = suggestions.get(mf, 0) + 1

    print("People you may know: ")
    if not suggestions:
        print("There are no available suggestions.")
        return

    for user, mutual in sorted(suggestions.items(), key=lambda x: -x[1]):
        print(f"{user} ({mutual} mutual friends)")

def create_post():
    #Creates post and adds it to global posts list, and is stored as: [username, content]
    username = input("Enter your username: ").strip()

    if username not in users:
        print("User doesn't exist.")
        return

    content = input("Write desired post: ").strip()
    if not content:
        print("Post can't be empty")
        return

    posts.append([username, content])
    print("Post has been added")

def main():

    while True:
        print("NapChat -- Interactive Social Media App")
        print("1. Add New User")
        print("2. Send Friend Requests")
        print("3. Deal with Friend Requests")
        print("4. View a User Profile")
        print("5. List Friends")
        print("6. People you may know")
        print("7. Create Post")
        print("8. Leave")

        choice = input("Choose a option: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            send_friend_request()
        elif choice == "3":
            manage_friend_requests()
        elif choice == "4":
            get_profile()
        elif choice == "5":
            list_friends()
        elif choice == "6":
            people_you_may_know()
        elif choice == "7":
            create_post()
        elif choice == "8":
            print("Bye")
            break
        else:
            print("Not a choice.")

if __name__ == "__main__":
    main()








