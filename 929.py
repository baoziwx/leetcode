# 929. Unique Email Addresses

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniques = set()
        for e in emails:
            parts = e.split('@')
            local, remote = parts[0], parts[1]
            local_processed = ''
            for c in local:
                if c == '.':
                    continue
                elif c == '+':
                    break
                local_processed += c
            processed_addr = local_processed + '@' + remote
            uniques.add(processed_addr)
        return len(uniques)
