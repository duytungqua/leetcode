
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