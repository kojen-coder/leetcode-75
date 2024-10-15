class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Pointer for where to write the compressed character
        read = 0  # Pointer for reading through the chars array

        while read < len ( chars ):
            char = chars[read]
            count = 0

            # Count the number of occurrences of the current character
            while read < len ( chars ) and chars[read] == char:
                read += 1
                count += 1

            # Write the character to the write pointer
            chars[write] = char
            write += 1

            # If count is greater than 1, write the count to the write pointer
            if count > 1:
                for c in str ( count ):
                    chars[write] = c
                    write += 1

        # Return the new length of the array
        return write