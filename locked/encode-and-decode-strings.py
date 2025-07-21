class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_strings = ""

        for string in strs:
            encoded_string = ""
            for char in string:
                encoded_string += f"{ord(char)}|"
            encoded_strings += f"{encoded_string}."
            
        return encoded_strings
    
    def decode(self, s: str) -> list[str]:
        if not s:
            return []
            
        encoded_strings = s.split('|')
        decoded_strings = []

        last_pipe = 0
        string = ""

        for char in encoded_strings:
            if char == '.':
                decoded_strings.append(string)
                string = ""
                continue
            elif char[0] == '.':
                decoded_strings.append(string)
                string = "" + chr(int(char[1:]))
                continue
            
            string += chr(int(char))
        
        return decoded_strings

solution = Solution()

strings = ["neet","code","love","you"]
encoded_string = solution.encode(strings)
strings = solution.decode(encoded_string)

print(f"{encoded_string} : {strings}")