"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
"""

from collections import defaultdict


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_adjacency_list = defaultdict(set)
        email_owner = {}
        for account in accounts:
            name = account[0]

            for email in account[1:]:
                # connect first email to all emails
                email_adjacency_list[account[1]].add(email)
                email_adjacency_list[email].add(account[1])

                # maintain owner of emails
                email_owner[email] = name

        print(email_adjacency_list)
        print(email_owner)

        seen = set()
        ans = []
        for email in email_adjacency_list:
            if email not in seen:
                seen.add(email)
                st = [email]
                comp = []

                while st:
                    edge = st.pop()
                    comp.append(edge)
                    for n_edge in email_adjacency_list[edge]:
                        if n_edge not in seen:
                            seen.add(n_edge)
                            st.append(n_edge)

                ans.append([email_owner[email]] + sorted(comp))
        print(ans)


s = Solution()
s.accountsMerge(
    [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
     ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
