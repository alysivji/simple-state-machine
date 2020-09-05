from finite_state_machine import StateMachine, transition
import pytest


def test_state_machine_requires_state_instance_variable():
    class LightSwitch(StateMachine):
        def turn_on(self):
            pass

        def turn_off(self):
            pass

    with pytest.raises(ValueError, match="Need to set a state instance variable"):
        LightSwitch()


def test_source_parameter_is_tuple():
    with pytest.raises(ValueError):

        @transition(source=("here",), target="there")
        def conditions_check(instance):
            pass


def test_target_parameter_is_tuple():
    with pytest.raises(ValueError):

        @transition(source="here", target=("there",))
        def conditions_check(instance):
            pass


def test_conditions_parameter_is_tuple():
    with pytest.raises(ValueError):

        @transition(source="here", target="there", conditions=(1, 2))
        def conditions_check(instance):
            pass
