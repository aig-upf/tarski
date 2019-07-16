
from ..errors import TarskiError


class TarskiDLError(TarskiError):
    """ Common ancestor class to all of Tarski's Description Language exceptions """


class SyntacticDLError(TarskiDLError):
    def __init__(self, msg=None):
        msg = msg or 'Unexplained Tarski DL syntactic error'
        super().__init__(msg)

#
# class SemanticDLError(TarskiDLError):
#     def __init__(self, msg=None):
#         msg = msg or 'Unexplained Tarski DL semantic error'
#         super().__init__(msg)


class ArityDLMismatch(SyntacticDLError):
    def __init__(self, msg=None):
        msg = msg or 'Mismatch between language element and DL element'
        super().__init__(msg)
