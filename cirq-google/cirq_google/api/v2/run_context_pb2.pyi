# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class RunContext(google___protobuf___message___Message):

    @property
    def parameter_sweeps(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ParameterSweep]: ...

    def __init__(self,
        parameter_sweeps : typing___Optional[typing___Iterable[ParameterSweep]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RunContext: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"parameter_sweeps"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"parameter_sweeps"]) -> None: ...

class ParameterSweep(google___protobuf___message___Message):
    repetitions = ... # type: int

    @property
    def sweep(self) -> Sweep: ...

    def __init__(self,
        repetitions : typing___Optional[int] = None,
        sweep : typing___Optional[Sweep] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ParameterSweep: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"sweep"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"repetitions",u"sweep"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"sweep",b"sweep"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"repetitions",b"sweep"]) -> None: ...

class Sweep(google___protobuf___message___Message):

    @property
    def sweep_function(self) -> SweepFunction: ...

    @property
    def single_sweep(self) -> SingleSweep: ...

    def __init__(self,
        sweep_function : typing___Optional[SweepFunction] = None,
        single_sweep : typing___Optional[SingleSweep] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Sweep: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"single_sweep",u"sweep",u"sweep_function"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"single_sweep",u"sweep",u"sweep_function"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"single_sweep",b"single_sweep",u"sweep",b"sweep",u"sweep_function",b"sweep_function"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"single_sweep",b"sweep",b"sweep_function"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"sweep",b"sweep"]) -> typing_extensions___Literal["sweep_function","single_sweep"]: ...

class SweepFunction(google___protobuf___message___Message):
    class FunctionType(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> SweepFunction.FunctionType: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[SweepFunction.FunctionType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, SweepFunction.FunctionType]]: ...
    FUNCTION_TYPE_UNSPECIFIED = typing___cast(FunctionType, 0)
    PRODUCT = typing___cast(FunctionType, 1)
    ZIP = typing___cast(FunctionType, 2)

    function_type = ... # type: SweepFunction.FunctionType

    @property
    def sweeps(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Sweep]: ...

    def __init__(self,
        function_type : typing___Optional[SweepFunction.FunctionType] = None,
        sweeps : typing___Optional[typing___Iterable[Sweep]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SweepFunction: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"function_type",u"sweeps"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"function_type",b"sweeps"]) -> None: ...

class DeviceParameter(google___protobuf___message___Message):
    path = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    idx = ... # type: int
    units = ... # type: typing___Text

    def __init__(self,
        path : typing___Optional[typing___Iterable[typing___Text]] = None,
        idx : typing___Optional[int] = None,
        units : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeviceParameter: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"idx",u"path",u"units"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"idx",b"path",b"units"]) -> None: ...

class SingleSweep(google___protobuf___message___Message):
    parameter_key = ... # type: typing___Text

    @property
    def points(self) -> Points: ...

    @property
    def linspace(self) -> Linspace: ...

    @property
    def parameter(self) -> DeviceParameter: ...

    def __init__(self,
        parameter_key : typing___Optional[typing___Text] = None,
        points : typing___Optional[Points] = None,
        linspace : typing___Optional[Linspace] = None,
        parameter : typing___Optional[DeviceParameter] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SingleSweep: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"linspace",u"parameter",u"points",u"sweep"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"linspace",u"parameter",u"parameter_key",u"points",u"sweep"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"linspace",b"linspace",u"parameter",b"parameter",u"points",b"points",u"sweep",b"sweep"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"linspace",b"parameter",b"parameter_key",b"points",b"sweep"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"sweep",b"sweep"]) -> typing_extensions___Literal["points","linspace"]: ...

class Points(google___protobuf___message___Message):
    points = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[float]

    def __init__(self,
        points : typing___Optional[typing___Iterable[float]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Points: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"points"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"points"]) -> None: ...

class Linspace(google___protobuf___message___Message):
    first_point = ... # type: float
    last_point = ... # type: float
    num_points = ... # type: int

    def __init__(self,
        first_point : typing___Optional[float] = None,
        last_point : typing___Optional[float] = None,
        num_points : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Linspace: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"first_point",u"last_point",u"num_points"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"first_point",b"last_point",b"num_points"]) -> None: ...
