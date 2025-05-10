#! /usr/bin/python3.6
import os
import sys

sys.path.insert(0, os.path.abspath(".."))
from pycatia import catia
from pycatia.exception_handling import CATIAApplicationException


def initialise():
    """

    :return:
    """
    documents = catia.documents
    if documents.count > 0:
        raise CATIAApplicationException(
            "Please close all documents before running tests."
        )

    return catia, documents
