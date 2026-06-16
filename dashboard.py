"""
=============================================================
CODTECH IT SOLUTIONS - DATA ANALYTICS INTERNSHIP
TASK 3: DASHBOARD DEVELOPMENT

---

## 🏢 Internship Details

| Field | Details |
|---|---|
| **Company** | CODTECH IT Solutions Pvt. Ltd. |
| **Intern Name** | Abhijeet Das |
| **Intern ID** | CITS500 |
| **Domain** | Data Analytics |
| **Task** | Task 3 — Dashboard Development |
| **Duration** | 4 Weeks |
| **Mentor** | Neela Santhosh Kumar |

---
=============================================================

Objective:
    Create an interactive dashboard using Dash (Python) to
    visualize a sales dataset with actionable insights.

Tools Used:
    - Dash  (interactive web dashboard)
    - Plotly (interactive charts)
    - Pandas (data processing)

How to Run:
    1. pip install dash plotly pandas
    2. python dashboard.py
    3. Open browser: http://127.0.0.1:8050
"""

# ── IMPORTS ───────────────────────────────────────────────
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ── LOAD DATA ─────────────────────────────────────────────
df = pd.read_csv('sales_data.csv', parse_dates=['date'])
df['year']       = df['date'].dt.year
df['month_num']  = df['date'].dt.month
df['year_month'] = df['date'].dt.to_period('M').astype(str)
df['profit_margin'] = (df['profit'] / df['sales'] * 100).round(2)

# ── COLOUR PALETTE ────────────────────────────────────────
COLORS = {
    'bg':       '#F8F9FA',
    'card':     '#FFFFFF',
    'primary':  '#2C3E50',
    'accent':   '#E74C3C',
    'green':    '#27AE60',
    'blue':     '#2980B9',
    'orange':   '#F39C12',
    'purple':   '#8E44AD',
    'text':     '#2C3E50',
    'subtext':  '#7F8C8D',
}

CHART_COLORS = px.colors.qualitative.Set2

# ── HELPER: KPI CARD ──────────────────────────────────────
def kpi_card(title, value, subtitle='', color=COLORS['blue']):
    return html.Div([
        html.P(title, style={
            'margin': '0 0 4px 0', 'fontSize': '13px',
            'color': COLORS['subtext'], 'fontWeight': '500',
            'textTransform': 'uppercase', 'letterSpacing': '0.5px'
        }),
        html.H2(value, style={
            'margin': '0 0 4px 0', 'fontSize': '28px',
            'fontWeight': '700', 'color': color
        }),
        html.P(subtitle, style={
            'margin': '0', 'fontSize': '12px', 'color': COLORS['subtext']
        }),
    ], style={
        'background': COLORS['card'],
        'borderRadius': '12px',
        'padding': '20px 24px',
        'boxShadow': '0 2px 12px rgba(0,0,0,0.08)',
        'borderLeft': f'4px solid {color}',
        'flex': '1',
        'minWidth': '180px',
    })

# ── APP LAYOUT ────────────────────────────────────────────
app = dash.Dash(__name__, title='Sales Dashboard — CODTECH')

