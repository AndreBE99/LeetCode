# function getSubstringCount(s) {
#     let count = 0;
#     const groups = [];
#     let currentChar = s[0];
#     let currentCount = 1;

#     for (let i = 1; i < s.length; i++) {
#         if (s[i] === currentChar) {
#             currentCount++;
#         } else {
#             groups.push(currentCount);
#             currentChar = s[i];
#             currentCount = 1;
#         }
#     }

#     groups.push(currentCount);

#     for (let i = 0; i < groups.length - 1; i++) {
#         const leftGroupLength = groups[i];
#         const rightGroupLength = groups[i + 1];


#         count += Math.min(leftGroupLength, rightGroupLength);
#     }

#     return count;
# }
def get_substring_count(s):
    count = 0
    groups = []
    current_char = s[0]
    current_count = 1

    # Create groups of consecutive characters
    for i in range(1, len(s)):
        if s[i] == current_char:
            current_count += 1
        else:
            groups.append(current_count)
            current_char = s[i]
            current_count = 1

    groups.append(current_count)  # Append the last group count

    # Count valid substrings between adjacent groups
    for i in range(len(groups) - 1):
        left_group_length = groups[i]
        right_group_length = groups[i + 1]
        count += min(left_group_length, right_group_length)

    return count

if __name__ == "__main__":
    test_strings = [
        "00110011",  # Example 1
        "10101",     # Example 2
        "111000",    # Example 3
        "000111",    # Example 4
        "1111",      # Example 5
        "01010101",   # Example 6
        "0011100110",  # Example 7
    ]

    for s in test_strings:
        print(f"Input string: {s}")
        print(f"Substring count: {get_substring_count(s)}\n")
