import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 💡 環境に合わせた「インタラクティブ化」の設定
# ==========================================
# ① 通常のPython実行（コマンドプロンプト/ターミナル）や VS Code の場合：
plt.ion()  # インタラクティブモードをオン（デフォルトで動くことが多いです）

# ② Jupyter Notebook / JupyterLab の場合：
# もし上記で動かない場合は、以下の行のコメントアウト(#)を外して実行してください
# %matplotlib notebook
# %matplotlib widget
# ==========================================

def zeta_approx(s, N=3000):
    n = np.arange(1, N + 1)
    signs = (-1) ** (n - 1)
    eta = np.zeros_like(s, dtype=complex)
    for i in range(N):
        eta += signs[i] / (n[i] ** s)
    return eta / (1.0 - 2.0 ** (1.0 - s))

x = np.linspace(0.0, 1.0, 100)
y = np.linspace(10.0, 30.0, 200)
X, Y = np.meshgrid(x, y)
S = X + 1j * Y

Z = np.abs(zeta_approx(S))
Z = np.clip(Z, 0, 4)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)
ax.plot([0.5, 0.5], [10, 30], [0, 0], color='red', linewidth=2.5, label='Critical Line (Re(s)=0.5)')

ax.set_title('Absolute Value of Riemann Zeta Function |$\zeta$(s)|', fontsize=14, pad=20)
ax.set_xlabel('Real Part: Re(s)', fontsize=12)
ax.set_ylabel('Imaginary Part: Im(s)', fontsize=12)
ax.set_zlabel('|$\zeta$(s)|', fontsize=12)
ax.legend()
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

ax.view_init(elev=30, azim=-60)

plt.show()

# グラフウィンドウがすぐに閉じないようにするための待機（通常のスクリプト実行用）
input("Enterキーを押すと終了します...")