app.layout = html.Div(style={
    'fontFamily': '"Segoe UI", Arial, sans-serif',
    'background': COLORS['bg'],
    'minHeight': '100vh',
    'padding': '0',
}, children=[

    # ── HEADER ──────────────────────────────────────────
    html.Div([
        html.Div([
            html.H1('📊 Sales Analytics Dashboard',
                style={'margin': '0', 'fontSize': '26px',
                       'fontWeight': '700', 'color': '#FFFFFF'}),
            html.P('CODTECH IT Solutions — Data Analytics Internship | Task 3: Dashboard Development',
                style={'margin': '4px 0 0 0', 'fontSize': '13px',
                       'color': 'rgba(255,255,255,0.75)'}),
        ]),
        html.Div([
            html.P('[Name : Ritesh Chandra] | [Intern ID : CITS419]',
                style={'margin': '0', 'color': 'rgba(255,255,255,0.85)',
                       'fontSize': '13px', 'textAlign': 'right'}),
        ]),
    ], style={
        'background': f'linear-gradient(135deg, {COLORS["primary"]} 0%, #34495E 100%)',
        'padding': '20px 32px',
        'display': 'flex',
        'justifyContent': 'space-between',
        'alignItems': 'center',
        'boxShadow': '0 2px 8px rgba(0,0,0,0.15)',
    }),

    # ── FILTERS ─────────────────────────────────────────
    html.Div([
        html.Div([
            html.Label('📅 Year', style={'fontWeight': '600',
                'fontSize': '13px', 'color': COLORS['text'], 'marginBottom': '6px', 'display': 'block'}),
            dcc.Dropdown(
                id='year-filter',
                options=[{'label': 'All Years', 'value': 'All'}] +
                        [{'label': str(y), 'value': y} for y in sorted(df['year'].unique())],
                value='All',
                clearable=False,
                style={'fontSize': '13px'}
            ),
        ], style={'flex': '1', 'minWidth': '160px'}),

        html.Div([
            html.Label('🏷️ Category', style={'fontWeight': '600',
                'fontSize': '13px', 'color': COLORS['text'], 'marginBottom': '6px', 'display': 'block'}),
            dcc.Dropdown(
                id='category-filter',
                options=[{'label': 'All Categories', 'value': 'All'}] +
                        [{'label': c, 'value': c} for c in sorted(df['category'].unique())],
                value='All',
                clearable=False,
                style={'fontSize': '13px'}
            ),
        ], style={'flex': '1', 'minWidth': '160px'}),

        html.Div([
            html.Label('🌍 Region', style={'fontWeight': '600',
                'fontSize': '13px', 'color': COLORS['text'], 'marginBottom': '6px', 'display': 'block'}),
            dcc.Dropdown(
                id='region-filter',
                options=[{'label': 'All Regions', 'value': 'All'}] +
                        [{'label': r, 'value': r} for r in sorted(df['region'].unique())],
                value='All',
                clearable=False,
                style={'fontSize': '13px'}
            ),
        ], style={'flex': '1', 'minWidth': '160px'}),

        html.Div([
            html.Label('👤 Segment', style={'fontWeight': '600',
                'fontSize': '13px', 'color': COLORS['text'], 'marginBottom': '6px', 'display': 'block'}),
            dcc.Dropdown(
                id='segment-filter',
                options=[{'label': 'All Segments', 'value': 'All'}] +
                        [{'label': s, 'value': s} for s in sorted(df['customer_segment'].unique())],
                value='All',
                clearable=False,
                style={'fontSize': '13px'}
            ),
        ], style={'flex': '1', 'minWidth': '160px'}),

    ], style={
        'background': COLORS['card'],
        'padding': '16px 32px',
        'display': 'flex',
        'gap': '20px',
        'flexWrap': 'wrap',
        'boxShadow': '0 1px 4px rgba(0,0,0,0.06)',
        'borderBottom': '1px solid #ECF0F1',
    }),

    # ── MAIN CONTENT ────────────────────────────────────
    html.Div(style={'padding': '24px 32px'}, children=[

        # KPI Row
        html.Div(id='kpi-row', style={
            'display': 'flex', 'gap': '16px',
            'flexWrap': 'wrap', 'marginBottom': '24px'
        }),

        # Row 1: Sales Trend + Category Sales
        html.Div([
            html.Div([
                dcc.Graph(id='sales-trend-chart', config={'displayModeBar': False})
            ], style={
                'background': COLORS['card'], 'borderRadius': '12px',
                'padding': '16px', 'flex': '2',
                'boxShadow': '0 2px 12px rgba(0,0,0,0.06)'
            }),
            html.Div([
                dcc.Graph(id='category-bar-chart', config={'displayModeBar': False})
            ], style={
                'background': COLORS['card'], 'borderRadius': '12px',
                'padding': '16px', 'flex': '1',
                'boxShadow': '0 2px 12px rgba(0,0,0,0.06)'
            }),
        ], style={'display': 'flex', 'gap': '16px',
                  'marginBottom': '16px', 'flexWrap': 'wrap'}),

        # Row 2: Region Pie + Profit Scatter + Segment Donut
        html.Div([
            html.Div([
                dcc.Graph(id='region-pie-chart', config={'displayModeBar': False})
            ], style={
                'background': COLORS['card'], 'borderRadius': '12px',
                'padding': '16px', 'flex': '1',
                'boxShadow': '0 2px 12px rgba(0,0,0,0.06)'
            }),
            html.Div([
                dcc.Graph(id='profit-scatter-chart', config={'displayModeBar': False})
            ], style={
                'background': COLORS['card'], 'borderRadius': '12px',
                'padding': '16px', 'flex': '2',
                'boxShadow': '0 2px 12px rgba(0,0,0,0.06)'
            }),
            html.Div([
                dcc.Graph(id='segment-donut-chart', config={'displayModeBar': False})
            ], style={
                'background': COLORS['card'], 'borderRadius': '12px',
                'padding': '16px', 'flex': '1',
                'boxShadow': '0 2px 12px rgba(0,0,0,0.06)'
            }),
        ], style={'display': 'flex', 'gap': '16px',
                  'marginBottom': '16px', 'flexWrap': 'wrap'}),

        # Row 3: Heatmap + Top Products
        html.Div([
            html.Div([
                dcc.Graph(id='heatmap-chart', config={'displayModeBar': False})
            ], style={
                'background': COLORS['card'], 'borderRadius': '12px',
                'padding': '16px', 'flex': '1',
                'boxShadow': '0 2px 12px rgba(0,0,0,0.06)'
            }),
            html.Div([
                dcc.Graph(id='top-products-chart', config={'displayModeBar': False})
            ], style={
                'background': COLORS['card'], 'borderRadius': '12px',
                'padding': '16px', 'flex': '1',
                'boxShadow': '0 2px 12px rgba(0,0,0,0.06)'
            }),
        ], style={'display': 'flex', 'gap': '16px', 'flexWrap': 'wrap'}),

    ]),

    # ── FOOTER ──────────────────────────────────────────
    html.Div([
        html.P('CODTECH IT Solutions Pvt. Ltd. — Data Analytics Internship — Task 3: Dashboard Development',
            style={'margin': '0', 'color': COLORS['subtext'],
                   'fontSize': '12px', 'textAlign': 'center'})
    ], style={'padding': '16px', 'borderTop': '1px solid #ECF0F1',
              'background': COLORS['card'], 'marginTop': '8px'}),
])


