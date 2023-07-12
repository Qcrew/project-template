""" """


from qcore import Dataset, Sweep, Stage

################################# PROJECT FOLDER PATH ##################################
# to obtain Resources (Instruments, Modes, Pulses) from and save data file to

FOLDER = "C:/Users/qcrew/project-template/"

######################## CONFIGURE STAGED RESOURCES IF NEEDED ##########################

with Stage(FOLDER + "config/modes.yml") as stage:
    qubit, rr = stage.get("qubit", "rr")

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
    save=True,
    plot=False,
)

Q = Dataset(
    name="Q",
    save=True,
    plot=False,
)

MAG = Dataset(
    name="Magnitude",
    save=False,
    plot=True,
    datafn="mag",
    fitfn="lorentzian",
)

PHASE = Dataset(
    name="Phase",
    save=False,
    plot=True,
    datafn="phase",
    datafn_args={"delay": 50e-8, "freq": rr.int_freq},
)
