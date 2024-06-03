class Computer:
    def __init__(self,__os) :
        self.os=__os
    def __install_os(self):
        print(self.os)
    def install_os(self):
        return(self.__install_os())
c1=Computer("ios")
c1.install_os()

        