# ── CALLBACKS ─────────────────────────────────────────────
def filter_df(year, category, region, segment):
    d = df.copy()
    if year     != 'All': d = d[d['year'] == year]
    if category != 'All': d = d[d['category'] == category]
    if region   != 'All': d = d[d['region'] == region]
    if segment  != 'All': d = d[d['customer_segment'] == segment]
    return d


@app.callback(
    Output('kpi-row',             'children'),
    Output('sales-trend-chart',   'figure'),
    Output('category-bar-chart',  'figure'),
    Output('region-pie-chart',    'figure'),
    Output('profit-scatter-chart','figure'),
    Output('segment-donut-chart', 'figure'),
    Output('heatmap-chart',       'figure'),
    Output('top-products-chart',  'figure'),
    Input('year-filter',     'value'),
    Input('category-filter', 'value'),
    Input('region-filter',   'value'),
    Input('segment-filter',  'value'),
)
def update_dashboard(year, category, region, segment):
    d = filter_df(year, category, region, segment)

    if d.empty:
        empty = go.Figure()
        empty.update_layout(title='No data for selected filters')
        return [], empty, empty, empty, empty, empty, empty, empty

    total_sales   = d['sales'].sum()
    total_profit  = d['profit'].sum()
    total_orders  = len(d)
    avg_order     = d['sales'].mean()
    profit_margin = (total_profit / total_sales * 100) if total_sales else 0

    # ── KPIs ──────────────────────────────────────────
    kpis = html.Div([
        kpi_card('Total Sales',    f'₹{total_sales:,.0f}',   f'{total_orders} orders',       COLORS['blue']),
        kpi_card('Total Profit',   f'₹{total_profit:,.0f}',  f'Margin: {profit_margin:.1f}%', COLORS['green']),
        kpi_card('Total Orders',   f'{total_orders:,}',       'Filtered records',              COLORS['orange']),
        kpi_card('Avg Order Value',f'₹{avg_order:,.0f}',     'Per transaction',               COLORS['purple']),
        kpi_card('Profit Margin',  f'{profit_margin:.1f}%',  'Net profitability',             COLORS['accent']),
    ], style={'display': 'flex', 'gap': '16px', 'flexWrap': 'wrap'})

    # ── SALES TREND ───────────────────────────────────
    monthly = d.groupby('year_month')[['sales','profit']].sum().reset_index()
    monthly = monthly.sort_values('year_month')
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=monthly['year_month'], y=monthly['sales'],
        name='Sales', mode='lines+markers',
        line=dict(color=COLORS['blue'], width=2.5),
        fill='tozeroy', fillcolor='rgba(41,128,185,0.08)'
    ))
    fig_trend.add_trace(go.Scatter(
        x=monthly['year_month'], y=monthly['profit'],
        name='Profit', mode='lines+markers',
        line=dict(color=COLORS['green'], width=2, dash='dash')
    ))
    fig_trend.update_layout(
        title='📈 Monthly Sales & Profit Trend',
        xaxis_title='Month', yaxis_title='Amount (₹)',
        legend=dict(orientation='h', y=1.1),
        plot_bgcolor='white', paper_bgcolor='white',
        margin=dict(l=10, r=10, t=50, b=10),
        height=320,
    )

    # ── CATEGORY BAR ──────────────────────────────────
    cat_sales = d.groupby('category')['sales'].sum().sort_values(ascending=True).reset_index()
    fig_cat = px.bar(cat_sales, x='sales', y='category', orientation='h',
                     color='sales', color_continuous_scale='Blues',
                     title='🏷️ Sales by Category', labels={'sales': 'Sales (₹)', 'category': ''})
    fig_cat.update_layout(
        plot_bgcolor='white', paper_bgcolor='white',
        margin=dict(l=10, r=10, t=50, b=10),
        height=320, showlegend=False, coloraxis_showscale=False
    )

    # ── REGION PIE ────────────────────────────────────
    reg_sales = d.groupby('region')['sales'].sum().reset_index()
    fig_region = px.pie(reg_sales, names='region', values='sales',
                        title='🌍 Sales by Region', hole=0.35,
                        color_discrete_sequence=CHART_COLORS)
    fig_region.update_layout(
        paper_bgcolor='white', margin=dict(l=10, r=10, t=50, b=10),
        height=300, legend=dict(orientation='h', y=-0.1)
    )

    # ── PROFIT SCATTER ────────────────────────────────
    fig_scatter = px.scatter(
        d, x='sales', y='profit', color='category',
        size='quantity', hover_data=['product', 'region', 'discount'],
        title='💰 Sales vs Profit by Category',
        labels={'sales': 'Sales (₹)', 'profit': 'Profit (₹)'},
        color_discrete_sequence=CHART_COLORS
    )
    fig_scatter.add_hline(y=0, line_dash='dot', line_color='red', opacity=0.5)
    fig_scatter.update_layout(
        plot_bgcolor='white', paper_bgcolor='white',
        margin=dict(l=10, r=10, t=50, b=10),
        height=300,
    )

    # ── SEGMENT DONUT ─────────────────────────────────
    seg_sales = d.groupby('customer_segment')['sales'].sum().reset_index()
    fig_seg = px.pie(seg_sales, names='customer_segment', values='sales',
                     title='👤 Sales by Segment', hole=0.45,
                     color_discrete_sequence=[COLORS['blue'], COLORS['green'], COLORS['orange']])
    fig_seg.update_layout(
        paper_bgcolor='white', margin=dict(l=10, r=10, t=50, b=10),
        height=300, legend=dict(orientation='h', y=-0.1)
    )

    # ── HEATMAP ───────────────────────────────────────
    heat = d.groupby(['category', 'quarter'])['sales'].sum().unstack(fill_value=0)
    fig_heat = px.imshow(heat / 1e3, text_auto='.0f',
                         color_continuous_scale='YlOrRd',
                         title='🔥 Sales Heatmap — Category × Quarter (₹K)',
                         labels=dict(color='Sales (₹K)'))
    fig_heat.update_layout(
        paper_bgcolor='white', margin=dict(l=10, r=10, t=50, b=10),
        height=320
    )

    # ── TOP PRODUCTS ──────────────────────────────────
    top10 = d.groupby('product')['sales'].sum().sort_values(ascending=False).head(10).reset_index()
    fig_top = px.bar(top10, x='sales', y='product', orientation='h',
                     color='sales', color_continuous_scale='Viridis',
                     title='🏆 Top 10 Products by Sales',
                     labels={'sales': 'Sales (₹)', 'product': ''})
    fig_top.update_layout(
        plot_bgcolor='white', paper_bgcolor='white',
        margin=dict(l=10, r=10, t=50, b=10),
        height=320, showlegend=False, coloraxis_showscale=False,
        yaxis=dict(autorange='reversed')
    )

    return kpis, fig_trend, fig_cat, fig_region, fig_scatter, fig_seg, fig_heat, fig_top


# ── RUN ───────────────────────────────────────────────────
if __name__ == '__main__':
    print('=' * 55)
    print('  CODTECH TASK 3 — Sales Analytics Dashboard')
    print('=' * 55)
    print('  Starting Dash server...')
    print('  Open browser: http://127.0.0.1:8050')
    print('  Press Ctrl+C to stop')
    print('=' * 55)
    app.run(debug=True)
