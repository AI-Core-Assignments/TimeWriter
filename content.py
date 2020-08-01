class Content():

    def __init__(self):
        pass

    def factorial(self, n):
        if n==1:
            return n
        else:
            factn = n * self.factorial(n-1)
            
        return factn


    def flatten_list(self, list_of_list):
        flat = [element for single_list in list_of_list for element in single_list]
        return flat


a = Content()
print(a.factorial(5))

print(a.flatten_list([[1,2,3], [2,4], [3,1,2]]))