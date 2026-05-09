"""
EN1: Social Media Senescence — Figure Generation
Academic style: grayscale-friendly, colorblind-safe, 300 DPI
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

# Style
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

DATA = Path(__file__).parent.parent / 'data'
OUT = Path(__file__).parent

# Colorblind-safe palette (Wong 2011)
C_BLUE = '#0072B2'
C_ORANGE = '#E69F00'
C_GREEN = '#009E73'
C_RED = '#D55E00'
C_PURPLE = '#CC79A7'
C_GRAY = '#999999'


# ============================================================
# Figure 1: Meta Senescence Curves (DAU + ARPU dual axis)
# ============================================================
def fig1_senescence_curves():
    df = pd.read_csv(DATA / 'meta_quarterly.csv')
    # Create time index
    q_map = {'Q1': 0, 'Q2': 0.25, 'Q3': 0.5, 'Q4': 0.75}
    df['t'] = df['year'] + df['quarter'].map(q_map)
    # Annual ARPU (sum of quarterly)
    annual = df.groupby('year').agg(
        dau=('dau_millions', 'last'),
        mau=('mau_millions', 'last'),
        arpu=('arpu_dollars', 'sum'),
        revenue=('revenue_billions', 'sum')
    ).reset_index()

    fig, ax1 = plt.subplots(figsize=(8, 4.5))

    # DAU bars
    ax1.bar(annual['year'], annual['dau'], width=0.7, color=C_BLUE,
            alpha=0.3, label='DAU (millions)', zorder=2)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Daily Active Users (millions)', color=C_BLUE)
    ax1.tick_params(axis='y', labelcolor=C_BLUE)
    ax1.set_ylim(0, 2600)

    # ARPU line on secondary axis
    ax2 = ax1.twinx()
    ax2.plot(annual['year'], annual['arpu'], color=C_RED, linewidth=2.5,
             marker='o', markersize=5, label='ARPU ($/year)', zorder=3)
    ax2.set_ylabel('Annual ARPU ($)', color=C_RED)
    ax2.tick_params(axis='y', labelcolor=C_RED)

    # Annotate key events
    ax2.annotate('Q4 2021:\nFirst DAU\ndecline', xy=(2021, annual[annual.year==2021].arpu.values[0]),
                 xytext=(2017.5, 55), fontsize=8, color=C_GRAY,
                 arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=0.8))
    ax2.annotate('ARPU 15.8x\n($5.32 → $84)',
                 xy=(2025, annual[annual.year==2025].arpu.values[0]),
                 xytext=(2022.5, 80), fontsize=8, color=C_RED, fontstyle='italic',
                 arrowprops=dict(arrowstyle='->', color=C_RED, lw=0.8))

    # DAU growth stagnation annotation
    ax1.annotate('DAU growth\nstagnates\n(<5% YoY)',
                 xy=(2021, annual[annual.year==2021].dau.values[0]),
                 xytext=(2023, 1200), fontsize=8, color=C_BLUE,
                 arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=0.8))

    ax1.set_title('Facebook/Meta: The Advertising Ratchet (M1)\nDAU Growth Stagnates While Extraction Accelerates')
    fig.tight_layout()
    fig.savefig(OUT / 'senescence_curves.png')
    fig.savefig(OUT / 'senescence_curves.pdf')
    plt.close(fig)
    print('[OK] senescence_curves.png')


# ============================================================
# Figure 2: Generational Displacement (Pew data)
# ============================================================
def fig2_generational_shift():
    lines = []
    with open(DATA / 'pew_social_media_by_age.csv') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            lines.append(line)

    from io import StringIO
    df = pd.read_csv(StringIO('\n'.join(lines)))
    df.columns = ['year', 'platform', 'age_group', 'usage_pct', 'source']
    df['usage_pct'] = pd.to_numeric(df['usage_pct'], errors='coerce')

    fb = df[df.platform == 'facebook'].copy()

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), sharey=True)

    # --- Panel A: Facebook ---
    ax = axes[0]
    age_colors = {'18-29': C_RED, '30-49': C_ORANGE, '50-64': C_GREEN, '65+': C_PURPLE}
    age_markers = {'18-29': 'o', '30-49': 's', '50-64': '^', '65+': 'D'}
    for age in ['18-29', '30-49', '50-64', '65+']:
        sub = fb[fb.age_group == age].sort_values('year')
        ax.plot(sub.year, sub.usage_pct, color=age_colors[age],
                marker=age_markers[age], markersize=5, linewidth=1.8, label=age)

    ax.set_title('A. Facebook: Generational Displacement (M2)')
    ax.set_xlabel('Year')
    ax.set_ylabel('% of U.S. Adults Using Platform')
    ax.set_ylim(0, 100)
    ax.legend(title='Age Group', loc='center right')

    # Gap annotation
    ax.annotate('Gap: 51pp\n(2012)', xy=(2012, 60), fontsize=8, color=C_GRAY,
                ha='center')
    ax.annotate('', xy=(2012, 86), xytext=(2012, 35),
                arrowprops=dict(arrowstyle='<->', color=C_GRAY, lw=1))
    ax.annotate('Gap: 11pp\n(2025)', xy=(2025, 63), fontsize=8, color=C_GRAY,
                ha='center')
    ax.annotate('', xy=(2025, 68), xytext=(2025, 57),
                arrowprops=dict(arrowstyle='<->', color=C_GRAY, lw=1))

    # --- Panel B: Snapchat (resistance) ---
    sc = df[df.platform == 'snapchat'].copy()
    ax2 = axes[1]
    for age in ['18-29', '30-49', '50-64', '65+']:
        sub = sc[sc.age_group == age].sort_values('year')
        ax2.plot(sub.year, sub.usage_pct, color=age_colors[age],
                 marker=age_markers[age], markersize=5, linewidth=1.8, label=age)

    ax2.set_title('B. Snapchat: Senescence Resistance')
    ax2.set_xlabel('Year')
    ax2.legend(title='Age Group', loc='upper left')
    ax2.annotate('65+ stuck\nat 4%', xy=(2025, 4), fontsize=8, color=C_PURPLE,
                 xytext=(2021, 18),
                 arrowprops=dict(arrowstyle='->', color=C_PURPLE, lw=0.8))

    fig.suptitle('Generational Displacement: Facebook vs. Snapchat\n'
                 'Pew Research Center, 2012–2025', fontsize=12, y=1.02)
    fig.tight_layout()
    fig.savefig(OUT / 'generational_shift.png')
    fig.savefig(OUT / 'generational_shift.pdf')
    plt.close(fig)
    print('[OK] generational_shift.png')


# ============================================================
# Figure 3: Question Platform Lifecycle (Gantt-style)
# ============================================================
def fig3_question_platforms():
    df = pd.read_csv(DATA / 'question_platforms.csv')

    # Sort by launch year then peak year
    df = df.sort_values(['launch_year', 'peak_year'], ascending=[True, True])

    # Determine end year (shutdown or 2025 if still active)
    df['end_year'] = df['shutdown_year'].fillna(2025).astype(int)
    df['duration'] = df['end_year'] - df['launch_year']

    fig, ax = plt.subplots(figsize=(9, 5.5))

    y_positions = range(len(df))
    colors = []
    for _, row in df.iterrows():
        if pd.notna(row['shutdown_year']):
            colors.append(C_RED)
        else:
            colors.append(C_GREEN)

    bars = ax.barh(y_positions, df['duration'], left=df['launch_year'],
                   color=colors, alpha=0.7, height=0.6, edgecolor='white', linewidth=0.5)

    # Peak markers
    for i, (_, row) in enumerate(df.iterrows()):
        if pd.notna(row['peak_year']):
            ax.plot(row['peak_year'], i, marker='*', color=C_ORANGE,
                    markersize=10, zorder=5)

    ax.set_yticks(list(y_positions))
    ax.set_yticklabels(df['name'], fontsize=8)
    ax.set_xlabel('Year')
    ax.set_xlim(2008, 2026)
    ax.set_title('Question Platform Lifecycles: Pull × One-Shot = Fastest Senescence\n'
                 'Median lifespan: 2–4 years (N=15)')
    ax.invert_yaxis()

    # Legend
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    legend_elements = [
        Patch(facecolor=C_RED, alpha=0.7, label='Shut down'),
        Patch(facecolor=C_GREEN, alpha=0.7, label='Still active (declining)'),
        Line2D([0], [0], marker='*', color='w', markerfacecolor=C_ORANGE,
               markersize=10, label='Peak year'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=8)

    # Median lifespan annotation
    median_duration = df['duration'].median()
    ax.axvline(x=2009 + median_duration, color=C_GRAY, linestyle='--', alpha=0.5)

    fig.tight_layout()
    fig.savefig(OUT / 'question_platform_lifecycle.png')
    fig.savefig(OUT / 'question_platform_lifecycle.pdf')
    plt.close(fig)
    print('[OK] question_platform_lifecycle.png')


# ============================================================
# Figure 4: Snapchat Recovery (DAU + ARPU, Streak effect)
# ============================================================
def fig4_snap_recovery():
    df = pd.read_csv(DATA / 'snap_quarterly.csv')
    q_map = {'Q1': 0, 'Q2': 0.25, 'Q3': 0.5, 'Q4': 0.75}
    df['t'] = df['year'] + df['quarter'].map(q_map)

    fig, ax1 = plt.subplots(figsize=(8, 4.5))

    # DAU line
    ax1.plot(df['t'], df['dau_millions'], color=C_BLUE, linewidth=2,
             marker='o', markersize=3, label='DAU (millions)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('DAU (millions)', color=C_BLUE)
    ax1.tick_params(axis='y', labelcolor=C_BLUE)
    ax1.set_ylim(150, 500)

    # ARPU on secondary axis
    ax2 = ax1.twinx()
    ax2.plot(df['t'], df['arpu_dollars'], color=C_ORANGE, linewidth=2,
             marker='s', markersize=3, label='ARPU ($)')
    ax2.set_ylabel('Quarterly ARPU ($)', color=C_ORANGE)
    ax2.tick_params(axis='y', labelcolor=C_ORANGE)

    # 2018 crisis zone
    ax1.axvspan(2018.0, 2019.0, alpha=0.08, color=C_RED, zorder=0)
    ax1.annotate('2018 redesign crisis\nDAU stagnation\n(188→186→186M)',
                 xy=(2018.5, 188), xytext=(2019.5, 220), fontsize=8,
                 color=C_RED,
                 arrowprops=dict(arrowstyle='->', color=C_RED, lw=0.8))

    # Streak annotation
    ax1.annotate('Streak mechanic\n= crude accumulation\n→ sustained recovery',
                 xy=(2020.0, 238), xytext=(2021.5, 300), fontsize=8,
                 color=C_GREEN,
                 arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=0.8))

    # Q4 2025 decline
    ax1.annotate('Q4 2025:\nFirst QoQ decline\nsince 2018',
                 xy=(2025.75, 474), xytext=(2023.8, 400), fontsize=8,
                 color=C_RED,
                 arrowprops=dict(arrowstyle='->', color=C_RED, lw=0.8))

    ax1.set_title('Snapchat: Senescence Resistance Through Accumulation\n'
                  'Streak mechanic creates switching cost absent in Q&A platforms')

    fig.tight_layout()
    fig.savefig(OUT / 'snap_recovery.png')
    fig.savefig(OUT / 'snap_recovery.pdf')
    plt.close(fig)
    print('[OK] snap_recovery.png')


# ============================================================
# Run all
# ============================================================
if __name__ == '__main__':
    print('Generating EN1 figures...')
    print(f'Data dir: {DATA}')
    print(f'Output dir: {OUT}')
    fig1_senescence_curves()
    fig2_generational_shift()
    fig3_question_platforms()
    fig4_snap_recovery()
    print('\nAll 4 figures generated successfully.')
