from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        op = ""
        for s in strs:
            # Fixed: Changed '=' to '+=' to accumulate the strings
            op += str(len(s)) + "#" + s  
        return op

    def decode(self, s: str) -> List[str]:
        op = []
        while s:
            index = s.find("#")
            num = int(s[:index])
            num_str = s[index + 1 : index + num + 1]
            op.append(num_str)
            s = s[index + num + 1 :]
        return op  # Fixed: Corrected typo 'retrun' to 'return'