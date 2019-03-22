class reverse:
    def rev(self,string):
        if len(string) == 0:
            return string
        else:
            return self.rev(string[1:])+string[0]
a=str(input("enter string:"))
b=reverse()
print(b.rev(a))
