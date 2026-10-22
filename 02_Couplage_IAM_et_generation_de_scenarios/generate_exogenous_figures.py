"""Regenerate the exogenous-trend figures used in slides_session3.tex.

All trajectories include the calibrated initial state (2015). 2015 is not a
model transition: the first transition occurs from 2015 to 2020.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).with_name("images")
YEARS = np.arange(2015, 2101, 5)

class Params:
    Delta=5; t0=2015; A0=5.115; gA=0.076; deltaA=0.005
    L0=7403.; Linf=10500.; lg=0.134
    sigma0=0.3503; pb=550.; theta2=2.6; deltapb=0.025
    EL0=2.6; deltaEL=0.115; f0=0.5; f1=1.0

p = Params()
COLORS = ["C0", "C1", "C2", "C3"]


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, bbox_inches="tight")
    plt.close(fig)


def converge(x0, target, speed):
    k = np.arange(len(YEARS))
    return x0 * (target / x0) ** (1 - (1 - speed) ** k)


def exponential_to(x0, xT):
    return x0 * (xT / x0) ** ((YEARS - 2015) / (2100 - 2015))


# Population: every calibration shares the observed 2015 initial condition.
fig, ax = plt.subplots(figsize=(8.2, 5.0))
for label, target, speed, color in zip(
    ["Baseline", "SSP1-like (lower)", "SSP3-like (higher)", "SSP5-like (even higher)"],
    [10500, 9500, 11500, 14000], [p.lg, 0.12, 0.14, 0.16], COLORS):
    ax.plot(YEARS, converge(p.L0, target, speed), label=label, color=color, lw=2)
ax.set(title="Population paths: baseline vs SSP-like calibrations", xlabel="Year", ylabel="Population (model units)", xlim=(2015, 2100), xticks=[2015, 2030, 2050, 2070, 2090, 2100])
ax.grid(True); ax.legend(); save(fig, "figure_L.pdf")

# Productivity: same observed 2015 level, alternative long-run growth profiles.
def productivity(gA):
    out = np.empty(len(YEARS)); out[0] = p.A0
    for i in range(1, len(out)):
        out[i] = out[i-1] / (1 - gA * np.exp(-p.deltaA * p.Delta * i))
    return out
fig, ax = plt.subplots(figsize=(8.2, 5.0))
for label, g, color in zip(
    ["Baseline (SSP2-like)", "SSP1-like (slower A growth)", "SSP3-like (moderately slower)", "SSP5-like (faster A growth)"],
    [0.076, 0.064, 0.070, 0.088], COLORS):
    ax.plot(YEARS, productivity(g), label=label, color=color, lw=2)
ax.set(title="Productivity paths under SSP-like calibrations", xlabel="Year", ylabel="Productivity A (model units)", xlim=(2015, 2100), xticks=[2015, 2030, 2050, 2070, 2090, 2100])
ax.grid(True); ax.legend(); save(fig, "figure_A.pdf")

# Non-CO2 forcing: include each scenario's 2015 initial forcing.
fig, ax = plt.subplots(figsize=(8.2, 5.0))
for label, x0, xT, color in zip(
    ["Baseline (SSP2-like)", "SSP1-like (lower non-CO$_2$ forcing)", "SSP3-like (higher non-CO$_2$ forcing)", "SSP5-like (intermediate)"],
    [0.50, 0.42, 0.55, 0.60], [1.00, 0.90, 1.10, 1.25], COLORS):
    ax.plot(YEARS, np.linspace(x0, xT, len(YEARS)), label=label, color=color, lw=2)
ax.set(title=r"Non-CO$_2$ forcing $F_t^{EX}$ under SSP-like assumptions", xlabel="Year", ylabel=r"Exogenous non-CO$_2$ forcing $F_t^{EX}$ (W/m$^2$)", xlim=(2015, 2100), xticks=[2015, 2030, 2050, 2070, 2090, 2100])
ax.grid(True); ax.legend(); save(fig, "figure_FEX.pdf")

# Emissions intensity and land-use emissions.
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.5))
labels = ["Baseline (SSP2-like)", "SSP1-like (fast decarb.)", "SSP3-like (slow decarb.)", "SSP5-like"]
for label, x0, xT, color in zip(labels, [0.3503, 0.320, 0.390, 0.340], [0.095, 0.085, 0.105, 0.090], COLORS):
    axes[0].plot(YEARS, exponential_to(x0, xT), label=label, color=color)
for label, x0, xT, color in zip(["Baseline (SSP2-like)", "SSP1-like", "SSP3-like", "SSP5-like"], [2.60, 2.05, 2.75, 2.90], [0.32, 0.14, 0.43, 0.55], COLORS):
    axes[1].plot(YEARS, exponential_to(x0, xT), label=label, color=color)
axes[0].set(title="Emission intensity paths", xlabel="Year", ylabel=r"Emission intensity $\sigma_t$", xlim=(2015, 2100), xticks=[2015, 2030, 2050, 2070, 2090, 2100])
axes[1].set(title="Land-use emissions paths", xlabel="Year", ylabel=r"Land-use emissions $E_t^{land}$", xlim=(2015, 2100), xticks=[2015, 2030, 2050, 2070, 2090, 2100])
for ax in axes: ax.grid(True); ax.legend(fontsize=8)
save(fig, "figure_sigma_Eland.pdf")

# Abatement-cost coefficient.
fig, ax = plt.subplots(figsize=(8.2, 5.0))
for label, x0, xT, color in zip(
    ["Baseline (SSP2-like)", "SSP1-like (cheaper abatement)", "SSP3-like (costlier abatement)", "SSP5-like (tech optimism)"],
    [0.074, 0.052, 0.089, 0.063], [0.013, 0.009, 0.016, 0.011], COLORS):
    ax.plot(YEARS, exponential_to(x0, xT), label=label, color=color, lw=2)
ax.set(title=r"Abatement cost trajectories $\theta_1(t)$ under SSP-like assumptions", xlabel="Year", ylabel=r"Abatement cost parameter $\theta_1$", xlim=(2015, 2100), xticks=[2015, 2030, 2050, 2070, 2090, 2100])
ax.grid(True); ax.legend(); save(fig, "figure_theta1.pdf")

# Baseline summary directly from the corrected model initialization.
baseline_series = [
    ("TFP $A_t$", productivity(p.gA)),
    (r"Decoupling $\sigma_t$", exponential_to(p.sigma0, 0.095)),
    (r"Abatement to GDP $\theta_{1,t}$", exponential_to(p.pb/(1000*p.theta2)*p.sigma0, 0.013)),
    (r"Non-CO2 Radiative Forcing $F_t^{EX}$", np.linspace(p.f0, p.f1, len(YEARS))),
    (r"Land-use Emissions (GtCO$_2$) $E_t^{land}$", exponential_to(p.EL0, 0.32)),
    (r"Population $L_t$", converge(p.L0, p.Linf, p.lg)),
]
fig, axes = plt.subplots(2, 3, figsize=(11.5, 6.0))
for ax, (title, values) in zip(axes.flat, baseline_series):
    ax.plot(YEARS, values, color="firebrick")
    ax.set_title(title); ax.set_xlim(2015, 2100); ax.set_xticks([2015, 2040, 2060, 2080, 2100]); ax.grid(True)
save(fig, "figure_2.pdf")
