""" """

from qcore import Dataset, Sweep, Stage

################################# PROJECT FOLDER PATH ##################################
# to obtain Resources (Instruments, Modes, Pulses) from and save data file to

FOLDER = "C:/Users/qcrew/project-template/"

MODES_CONFIG = FOLDER + "config/modes.yml"

######################## CONFIGURE STAGED RESOURCES IF NEEDED ##########################

with Stage(MODES_CONFIG, remote=True) as stage:
    QUBIT, RR = stage.get("qubit", "rr")
    LO_QUBIT, LO_RR, SA = stage.get("lo_qubit", "lo_rr", "sa")
(READOUT_PULSE,) = RR.get_operations("rr_readout_pulse")

################## DEFINE REUSABLE SWEEP (INDEPENDENT) VARIABLES #######################

# averaging sweep "N"
N = Sweep(
    name="N",
    num=1000,
    dtype=int,
    save=False,
)

# linspace Frequency sweep
FREQ = Sweep(
    name="freq",
    dtype=int,
    units="Hz",
)

################## DEFINE REUSABLE DATASET (DEPENDENT) VARIABLES #######################

I = Dataset(
    name="I",
    save=False,
    save_args={"save_avg": False},
    plot=False,
    plot_args={"plot_err": False, "plot_avg": True},
)

Q = Dataset(
    name="Q",
    save=False,
    save_args={"save_avg": False},
    plot=False,
    plot_args={"plot_err": False, "plot_avg": True},
)

ADC = Dataset(
    name="adc",
    stream=RR.ports["out"],
    save=False,
    plot=True,
    plot_args={
        "plot_avg": True,
        "plot_type": "line",
        "plot_err": False,
        "xlabel": "Time (ns)",
    },
)

ADC_FFT = Dataset(
    name="adc_fft",
    save=False,
    plot=True,
    datafn="fft",
    datafn_args={"length": READOUT_PULSE.total_length},
    plot_args={"plot_type": "line", "plot_err": False},
)

MAG = Dataset(
    name="Magnitude",
    save=False,
    plot=True,
    datafn="mag",
    fitfn="lorentzian_asymmetric",
    plot_args={"plot_err": False},
)

PHASE = Dataset(
    name="Phase",
    save=False,
    plot=True,
    datafn="phase",
    datafn_args={"delay": 2.792e-7, "freq": RR.int_freq, "unwrap": True},
    fitfn="atan",
    plot_args={"plot_err": False},
)
