
def longest_common_prefix(strs):
    """ Leetcode Problems """
    result = ""
    choice_txt = strs[0]

    for txt in strs[1:]:
        length = len(choice_txt) if len(txt) >= len(choice_txt) else len(txt)
        cond = -1

        for i in range(length):
            if txt[i] == choice_txt[i] and cond == i - 1:
                result += txt[i]
                cond = i

        choice_txt = result
        result = ""

    return choice_txt
