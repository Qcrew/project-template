""" """

from pathlib import Path

from qcore.helpers import Stage
from qcore.modes import *
from qcore.pulses import *

if __name__ == "__main__":
    """ """

    # configpath must be the path to the modes config file
    # remote = True means the Stage will connect with the Server and stage instruments
    # for remote = True to work, please run setup_server.bat first

    with Stage(configpath=Path.cwd() / "modes.yml", remote=True) as stage:
        # RETRIEVE INSTRUMENTS AND MODES
        lo_qubit, lo_rr = stage.get("lo_qubit", "lo_rr")
        qubit, rr = stage.get("qubit", "rr")

        lo_qubit.frequency = 6e9
        lo_qubit.power = 13

        lo_rr.frequency = 6e9
        lo_rr.power = 13

        # CONFIGURE THE QUBIT PROPERTIES AND OPERATIONS
        qubit.configure(
            name="qubit",
            lo_name="lo_qubit",
            ports={"I": 1, "Q": 2},
        )

        qubit.operations = [
            ConstantPulse(
                name="qubit_constant_pulse",
                length=1000,
                I_ampx=1.0,
            ),
            GaussianPulse(
                name="qubit_gaussian_pulse",
                sigma=200,
                chop=4,
                I_ampx=1.0,
                Q_ampx=0.0,
            ),
            RampedConstantPulse(
                name="qubit_cos_ramp_pulse",
                ramp=10,
                rampfn="cos",
                length=20,
                I_ampx=1.4,
            ),
        ]

        # CONFIGURE THE RR PROPERTIES AND OPERATIONS
        rr.configure(
            name="rr",
            lo_name="lo_rr",
            ports={"I": 3, "Q": 4, "out": 1},
            int_freq=-50e6,
            time_of_flight=180,
        )

        rr.operations = [
            ConstantPulse(
                name="rr_constant_pulse",
                length=4000,
                I_ampx=1.0,
            ),
            GaussianPulse(
                name="rr_gaussian_pulse",
                sigma=100,
                chop=6,
                I_ampx=1.0,
                Q_ampx=0.0,
            ),
            ConstantReadoutPulse(
                name="rr_readout_pulse",
                length=1200,
                I_ampx=0.2,
                pad=1000,
            ),
        ]
