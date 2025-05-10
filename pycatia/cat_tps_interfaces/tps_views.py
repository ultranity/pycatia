#! usr/bin/python3.9
"""
Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

.. warning::
    The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
    They are there as a guide as to how the visual basic / catscript functions work
    and thus help debugging in pycatia.

"""

from pycatia.cat_tps_interfaces.tps_view import TPSView
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class TPSViews(Collection[TPSView]):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.Collection
            |                     TPSViews
            |
            | Interface for collection of TPS Views CATIATPSView.

    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=TPSView)
        self.tps_views = com_object

    def item(self, i_index: cat_variant) -> TPSView:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As AnyObject
                |
                |     Retrieve a TPS View.

        :param cat_variant i_index:
        :rtype: AnyObject
        """
        return TPSView(self.tps_views.Item(i_index))
