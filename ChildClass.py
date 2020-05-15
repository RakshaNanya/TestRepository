from ParentObj import Calculator


class Super(Calculator):
    num2 = 200

    def __int__(self):
        Calculator.__init__(self, 2, 5)
        print("init calculator")

    def getcompletedata(self):
        print("Git Testing 1")
	print("SubBranch testing 2")
	print("Checking that the changes done to Subbranches effects 		master barsnch or not")
        return self.num2 + self.summation() + self.num


obj = Super(1, 2)
print(obj.getcompletedata())



