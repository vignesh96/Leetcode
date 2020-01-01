def check_substring(find_me, substr):
    find_index = 0
    for letter in substr:
        if find_me[find_index] == letter:
            #find_index +=1
            break
        # if we reach the end of find_me, return true
        if find_index >= len(find_me):
            return find_index
    return False

def check_string(find_me, look_here, max_len):
    cnt = 0
    for index in range(len(look_here)):
        if find_me[0] == look_here[index]:
            if check_substring(find_me, look_here[index:index + max_len]):
                cnt += 1
    return cnt



fm = "YOYO"
lh = "VIBGYOYORBGIIOYVVVRYOYOV"
ml = len(lh)

print check_string(fm, lh, ml)
