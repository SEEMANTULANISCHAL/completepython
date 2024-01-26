#ITERATOR INBUILT
list =[2,3,4,5]
it = iter(list)
print(it.__next__())
print(next(it))
# Create own Iterator
#Print top 10 values
class Values:
    def __init__(self):
        self.value = 1 
    def __iter__(self):
        return self
    def __next__(self):
        if self.value <= 10:
            num = self.value
            self.value += 1 
            return num  
        else:
            raise StopIteration
v1 = Values()
print(v1.__next__())
print(next(v1))
for i in v1:
    print(i)

    