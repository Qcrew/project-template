""" """

from qcore.helpers import Stage
from qcore.modes import *
from qcore.pulses import *

from config.experiment_config import MODES_CONFIG

if __name__ == "__main__":
    """ """

    # configpath must be the path to the modes config file
    # remote = True means the Stage will connect with the Server and stage instruments
    # for remote = True to work, please run setup_server.bat first

    with Stage(configpath=MODES_CONFIG, remote=True) as stage:
        # RETRIEVE INSTRUMENTS AND MODES
        lo_qubit, lo_rr = stage.get("lo_qubit", "lo_rr")
        qubit, rr = stage.get("qubit", "rr")

        lo_qubit.frequency = 4.26975e9
        lo_qubit.power = 15.0
        lo_qubit.output = True

        lo_rr.frequency = 7.466e9
        lo_rr.power = 15.0
        lo_rr.output = True

        # CONFIGURE THE QUBIT PROPERTIES AND OPERATIONS
        qubit.configure(
            name="qubit",
            lo_name="lo_qubit",
            ports={"I": 1, "Q": 2},
            int_freq=50e6,
        )

        qubit.operations = [
            ConstantPulse(
                name="qubit_constant_pulse",
                length=10000,
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
            int_freq=50e6,
            tof=272,
        )

        rr.operations = [
            ConstantPulse(
                name="rr_constant_pulse",
                length=1000,
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
                length=400,
                I_ampx=1.0,
                pad=400,
                digital_marker=DigitalWaveform("ADC_ON"),
            ),
        ]
