def yes_or_no():
    while True:
        answer = input().strip().lower()
        if answer in ("yes", "no"):
            return answer
        print("Enter yes or no.")

class BinaryTree:
    def __init__(self, val, left = None, right = None):
        self.value = val
        self.left_child = left
        self.right_child = right

class GameTree:
    def __init__(self, root):
        self.root = root

    def play_game(self):
            while True:
                print("Let's play 20 question's!")

                currantNode = self.root

                while currantNode.left_child is not None and currantNode.right_child is not None:
                    print(currantNode.value)
                    answer = yes_or_no()
                    if answer == "yes":
                        currantNode = currantNode.left_child
                    else:
                        currantNode = currantNode.right_child

                print(f"I understand! Your thinking of a {currantNode.value}")
                print("Was I right?")
                if yes_or_no() == "yes":
                    pass
                else:

                    print("What were you thinking of mate?")
                    new_answer = input().strip()

                    print("What questions should I ask to decide between " + f"{currantNode.value} and {new_answer}?")
                    new_question = input().strip()

                    print(f"If your thinking of {new_answer}, what would be the answer to that question?")
                    answer_for_new = yes_or_no()

                    previous_guess = BinaryTree(currantNode.value)
                    new_guess = BinaryTree(new_answer)

                    currantNode.value = new_question
                    if answer_for_new == "yes":
                        currantNode.left_child = new_guess
                        currantNode.right_child = previous_guess
                    else:
                        currantNode.left_child = previous_guess
                        currantNode.right_child = new_guess

                    print("LOL, I've become smarter!")

                print("Play again?")
                if yes_or_no() == "no":
                    print("--Thanks for playing!--")
                    break

cat = BinaryTree("cat")
dog = BinaryTree("dog")
parrot = BinaryTree("parrot")
fish = BinaryTree("fish")

pointy_ears = BinaryTree("Does it have pointy ears?", cat, dog)
can_it_swim = BinaryTree("Can it swim?", fish, parrot)

root_node = BinaryTree("Does it have 4 legs?", pointy_ears, can_it_swim)

game_tree_instance = GameTree(root_node)

if __name__ == "__main__":
    game_tree_instance.play_game()