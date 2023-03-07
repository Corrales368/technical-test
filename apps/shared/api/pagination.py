# Import django
from rest_framework.pagination import PageNumberPagination


class SmallPageNumberPagination(PageNumberPagination):
    """"
    A custom pagination class that limits the number of items per page and 
    sets reasonable defaults for the page size and maximum page size.
    """
    page_size = 10  # Default number of items per page
    max_page_size = 100  # Maximum number of items per page


class MediumPageNumberPagination(PageNumberPagination):
    """"
    A custom pagination class that limits the number of items per page and 
    sets reasonable defaults for the page size and maximum page size.
    """
    page_size = 20  # Default number of items per page
    max_page_size = 100  # Maximum number of items per page


class LargePageNumberPagination(PageNumberPagination):
    """"
    A custom pagination class that limits the number of items per page and 
    sets reasonable defaults for the page size and maximum page size.
    """
    page_size = 50  # Default number of items per page
    max_page_size = 100  # Maximum number of items per page


class ExtraLargePageNumberPagination(PageNumberPagination):
    """"
    A custom pagination class that limits the number of items per page and 
    sets reasonable defaults for the page size and maximum page size.
    """
    page_size = 100  # Default number of items per page
    max_page_size = 100  # Maximum number of items per page