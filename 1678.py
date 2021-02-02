class Solution:
    def interpret(self, command: str) -> str:
        newstr = command.replace("()", "o")
        newstr = newstr.replace("(", "")
        newstr = newstr.replace(")", "")
        return newstr
