class Vector:
    def __init__(self,li):
        self.li = li
    def __add__(self,other):
        newList = []
        for i in range(len(self.li)):
            newList.append(self.li[i]+other.li[i])
        return f'The vector addition of given two vectors is {newList}.'
    def __mul__(self,other):
        sum = 0
        for i in range(len(self.li)):
            sum = sum + (self.li[i] * other.li[i])
        return f"The dot product of given two vector is {sum}."
v1 = Vector([1,2,8])
v2 = Vector([4,6,9])
print(v1+v2)
print(v1*v2)