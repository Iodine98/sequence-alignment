import sys
from random import randrange
from typing import Optional, Tuple, Union
import datetime

from tqdm import tqdm


class SingleLinkedList(object):
    def __init__(self, val=0, next_node=None, from_list=None, length=None):
        if from_list is None:
            self.val, self.next_node, self.__length = val, next_node, length
            if self.__length is None:
                self.__length = self.__len__()
        else:
            self.val, self.next_node, self.__length = create_linked_list(from_list)

    def __str__(self):
        return str(self.val)

    def __dict__(self):
        dictionaries = []
        current = self
        bar = tqdm(total=self.__length, desc='Creating separate dictionaries')
        while current is not None:
            bar.update(1)
            node_dict = dict(val=current.val, next_node=dict() if current.next_node is not None else None)
            dictionaries.append(node_dict)
            current = current.next_node
        bar.close()
        for i in tqdm(range(0, len(dictionaries) - 1), desc='Merging dictionaries'):
            dictionaries[i]['next_node'] = dictionaries[i + 1]
        return dictionaries[0]

    def __len__(self):
        if self.__length is not None:
            return self.__length
        if self.next_node is None:
            return 1
        length, current_node = 0, self
        bar = tqdm(total=0, position=0, desc="Calculating length of manually defined linked list")
        while current_node is not None:
            length += 1
            bar.update(1)
            current_node = current_node.next_node
        bar.close()
        return length

    def tuple_representation(self) -> str:
        current_node = self
        string_list, end_parens = "", ""
        bar = tqdm(total=self.__len__(), desc="Creating string representation")
        while current_node is not None:
            bar.update(1)
            if current_node.next_node is None:
                string_list += current_node.__str__()
            else:
                string_list += '(' + current_node.__str__() + ','
                end_parens += ')'
            current_node = current_node.next_node
        return string_list + end_parens

    def arrow_representation(self):
        current_node = self
        string_list = ""
        bar = tqdm(total=self.__len__(), desc="Creating string representation")
        while current_node is not None:
            if current_node.next_node is None:
                string_list += current_node.__str__()
            else:
                string_list += current_node.__str__() + " --> "
            bar.update(1)
            current_node = current_node.next_node
        bar.close()
        return string_list

    def reverse_list(self):
        previous = None
        current = self
        bar = tqdm(total=self.__len__(), desc='Reversing linked list:')
        while current is not None:
            temp = current.next_node
            current.next_node = previous
            previous = current
            current = temp
            bar.update(1)
        bar.close()
        return previous

    def get_last_node(self, pop=False):
        current = self
        while current.next_node is not None:
            if pop and current.next_node.next_node is None:
                current.next_node = None
                break
            current = current.next_node
        return current

    def prepend(self, linked_list):
        temp_val, temp_linked_list, temp_length = self.val, self.next_node, self.__length
        self.val, self.next_node, self.__length = linked_list.val, linked_list.next_node, linked_list.__length
        last_node = self.get_last_node()
        last_node.next_node = SingleLinkedList(val=temp_val, next_node=temp_linked_list, length=temp_length)

    def append(self, linked_list):
        last_node = self.get_last_node()
        last_node.next_node = linked_list

    def unshift(self, times=1):
        for i in range(times):
            if self.next_node is None:
                break
            self.val, self.next_node, self.__length = self.next_node.val, self.next_node.next_node, self.__length - 1

    def pop(self, times=1):
        for i in range(times):
            self.get_last_node(pop=True)
            self.__length -= 1

    def stringify_dict(self):
        stringification = ''
        end_accolades = ''
        current = self
        bar = tqdm(total=self.__length, desc='Creating string representation of linked list')
        while current is not None:
            bar.update(1)
            stringification += '{' + '"val": ' + str(current.val) + ', "next_node": '
            end_accolades += '}'
            if current.next_node is None:
                stringification += '{}'
            current = current.next_node
        bar.close()
        return stringification + end_accolades


class DoubleLinkedList(SingleLinkedList):
    def __init__(self, prev_node=None, val=0, next_node=None, from_list=None, length=None):
        super().__init__(val, next_node, from_list, length)
        self.prev_node: Optional[DoubleLinkedList] = prev_node
        self.convert_to_double_linked_list()

    def convert_to_double_linked_list(self):
        current = self
        previous = None
        while current is not None:
            current.prev_node = previous
            previous = current
            current = current.next_node


def create_linked_list(from_list: Union[list, range]) -> Tuple[int, Optional[SingleLinkedList], int]:
    if len(from_list) == 0:
        pass
    single_linked_list = None
    for i in tqdm(range(1, len(from_list) + 1), desc="Creating linked list from ordinary list."):
        single_linked_list = SingleLinkedList(val=from_list[-i], next_node=single_linked_list, length=i)
    return single_linked_list.val, single_linked_list.next_node, len(from_list)


if __name__ == "__main__":
    a = datetime.datetime.now()
    this_node = SingleLinkedList(from_list=[['A', 'C', 'G', 'T'][randrange(4)] for _ in range(2 ** 25)])
    print(len(this_node) * sys.getsizeof(this_node))
    b = datetime.datetime.now() - a
    print(b)
