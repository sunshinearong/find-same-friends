class LinkedList:
    def __init__(self,name):
        self._name = name#init name
        self._friends = None#init friends
        self._next = None#init next
    def add_friend(self,friend):
        if self._friends == None:#no friends
            self._friends = friend
        else:
            first_friend = self._friends
            while self._friends:
                if self._friends._next == None:#friend is not in self._friends
                    self._friends._next = friend
                    break
                if self._friends._name == friend._name:#friend is in self,_friends
                    break
                self._friends = self._friends._next
            self._friends = first_friend