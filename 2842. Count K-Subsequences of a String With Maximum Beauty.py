class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        mod=10**9+7
        f=Counter(s)
        if len(f)<k:
            return 0
        freq=Counter(f.values())
        p=list(sorted(freq.items(),reverse=True))
        ans=1
        for frequency , occurence in p:
            if occurence<=k:
                ans=(ans*pow(frequency,occurence,mod))%mod
                k-=occurence
            else:
                ans=(ans*comb(occurence,k)*pow(frequency,k,mod))%mod
                break
        return ans % mod