#! usr/bin/python3.9
"""
Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

.. warning::
    The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
    They are there as a guide as to how the visual basic / catscript functions work
    and thus help debugging in pycatia.

"""

from pycatia.enumeration.enum_items import CatGeometricType
from pycatia.system_interfaces.any_object import AnyObject


class GeometricElement(AnyObject):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.AnyObject
            |                     GeometricElement
            |
            | Superclass of 2D or 3D wireframe geometric element.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.geometric_element = com_object

    @property
    def geometric_type(self) -> CatGeometricType:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property GeometricType() As CatGeometricType (Read Only)
                |
                |     Returns the type of the underlying geometrical element
                |
                |     Parameters:
                |
                |         oType
                |             Specific type of the geometric interface

        :return: enum cat_geometric_type
        :rtype: int
        """
        return CatGeometricType(self.com_object.GeometricType)

    def to_dict(self):
        return super().to_dict() | {
            "geometric_type": self.geometric_type.name,
            "gemetric_type_value": self.geometric_type.value,
        }
