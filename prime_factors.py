

def prime_factors(n):
    def _prime_factors(n, p=[]):
        if n < 2:
            return p
        for i in range(2, round(n**0.5)+1):
            if n%i == 0:
                p.append(i)
                _prime_factors(n/i)
                break
        else:
            p.append(int(n))
        return p
    return _prime_factors(n)

