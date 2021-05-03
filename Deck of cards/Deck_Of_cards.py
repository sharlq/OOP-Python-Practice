import random
class Card():
    def __init__(self,sute,value):
        self.sute=sute
        self.value=value
    
    def show(self):
        print(f"{self.value} of {self.sute}")

class DecK():
    def __init__(self):
        self.cards=[]
        self.build

    def build(self):
        for s in ["Spades","Clubs","Diamonds","Hearts"]:
            for i in range(1,14):
                self.cards.append(Card(s,i)) # see we have used the object card we have create now each card in teh deck is an instence of that object each card is a card

    def show(self):
        for c in self.cards:
            c.show() # note the chaining of objects

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]

    def draw(self):
       return self.cards.pop()



class Player():
    def __init__(self,name):
        self.name=name
        self.hand=[]

    def draw(self,deck):
        self.hand.append(deck.draw())

    def show(self):
        for i in self.hand:
            i.show() # i think it returns deck object instead of cards object

    def discard(self):
        return self.hand.pop()

deck = DecK()
guy = Player("guy")
deck.shuffle()
deck.build()
guy.draw(deck)
guy.show()

