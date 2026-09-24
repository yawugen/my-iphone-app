import numpy as np
import matplotlib.pyplot as plt

# 1. ゼータ関数を近似計算する関数
def zeta_approx(s, N=3000):
    n = np.arange(1, N + 1)
    signs = (-1) ** (n - 1)
    eta = np.zeros_like(s, dtype=complex)
    for i in range(N):
        eta += signs[i] / (n[i] ** s)
    return eta / (1.0 - 2.0 ** (1.0 - s))

# 2. 実部を 0.5 に固定し、虚部 t の範囲（10〜30）を設定
t = np.linspace(10.0, 30.0, 500)  # 滑らかにするためにサンプリング数を500に増加
s = 0.5 + 1j * t

# 3. ゼータ関数の絶対値 |ζ(0.5 + it)| を計算
z_abs = np.abs(zeta_approx(s))

# 4. 2次元断面グラフの描画
plt.figure(figsize=(10, 5))
plt.plot(t, z_abs, color='red', linewidth=2, label=r'$|\zeta(0.5 + it)|$')

# 既知の非自明な零点（谷底が0になるポイント）をグラフ上にプロット
zeros = [14.1347, 21.0220, 25.0109]
for zero in zeros:
    plt.axvline(x=zero, color='blue', linestyle='--', alpha=0.5)
    plt.plot(zero, 0, 'bo')  # 青い点で零点を強調
    plt.text(zero, -0.15, f'{zero:.2f}', color='blue', ha='center', fontsize=9)

# グラフの装飾
plt.title(r'Cross Section on the Critical Line: $|\zeta(0.5 + it)|$', fontsize=14)
plt.xlabel('Imaginary Part: t', fontsize=12)
plt.ylabel(r'Absolute Value: $|\zeta(0.5 + it)|$', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xlim(10, 30)
plt.ylim(-0.3, 3.5)  # 下部にラベル用の余白を確保
plt.legend()

plt.show()
