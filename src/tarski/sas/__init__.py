# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez <miquel.ramirez@pm.me>
# ----------------------------------------------------------------------------------------------------------------------
# src/tarski/sas/__init__.py
#
# SAS Modeling support
# ----------------------------------------------------------------------------------------------------------------------

from collections import namedtuple


Schema = namedtuple('Schema', ['name', 'variables', 'constraints', 'transitions'])
Action = namedtuple('Action', ['name', 'arguments', 'transitions'])
