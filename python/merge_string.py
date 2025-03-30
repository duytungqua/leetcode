class Soluthon(object):
    def merge_string(self, s1, s2):
        merge = []
        i , j = 0
        while i < len(s1) and j < len(s2):
            merge.append(s1[i])
            merge.append(s2[i])
            i += 1
            j += 1

        merge.extend(s1[i:])
        merge.extend(s2[j:]) 
        return "".join(merge)