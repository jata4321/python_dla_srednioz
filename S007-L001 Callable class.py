class NoDuplicates():
    def __init__(self, lists):
        self.lists = lists

    def __call__(self, new_item, *args, **kwargs):
        for a in new_item, *args, *kwargs.values():
            self.lists.append(a)


new_list = NoDuplicates([])
dirty_list = 1
new_list(dirty_list)
print(new_list.lists)
new_list(7, 9, z=2)
print(new_list.lists)
