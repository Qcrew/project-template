qm_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                3: {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {"feedforward": [], "feedback": []},
                },
                4: {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {"feedforward": [], "feedback": []},
                },
            },
            "analog_inputs": {1: {"offset": 0.0, "gain_db": 0, "shareable": False}},
        }
    },
    "oscillators": {},
    "elements": {
        "rr": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {"out1": ("con1", 1)},
            "time_of_flight": 180,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {"readout_pulse": "rr.rr_readout_pulse"},
            "mixInputs": {
                "I": ("con1", 3),
                "Q": ("con1", 4),
                "mixer": "mixer_34",
                "lo_frequency": 6000000000.0,
            },
        }
    },
    "pulses": {
        "rr.rr_readout_pulse": {
            "length": 1200,
            "waveforms": {
                "I": "rr.rr_readout_pulse.waveform.I",
                "Q": "rr.rr_readout_pulse.waveform.Q",
            },
            "integration_weights": {
                "cos": "rr.rr_readout_pulse.cos",
                "sin": "rr.rr_readout_pulse.sin",
            },
            "operation": "measurement",
        }
    },
    "waveforms": {
        "rr.rr_readout_pulse.waveform.I": {
            "sample": 0.04000000000000001,
            "type": "constant",
        },
        "rr.rr_readout_pulse.waveform.Q": {"sample": 0.0, "type": "constant"},
    },
    "digital_waveforms": {},
    "integration_weights": {
        "rr.rr_readout_pulse.sin": {"cosine": [(0.0, 1200)], "sine": [(1.0, 1200)]},
        "rr.rr_readout_pulse.cos": {"cosine": [(1.0, 1200)], "sine": [(0.0, 1200)]},
    },
    "mixers": {
        "mixer_34": [
            {
                "intermediate_frequency": 50000000.0,
                "lo_frequency": 6000000000.0,
                "correction": [1.0, 0.0, 0.0, 1.0],
            }
        ]
    },
}
