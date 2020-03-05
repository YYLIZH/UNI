import numpy as np


class note(object):
    def __init__(self):
        self.position = None
        self.property = None

    def construct(self, array):
        self.position = array

    def update_sig(self, array):
        if abs(array[0] - self.position[0]) < 10:
            if array[1] - self.position[1] > 0:
                return 'clear'
            else:
                return 'fixed'
        else:
            return 'new'

    def update_pos(self, array):
        self.position = array

    def __del__(self):
        return


class notelist(object):
    def __init__(self):
        self.list = None
        self.fixed_list = np.array([], dtype=int)
        self.fixed_curr = 0

    def add(self, List):
        self.list = List

    def update(self, List):
        self_curr = self.fixed_curr
        self_tail = len(self.list)
        List_curr = 0
        List_tail = len(List)
        while self_tail - self_curr > 0:
            obj = self.list[self_curr]
            Note = List[List_curr]
            if Note not in self.fixed_list:
                sig = obj.update_sig(Note)
                if sig == 'clear':
                    obj.update_pos(Note)
                    self_curr = self_curr + 1
                    List_curr = List_curr + 1
                if sig == 'new':
                    New_obj = note()
                    New_obj.construct(Note)
                    self.list.insert(self.fixed_curr, New_obj)
                    self_curr = self_curr + 2
                    self_tail = self_tail + 1
                if sig == 'fixed':
                    self.fixed_list = np.append(self.fixed_list, Note)
                    self.fixed_list.reshape(-1, 2)
                    self_curr = self_curr + 1
                    List_curr = List_curr + 1
                    self.fixed_curr = self.fixed_curr + 1
            else:
                List_curr = List_curr + 1
