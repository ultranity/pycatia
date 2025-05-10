#! usr/bin/python3.9
"""
Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

.. warning::
    The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
    They are there as a guide as to how the visual basic / catscript functions work
    and thus help debugging in pycatia.

"""

from pycatia.cat_tps_interfaces.capture import Capture
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Captures(Collection[Capture]):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.Collection
            |                     Captures
            |
            | The interface to access a CATIACaptures

    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AnyObject)
        self.captures = com_object

    def item(self, i_index: cat_variant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As AnyObject
                |
                |     Retrieve a Capture.

        :param cat_variant i_index:
        :rtype: AnyObject
        """
        return AnyObject.new(self.captures.Item(i_index))
