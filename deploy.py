from pathlib import Path
from shutil import copy2


def deploy():
    destination = Path.home() / "jenkins_deployment" / "Lab10_Tara_El_Khoury"
    destination.mkdir(parents=True, exist_ok=True)

    source = Path(__file__).resolve().parent / "app.py"
    copy2(source, destination / "app.py")

    print(f"Application deployed successfully to {destination}")


if __name__ == "__main__":
    deploy()