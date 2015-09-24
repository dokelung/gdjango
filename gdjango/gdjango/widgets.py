"""
settings output widget

release |release|, version |version|

.. versionadded:: 1.0

    Initial

Contents
--------

Classes:

Functions:

Variables:

Members
-------

"""

from django.forms import widgets


class TupleToCheckBoxGroup(widgets.CheckboxSelectMultiple):
    """
    Proxy widget for future extension
    """
    pass


class BooleanToRadio(widgets.RadioChoiceInput):
    """
    Proxy widget for future extension
    """
    pass


class DictToClosure(widgets.Input):
    """
    Proxy widget for future extension
    """

    def render(self, name=None, value=None, attrs=None):

        if value is None:
            if self.value is None:
                return ""
            value = self.value

        results = []
        for k, v in value.items():
            results.append(get_customized_widget(k, v).render())

        return "".join(results)


def get_customized_widget(name, value):
    """get cutsomized widget which is extended from built-in widgets

    :param name: TODO
    :param value: TODO
    :returns: TODO

    """
    if isinstance(value, tuple):
        return TupleToCheckBoxGroup(name, name, choices=value)

    if isinstance(value, dict):
        return DictToClosure(name, value)

    if isinstance(value, bool):
        return BooleanToRadio(name, value)

    raise AttributeError("Such data type <{}> isn't supported yet.".format(type(value)))
