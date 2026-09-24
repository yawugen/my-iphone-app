import matplotlib.pyplot as plt


def generate_primes(n_primes):
    """エラトステネスの篩を使って、指定した個数の素数を取得する関数"""
    # 10万番目の素数は約130万件の範囲内に存在するため、探索上限を150万に設定
    limit = 1500000
    is_prime = [True] * limit
    primes = []

    for p in range(2, limit):
        if is_prime[p]:
            primes.append(p)
            if len(primes) == n_primes:
                break
            # pの倍数をすべて除外
            for i in range(p * p, limit, p):
                is_prime[i] = False
    return primes


# 1. 10万個の素数を生成
print("素数を計算中...")
n_primes = 100000
primes = generate_primes(n_primes)

# 2. 前の素数からの増加量（素数間隔）を計算
# n番目の素数 (index i) と n-1番目の素数 (index i-1) の差
gaps = [primes[i] - primes[i - 1] for i in range(1, len(primes))]

# 3. グラフの描画
print("グラフを描画中...")
# X軸: n番目の素数 (2番目から100,000番目)
x = list(range(2, n_primes + 1))

plt.figure(figsize=(12, 6))

# 10万点あるため、ドットを小さく(s=1)、透過(alpha=0.3)させて密度を分かりやすくします
plt.scatter(x, gaps, s=1, alpha=0.3, color="blue")

plt.title("Prime Gaps (Difference from Previous Prime) up to 100,000th Prime")
plt.xlabel("n-th Prime")
plt.ylabel("Gap (p_n - p_{n-1})")
plt.grid(True, linestyle="--", alpha=0.5)

# グラフを表示
plt.show()
