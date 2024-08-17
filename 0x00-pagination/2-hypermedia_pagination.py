#!/usr/bin/env python3
""" Pagination """


import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[Tuple]:
        """ Function that reads the number of a page
        page: (int) - number of page
        page_size: (int) - total page size

        return: (tuple)
        """
        self.page = page
        self.page_size = page_size
        if self.page <= 0:
            return None

        if self.page_size == 0:
            return (self.page, self.page_size)
            # I can instead return page and page
        page_start = (self.page - 1) * self.page_size
        page_end = page_start + self.page_size
        return (page_start, page_end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get page function """
        assert isinstance(page, int) and page > 0
        # assert isinstance(self.page, int) and isinstance(self.page_size, int)
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()

        try:
            pages, pagesize = self.index_range(page, page_size)
            page_line = dataset[pages:pagesize]
        except IndexError:
            return []

        return page_line

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ A function that returns dictionary of list """
        next_page = 0
        prev_page = 0
        total_page = round(int(19419 / page_size))
        if page <= 1:
            prev_page = None

        if page > 1:
            prev_page = page - 1

        if page > total_page:
            next_page = None

        else:
            next_page = page + 1

        # page_sizes = 19419 / total_page

        diction = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(
                page,
                page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_page}
        return diction
