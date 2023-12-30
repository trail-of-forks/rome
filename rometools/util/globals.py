from pathlib import Path

# import yaml

# with open("globals.yml", "r") as stream:
#     data = yaml.safe_load(stream)

(RESULTS_DIR, DATA_DIR, STATS_DIR, HPARAMS_DIR,) = (
    Path(z)
    for z in [
        # data["RESULTS_DIR"],
        "results",
        # data["DATA_DIR"],
        "data",
        # data["STATS_DIR"],
        "data/stats",
        # data["HPARAMS_DIR"],
        "hparams",
    ]
)

# REMOTE_ROOT_URL = data["REMOTE_ROOT_URL"]
REMOTE_ROOT_URL = "https://rome.baulab.info"
