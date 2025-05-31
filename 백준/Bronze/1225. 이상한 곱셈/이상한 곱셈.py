a, b = input().split()
print(sum(list(map(int, a))) * sum(list(map(int, b))))

# r = a₁×b₁ + a₁×b₂ + ... + a₁×bₘ + a₂×b₁ + a₂×b₂ + ... + a₂×bₘ + ... + aₙ×b₁ + aₙ×b₂ + ... + aₙ×bₘ
# 이걸 인수분해하면
# r = a₁×(b₁+b₂+...+bₘ) + a₂×(b₁+b₂+...+bₘ) + ... + aₙ×(b₁+b₂+...+bₘ)
#   = (a₁+a₂+...+aₙ) × (b₁+b₂+...+bₘ)
#   = sum(a) × sum(b)