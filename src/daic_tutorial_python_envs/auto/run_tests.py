import subprocess  # noqa: D100


def run_tests():  # noqa: D103
    subprocess.run(["pytest"], check=False)
