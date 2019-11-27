#label: string difficulty: easy

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = dict()
        for visit in cpdomains:
            cnt,domain = visit.split(" ")
            hashmap[domain] = hashmap.get(domain,0) + int(cnt)
            
            while('.' in domain):
                domain = domain[domain.index('.') + 1:]
                hashmap[domain] = hashmap.get(domain,0) + int(cnt)
                
        res = list()
        for domain,cnt in hashmap.items():
            res.append(str(cnt) + ' ' + domain)
            
        return res
