
class Euclidean: 
    #pseudo code:
    """
    func gcd(a,b):
        while b != 0:
            tem =  b
            b = a% b
            a = tem
        return a
    """
    def gcd():
        a = 10
        b = 5
        while b != 0:
            temp = b
            b = a % 10
            a = temp
        return a
    #test
    def  gcd_string(str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        len = gcd(len(str1), len(str2)) 
        return str1[:len]
