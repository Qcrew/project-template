""" """

from qcore import Dataset, Experiment, qua, Stage, Sweep


class ResonatorSpectroscopy(Experiment):
    """ """

    primary_datasets = ["I", "Q"]
    primary_sweeps = ["freq"]

    def sequence(self):
        """ """
        qua.update_frequency(self.resonator, self.freq)
        self.resonator.measure(self.readout_pulse, (self.I, self.Q), ampx=self.ro_ampx)
        qua.wait(self.wait_time, self.resonator)


if __name__ == "__main__":
    """ """

    folder = "C:/Users/qcrew/project-template"

    modes = {"resonator": "rr"}

    pulses = {"readout_pulse": "rr_readout_pulse"}

    parameters = {"wait_time": 400000, "ro_ampx": 1.0}

    N = Sweep(name="N", num=5001, dtype=int, save=False)
    FREQ = Sweep(name="freq", start=-51e6, stop=-49e6, num=11, dtype=int, units="Hz")
    sweeps = [N, FREQ]

    with Stage(folder + "/modes.yml") as stage:
        (rr,) = stage.get("rr")

    I = Dataset(name="I", save=True, plot=False)
    Q = Dataset(name="Q", save=True, plot=False)
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
        fitfn="sine",
    )
    datasets = [I, Q, MAG, PHASE]

    expt = ResonatorSpectroscopy(folder, modes, pulses, sweeps, datasets, **parameters)
    expt.run()
