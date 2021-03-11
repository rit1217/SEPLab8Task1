class Hanoi( object ):
    def __init__ ( self, n = 3, start = "A", workspace = "B", destination = "C"):
        self.startp = Pole( start, 0, 0)
        self.workspace