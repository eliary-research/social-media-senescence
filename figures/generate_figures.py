"""
EN1: Social Media Senescence — Figure Generation
Generates 4 figures for the paper using collected data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pathlib import Path

# Style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'figure.facecolor': 'white',
})

DATA_DIR = Path(__file__).parent.parent / 'data'
FIG_DIR = Path(__file__).parent


# ── Figure 1: Facebook Senescence Curve ──────────────────────────────

def fig1_facebook_senescence():
    df = pd.read_csv(DATA_DIR / 'meta_quarterly.csv')

    # Create numeric quarter index
    quarters = [f"{r['year']} {r['quarter']}" for _, r in df.iterrows()]
    x = range(len(df))

    fig, ax1 = plt.subplots(figsize=(12, 5.5))

    # DAU/MAU ratio (left axis)
    color_ratio = '#2563EB'
    ax1.plot(x, df['dau_mau_ratio'], color=color_ratio, linewidth=2, label='DAU/MAU Ratio')
    ax1.set_ylabel('DAU/MAU Ratio', color=color_ratio, fontsize=12)
    ax1.tick_params(axis='y', labelcolor=color_ratio)
    ax1.set_ylim(0.55, 0.76)

    # ARPU (right axis)
    ax2 = ax1.twinx()
    color_arpu = '#DC2626'
    ax2.fill_between(x, df['arpu_dollars'], alpha=0.15, color=color_arpu)
    ax2.plot(x, df['arpu_dollars'], color=color_arpu, linewidth=2, linestyle='--', label='ARPU ($)')
    ax2.set_ylabel('ARPU (USD)', color=color_arpu, fontsize=12)
    ax2.tick_params(axis='y', labelcolor=color_arpu)

    # Q4 2021 marker (first DAU decline)
    q4_2021_idx = df[(df['year'] == 2021) & (df['quarter'] == 'Q4')].index[0]
    ax1.axvline(x=q4_2021_idx, color='gray', linestyle=':', alpha=0.7)
    ax1.annotate('First DAU\ndecline\n(Q4 2021)', xy=(q4_2021_idx, 0.665),
                fontsize=9, ha='center', color='gray',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

    # X-axis: show every 8th quarter
    tick_positions = list(range(0, len(df), 8))
    tick_labels = [quarters[i] for i in tick_positions]
    ax1.set_xticks(tick_positions)
    ax1.set_xticklabels(tick_labels, rotation=45, ha='right', fontsize=9)

    ax1.set_title('Facebook: The Advertising Ratchet\nDAU/MAU Ratio Rising (Survivor Bias) While ARPU Extraction Accelerates', fontsize=13)

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

    ax1.grid(axis='y', alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig1_facebook_senescence.png')
    plt.close()
    print("  ✓ fig1_facebook_senescence.png")


# ── Figure 2: Generational Displacement ──────────────────────────────

def fig2_generational_displacement():
    # Parse Pew CSV (skip comment lines)
    rows = []
    with open(DATA_DIR / 'pew_social_media_by_age.csv') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('year,'):
                continue
            parts = line.split(',')
            if len(parts) >= 4:
                try:
                    rows.append({
                        'year': int(parts[0]),
                        'platform': parts[1],
                        'age_group': parts[2],
                        'usage_pct': float(parts[3])
                    })
                except ValueError:
                    continue

    df = pd.DataFrame(rows)
    fb = df[df['platform'] == 'facebook'].copy()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Left: Facebook generational displacement
    colors = {'18-29': '#EF4444', '30-49': '#F59E0B', '50-64': '#10B981', '65+': '#6366F1'}
    markers = {'18-29': 'o', '30-49': 's', '50-64': '^', '65+': 'D'}

    for ag in ['18-29', '30-49', '50-64', '65+']:
        subset = fb[fb['age_group'] == ag].sort_values('year')
        ax1.plot(subset['year'], subset['usage_pct'],
                color=colors[ag], marker=markers[ag], markersize=6,
                linewidth=2, label=f'Age {ag}')

    ax1.set_title('Facebook: Generational Displacement\n"Parents Join → Youth Leave"', fontsize=12)
    ax1.set_ylabel('% of U.S. Adults Using Facebook', fontsize=11)
    ax1.set_xlabel('Year', fontsize=11)
    ax1.legend(fontsize=9, loc='center right')
    ax1.set_ylim(25, 95)
    ax1.grid(alpha=0.3)

    # Annotate the gap
    ax1.annotate('Gap: 51pp\n(2012)', xy=(2012, 60), fontsize=8, color='gray', ha='center')
    ax1.annotate('Gap: 11pp\n(2025)', xy=(2025, 62), fontsize=8, color='gray', ha='center')

    # Right: Instagram (early stage of same pattern)
    ig = df[df['platform'] == 'instagram'].copy()
    for ag in ['18-29', '30-49', '50-64', '65+']:
        subset = ig[ig['age_group'] == ag].sort_values('year')
        ax2.plot(subset['year'], subset['usage_pct'],
                color=colors[ag], marker=markers[ag], markersize=6,
                linewidth=2, label=f'Age {ag}')

    ax2.set_title('Instagram: Early Displacement\nYouth Plateauing, Elders Rising', fontsize=12)
    ax2.set_ylabel('% of U.S. Adults Using Instagram', fontsize=11)
    ax2.set_xlabel('Year', fontsize=11)
    ax2.legend(fontsize=9, loc='center right')
    ax2.set_ylim(-5, 95)
    ax2.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig2_generational_displacement.png')
    plt.close()
    print("  ✓ fig2_generational_displacement.png")


# ── Figure 3: Question Platform Lifecycles ───────────────────────────

def fig3_question_platform_lifecycle():
    df = pd.read_csv(DATA_DIR / 'question_platforms.csv')

    # Calculate lifespan
    df['end_year'] = df['shutdown_year'].fillna(2026)  # NA = still alive (barely)
    df['lifespan'] = df['end_year'] - df['launch_year']
    df = df.sort_values('launch_year')

    fig, ax = plt.subplots(figsize=(12, 7))

    # Color by cause
    cause_colors = {
        'cyberbullying': '#EF4444',
        'acquihire': '#8B5CF6',
        'regulatory': '#F59E0B',
        'novelty': '#6B7280',
        'other': '#3B82F6'
    }

    def get_cause_category(cause):
        cause = str(cause).lower()
        if 'cyberbullying' in cause or 'safety' in cause or 'suicide' in cause:
            return 'cyberbullying'
        if 'acquired' in cause or 'acquihire' in cause:
            return 'acquihire'
        if 'ftc' in cause or 'regulatory' in cause or 'removed' in cause or 'suspended' in cause:
            return 'regulatory'
        if 'novelty' in cause or 'plateau' in cause or 'attrition' in cause:
            return 'novelty'
        return 'other'

    df['cause_cat'] = df['cause_of_decline'].apply(get_cause_category)

    y_positions = range(len(df))
    for i, (_, row) in enumerate(df.iterrows()):
        color = cause_colors.get(row['cause_cat'], '#6B7280')
        ax.barh(i, row['lifespan'], left=row['launch_year'],
               color=color, alpha=0.8, height=0.7, edgecolor='white', linewidth=0.5)
        # Peak marker
        if pd.notna(row['peak_year']):
            ax.plot(row['peak_year'], i, 'k*', markersize=10, zorder=5)

    ax.set_yticks(y_positions)
    ax.set_yticklabels(df['name'], fontsize=9)
    ax.set_xlabel('Year', fontsize=11)
    ax.set_title('Question Platform Lifecycles: All Pull×One-Shot, Median 2–4 Years\n★ = Peak Year', fontsize=13)
    ax.set_xlim(2008, 2027)
    ax.grid(axis='x', alpha=0.3)

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#EF4444', alpha=0.8, label='Cyberbullying/Safety'),
        Patch(facecolor='#8B5CF6', alpha=0.8, label='Acqui-hire → Kill'),
        Patch(facecolor='#F59E0B', alpha=0.8, label='Regulatory Action'),
        Patch(facecolor='#6B7280', alpha=0.8, label='Novelty Exhaustion'),
        Patch(facecolor='#3B82F6', alpha=0.8, label='Other'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig3_question_platform_lifecycle.png')
    plt.close()
    print("  ✓ fig3_question_platform_lifecycle.png")


# ── Figure 4: Cross-Platform Age-Engagement Gradient ─────────────────

def fig4_engagement_gradient():
    # Data from engagement_rate_decline.md
    platforms = ['TikTok\n(2017)', 'Instagram\n(2010)', 'Facebook\n(2004)', 'X/Twitter\n(2006)']
    engagement = [3.70, 0.48, 0.15, 0.12]
    ages = [9, 16, 22, 20]  # platform age in years (as of 2026)
    colors = ['#00F2EA', '#E4405F', '#1877F2', '#1DA1F2']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Left: Bar chart
    bars = ax1.bar(platforms, engagement, color=colors, alpha=0.85, edgecolor='white', linewidth=1.5)
    ax1.set_ylabel('Engagement Rate (%)', fontsize=11)
    ax1.set_title('2025 Engagement Rate by Platform\nOlder = Lower Engagement', fontsize=12)
    ax1.grid(axis='y', alpha=0.3)

    # Add value labels
    for bar, val in zip(bars, engagement):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.08,
                f'{val}%', ha='center', fontsize=11, fontweight='bold')

    ax1.set_ylim(0, 4.5)

    # Right: Instagram engagement decline timeline (Rival IQ)
    ig_years = [2019, 2020, 2021, 2022, 2023, 2025]
    ig_engagement = [1.22, 0.98, 0.98, 0.67, 0.43, 0.36]

    ax2.plot(ig_years, ig_engagement, 'o-', color='#E4405F', linewidth=2.5, markersize=8)
    ax2.fill_between(ig_years, ig_engagement, alpha=0.1, color='#E4405F')
    ax2.set_ylabel('Median Engagement Rate (%)', fontsize=11)
    ax2.set_xlabel('Year', fontsize=11)
    ax2.set_title('Instagram Engagement Decline\n1.22% → 0.36% (−70% in 6 years)', fontsize=12)
    ax2.grid(alpha=0.3)
    ax2.set_ylim(0, 1.5)

    # Annotation
    ax2.annotate('−70%', xy=(2022, 0.8), fontsize=14, fontweight='bold',
                color='#EF4444', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.9))

    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig4_engagement_gradient.png')
    plt.close()
    print("  ✓ fig4_engagement_gradient.png")


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Generating EN1 figures...")
    fig1_facebook_senescence()
    fig2_generational_displacement()
    fig3_question_platform_lifecycle()
    fig4_engagement_gradient()
    print("\nAll figures saved to Papers/EN1/figures/")
