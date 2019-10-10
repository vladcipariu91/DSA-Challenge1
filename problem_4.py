"""
In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy
as such. Where User is represented by str representing their ids.
"""


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if user is None or group is None:
        return False

    if user in group.users:
        return True

    for sub_group in group.groups:
        if is_user_in_group(user, sub_group):
            return True

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_1 = Group("subchild_1")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

for i in range(0, 100):
    sub_child_1.add_user("User: {}".format(i))

child.add_group(sub_child)
child.add_group(sub_child_1)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent))
# expected True
print(is_user_in_group("sub_child_user", sub_child_1))
# expected False
print(is_user_in_group("sub_child_user", None))
# expected False
print(is_user_in_group("User: 78", parent))
# expected True
print(is_user_in_group("User: 78", sub_child))
# expected False
print(is_user_in_group("User: 101", parent))
# expected False
print(is_user_in_group("", parent))
# expected False
print(is_user_in_group(None, parent))
# expected False
