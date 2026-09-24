import numpy as np
import plotly.graph_objects as go

def dirichlet_eta(s, N=500):
    """
    ディリクレのイータ関数を用いて複素平面上のゼータ関数を近似計算する
    ゼータ関数との関係式: zeta(s) = eta(s) / (1 - 2^(1-s))
    """
    eta = np.zeros_like(s, dtype=complex)
    for n in range(1, N + 1):
        eta += ((-1) ** (n - 1)) / (n ** s)
    return eta / (1 - 2.0 ** (1.0 - s))

# 1. 複素平面上のグリッドを作成 (実部: -1〜2, 虚部: 0〜35)
re = np.linspace(-1, 2, 150)
im = np.linspace(0, 35, 250)
RE, IM = np.meshgrid(re, im)
S = RE + 1j * IM

# 2. ゼータ関数の絶対値を計算
Z = dirichlet_eta(S)
Z_abs = np.abs(Z)

# グラフを綺麗に見せるため、値が大きすぎる部分はクリッピング（制限）する
Z_abs = np.clip(Z_abs, 0, 7)

# 3. 3D曲面のプロット作成
fig = go.Figure(data=[go.Surface(
    x=RE, y=IM, z=Z_abs,
    colorscale='Viridis',
    hovertemplate='Re(s): %{x:.2f}<br>Im(s): %{y:.2f}<br>|zeta(s)|: %{z:.2f}<extra></extra>'
)])

# 4. 臨界線 Re(s) = 0.5 を赤線でハイライト
im_line = np.linspace(0, 35, 500)
s_line = 0.5 + 1j * im_line
z_line = np.clip(np.abs(dirichlet_eta(s_line)), 0, 7)

fig.add_trace(go.Scatter3d(
    x=np.ones_like(im_line) * 0.5,
    y=im_line,
    z=z_line,
    mode='lines',
    line=dict(color='red', width=5),
    name='臨界線 Re(s) = 0.5'
))

# 5. 最初の4つの非自明な零点 (底の谷) をマーカーでプロット
# 零点の虚部 (t) の理論値: 約 14.13, 21.02, 25.01, 30.42
zeros_im = [14.1347, 21.0220, 25.0109, 30.4249]
fig.add_trace(go.Scatter3d(
    x=[0.5] * len(zeros_im),
    y=zeros_im,
    z=[0] * len(zeros_im),
    mode='markers',
    marker=dict(size=6, color='crimson', symbol='diamond'),
    name='非自明な零点 (Zero points)'
))

# 6. レイアウトの設定
fig.update_layout(
    title='リーマン・ゼータ関数 |ζ(s)| の3Dプロットとリーマン予想',
    scene=dict(
        xaxis_title='実部 Re(s)',
        yaxis_title='虚部 Im(s)',
        zaxis_title='絶対値 |ζ(s)|',
        aspectratio=dict(x=1, y=1.5, z=0.8)
    ),
    margin=dict(l=0, r=0, b=0, t=50)
)

# ブラウザを開いてインタラクティブなグラフを表示
fig.show()

# (オプション) HTMLファイルとして保存したい場合は以下を実行してください
# fig.write_html("riemann_zeta_3d.html")
# fig.write_html("riemann_zeta_3d.html")
