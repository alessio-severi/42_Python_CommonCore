import importlib
from typing import Generator, TYPE_CHECKING
from types import ModuleType

if TYPE_CHECKING:
    import numpy as np_type
    import pandas as pd_type
    import matplotlib.pyplot as plt_type


def init() -> tuple[list[str], list[str], dict[str, ModuleType | None]]:
    dependencies = ["numpy", "pandas", "matplotlib"]
    module: dict[str, ModuleType | None] = {x: None for x in dependencies}
    msg_ready = ["Numerical computation ready", "Data manipulation ready",
                 "Visualization ready"]
    return dependencies, msg_ready, module


def check_dependencies(dependencies: list[str],
                       msg_ready: list[str],
                       module: dict[str, ModuleType | None]
                       ) -> Generator[str, None, bool]:

    # dependence_msg: str, truthy_falsy_flag: str, module: ModuleType | None
    def check_dependence(name: str) -> tuple[str, str, ModuleType | None]:
        try:
            mod = importlib.import_module(name)
            return f"\033[32m[OK] {name} ({mod.__version__}) - ", "_", mod
        except ModuleNotFoundError:
            return f"\033[31m[KO] {name} [Missing dependency] - ", "", None

    flag = ""
    for x in zip(dependencies, msg_ready):
        *msg, module[x[0]] = check_dependence(x[0])
        yield (msg[0] +
               (x[1] if msg[1] else (flag := x[1].replace(" r", " not r"))) +
               "\033[0m")
    return not flag


def data_set(np: ModuleType) -> tuple["np_type.ndarray", "np_type.ndarray"]:
    if TYPE_CHECKING:
        np = np_type

    Om = 0.3        # Angular velocity omega
    R = 6.2         # Radius of the uniform circular motion trajectory

    t = np.arange(0, 62.8, step=0.005)
    p = np.sin(Om * t) * R
    return t, p


def data_manipulation(t: "np_type.ndarray",
                      p: "np_type.ndarray",
                      pd: ModuleType) -> "pd_type.DataFrame":
    if TYPE_CHECKING:
        pd = pd_type
        data: pd_type.DataFrame

    data = pd.DataFrame({'time': t, 'position': p})
    data['positive'] = data['position'].where(data['position'] >= 0)  # Series
    data['negative'] = data['position'].where(data['position'] < 0)   # Series
    return data


def visualization(data: "pd_type.DataFrame", mpl: ModuleType) -> None:

    plt = importlib.import_module(f"{mpl.__name__}.pyplot")
    if TYPE_CHECKING:
        plt = plt_type

    font = {'family': 'serif', 'color': 'steelblue', 'weight': 'normal'}

    plt.figure(figsize=(10, 6), dpi=100)
    plt.title('Matrix analysis', **font, size=18)
    plt.xlabel('t/s', **font, size=13)
    plt.ylabel('x(t)/m', **font, size=13)
    plt.xlim(-4, 66)
    plt.ylim(-11, 11)
    plt.text(0, -9.5,  r'$\omega=0.3\:rad/s$', **font, size=12)
    plt.text(0, -10.5,  r'$R=6.2\:m$', **font, size=12)

    plt.plot(data['time'], data['positive'], '-b',
             label=r'$x(t)=R\,\sin(\omega t) \geq 0$', linewidth=3)  # leq
    plt.plot(data['time'], data['negative'], '-c',
             label=r'$x(t)=R\,\sin(\omega t) < 0$', linewidth=3)

    plt.legend(loc='lower right', labelcolor='linecolor')
    plt.savefig('matrix_analysis.png')
    plt.show()


if __name__ == "__main__":
    print("\n\033[34mLOADING STATUS: Loading programs...\033[0m")

    dependencies, msg_ready, module = init()
    print("\nChecking dependencies:")
    g = check_dependencies(dependencies, msg_ready, module)
    while g:
        try:
            print(next(g))
        except StopIteration as s:
            if s.value:
                print("\nAnalyzing Matrix data...")
                assert module["numpy"] is not None
                t, p = data_set(module['numpy'])
                print("Processing 1000 data points...")
                assert module["pandas"] is not None
                data = data_manipulation(t, p, module['pandas'])
                print("Generating visualization...")
                assert module["matplotlib"] is not None
                visualization(data, module['matplotlib'])
                print("\nAnalysis complete!")
                print("\033[32m[OK] Results saved to: "
                      "matrix_analysis.png\033[0m")
            else:
                print("\n\033[31mLoading failed: [Missing dependency]\033[0m")
                print("\nInstall missing packages with:")
                print("\033[32mpip install -r requirements.txt\033[0m")
                print("\nOr using Poetry:")
                print("\033[32mpoetry install\033[0m")
            break
