#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict
Server2 = __import__("2-hypermedia_pagination").Server


Servers = Server2()


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Getting hyper index """
        page = 1000
        assert index < len(self.__indexed_dataset)

        dictionary = {
            'index': index,
            'data': Servers.get_page(page, page_size),
            'page_size': page_size,
            'next_index': 3
        }

        if index >= 0 and page_size > index:
            for index in page_size:
                return page_size[index]

    def get(idx: str) -> str:
        """ Get method to get indexes """
        dataset = self.__indexed_dataset

        for string in dataset:
            return string[idx]
