# Copyright 2023 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cirq
import cirq_ft
import pytest


def test_assert_circuit_inp_out_cirqsim():
    qubits = cirq.LineQubit.range(4)
    initial_state = [0, 1, 0, 0]
    circuit = cirq.Circuit(cirq.X(qubits[3]))
    final_state = [0, 1, 0, 1]

    cirq_ft.testing.assert_circuit_inp_out_cirqsim(circuit, qubits, initial_state, final_state)

    final_state = [0, 0, 0, 1]
    with pytest.raises(AssertionError):
        cirq_ft.testing.assert_circuit_inp_out_cirqsim(circuit, qubits, initial_state, final_state)


def test_gate_helper():
    g = cirq_ft.testing.GateHelper(cirq_ft.And(cv=(1, 0, 1, 0)))
    assert g.gate == cirq_ft.And(cv=(1, 0, 1, 0))
    assert g.r == cirq_ft.Registers.build(control=4, ancilla=2, target=1)
    assert g.quregs == {
        'control': cirq.NamedQubit.range(4, prefix='control'),
        'ancilla': cirq.NamedQubit.range(2, prefix='ancilla'),
        'target': [cirq.NamedQubit('target')],
    }
    assert g.operation.qubits == tuple(g.all_qubits)
    assert len(g.circuit) == 1


class DoesNotDecompose(cirq.Operation):
    def _t_complexity_(self) -> cirq_ft.TComplexity:
        return cirq_ft.TComplexity(t=1, clifford=2, rotations=3)

    @property
    def qubits(self):
        return []

    def with_qubits(self, _):
        pass


class InconsistentDecompostion(cirq.Operation):
    def _t_complexity_(self) -> cirq_ft.TComplexity:
        return cirq_ft.TComplexity(rotations=1)

    def _decompose_(self) -> cirq.OP_TREE:
        yield cirq.X(self.qubits[0])

    @property
    def qubits(self):
        return tuple(cirq.LineQubit(3).range(3))

    def with_qubits(self, _):
        pass


@pytest.mark.parametrize(
    "val", [cirq.T, DoesNotDecompose(), cirq_ft.testing.GateHelper(cirq_ft.And()).operation]
)
def test_assert_decompose_is_consistent_with_t_complexity(val):
    cirq_ft.testing.assert_decompose_is_consistent_with_t_complexity(val)


def test_assert_decompose_is_consistent_with_t_complexity_raises():
    with pytest.raises(AssertionError):
        cirq_ft.testing.assert_decompose_is_consistent_with_t_complexity(InconsistentDecompostion())
