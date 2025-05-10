#! usr/bin/python3.9
"""
Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

.. warning::
    The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
    They are there as a guide as to how the visual basic / catscript functions work
    and thus help debugging in pycatia.

"""

import inspect
import sys
from typing import TYPE_CHECKING, Any, Dict, Optional, Type, TypeVar

from pycatia.base_interfaces.pycatia import PyCATIA

if TYPE_CHECKING:
    from pycatia.in_interfaces.application import Application
T = TypeVar("T", bound="AnyObject")

# Global registry to cache class mappings
_COM_TYPE_TO_CLASS_REGISTRY: Dict[str, Type] = {}


class AnyObject(PyCATIA):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 AnyObject
            |
            | Represents the base object for all other objects except collection and
            | reference objects.
            | As a base object, it provides properties shared by any other
            | object.

    """

    @classmethod
    def new(cls, com_object):
        """
        Create a new instance of the class.

        :param com_object: The COM object to wrap
        :return: An instance of the class
        """
        return cls(com_object).cast()

    def __init__(self, com_object):
        super().__init__()
        self._com = self.com_object = com_object

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance of the class.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: An instance of the class
        """
        if args[0] is None:
            return None
        return super().__new__(cls)

    @property
    def application(self) -> "Application":
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Application() As Application (Read Only)
                |
                |     Returns the application. The application is the root object of the object
                |     structure and can be retrieved from any object in this object structure using
                |     the Application property. The root object, also called top-level object, is the
                |     object located at the top of the application's object structure. It is used by
                |     clients to retrieve and navigate across all the application's subordinate
                |     objects. If the client runs in-process, it retrieves the object at the top of
                |     the object structure. If the client runs out-process, it should call the
                |     GetApplication method to retrieve the object at the top of the object
                |     structure, which is the only object accessible from outside. The Application
                |     property is thus the way to jump from any object up to the root of the object
                |     structure, allowing then to navigate downwards. For in-process scripting, the
                |     application is always referred to as CATIA. Note that the Application property
                |     of the Application object returns the Application object
                |     itself.
                |
                |     Example:
                |         This example retrieves in CurrentApplication the application object,
                |         root of the object structure, from a given object of this structure: a document
                |         refered to using the MyDoc variable.
                |
                |          Dim CurrentApplication As Application
                |          Set CurrentApplication = MyDoc.Application

        :rtype: com_object
        """
        from pycatia.in_interfaces.application import Application

        return Application(self.com_object.Application)

    @property
    def name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Name() As CATBSTR
                |
                |     Returns or sets the name of the object. The name is a character string
                |     automatically assigned to any object to handle it easier. Even if the Name
                |     property allows you to reassign an object name, this is not advised. Many
                |     objects, such as the application and the collections, have names that you must
                |     not change, and it's safer to use Name as a read only property. When an object
                |     is part of a collection, the object name can often be used in place of the
                |     object rank to retrieve or remove the object, providing the Item and Remove
                |     methods of the collection feature an argument with the Variant type. A name
                |     must start with a letter. It can include numbers, but it can't include spaces.
                |     If the object has no name set, the default name returned is the object type.
                |     For example, the Name property of a Viewer3D object with no name set returns
                |     Viewer3D.
                |
                |     Example:
                |         This example retrieves in MyObjectName the name of the MyObject
                |         object.
                |
                |          MyObjectName = MyObject.Name

        :rtype: str
        """
        if self.com_object is None:
            return None
        return self.com_object.Name

    @name.setter
    def name(self, value: str):
        """
        :param str value:
        """

        self.com_object.Name = value

    @property
    def parent(self) -> "AnyObject":
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Parent() As CATBaseDispatch (Read Only)
                |
                |     Returns the parent object. The parent object of a given object is the
                |     object just above in the object structure, usually the object that created this
                |     object and that aggregates it. In the case of an object part of a collection,
                |     the parent object can be the collection object itself or the object that
                |     aggregates the collection object. The Parent property is the way to step
                |     upwards in the object structure. Note that the Parent property of the
                |     Application object returns the Application object itself.
                |
                |     Example:
                |         This example retrieves in ParentObject the parent object of the
                |         GivenObject object.
                |
                |          Dim ParentObject As AnyObject
                |          Set ParentObject = GivenObject.Parent

        :rtype: AnyObject
        """
        if self.com_object is None:
            return None
        return AnyObject.new(self.com_object.Parent)

    def get_item(self, id_name: str) -> "AnyObject":
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetItem(CATBSTR IDName) As CATBaseDispatch
                |
                |     Returns an object from its name.
                |     Role: To retrieve an object when only its name is
                |     available.
                |
                |     Parameters:
                |
                |         IDName
                |             The searched object name
                |
                |     Returns:
                |         The searched object

        :param str id_name:
        :rtype: AnyObject
        """
        return AnyObject.new(self.com_object.GetItem(id_name))

    def __getattr__(self, name):
        # convert to snake case if name is UpperCamelCase
        if name[0].isupper():
            name = "".join(
                ["_" + i.lower() if i.isupper() else i for i in name]
            ).lstrip("_")
        return self.__getattribute__(name)

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name}")'

    # def com_type(self) -> str:
    #     vba_function_name = "com_type"
    #     vba_code = f"""
    #     Public Function {vba_function_name}(obj As AnyObject) as String
    #         {vba_function_name} = typename(obj)
    #     End Function
    #     """
    #     # print(__name__, "com_type", self.name())
    #     return self.application().system_service().evaluate(vba_code, 0, vba_function_name, [self._com])

    @property
    def com_type(self) -> str:
        """
        Get the COM type name of the object.

        This property returns the COM type name of the object by accessing the type information
        from the COM object. This is equivalent to the Visual Basic TypeName function.

        :return: The COM type name of the object
        """
        if self.com_object is None:
            return None
        return self.com_object._oleobj_.GetTypeInfo(0).GetDocumentation(-1)[0]

    def get_class_by_com_type(self, com_type_name: str = None) -> Optional[Type[T]]:
        """
        Get the Python class corresponding to a COM type name.

        This function searches through all pycatia modules to find a class that matches
        the given COM type name. Results are cached for better performance.

        :param com_type_name: The COM type name to find the class for
        :return: The Python class corresponding to the COM type name, or None if not found
        """
        if com_type_name is None:
            com_type_name = self.com_type
        # Check if we already have this type in our registry
        if com_type_name in _COM_TYPE_TO_CLASS_REGISTRY:
            return _COM_TYPE_TO_CLASS_REGISTRY[com_type_name]

        # If not found in registry, search for it
        result_class = None

        # First check if the class is in the current module
        current_module = sys.modules.get(self.__class__.__module__)
        if current_module and hasattr(current_module, com_type_name):
            result_class = getattr(current_module, com_type_name)
            if inspect.isclass(result_class) and issubclass(result_class, AnyObject):
                _COM_TYPE_TO_CLASS_REGISTRY[com_type_name] = result_class
                return result_class

        # Search through all pycatia modules
        for module_name in list(sys.modules.keys()):
            if module_name.startswith("pycatia.") and "interfaces" in module_name:
                try:
                    module = sys.modules[module_name]
                    if hasattr(module, com_type_name):
                        potential_class = getattr(module, com_type_name)
                        if inspect.isclass(potential_class) and issubclass(
                            potential_class, AnyObject
                        ):
                            result_class = potential_class
                            break
                except (ImportError, AttributeError):
                    continue

        # Cache the result (even if None)
        _COM_TYPE_TO_CLASS_REGISTRY[com_type_name] = result_class
        return result_class

    def cast(self) -> "T":
        """Cast to subclass of AnyObject by com_type

        This method automatically casts the AnyObject to the appropriate Python class
        based on its COM type name. If no matching class is found, the original AnyObject
        is returned.

        :return: The object cast to its specific type, or the original AnyObject if no matching class is found
        """
        target_class = self.get_class_by_com_type()

        if target_class is None:
            # If no matching class is found, return the original object
            return self

        # Cast to the target class
        return self.as_pyclass(target_class)

    def _vba_cast(self, com_object, vba_class_name):
        """
        Internal helper method to cast a COM object to a specific VBA class.

        :param com_object: The COM object to cast
        :param vba_class_name: The name of the VBA class to cast to
        :return: The COM object cast to the specified VBA class
        """
        vba_function_name = "generalizedCastToVBA"
        vba_code = f"""
        Public Function generalizedCastToVBA(obj as AnyObject) as {vba_class_name}
            set generalizedCastToVBA = obj
        End Function
        """
        return self.application.system_service.evaluate(
            vba_code, 0, vba_function_name, [com_object]
        )

    def as_pyclass(self, target_class: Type[T], vba_class_name: str = None) -> T:
        """
        Cast the current object to a specific Python class.

        This method casts the underlying COM object to the specified Python class.
        If no VBA class name is provided, the name of the target Python class is used.

        :param target_class: The Python class to cast to
        :param vba_class_name: Optional VBA class name to use for casting
        :return: The object cast to the specified Python class
        """
        if self.com_object is None:
            return self

        if vba_class_name is None:
            vba_class_name = target_class.__name__

        # Verify that target_class is a subclass of AnyObject
        if not issubclass(
            target_class, AnyObject
        ):  # TODO: check for BaseClasses like Shape and GeometricElement
            raise TypeError(
                f"Target class {target_class.__name__} must be a subclass of AnyObject"
            )
        try:
            return target_class(self._vba_cast(self.com_object, vba_class_name))
        except Exception:
            # print(f"Error casting to {target_class.__name__}: {e}")
            # TODO: return None or self?
            return None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "type": self.com_type,
        } | ({"parent": str(self.parent)} if self.parent else {})
