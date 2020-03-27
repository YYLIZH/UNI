import numpy as np


class note(object):
    def __init__(self):
        self.position = None
        self.property = None
        self.type = None

    def construct(self, array):
        self.position = array[0:3]
        self.property = array[3]

    def update_sig(self, array):
        if abs(array[0] - self.position[0]) < 10:
            if array[1] - self.position[1] > 0:
                return 'clear'
            else:
                return 'fixed'
        else:
            return 'new'

    def update_pos(self, array):
        self.position = array[0:3]

    def note_classify(self, imgray):
        # print(type(note))
        mea = imgray[self.position[2]:self.position[1], self.position[0]]
        sig = np.mean(mea)
        if self.property == 1:
            if sig < 135:
                self.type = 'Left  '
            elif sig < 150:
                self.type = 'Right'
            elif sig < 185:
                self.type = 'Hold'
            else:
                self.type = 'Click'
        elif self.property == 0:
            self.type = 'Other Click'

    def __del__(self):
        return


class notelist(object):
    def __init__(self):
        self.list = []
        self.fixed_list = np.empty((0, 4), dtype=int)
        self.fixed_curr = 0

    def update(self, List, imgray):
        if len(self.list) == 0:
            self.list = List
        else:
            self_curr = self.fixed_curr
            self_tail = len(self.list)
            List_curr = 0
            List_tail = len(List)
            while self_tail - self_curr > 0:
                obj = self.list[self_curr]
                # print('obj= ',obj.position)
                if List_tail - List_curr > 0:
                    Note = List[List_curr]
                    if Note.tolist() not in self.fixed_list.tolist():
                        sig = obj.update_sig(Note)
                        if sig == 'clear':
                            obj.update_pos(Note)
                            self_curr = self_curr + 1
                            List_curr = List_curr + 1
                        if sig == 'new':
                            New_obj = note()
                            New_obj.construct(Note)
                            New_obj.note_classify(imgray)
                            self.list.insert(self.fixed_curr, New_obj)
                            self_curr = self_curr + 2
                        if sig == 'fixed':
                            self.fixed_list = np.append(self.fixed_list, [Note], axis=0)
                            self.fixed_list.reshape(-1, 4)
                            self_curr = self_curr + 1
                            List_curr = List_curr + 1
                            self.fixed_curr = self.fixed_curr + 1
                    else:
                        List_curr = List_curr + 1
                else:
                    break

    def evoke(self, imgray, limit):
        evoke_note = []
        leng = len(self.list)
        while leng > 0:
            if self.list[leng - 1].position[1] >= limit-20:
                print(self.list[leng - 1].type)
                evoke_note.append(self.list.pop())
                leng = leng - 1
            else:
                #print(' ')
                break
        return evoke_note



