#! /usr/bin/python3.9

import logging

from pycatia.cat_logger import create_logger


class PyCATIA:
    """
    Base class for the catia application.
    """

    def __init__(self):
        pass

    @property
    def logger(self) -> logging.Logger:
        """
        :rtype: logging.Logger
        """
        return create_logger()

    def release_check(self, current: int, required: int, name: str):
        """

        Used to notify user if the CATIA V5 version is lower than that required.

        :param int current:
        :param int required:
        :param str name:
        """
        if current < required:
            self.logger.info(
                f'"{name}" was introduced in R{required}. You are running R{current}.'
            )

    def __repr__(self):
        return "PyCATIA()"

    def __getattr__(self, name):
        # convert to snake case if name is UpperCamelCase
        if name[0].isupper():
            name = "".join(
                ["_" + i.lower() if i.isupper() else i for i in name]
            ).lstrip("_")
        return self.__getattribute__(name)
