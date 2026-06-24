class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.last = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr < len(self.history):
            self.history[self.curr] = url
        else:
           self.history.append(url)

        self.last = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.last,self.curr + steps)
        return self.history[self.curr]

# visit	O(1)
# back	O(1)
# forward	O(1)

bh = BrowserHistory("leetcode.com")

bh.visit("google.com")        # leetcode → google
bh.visit("facebook.com")      # google → facebook
bh.visit("youtube.com")       # facebook → youtube

print(bh.back(1))             # go back to facebook
print(bh.back(1))             # go back to google
print(bh.forward(1))          # go forward to facebook

bh.visit("linkedin.com")      # new visit from facebook (cuts forward history)

print(bh.forward(2))          # cannot go forward, stays at linkedin
print(bh.back(2))             # go back to google
print(bh.back(7))             # go back to homepage (leetcode)