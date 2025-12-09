from ...errors import DuplicateDefinition, TarskiError, UndefinedElement


class ObservationExpressivenessMismatch(TarskiError):
    def __init__(self, sensor, msg=None):
        msg = msg or "mismatch between the expressiveness of the specified sensor and that supported by the language!"
        super().__init__(
            f"Sensing action: {sensor.name}: {msg}\nObservation should be literal (Atom, or CompoundFormula)"
            f" and it is: {type(sensor.obs)}"
        )


class DuplicateSensorDefinition(DuplicateDefinition):
    pass


class UndefinedSensor(UndefinedElement):
    pass
